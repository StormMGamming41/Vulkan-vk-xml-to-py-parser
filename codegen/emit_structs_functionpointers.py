from model import Registry, Member
from resolve import resolve_c_type

def emit_member_field(member: Member, registry: Registry) -> str:
    base = resolve_c_type(member.type, registry)
    if member.array_len:
        for dim in reversed(member.array_len):
            base = f"({base} * {dim})"
    return f'    ("{member.name}", {base}),'

def emit_structs_and_funcpointers(registry: Registry, order: list[str]) -> str:
    lines = ["from ctypes import *", "from .enums import *", ""]

    # Phase 1: struct/union stubs
    for name in order:
        struct = registry.structs_unions[name]
        base = "Union" if struct.is_union else "Structure"
        lines.append(f"class {name}({base}):")
        lines.append("    pass")
    lines.append("")

    # Phase 2: funcpointers (can reference struct stubs now)
    for fp in registry.function_pointers.values():
        restype = resolve_c_type(fp.return_type, registry)
        restype_str = restype if restype is not None else "None"
        argtypes = [resolve_c_type(p.type, registry) for p in fp.params]
        args_str = ", ".join([restype_str] + argtypes)
        lines.append(f"{fp.name} = CFUNCTYPE({args_str})")
    lines.append("")

    # Phase 3: struct/union fields (can reference PFN_* names now)
    skipped = []
    for name in order:
        struct = registry.structs_unions[name]
        try:
            fields = [emit_member_field(m, registry) for m in struct.members]
        except ValueError:
            skipped.append(name)
            continue
        lines.append(f"{name}._fields_ = [")
        lines.extend(fields)
        lines.append("]")
        lines.append("")

    if skipped:
        print(f"Skipped {len(skipped)} structs: {skipped}")

    return "\n".join(lines)