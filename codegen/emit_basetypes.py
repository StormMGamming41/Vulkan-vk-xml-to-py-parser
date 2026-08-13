
from model import Registry
from resolve import resolve_c_type

def emit_basetypes(registry: Registry) -> str:
    lines = ["from ctypes import *", ""]

    for basetype in registry.basetypes.values():
        base = resolve_c_type(basetype.type, registry)
        lines.append(f"{basetype.name} = {base}")

    return "\n".join(lines)
