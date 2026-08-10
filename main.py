
from parser import Registry_Parser
from collections import Counter
import xml.etree.ElementTree as ET


registry = Registry_Parser("vk.xml").parse()
registry_parser = Registry_Parser("vk.xml")

# for element in types.findall("type"):
#     if element.get("category") == "enum":
#         print(ET.tostring(element, encoding="unicode"))
#         print("-" * 50)
#         num_elem += 1
# print(num_elem)

counter = Counter()

result_group = registry.enums_groups["VkResult"]
print(len(result_group.values))  # should jump up from the base-only count

for ev in result_group.values:
    if ev.name == "VK_ERROR_OUT_OF_DATE_KHR":
        print(ev.name, ev.value)   # expect -1000001004
    if ev.name == "VK_SUBOPTIMAL_KHR":
        print(ev.name, ev.value)   # expect 1000001003 (positive, no dir)
