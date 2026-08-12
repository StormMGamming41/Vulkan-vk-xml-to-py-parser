
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

@dataclass(slots=True)
class Enum_Value:
    name: str

    value: str | None = None
    bitpos: int | None = None

    type: C_Type | None = None

    alias: str | None = None
    comment: str | None = None

@dataclass(slots=True)
class Enums_Group:
    name: str
    type: str
    comment: str | None = None

    values: list[Enum_Value] = field(default_factory=list)

@dataclass(slots=True)
class Member:
    name: str
    type: C_Type
    array_len: str | None = None
    len: str | None = None
    optional: bool = False
    comment: str | None = None

@dataclass(slots=True)
class Struct:
    name: str
    is_union: bool = False
    members: list[Member] = field(default_factory=list)
    returnedonly: bool = False
    struct_extends: list[str] | None = None
    comment: str | None = None

@dataclass
class Registry:
    handles: dict[str, Handle] = field(default_factory=dict)
    basetypes: dict[str, Base_Type] = field(default_factory=dict)
    bitmasks: dict[str, Bitmask] = field(default_factory=dict)
    enums_groups: dict[str, Enums_Group] = field(default_factory=dict)
    structs_unions: dict[str, Struct] = field(default_factory=dict)
