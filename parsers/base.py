
from abc import ABC, abstractmethod

class Base_Parser(ABC):

    selection = "types"
    category = None

    @abstractmethod
    def parse(self, element, registry):
        raise NotImplementedError