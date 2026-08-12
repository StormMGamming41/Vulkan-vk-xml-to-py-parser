# resolve.py
from model import Registry

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