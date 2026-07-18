
from model import Handle, Registry
from .base import Base_Parser

class Handle_Parser(Base_Parser):

    category: str = "handle"

    def parse(self, element, registry: Registry):

        handle = Handle(
            name=element.findtext("name"),
            parent=element.get("parent")
        )

        registry.handles[handle.name] = handle