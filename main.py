
from resolve import topological_sort_structs, build_extension_map
from parser import Registry_Parser
from model import Registry
from collections import Counter
import xml.etree.ElementTree as ET


registry = Registry_Parser("vk.xml").parse()
from resolve import topological_sort_structs, build_extension_map

registry = Registry_Parser("vk.xml").parse()
struct_order = topological_sort_structs(registry)
extension_map = build_extension_map(registry)
counter = Counter()

PRIMITIVE_MAP = {
    "void": None,          # special-cased — only valid behind a pointer
    "char": "c_char",
    "float": "c_float",
    "double": "c_double",
    "uint8_t": "c_uint8",
    "uint16_t": "c_uint16",
    "uint32_t": "c_uint32",
    "uint64_t": "c_uint64",
    "int8_t": "c_int8",
    "int16_t": "c_int16",
    "int32_t": "c_int32",
    "int64_t": "c_int64",
    "size_t": "c_size_t",
    "int": "c_int",
}

def resolve_type(name: str, registry: Registry) -> str:
    if name in PRIMITIVE_MAP:
        return PRIMITIVE_MAP[name]
    if name in registry.handles:
        return "c_void_p"
    if name in registry.basetypes:
        return resolve_type(registry.basetypes[name].type.name, registry)
    if name in registry.bitmasks:
        return resolve_type(registry.bitmasks[name].type.name, registry)
    if name in registry.enums_groups:
        return "c_int32"
    if name in registry.structs_unions:
        return name
    if name in registry.function_pointers:
        return name
    raise ValueError(f"{name} type cannot be resolved as c_type object")

print(resolve_type("VkQueueFlags", registry))