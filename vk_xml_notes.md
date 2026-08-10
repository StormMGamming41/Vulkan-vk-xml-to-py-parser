# vk.xml Notes

## Registry architecture
- `Registry_Parser` walks vk.xml, dispatches per-element to registered parser classes.
- Two dispatch paths, both driven by `Base_Parser.selection`:
  - `selection = "types"` -> parser keyed by `category` attr, runs on `<types><type category=X>` children
  - `selection = <tag>` (e.g. "enums", "extensions") -> parser runs once per matching
    top-level element via `root.findall(tag)` — GOTCHA: must be `.findall`, not `.find`,
    or you silently only process the first matching element in the whole doc.
- All parsers write into a single shared `Registry` dataclass (dict-of-dicts by name).
- New category checklist: (1) dataclass in model.py, (2) parser class in parsers/,
  subclassing Base_Parser with `category`/`selection` set, (3) register in parser.py
  __init__ in the right order if it depends on another category already existing.

## Handle — `<type category="handle">`
- Simple: `name`, optional `parent` (some handles are owned-by another, e.g. VkQueue -> VkDevice).

## Base_Type — `<type category="basetype">`
- Typedefs like `typedef uint64_t VkDeviceSize;` -> name + underlying C_Type.

## Bitmask — `<type category="bitmask">`
- Typedef of VkFlags/VkFlags64 with an optional `requires`/`bitvalues` attr pointing at
  the paired *FlagBits enum group name (the actual bit values live in that enum group,
  not on the bitmask type itself — bitmask type is just the flags container typedef).

## C_Type
- Shared value type for "a C type reference": name + pointer_level + const.
- Used wherever vk.xml embeds a raw type reference (basetype underlying type,
  bitmask underlying type, struct/function param types later on).

## Enums — see below (two-phase, base + extension contributions)

### 1. Base groups — `<enums>` (top-level, sibling of `<types>`)
- `<type category="enum" name="X"/>` under `<types>` is just a STUB, no values.
- Real values in separate top-level `<enums name="X" type="enum|bitmask">`.
- Each `<enum>` child: `value=`, OR `bitpos=` (bitmask groups, real value = 1<<bitpos),
  OR `alias=` (means-same-as another name, no independent value).
- `<unused start=".." end=".."/>` siblings inside groups — not values, ignore.
- "API Constants" group: no `type` attr on the group; its entries carry `type=` attr
  (uint32_t/float/etc) instead of being plain numeric values.
- GOTCHA: `root.findall("enums")` not `.find()` — cost an hour, see git history.

### 2. Extension-contributed values — `<extensions><extension><require><enum extends="X">`
- Do NOT create new groups — append Enum_Values into a group already built in phase 1.
  MUST run after the base enums pass (registration order in parser.py matters).
- Only process `<extension>` where `supported` contains "vulkan" (skip vulkansc-only/disabled).
- Value resolution priority: `bitpos` > `value` > `offset`.
  offset formula: value = 1_000_000_000 + (extension_number - 1) * 1000 + offset
                  if dir == "-": value = -value
  extension_number is on the parent <extension> element, not the <enum> itself.
- `extends` may be absent on some `<enum>` in `<require>` — those are unrelated
  feature-gated constants, skip if absent.
- Result: contributed values land in the SAME Enums_Group.values list as base values,
  no separate structure — indistinguishable by source once merged, unless tagged.

## Open TODOs
- [ ] Confirm behavior if `extends` points to a group not yet in registry.enums_groups
- [ ] Decide whether to tag Enum_Value with its source (core spec vs extension name) —
      useful later for codegen doc comments / conditional compilation per extension
- [ ] Alias resolution: does `alias=` get resolved to the target's real value at parse
      time, or deferred to codegen? (currently: deferred, alias field stored as-is)

## Next categories to implement
- struct / union — nested members, fixed arrays (`[N]` in name text), `len` attr for
  dynamic arrays, pointer levels, const-ness
- funcpointer — raw C typedef text, needs manual parsing (not structured XML)
- commands — under top-level `<commands>`, NOT under `<types>` — different traversal
  entirely, needs its own top-level `selection` parser like extensions/enums