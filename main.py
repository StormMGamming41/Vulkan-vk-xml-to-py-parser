
from resolve import topological_sort_structs, build_extension_map
from parser import Registry_Parser
from collections import Counter
import xml.etree.ElementTree as ET


registry = Registry_Parser("vk.xml").parse()
from resolve import topological_sort_structs, build_extension_map

registry = Registry_Parser("vk.xml").parse()
struct_order = topological_sort_structs(registry)
extension_map = build_extension_map(registry)

# print(len(struct_order))
# print(struct_order[:5])   # should be leaf structs with no by-value struct members - e.g. VkExtent2D, VkOffset2D
# print(extension_map["VkPhysicalDeviceFeatures2"][:5])  # should list several VkPhysicalDeviceXFeatures structs
 
# for element in types.findall("type"):
#     if element.get("category") == "enum":
#         print(ET.tostring(element, encoding="unicode"))
#         print("-" * 50)
#         num_elem += 1
# print(num_elem)

counter = Counter()

print(registry.commands["vkGetPhysicalDeviceFeatures2KHR"])

# print(len(registry.structs_unions))

# print(registry.structs_unions["VkClearColorValue"].is_union)
