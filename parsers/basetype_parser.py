
from model import Base_Type, Registry
from parsers.c_type_parser import C_Type_Parser
from .base import Base_Parser

class Base_Type_Parser(Base_Parser):

    category: str = "basetype"

    def parse(self, element, registry: Registry):

        type_elem = element.find("type")

        if type_elem is None:
            return

        c_type = C_Type_Parser.from_xml(element.find("text"))
        
        if c_type is None:
            return
        
        basetype = Base_Type(
            name=element.findtext("name"),
            type=c_type
        )

        registry.basetypes[basetype.name] = basetype