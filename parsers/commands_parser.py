
from model import Registry, Command
from .common import parse_member
from .base import Base_Parser

class Command_Parser(Base_Parser):
    selection = "commands"

    def parse(self, element, registry: Registry):
        for command_el in element.findall("command"):
            alias = command_el.get("alias")
            if alias:
                registry.commands[command_el.get("name")] = Command(
                    name=command_el.get("name"),
                    alias=alias,
                )
                continue

            proto = parse_member(command_el.find("proto"))
            params = [parse_member(p) for p in command_el.findall("param")]

            registry.commands[proto.name] = Command(
                name=proto.name,
                return_type=proto.type,
                params=params,
            )