from model import Registry, Enums_Group, Enum_Value, C_Type
from .base import Base_Parser

class Enums_Group_Parser(Base_Parser):

    selection = "enums"

    def parse(self, element, registry: Registry):
        name = element.get("name")
        enum_type = element.get("type")   # "enum" | "bitmask" | None (constants group)
        comment = element.get("comment")

        group = Enums_Group(name=name, type=enum_type, comment=comment)

        for enum_el in element.findall("enum"):
            ev_name = enum_el.get("name")
            value = enum_el.get("value")
            bitpos = enum_el.get("bitpos")
            alias = enum_el.get("alias")
            comment = enum_el.get("comment")
            type_attr = enum_el.get("type")
            ev_type = C_Type(name=type_attr) if type_attr else None

            group.values.append(Enum_Value(
                name=ev_name,
                value=value,
                bitpos=int(bitpos) if bitpos is not None else None,
                type=ev_type,
                alias=alias,
                comment=comment,
            ))

        registry.enums_groups[name] = group