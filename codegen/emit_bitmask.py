from model import Registry
from resolve import resolve_c_type

def emit_bitmasks(registry: Registry) -> str:
    lines = ["from ctypes import *", ""]

    for bitmask in registry.bitmasks.values():
        base = resolve_c_type(bitmask.type, registry)
        if bitmask.bits:
            lines.append(f"{bitmask.name} = {base}  # bits: {bitmask.bits}")
        else:
            lines.append(f"{bitmask.name} = {base}")

    return "\n".join(lines)