
from dataclasses import dataclass, field

@dataclass(slots=True)
class Handle:
    name: str
    parent: str | None = None

@dataclass(slots=True)
class C_Type:
    name: str
    pointer_level: int = 0
    const: bool = False

    def __str__(self):
        result = ""

        if self.const:
            result += "const "
        
        result += self.name
        result += "*" * self.pointer_level

        return result

@dataclass(slots=True)
class Base_Type:
    name: str
    type: C_Type

@dataclass(slots=True)
class Bitmask:
    name: str
    type: C_Type
    bits: str | None = None

@dataclass
class Registry:
    handles: dict[str, Handle] = field(default_factory=dict)
    basetypes: dict[str, Base_Type] = field(default_factory=dict)
    bitmasks: dict[str, Bitmask] = field(default_factory=dict)
