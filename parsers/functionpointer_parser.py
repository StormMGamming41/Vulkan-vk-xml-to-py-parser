# parsers/functionpointer_parser.py
from model import Registry, Function_Pointer
from .common import parse_member
from .base import Base_Parser

class Function_Pointer_Parser(Base_Parser):
    category = "funcpointer"

    def parse(self, element, registry: Registry):
        proto = parse_member(element.find("proto"))
        params = [parse_member(p) for p in element.findall("param")]

        registry.function_pointers[proto.name] = Function_Pointer(
            name=proto.name,
            return_type=proto.type,
            params=params,
        )