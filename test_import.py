from ctypes import c_uint32, byref, pointer, c_float

from output.types import (
    VkApplicationInfo, VkInstanceCreateInfo,
    VkDeviceCreateInfo, VkDeviceQueueCreateInfo,
    VkPhysicalDeviceProperties,
)
from output.handles import VkInstance, VkDevice, VkPhysicalDevice
from output.loader import vkCreateInstance
from output.wrapper import Instance, Device

app_info = VkApplicationInfo(apiVersion=(1 << 22))
create_info = VkInstanceCreateInfo(pApplicationInfo=pointer(app_info))

raw_instance = VkInstance()
result = vkCreateInstance(byref(create_info), None, byref(raw_instance))
print("vkCreateInstance:", result)

instance = Instance(raw_instance)

# 2. Enumerate physical devices - now going through the wrapper, no manual byref/pointer needed
count = c_uint32(0)
instance.vkEnumeratePhysicalDevices(count, None)
print("Physical device count:", count.value)

devices_array = (VkPhysicalDevice * count.value)()
instance.vkEnumeratePhysicalDevices(count, devices_array)
physical_device = devices_array[0]

# 3. First-arg is VkPhysicalDevice, NOT the instance - tests the auto-prepend fix
props = VkPhysicalDeviceProperties()
instance.vkGetPhysicalDeviceProperties(physical_device, props)
print("GPU name:", props.deviceName.decode(errors="ignore"))

# 4. Create a logical device
priority = c_float(1.0)
queue_create_info = VkDeviceQueueCreateInfo(
    queueFamilyIndex=0,
    queueCount=1,
    pQueuePriorities=pointer(priority),
)
device_create_info = VkDeviceCreateInfo(
    queueCreateInfoCount=1,
    pQueueCreateInfos=pointer(queue_create_info),  # struct-holding-a-struct-pointer field - still pointer()
)

raw_device = VkDevice()
instance.vkCreateDevice(physical_device, device_create_info, None, raw_device)
device = Device(raw_device)
print("Device created:", raw_device)

# 5. Cleanup
device.vkDestroyDevice(None)
instance.vkDestroyInstance(None)
print("Done - no crash")