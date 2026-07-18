
from abc import ABC, abstractmethod

class Base_Parser(ABC):

    @abstractmethod
    def parse(self, element, registry):
        raise NotImplementedError