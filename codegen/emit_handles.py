
from model import Registry

def emit_handles(registry: Registry) -> str:
    lines = ["from ctypes import *", ""]
    for handle in registry.handles.values():
        if handle.alias:
            lines.append(f"{handle.name} = {handle.alias}")
            continue
        base = "c_void_p" if handle.dispatchable else "c_uint64"
        lines.append(f"class {handle.name}({base}):")
        lines.append("    pass")
        lines.append("")
    return "\n".join(lines)