# vk.xml Notes

Reference doc: what each vk.xml object type looks like, and how this parser handles it.

## Registry architecture
`Registry_Parser` walks vk.xml, dispatches per-element to registered parser classes
via `Base_Parser.selection`:
- `selection = "types"` — parser keyed by `category` attr, runs on `<types><type category=X>` children
- `selection = <tag>` (e.g. "enums", "extensions") — parser runs once per matching
  top-level element via `root.findall(tag)`
  - GOTCHA: must be `.findall`, not `.find` — `.find()` silently only grabs the first
    matching element in the whole doc and iterating its children looks like progress
    while actually skipping everything else. (cost ~1hr once, see git history)

All parsers write into one shared `Registry` dataclass (dict-of-dicts, keyed by name).

New category checklist:
1. dataclass in model.py
2. parser class in parsers/, subclassing Base_Parser, `category`/`selection` set
3. register in parser.py — order matters if the parser depends on another
   category already existing (e.g. extension enums need base enum groups first)

---

## Handle — `<type category="handle">`
Shape: `name`, optional `parent` (some handles are owned-by another, e.g. VkQueue -> VkDevice).
Status: ✅ implemented (`Handle_Parser`)

## Base_Type — `<type category="basetype">`
Shape: typedef like `typedef uint64_t VkDeviceSize;` -> name + underlying C_Type.
Status: ✅ implemented (`Base_Type_Parser`)

## Bitmask — `<type category="bitmask">`
Shape: typedef of VkFlags/VkFlags64, optional `requires`/`bitvalues` attr pointing at
the paired *FlagBits enum group name. Actual bit values live in that enum group,
not on the bitmask type itself — this is just the flags container typedef.
Status: ✅ implemented (`Bitmask_Parser`)

## C_Type (shared value type, not a vk.xml element)
Represents any "C type reference" embedded elsewhere: name + pointer_level + const.
Used by basetype/bitmask underlying types, will be reused for struct members and
function params.

## Enums (two-phase: base groups + extension contributions)

### Base groups — `<enums>` (top-level, sibling of `<types>`)
- `<type category="enum" name="X"/>` under `<types>` is a STUB only, no values.
- Real values live in a separate top-level `<enums name="X" type="enum|bitmask">`.
- Each `<enum>` child: `value=`, OR `bitpos=` (bitmask groups, real value = 1<<bitpos),
  OR `alias=` (means-same-as another name, no independent value).
- `<unused start=".." end=".."/>` siblings inside groups — not values, ignore.
- "API Constants" group: no `type` attr on the group itself; entries carry a `type=`
  attr (uint32_t/float/etc) instead of numeric value semantics.
Status: ✅ implemented (`Enums_Group_Parser`)

### Extension-contributed values — `<extensions><extension><require><enum extends="X">`
- Append Enum_Values into a group already built by the base pass — do NOT create new
  groups. Must run after the base enums pass (registration order in parser.py).
- Only process `<extension>` where `supported` contains "vulkan" (skip vulkansc-only/disabled).
- Value resolution priority: `value` (as-is) > `bitpos` (kept in bitpos field, same as
  base pass) > `offset` (computed) > neither (pure alias, value stays None).
- Offset formula:
      value = 1_000_000_000 + (extension_number - 1) * 1000 + offset
      if dir == "-": value = -value
  extension_number comes from the parent `<extension>` element's `number` attr.
- `extends` may be absent on some `<enum>` in `<require>` — unrelated feature-gated
  constant, skip if absent.
- Verified against known values: VK_SUBOPTIMAL_KHR = 1000001003,
  VK_ERROR_OUT_OF_DATE_KHR = -1000001004 (offset=1, dir="-")
Status: ✅ implemented (`Extension_Enum_Parser`)

---

## Not yet implemented

### Struct / Union — `<type category="struct">` / `<type category="union">`
Shape (not yet explored in depth): nested `<member>` elements with their own type +
name, fixed-size arrays expressed as `[N]` in the trailing text of the member (not a
clean attribute), `len` attribute on members describing a relationship to another
member holding the runtime array length. Structs can reference other not-yet-defined
structs — needs topological sort before emitting.

### Funcpointer — `<type category="funcpointer">`
Shape: raw C typedef text, not structured XML — needs manual/regex parsing of the
function pointer signature.

### Commands — `<commands>` (top-level, NOT under `<types>`)
Different traversal entirely — needs a new top-level `selection` parser like
extensions/enums, not the category-dispatch path.

---

## General pitfalls (apply across categories)
- Filter to `api="vulkan"` — some elements are `vulkansc`-only or `disabled`.
- Use `.findall`, never `.find`, when iterating multiple same-name siblings.