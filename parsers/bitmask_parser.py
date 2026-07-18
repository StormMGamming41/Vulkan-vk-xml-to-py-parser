
from model import Registry, Bitmask
from parsers.c_type_parser import C_Type_Parser
from .base import Base_Parser

class Bitmask_Parser(Base_Parser):

    category: str = "bitmask"

    def parse(self, element, registry: Registry):

        #skip aliases for now
        if element.get("alias"):
            return
        
        type_element = element.find("type")

        if type_element is None:
            return
        
        c_type = C_Type_Parser.from_xml(element.find("type"))

        if c_type is None:
            return
        
        bitmask = Bitmask(
            name=element.findtext("name"),
            type=c_type,
            bits=element.get("bitvalues") or element.get("requires")
        )

        registry.bitmasks[bitmask.name] = bitmask