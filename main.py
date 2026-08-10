
from parser import Registry_Parser
from collections import Counter
import xml.etree.ElementTree as ET


registry = Registry_Parser("vk.xml").parse()
registry_parser = Registry_Parser("vk.xml")

types = registry_parser.root.find("types")
num_elem = 0

# for element in types.findall("type"):
#     if element.get("category") == "enum":
#         print(ET.tostring(element, encoding="unicode"))
#         print("-" * 50)
#         num_elem += 1
# print(num_elem)

counter = Counter()

print(sorted(registry.enums_groups.keys())[:10])
print("API Constants" in registry.enums_groups)

print(len(registry.enums_groups))
print("------------------------------")
print(registry.enums_groups["VkResult"].values)
