from ctypes import *

class VkInstance(c_void_p):
    pass

class VkPhysicalDevice(c_void_p):
    pass

class VkDevice(c_void_p):
    pass

class VkQueue(c_void_p):
    pass

class VkCommandBuffer(c_void_p):
    pass

class VkDeviceMemory(c_uint64):
    pass

class VkCommandPool(c_uint64):
    pass

class VkBuffer(c_uint64):
    pass

class VkBufferView(c_uint64):
    pass

class VkImage(c_uint64):
    pass

class VkImageView(c_uint64):
    pass

class VkShaderModule(c_uint64):
    pass

class VkPipeline(c_uint64):
    pass

class VkPipelineLayout(c_uint64):
    pass

class VkSampler(c_uint64):
    pass

class VkDescriptorSet(c_uint64):
    pass

class VkDescriptorSetLayout(c_uint64):
    pass

class VkDescriptorPool(c_uint64):
    pass

class VkFence(c_uint64):
    pass

class VkSemaphore(c_uint64):
    pass

class VkEvent(c_uint64):
    pass

class VkQueryPool(c_uint64):
    pass

class VkFramebuffer(c_uint64):
    pass

class VkRenderPass(c_uint64):
    pass

class VkPipelineCache(c_uint64):
    pass

class VkPipelineBinaryKHR(c_uint64):
    pass

class VkIndirectCommandsLayoutNV(c_uint64):
    pass

class VkIndirectCommandsLayoutEXT(c_uint64):
    pass

class VkIndirectExecutionSetEXT(c_uint64):
    pass

class VkDescriptorUpdateTemplate(c_uint64):
    pass

VkDescriptorUpdateTemplateKHR = VkDescriptorUpdateTemplate
class VkSamplerYcbcrConversion(c_uint64):
    pass

VkSamplerYcbcrConversionKHR = VkSamplerYcbcrConversion
class VkValidationCacheEXT(c_uint64):
    pass

class VkAccelerationStructureKHR(c_uint64):
    pass

class VkAccelerationStructureNV(c_uint64):
    pass

class VkPerformanceConfigurationINTEL(c_uint64):
    pass

class VkBufferCollectionFUCHSIA(c_uint64):
    pass

class VkDeferredOperationKHR(c_uint64):
    pass

class VkPrivateDataSlot(c_uint64):
    pass

VkPrivateDataSlotEXT = VkPrivateDataSlot
class VkCuModuleNVX(c_uint64):
    pass

class VkCuFunctionNVX(c_uint64):
    pass

class VkOpticalFlowSessionNV(c_uint64):
    pass

class VkMicromapEXT(c_uint64):
    pass

class VkShaderEXT(c_uint64):
    pass

class VkTensorARM(c_uint64):
    pass

class VkTensorViewARM(c_uint64):
    pass

class VkDataGraphPipelineSessionARM(c_uint64):
    pass

class VkShaderInstrumentationARM(c_uint64):
    pass

class VkDisplayKHR(c_uint64):
    pass

class VkDisplayModeKHR(c_uint64):
    pass

class VkSurfaceKHR(c_uint64):
    pass

class VkSwapchainKHR(c_uint64):
    pass

class VkDebugReportCallbackEXT(c_uint64):
    pass

class VkDebugUtilsMessengerEXT(c_uint64):
    pass

class VkVideoSessionKHR(c_uint64):
    pass

class VkVideoSessionParametersKHR(c_uint64):
    pass

class VkSemaphoreSciSyncPoolNV(c_uint64):
    pass

class VkCudaModuleNV(c_uint64):
    pass

class VkCudaFunctionNV(c_uint64):
    pass

class VkExternalComputeQueueNV(c_void_p):
    pass
