from enum import IntEnum
from model import Registry
from resolve import resolve_group_values

def emit_constants_body(registry: Registry) -> str:
    group = registry.enums_groups.get("API Constants")
    if group is None:
        return ""

    lines = [""]

    for ev in group.values:
        raw = ev.value
        if raw is None:
            continue  # alias entries - handle separately if needed later

        if raw.endswith(("F", "f")):
            value = float(raw[:-1])
        elif raw.startswith("(~") and raw.endswith(")"):
            inner = raw[2:-1]  # strip "(~" and ")"
            bits = 64 if "ULL" in inner else 32
            value = (1 << bits) - 1
        else:
            value = int(raw, 0)

        lines.append(f"{ev.name} = {value}")

    return "\n".join(lines)

def emit_enums(registry: Registry) -> str:
    lines = ["from enum import IntEnum"]

    lines.append(emit_constants_body(registry))
    lines.append("")

    for group in registry.enums_groups.values():
        if group.type == "constants" or group.name == "API Constants":
            continue

        values = resolve_group_values(group)

        lines.append(f"class {group.name}(IntEnum):")
        seen = set()
        emitted = False
        for ev in group.values:
            if ev.name not in values:
                continue
            if ev.name in seen:
                continue
            seen.add(ev.name)
            lines.append(f"    {ev.name} = {values[ev.name]}")
            emitted = True
        if not emitted:
            lines.append("    pass")
        lines.append("")

    return "\n".join(lines)
