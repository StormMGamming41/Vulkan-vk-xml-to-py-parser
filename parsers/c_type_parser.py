from model import C_Type

class C_Type_Parser:
    
    @staticmethod
    def from_xml(type_element):
        
        if type_element is None:
            return None
        
        text = type_element.text or ""

        if type_element.tail:
            text += type_element.tail.strip()
        
        return C_Type_Parser.parse(text)
    
    @staticmethod
    def parse(name: str) -> C_Type:

        pointer_level = name.count("*")

        name = name.replace("*", "").strip()

        const = False

        if name.startswith("const"):
            const = True
            name = name[6:]
        
        return C_Type(
            name=name,
            pointer_level=pointer_level,
            const=const
        )