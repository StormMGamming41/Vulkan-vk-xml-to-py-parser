
import xml.etree.ElementTree as ET
# import debug
from model import Registry
from parsers.handle_parser import Handle_Parser
from parsers.basetype_parser import Base_Type_Parser
from parsers.bitmask_parser import Bitmask_Parser
from parsers.enums_group_parser import Enums_Group_Parser
from parsers.extension_enum_parser import Extension_Enum_Parser

class Registry_Parser:

    def __init__(self, filename: str):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

        self.type_parsers = {}
        self.selection_parsers = {}

        self.register_parser(Handle_Parser())
        self.register_parser(Base_Type_Parser())
        self.register_parser(Bitmask_Parser())
        self.register_parser(Enums_Group_Parser())
        self.register_parser(Extension_Enum_Parser())
    
    def register_parser(self, parser):
        if parser.selection == "types":
            self.type_parsers[parser.category] = parser
        else:
            self.selection_parsers[parser.selection] = parser

    def parse(self) -> Registry:
        registry = Registry()

        types = self.root.find("types")

        ## For debigging purposes ##
        # for element in types.findall("type"):
        #     if element.findtext("name") == "VkRemoteAddressNV":
        #         debug.dump(element)
        #         break

        for element in types.findall("type"):
            
            category = element.get("category")
            parser = self.type_parsers.get(category)

            if parser:
                parser.parse(element, registry)

        for tag, parser in self.selection_parsers.items():
            for element in self.root.findall(tag):
                parser.parse(element, registry)
        
        return registry