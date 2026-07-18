
import xml.etree.ElementTree as ET
# import debug
from model import Registry
from parsers.handle_parser import Handle_Parser
from parsers.basetype_parser import Base_Type_Parser
from parsers.bitmask_parser import Bitmask_Parser

class Registry_Parser:

    def __init__(self, filename: str):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

        self.parsers = {}

        self.register_parser(Handle_Parser())
        self.register_parser(Base_Type_Parser())
        self.register_parser(Bitmask_Parser())
    
    def register_parser(self, parser):
        self.parsers[parser.category] = parser

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
            parser = self.parsers.get(category)

            if parser:
                parser.parse(element, registry)
        
        return registry