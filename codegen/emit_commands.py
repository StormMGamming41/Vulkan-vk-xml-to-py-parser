
from model import Registry
from resolve import resolve_c_type

def emit_command_pointers(registry: Registry) -> str:
    lines = ["from ctypes import *", "from .types import *", "from .handles import *", "from .basetypes import *", ""]
    skipped = []

    skipped_names = set()

    for cmd in registry.commands.values():
        if cmd.alias:
            if cmd.alias in skipped_names:
                skipped.append(cmd.name)
                skipped_names.add(cmd.name)
                continue
            lines.append(f"PFN_{cmd.name} = PFN_{cmd.alias}")
            continue

        try:
            restype = resolve_c_type(cmd.return_type, registry)
            argtypes = [resolve_c_type(p.type, registry) for p in cmd.params]
        except ValueError:
            skipped.append(cmd.name)
            skipped_names.add(cmd.name)
            continue

        restype_str = restype if restype is not None else "None"
        args_str = ", ".join([restype_str] + argtypes)
        lines.append(f"PFN_{cmd.name} = CFUNCTYPE({args_str})")

    if skipped:
        print(f"Skipped {len(skipped)} commands (unresolvable types): {skipped}")

    return "\n".join(lines)