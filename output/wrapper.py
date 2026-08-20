import ctypes
from ctypes import byref, cast, Structure, Union, _SimpleCData

from .commands import *
from .loader import vkGetInstanceProcAddr, vkGetDeviceProcAddr


def is_pointer_type(t) -> bool:
    return hasattr(t, "_type_") and issubclass(t, ctypes._Pointer)


def needs_wrapping(value, expected_type) -> bool:
    if not is_pointer_type(expected_type):
        return False
    return isinstance(value, (Structure, Union, _SimpleCData))


class Instance:
    def __init__(self, handle):
        self._handle = handle
        self._cache = {}

    def __getattr__(self, name):
        if name in self._cache:
            return self._cache[name]

        addr = vkGetInstanceProcAddr(self._handle, name.encode())
        if not addr:
            raise AttributeError(f"{name} not available on this instance")

        pfn_type = globals()[f"PFN_{name}"]
        raw_fn = cast(addr, pfn_type)
        arg_types = pfn_type._argtypes_

        def wrapped(*args, _raw_fn=raw_fn, _arg_types=arg_types, _handle=self._handle):
            if _arg_types and _arg_types[0] is type(_handle):
                full_args = (_handle,) + args
            else:
                full_args = args

            converted = []
            for value, expected_type in zip(full_args, _arg_types):
                if needs_wrapping(value, expected_type):
                    converted.append(byref(value))
                else:
                    converted.append(value)
            return _raw_fn(*converted)

        self._cache[name] = wrapped
        return wrapped


class Device:
    def __init__(self, handle):
        self._handle = handle
        self._cache = {}

    def __getattr__(self, name):
        if name in self._cache:
            return self._cache[name]

        addr = vkGetDeviceProcAddr(self._handle, name.encode())
        if not addr:
            raise AttributeError(f"{name} not available on this device")

        pfn_type = globals()[f"PFN_{name}"]
        raw_fn = cast(addr, pfn_type)
        arg_types = pfn_type._argtypes_

        def wrapped(*args, _raw_fn=raw_fn, _arg_types=arg_types, _handle=self._handle):
            if _arg_types and _arg_types[0] is type(_handle):
                full_args = (_handle,) + args
            else:
                full_args = args

            converted = []
            for value, expected_type in zip(full_args, _arg_types):
                if needs_wrapping(value, expected_type):
                    converted.append(byref(value))
                else:
                    converted.append(value)
            return _raw_fn(*converted)

        self._cache[name] = wrapped
        return wrapped