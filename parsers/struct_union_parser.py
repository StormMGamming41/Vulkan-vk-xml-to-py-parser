from model import Registry, Struct, Member, C_Type
from .base import Base_Parser

class Struct_Parser(Base_Parser):
    category = "struct"

    def parse_member(self, member_el) -> Member:
        type_el = member_el.find("type")
        name_el = member_el.find("name")

        pre_text = (member_el.text or "")
        const = "const" in pre_text

        between = (type_el.tail or "")
        pointer_level = between.count("*")

        after = (name_el.tail or "").strip()

        array_len = None
        enum_el = member_el.find("enum")
        if enum_el is not None:
            array_len = enum_el.text          # e.g. <member>...<name>uuid</name>[<enum>VK_UUID_SIZE</enum>]</member>
        elif after.startswith("["):
            array_len = after.strip("[]")     # e.g. "[4]" -> "4"

        c_type = C_Type(name=type_el.text, pointer_level=pointer_level, const=const)

        return Member(
            name=name_el.text,
            type=c_type,
            array_len=array_len,
            len=member_el.get("len"),
            optional=member_el.get("optional") == "true",
            comment=member_el.findtext("comment"),
        )

    def parse(self, element, registry: Registry):
        self._parse_struct_or_union(element, registry, is_union=False)

    def _parse_struct_or_union(self, element, registry, is_union):
        name = element.get("name")
        extends = element.get("structextends")

        struct = Struct(
            name=name,
            is_union=is_union,
            members=[self.parse_member(m) for m in element.findall("member")],
            returnedonly=element.get("returnedonly") == "true",
            struct_extends=extends.split(",") if extends else None,
            comment=element.get("comment"),
        )
        registry.structs_unions[name] = struct


class Union_Parser(Struct_Parser):
    category = "union"

    def parse(self, element, registry: Registry):
        self._parse_struct_or_union(element, registry, is_union=True)