# loader.py
import platform
from ctypes import *
from .handles import VkInstance
from .commands import PFN_vkGetInstanceProcAddr, PFN_vkCreateInstance, PFN_vkGetDeviceProcAddr

def _load_vulkan_library():
    system = platform.system()
    try:
        if system == "Windows":
            return WinDLL("vulkan-1.dll")
        elif system == "Linux":
            return CDLL("libvulkan.so.1")
        elif system == "Darwin":
            return CDLL("libvulkan.dylib")
        raise RuntimeError(f"Unsupported platform: {system}")
    except OSError as e:
        raise RuntimeError(
            "Could not load the Vulkan runtime library. "
            "Make sure Vulkan-capable GPU drivers are installed."
        ) from e

_lib = _load_vulkan_library()

vkGetInstanceProcAddr = _lib.vkGetInstanceProcAddr
vkGetInstanceProcAddr.restype = PFN_vkGetInstanceProcAddr._restype_
vkGetInstanceProcAddr.argtypes = PFN_vkGetInstanceProcAddr._argtypes_

vkCreateInstance = _lib.vkCreateInstance
vkCreateInstance.restype = PFN_vkCreateInstance._restype_
vkCreateInstance.argtypes = PFN_vkCreateInstance._argtypes_

vkGetDeviceProcAddr = _lib.vkGetDeviceProcAddr
vkGetDeviceProcAddr.restype = PFN_vkGetDeviceProcAddr._restype_
vkGetDeviceProcAddr.argtypes = PFN_vkGetDeviceProcAddr._argtypes_
