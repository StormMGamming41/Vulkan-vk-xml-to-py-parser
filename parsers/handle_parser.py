
from model import Handle, Registry
from .base import Base_Parser

class Handle_Parser(Base_Parser):

    category: str = "handle"

    def parse(self, element, registry: Registry):
        alias = element.get("alias")
        if alias:
            registry.handles[element.get("name")] = Handle(
                name=element.get("name"),
                dispatchable=registry.handles[alias].dispatchable,
                alias=alias,
            )
            return

        macro = element.findtext("type")
        dispatchable = macro == "VK_DEFINE_HANDLE"

        handle = Handle(
            name=element.findtext("name"),
            parent=element.get("parent"),
            dispatchable=dispatchable
        )

        registry.handles[handle.name] = handle