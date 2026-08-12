from model import Registry, Struct, Member, C_Type
from .common import parse_member
from .base import Base_Parser

class Struct_Parser(Base_Parser):
    category = "struct"

    def parse(self, element, registry: Registry):
        self._parse_struct_or_union(element, registry, is_union=False)

    def _parse_struct_or_union(self, element, registry, is_union):
        name = element.get("name")
        extends = element.get("structextends")

        struct = Struct(
            name=name,
            is_union=is_union,
            members=[parse_member(m) for m in element.findall("member")],
            returnedonly=element.get("returnedonly") == "true",
            struct_extends=extends.split(",") if extends else None,
            comment=element.get("comment"),
        )
        registry.structs_unions[name] = struct


class Union_Parser(Struct_Parser):
    category = "union"

    def parse(self, element, registry: Registry):
        self._parse_struct_or_union(element, registry, is_union=True)