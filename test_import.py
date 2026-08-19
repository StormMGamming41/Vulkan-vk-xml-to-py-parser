from ctypes import byref, pointer, cast, c_uint32

from output.types import VkApplicationInfo, VkInstanceCreateInfo
from output.enums import VkStructureType
from output.handles import VkInstance
from output.loader import vkCreateInstance, vkGetInstanceProcAddr
from output.commands import PFN_vkDestroyInstance, PFN_vkEnumeratePhysicalDevices

app_info = VkApplicationInfo()
app_info.sType = VkStructureType.VK_STRUCTURE_TYPE_APPLICATION_INFO
app_info.pApplicationName = b"Test"
app_info.apiVersion = (1 << 22)

create_info = VkInstanceCreateInfo()
create_info.sType = VkStructureType.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
create_info.pApplicationInfo = pointer(app_info)

instance = VkInstance()
result = vkCreateInstance(byref(create_info), None, byref(instance))
print("Result:", result)

enum_phys = cast(vkGetInstanceProcAddr(instance, b"vkEnumeratePhysicalDevices"), PFN_vkEnumeratePhysicalDevices)
count = c_uint32(0)
enum_phys(instance, byref(count), None)
print("Physical device count:", count.value)

destroy = cast(vkGetInstanceProcAddr(instance, b"vkDestroyInstance"), PFN_vkDestroyInstance)
destroy(instance, None)