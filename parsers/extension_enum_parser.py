from model import Registry, Enum_Value, C_Type
from .base import Base_Parser

BASE_VALUE = 1_000_000_000
RANGE_SIZE = 1_000

class Extension_Enum_Parser(Base_Parser):

    selection = "extensions"

    def parse(self, element, registry: Registry):
        for extension in element.findall("extension"):
            supported = extension.get("supported", "")
            if "vulkan" not in supported.split(","):
                continue

            number = int(extension.get("number"))

            for require in extension.findall("require"):
                for enum_el in require.findall("enum"):
                    extends = enum_el.get("extends")
                    if not extends:
                        continue  # not extending anything - e.g. a plain constant, alias, or feature bit reference

                    group = registry.enums_groups.get(extends)
                    if group is None:
                        continue  # TODO: think about whether this should ever happen

                    offset  = enum_el.get("offset")
                    bitpos  = enum_el.get("bitpos")
                    value   = enum_el.get("value")
                    op_dir  = enum_el.get("dir")
                    name    = enum_el.get("name")
                    type_   = enum_el.get("type")
                    alias   = enum_el.get("alias")
                    comment = enum_el.get("comment")

                    if (not value) and offset:
                        value = BASE_VALUE + (number - 1) * RANGE_SIZE + int(offset)
                        if op_dir == "-": value = -value
                        value = str(value)

                    registry.enums_groups[extends].values.append(
                        Enum_Value(
                            name=name,
                            value=value if value is not None else None,
                            bitpos=int(bitpos) if bitpos is not None else None,
                            type=C_Type(type_) if type_ is not None else None,
                            alias=alias,
                            comment=comment,
                        )
                    )