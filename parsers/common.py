
from model import C_Type, Member
import re

def parse_member(member_el) -> Member:
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
        array_len = [enum_el.text]
    elif after:
        dims = re.findall(r"\[([^\]]+)\]", after)
        array_len = dims if dims else None
    else:
        array_len = None    # e.g. "[4]" -> "4"

    c_type = C_Type(name=type_el.text, pointer_level=pointer_level, const=const)

    return Member(
        name=name_el.text,
        type=c_type,
        array_len=array_len,
        len=member_el.get("len"),
        optional=member_el.get("optional") == "true",
        comment=member_el.findtext("comment"),
        default_value = member_el.get("values")
    )