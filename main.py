
from parser import Registry_Parser
from collections import Counter
import xml.etree.ElementTree as ET


registry = Registry_Parser("vk.xml").parse()
registry_parser = Registry_Parser("vk.xml")

types = registry_parser.root.find("types")
num_elem = 0

for element in types.findall("type"):
    if element.get("category") == "enum":
        print(ET.tostring(element, encoding="unicode"))
        print("-" * 50)
        num_elem += 1
print(num_elem)

counter = Counter()

print(len(registry.bitmasks))

# for bitmask in registry.bitmasks.values():
#     print(bitmask)
