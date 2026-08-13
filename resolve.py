# resolve.py
from model import Registry, C_Type, Enums_Group

PRIMITIVE_MAP = {
    "void": None,          # special-cased — only valid behind a pointer
    "char": "c_char",
    "float": "c_float",
    "double": "c_double",
    "uint8_t": "c_uint8",
    "uint16_t": "c_uint16",
    "uint32_t": "c_uint32",
    "uint64_t": "c_uint64",
    "int8_t": "c_int8",
    "int16_t": "c_int16",
    "int32_t": "c_int32",
    "int64_t": "c_int64",
    "size_t": "c_size_t",
    "int": "c_int",
}

def resolve_type(name: str, registry: Registry) -> str:
    if name in PRIMITIVE_MAP:
        return PRIMITIVE_MAP[name]
    if name in registry.handles:
        return "c_void_p"
    if name in registry.basetypes:
        return resolve_type(registry.basetypes[name].type.name, registry)
    if name in registry.bitmasks:
        return resolve_type(registry.bitmasks[name].type.name, registry)
    if name in registry.enums_groups:
        return "c_int32"
    if name in registry.structs_unions:
        return name
    if name in registry.function_pointers:
        return name
    raise ValueError(f"{name} type cannot be resolved as c_type object")

def resolve_c_type(c_type: C_Type, registry: Registry) -> str:
    base = resolve_type(c_type.name, registry)

    if c_type.name == "void" and c_type.pointer_level >= 1:
        result = "c_void_p"
        remaining = c_type.pointer_level - 1
    else:
        result = base
        remaining = c_type.pointer_level

    for _ in range(remaining):
        result = f"POINTER({result})"

    return result

def resolve_group_values(group: Enums_Group) -> dict[str, int]:
    name_to_value: dict[str, int] = {}

    # pass 1: entries with a direct value or bitpos
    for ev in group.values:
        if ev.bitpos is not None:
            name_to_value[ev.name] = 1 << ev.bitpos
        elif ev.value is not None:
            name_to_value[ev.name] = int(ev.value, 0)

    # pass 2: resolve aliases against what pass 1 found
    for ev in group.values:
        if ev.name not in name_to_value and ev.alias is not None:
            if ev.alias in name_to_value:
                name_to_value[ev.name] = name_to_value[ev.alias]

    return name_to_value

def struct_dependencies(struct, registry: Registry) -> set[str]:
    deps = set()
    for member in struct.members:
        if member.type.pointer_level == 0 and member.type.name in registry.structs_unions:
            deps.add(member.type.name)
    return deps

def topological_sort_structs(registry: Registry) -> list[str]:
    visited = set()
    in_progress = set()
    order = []

    def visit(name):
        if name in visited:
            return
        if name in in_progress:
            raise ValueError(f"Circular by-value struct dependency involving {name}")
        in_progress.add(name)

        struct = registry.structs_unions[name]
        for dep in struct_dependencies(struct, registry):
            visit(dep)

        in_progress.discard(name)
        visited.add(name)
        order.append(name)

    for name in registry.structs_unions:
        visit(name)

    return order

def build_extension_map(registry: Registry) -> dict[str, list[str]]:
    extension_map: dict[str, list[str]] = {}
    for name, struct in registry.structs_unions.items():
        if not struct.struct_extends:
            continue
        for base in struct.struct_extends:
            extension_map.setdefault(base, []).append(name)
    return extension_map