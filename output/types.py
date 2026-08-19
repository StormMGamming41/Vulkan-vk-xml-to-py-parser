from ctypes import *
from .enums import *

class VkBaseOutStructure(Structure):
    pass
class VkBaseInStructure(Structure):
    pass
class VkOffset2D(Structure):
    pass
class VkOffset3D(Structure):
    pass
class VkExtent2D(Structure):
    pass
class VkExtent3D(Structure):
    pass
class VkViewport(Structure):
    pass
class VkRect2D(Structure):
    pass
class VkClearRect(Structure):
    pass
class VkComponentMapping(Structure):
    pass
class VkPhysicalDeviceLimits(Structure):
    pass
class VkPhysicalDeviceSparseProperties(Structure):
    pass
class VkPhysicalDeviceProperties(Structure):
    pass
class VkExtensionProperties(Structure):
    pass
class VkLayerProperties(Structure):
    pass
class VkApplicationInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_APPLICATION_INFO
class VkAllocationCallbacks(Structure):
    pass
class VkDeviceQueueCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO
class VkDeviceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO
class VkInstanceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO
class VkQueueFamilyProperties(Structure):
    pass
class VkMemoryType(Structure):
    pass
class VkMemoryHeap(Structure):
    pass
class VkPhysicalDeviceMemoryProperties(Structure):
    pass
class VkMemoryAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO
class VkMemoryRequirements(Structure):
    pass
class VkSparseImageFormatProperties(Structure):
    pass
class VkSparseImageMemoryRequirements(Structure):
    pass
class VkMappedMemoryRange(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE
class VkFormatProperties(Structure):
    pass
class VkImageFormatProperties(Structure):
    pass
class VkDescriptorBufferInfo(Structure):
    pass
class VkDescriptorImageInfo(Structure):
    pass
class VkWriteDescriptorSet(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET
class VkCopyDescriptorSet(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET
class VkBufferUsageFlags2CreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_USAGE_FLAGS_2_CREATE_INFO
class VkBufferUsageFlags2CreateInfoKHR(Structure):
    pass
class VkBufferCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO
class VkBufferViewCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO
class VkImageSubresource(Structure):
    pass
class VkImageSubresourceLayers(Structure):
    pass
class VkImageSubresourceRange(Structure):
    pass
class VkMemoryBarrier(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_BARRIER
class VkBufferMemoryBarrier(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER
class VkImageMemoryBarrier(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER
class VkImageCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO
class VkSubresourceLayout(Structure):
    pass
class VkImageViewCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO
class VkBufferCopy(Structure):
    pass
class VkSparseMemoryBind(Structure):
    pass
class VkSparseImageMemoryBind(Structure):
    pass
class VkSparseBufferMemoryBindInfo(Structure):
    pass
class VkSparseImageOpaqueMemoryBindInfo(Structure):
    pass
class VkSparseImageMemoryBindInfo(Structure):
    pass
class VkBindSparseInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_SPARSE_INFO
class VkImageCopy(Structure):
    pass
class VkImageBlit(Structure):
    pass
class VkBufferImageCopy(Structure):
    pass
class VkStridedDeviceAddressRangeKHR(Structure):
    pass
class VkCopyMemoryIndirectCommandKHR(Structure):
    pass
class VkCopyMemoryIndirectCommandNV(Structure):
    pass
class VkCopyMemoryIndirectInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_INDIRECT_INFO_KHR
class VkCopyMemoryToImageIndirectCommandKHR(Structure):
    pass
class VkCopyMemoryToImageIndirectCommandNV(Structure):
    pass
class VkCopyMemoryToImageIndirectInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_TO_IMAGE_INDIRECT_INFO_KHR
class VkImageResolve(Structure):
    pass
class VkShaderModuleCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO
class VkDescriptorSetLayoutBinding(Structure):
    pass
class VkDescriptorSetLayoutCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO
class VkDescriptorPoolSize(Structure):
    pass
class VkDescriptorPoolCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO
class VkDescriptorSetAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO
class VkSpecializationMapEntry(Structure):
    pass
class VkSpecializationInfo(Structure):
    pass
class VkPipelineShaderStageCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO
class VkComputePipelineCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO
class VkComputePipelineIndirectBufferInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_INDIRECT_BUFFER_INFO_NV
class VkPipelineCreateFlags2CreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_CREATE_FLAGS_2_CREATE_INFO
class VkPipelineCreateFlags2CreateInfoKHR(Structure):
    pass
class VkVertexInputBindingDescription(Structure):
    pass
class VkVertexInputAttributeDescription(Structure):
    pass
class VkPipelineVertexInputStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO
class VkPipelineInputAssemblyStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO
class VkPipelineTessellationStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_STATE_CREATE_INFO
class VkPipelineViewportStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO
class VkPipelineRasterizationStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO
class VkPipelineMultisampleStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO
class VkPipelineColorBlendAttachmentState(Structure):
    pass
class VkPipelineColorBlendStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO
class VkPipelineDynamicStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO
class VkStencilOpState(Structure):
    pass
class VkPipelineDepthStencilStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_DEPTH_STENCIL_STATE_CREATE_INFO
class VkGraphicsPipelineCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO
class VkPipelineCacheCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_CACHE_CREATE_INFO
class VkPipelineCacheHeaderVersionOne(Structure):
    pass
class VkPipelineCacheStageValidationIndexEntry(Structure):
    pass
class VkPipelineCacheSafetyCriticalIndexEntry(Structure):
    pass
class VkPipelineCacheHeaderVersionSafetyCriticalOne(Structure):
    pass
class VkPipelineCacheHeaderVersionDataGraphQCOM(Structure):
    pass
class VkPushConstantRange(Structure):
    pass
class VkPipelineBinaryCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_BINARY_CREATE_INFO_KHR
class VkPipelineBinaryHandlesInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_BINARY_HANDLES_INFO_KHR
class VkPipelineBinaryDataKHR(Structure):
    pass
class VkPipelineBinaryKeysAndDataKHR(Structure):
    pass
class VkPipelineBinaryKeyKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_BINARY_KEY_KHR
class VkPipelineBinaryInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_BINARY_INFO_KHR
class VkReleaseCapturedPipelineDataInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RELEASE_CAPTURED_PIPELINE_DATA_INFO_KHR
class VkPipelineBinaryDataInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_BINARY_DATA_INFO_KHR
class VkPipelineCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_CREATE_INFO_KHR
class VkPipelineLayoutCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO
class VkSamplerCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO
class VkCommandPoolCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO
class VkCommandBufferAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO
class VkCommandBufferInheritanceInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO
class VkCommandBufferBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO
class VkRenderPassBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO
class VkClearColorValue(Union):
    pass
class VkClearDepthStencilValue(Structure):
    pass
class VkClearValue(Union):
    pass
class VkClearAttachment(Structure):
    pass
class VkAttachmentDescription(Structure):
    pass
class VkAttachmentReference(Structure):
    pass
class VkSubpassDescription(Structure):
    pass
class VkSubpassDependency(Structure):
    pass
class VkRenderPassCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO
class VkEventCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EVENT_CREATE_INFO
class VkFenceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FENCE_CREATE_INFO
class VkPhysicalDeviceFeatures(Structure):
    pass
class VkSemaphoreCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_CREATE_INFO
class VkQueryPoolCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO
class VkFramebufferCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO
class VkDrawIndirectCommand(Structure):
    pass
class VkDrawIndexedIndirectCommand(Structure):
    pass
class VkDispatchIndirectCommand(Structure):
    pass
class VkMultiDrawInfoEXT(Structure):
    pass
class VkMultiDrawIndexedInfoEXT(Structure):
    pass
class VkSubmitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBMIT_INFO
class VkDisplayPropertiesKHR(Structure):
    pass
class VkDisplayPlanePropertiesKHR(Structure):
    pass
class VkDisplayModeParametersKHR(Structure):
    pass
class VkDisplayModePropertiesKHR(Structure):
    pass
class VkDisplayModeCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_MODE_CREATE_INFO_KHR
class VkDisplayPlaneCapabilitiesKHR(Structure):
    pass
class VkDisplaySurfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR
class VkDisplaySurfaceStereoCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_SURFACE_STEREO_CREATE_INFO_NV
class VkDisplayPresentInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PRESENT_INFO_KHR
class VkSurfaceCapabilitiesKHR(Structure):
    pass
class VkAndroidSurfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_SURFACE_CREATE_INFO_KHR
class VkViSurfaceCreateInfoNN(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VI_SURFACE_CREATE_INFO_NN
class VkWaylandSurfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WAYLAND_SURFACE_CREATE_INFO_KHR
class VkUbmSurfaceCreateInfoSEC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_UBM_SURFACE_CREATE_INFO_SEC
class VkWin32SurfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WIN32_SURFACE_CREATE_INFO_KHR
class VkXlibSurfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_XLIB_SURFACE_CREATE_INFO_KHR
class VkXcbSurfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_XCB_SURFACE_CREATE_INFO_KHR
class VkDirectFBSurfaceCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DIRECTFB_SURFACE_CREATE_INFO_EXT
class VkImagePipeSurfaceCreateInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGEPIPE_SURFACE_CREATE_INFO_FUCHSIA
class VkStreamDescriptorSurfaceCreateInfoGGP(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_STREAM_DESCRIPTOR_SURFACE_CREATE_INFO_GGP
class VkScreenSurfaceCreateInfoQNX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SCREEN_SURFACE_CREATE_INFO_QNX
class VkSurfaceFormatKHR(Structure):
    pass
class VkSwapchainCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR
class VkPresentInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_INFO_KHR
class VkDebugReportCallbackCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_REPORT_CALLBACK_CREATE_INFO_EXT
class VkValidationFlagsEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VALIDATION_FLAGS_EXT
class VkValidationFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VALIDATION_FEATURES_EXT
class VkLayerSettingsCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_LAYER_SETTINGS_CREATE_INFO_EXT
class VkLayerSettingEXT(Structure):
    pass
class VkApplicationParametersEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_APPLICATION_PARAMETERS_EXT
class VkPipelineRasterizationStateRasterizationOrderAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_RASTERIZATION_ORDER_AMD
class VkDebugMarkerObjectNameInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_NAME_INFO_EXT
class VkDebugMarkerObjectTagInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_MARKER_OBJECT_TAG_INFO_EXT
class VkDebugMarkerMarkerInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_MARKER_MARKER_INFO_EXT
class VkDedicatedAllocationImageCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_IMAGE_CREATE_INFO_NV
class VkDedicatedAllocationBufferCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_BUFFER_CREATE_INFO_NV
class VkDedicatedAllocationMemoryAllocateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_MEMORY_ALLOCATE_INFO_NV
class VkExternalImageFormatPropertiesNV(Structure):
    pass
class VkExternalMemoryImageCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO_NV
class VkExportMemoryAllocateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO_NV
class VkImportMemoryWin32HandleInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_NV
class VkExportMemoryWin32HandleInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_NV
class VkExportMemorySciBufInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_MEMORY_SCI_BUF_INFO_NV
class VkImportMemorySciBufInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_SCI_BUF_INFO_NV
class VkMemoryGetSciBufInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_SCI_BUF_INFO_NV
class VkMemorySciBufPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_SCI_BUF_PROPERTIES_NV
class VkPhysicalDeviceExternalMemorySciBufFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_SCI_BUF_FEATURES_NV
class VkPhysicalDeviceExternalSciBufFeaturesNV(Structure):
    pass
class VkWin32KeyedMutexAcquireReleaseInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_NV
class VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_FEATURES_NV
class VkPushConstantBankInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_CONSTANT_BANK_INFO_NV
class VkPhysicalDevicePushConstantBankFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PUSH_CONSTANT_BANK_FEATURES_NV
class VkPhysicalDevicePushConstantBankPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PUSH_CONSTANT_BANK_PROPERTIES_NV
class VkPhysicalDeviceDeviceGeneratedCommandsComputeFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_COMPUTE_FEATURES_NV
class VkDevicePrivateDataCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_PRIVATE_DATA_CREATE_INFO
class VkDevicePrivateDataCreateInfoEXT(Structure):
    pass
class VkPrivateDataSlotCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRIVATE_DATA_SLOT_CREATE_INFO
class VkPrivateDataSlotCreateInfoEXT(Structure):
    pass
class VkPhysicalDevicePrivateDataFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIVATE_DATA_FEATURES
class VkPhysicalDevicePrivateDataFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV
class VkPhysicalDeviceClusterAccelerationStructureFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_ACCELERATION_STRUCTURE_FEATURES_NV
class VkPhysicalDeviceClusterAccelerationStructurePropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_ACCELERATION_STRUCTURE_PROPERTIES_NV
class VkStridedDeviceAddressNV(Structure):
    pass
class VkRayTracingPipelineClusterAccelerationStructureCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CLUSTER_ACCELERATION_STRUCTURE_CREATE_INFO_NV
class VkClusterAccelerationStructureGeometryIndexAndGeometryFlagsNV(Structure):
    pass
class VkClusterAccelerationStructureMoveObjectsInfoNV(Structure):
    pass
class VkClusterAccelerationStructureBuildClustersBottomLevelInfoNV(Structure):
    pass
class VkClusterAccelerationStructureGetTemplateIndicesInfoNV(Structure):
    pass
class VkClusterAccelerationStructureBuildTriangleClusterInfoNV(Structure):
    pass
class VkClusterAccelerationStructureBuildTriangleClusterTemplateInfoNV(Structure):
    pass
class VkClusterAccelerationStructureInstantiateClusterInfoNV(Structure):
    pass
class VkClusterAccelerationStructureClustersBottomLevelInputNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CLUSTER_ACCELERATION_STRUCTURE_CLUSTERS_BOTTOM_LEVEL_INPUT_NV
class VkClusterAccelerationStructureTriangleClusterInputNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CLUSTER_ACCELERATION_STRUCTURE_TRIANGLE_CLUSTER_INPUT_NV
class VkClusterAccelerationStructureMoveObjectsInputNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CLUSTER_ACCELERATION_STRUCTURE_MOVE_OBJECTS_INPUT_NV
class VkClusterAccelerationStructureOpInputNV(Union):
    pass
class VkClusterAccelerationStructureInputInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CLUSTER_ACCELERATION_STRUCTURE_INPUT_INFO_NV
class VkStridedDeviceAddressRegionKHR(Structure):
    pass
class VkClusterAccelerationStructureCommandsInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CLUSTER_ACCELERATION_STRUCTURE_COMMANDS_INFO_NV
class VkPhysicalDeviceMultiDrawPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTI_DRAW_PROPERTIES_EXT
class VkGraphicsShaderGroupCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GRAPHICS_SHADER_GROUP_CREATE_INFO_NV
class VkGraphicsPipelineShaderGroupsCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV
class VkBindShaderGroupIndirectCommandNV(Structure):
    pass
class VkBindIndexBufferIndirectCommandNV(Structure):
    pass
class VkBindVertexBufferIndirectCommandNV(Structure):
    pass
class VkSetStateFlagsIndirectCommandNV(Structure):
    pass
class VkIndirectCommandsStreamNV(Structure):
    pass
class VkIndirectCommandsLayoutTokenNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV
class VkIndirectCommandsLayoutCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV
class VkGeneratedCommandsInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV
class VkGeneratedCommandsMemoryRequirementsInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV
class VkPipelineIndirectDeviceAddressInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_INDIRECT_DEVICE_ADDRESS_INFO_NV
class VkBindPipelineIndirectCommandNV(Structure):
    pass
class VkPhysicalDeviceFeatures2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2
class VkPhysicalDeviceFeatures2KHR(Structure):
    pass
class VkPhysicalDeviceProperties2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROPERTIES_2
class VkPhysicalDeviceProperties2KHR(Structure):
    pass
class VkFormatProperties2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2
class VkFormatProperties2KHR(Structure):
    pass
class VkImageFormatProperties2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2
class VkImageFormatProperties2KHR(Structure):
    pass
class VkPhysicalDeviceImageFormatInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2
class VkPhysicalDeviceImageFormatInfo2KHR(Structure):
    pass
class VkQueueFamilyProperties2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_PROPERTIES_2
class VkQueueFamilyProperties2KHR(Structure):
    pass
class VkPhysicalDeviceMemoryProperties2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2
class VkPhysicalDeviceMemoryProperties2KHR(Structure):
    pass
class VkSparseImageFormatProperties2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SPARSE_IMAGE_FORMAT_PROPERTIES_2
class VkSparseImageFormatProperties2KHR(Structure):
    pass
class VkPhysicalDeviceSparseImageFormatInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2
class VkPhysicalDeviceSparseImageFormatInfo2KHR(Structure):
    pass
class VkPhysicalDevicePushDescriptorProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PUSH_DESCRIPTOR_PROPERTIES
class VkPhysicalDevicePushDescriptorPropertiesKHR(Structure):
    pass
class VkConformanceVersion(Structure):
    pass
class VkConformanceVersionKHR(Structure):
    pass
class VkPhysicalDeviceDriverProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRIVER_PROPERTIES
class VkPhysicalDeviceDriverPropertiesKHR(Structure):
    pass
class VkPresentRegionsKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_REGIONS_KHR
class VkPresentRegionKHR(Structure):
    pass
class VkRectLayerKHR(Structure):
    pass
class VkPhysicalDeviceVariablePointersFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VARIABLE_POINTERS_FEATURES
class VkPhysicalDeviceVariablePointersFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceVariablePointerFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceVariablePointerFeatures(Structure):
    pass
class VkExternalMemoryProperties(Structure):
    pass
class VkExternalMemoryPropertiesKHR(Structure):
    pass
class VkPhysicalDeviceExternalImageFormatInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_IMAGE_FORMAT_INFO
class VkPhysicalDeviceExternalImageFormatInfoKHR(Structure):
    pass
class VkExternalImageFormatProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_IMAGE_FORMAT_PROPERTIES
class VkExternalImageFormatPropertiesKHR(Structure):
    pass
class VkPhysicalDeviceExternalBufferInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO
class VkPhysicalDeviceExternalBufferInfoKHR(Structure):
    pass
class VkExternalBufferProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES
class VkExternalBufferPropertiesKHR(Structure):
    pass
class VkPhysicalDeviceIDProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ID_PROPERTIES
class VkPhysicalDeviceIDPropertiesKHR(Structure):
    pass
class VkExternalMemoryImageCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO
class VkExternalMemoryImageCreateInfoKHR(Structure):
    pass
class VkExternalMemoryBufferCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO
class VkExternalMemoryBufferCreateInfoKHR(Structure):
    pass
class VkExportMemoryAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_MEMORY_ALLOCATE_INFO
class VkExportMemoryAllocateInfoKHR(Structure):
    pass
class VkImportMemoryWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_WIN32_HANDLE_INFO_KHR
class VkExportMemoryWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_KHR
class VkImportMemoryZirconHandleInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_ZIRCON_HANDLE_INFO_FUCHSIA
class VkMemoryZirconHandlePropertiesFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_ZIRCON_HANDLE_PROPERTIES_FUCHSIA
class VkMemoryGetZirconHandleInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_ZIRCON_HANDLE_INFO_FUCHSIA
class VkMemoryWin32HandlePropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_WIN32_HANDLE_PROPERTIES_KHR
class VkMemoryGetWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_WIN32_HANDLE_INFO_KHR
class VkImportMemoryFdInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_FD_INFO_KHR
class VkMemoryFdPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_FD_PROPERTIES_KHR
class VkMemoryGetFdInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_FD_INFO_KHR
class VkWin32KeyedMutexAcquireReleaseInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WIN32_KEYED_MUTEX_ACQUIRE_RELEASE_INFO_KHR
class VkImportMemoryMetalHandleInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_METAL_HANDLE_INFO_EXT
class VkMemoryMetalHandlePropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_METAL_HANDLE_PROPERTIES_EXT
class VkMemoryGetMetalHandleInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_METAL_HANDLE_INFO_EXT
class VkPhysicalDeviceExternalSemaphoreInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO
class VkPhysicalDeviceExternalSemaphoreInfoKHR(Structure):
    pass
class VkExternalSemaphoreProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES
class VkExternalSemaphorePropertiesKHR(Structure):
    pass
class VkExportSemaphoreCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_CREATE_INFO
class VkExportSemaphoreCreateInfoKHR(Structure):
    pass
class VkImportSemaphoreWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR
class VkExportSemaphoreWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR
class VkD3D12FenceSubmitInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR
class VkSemaphoreGetWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_GET_WIN32_HANDLE_INFO_KHR
class VkImportSemaphoreFdInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_FD_INFO_KHR
class VkSemaphoreGetFdInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_GET_FD_INFO_KHR
class VkImportSemaphoreZirconHandleInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_ZIRCON_HANDLE_INFO_FUCHSIA
class VkSemaphoreGetZirconHandleInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_GET_ZIRCON_HANDLE_INFO_FUCHSIA
class VkPhysicalDeviceExternalFenceInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FENCE_INFO
class VkPhysicalDeviceExternalFenceInfoKHR(Structure):
    pass
class VkExternalFenceProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_FENCE_PROPERTIES
class VkExternalFencePropertiesKHR(Structure):
    pass
class VkExportFenceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_FENCE_CREATE_INFO
class VkExportFenceCreateInfoKHR(Structure):
    pass
class VkImportFenceWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_FENCE_WIN32_HANDLE_INFO_KHR
class VkExportFenceWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_FENCE_WIN32_HANDLE_INFO_KHR
class VkFenceGetWin32HandleInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FENCE_GET_WIN32_HANDLE_INFO_KHR
class VkImportFenceFdInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR
class VkFenceGetFdInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FENCE_GET_FD_INFO_KHR
class VkExportFenceSciSyncInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_FENCE_SCI_SYNC_INFO_NV
class VkImportFenceSciSyncInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_FENCE_SCI_SYNC_INFO_NV
class VkFenceGetSciSyncInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FENCE_GET_SCI_SYNC_INFO_NV
class VkExportSemaphoreSciSyncInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_SEMAPHORE_SCI_SYNC_INFO_NV
class VkImportSemaphoreSciSyncInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_SCI_SYNC_INFO_NV
class VkSemaphoreGetSciSyncInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_GET_SCI_SYNC_INFO_NV
class VkSciSyncAttributesInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SCI_SYNC_ATTRIBUTES_INFO_NV
class VkPhysicalDeviceExternalSciSyncFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SCI_SYNC_FEATURES_NV
class VkPhysicalDeviceExternalSciSync2FeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SCI_SYNC_2_FEATURES_NV
class VkSemaphoreSciSyncPoolCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_SCI_SYNC_POOL_CREATE_INFO_NV
class VkSemaphoreSciSyncCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_SCI_SYNC_CREATE_INFO_NV
class VkDeviceSemaphoreSciSyncPoolReservationCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_SEMAPHORE_SCI_SYNC_POOL_RESERVATION_CREATE_INFO_NV
class VkPhysicalDeviceMultiviewFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_FEATURES
class VkPhysicalDeviceMultiviewFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceMultiviewProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PROPERTIES
class VkPhysicalDeviceMultiviewPropertiesKHR(Structure):
    pass
class VkRenderPassMultiviewCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO
class VkRenderPassMultiviewCreateInfoKHR(Structure):
    pass
class VkSurfaceCapabilities2EXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT
class VkDisplayPowerInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_POWER_INFO_EXT
class VkDeviceEventInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_EVENT_INFO_EXT
class VkDisplayEventInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_EVENT_INFO_EXT
class VkSwapchainCounterCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_COUNTER_CREATE_INFO_EXT
class VkPhysicalDeviceGroupProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GROUP_PROPERTIES
class VkPhysicalDeviceGroupPropertiesKHR(Structure):
    pass
class VkMemoryAllocateFlagsInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_FLAGS_INFO
class VkMemoryAllocateFlagsInfoKHR(Structure):
    pass
class VkBindBufferMemoryInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO
class VkBindBufferMemoryInfoKHR(Structure):
    pass
class VkBindBufferMemoryDeviceGroupInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO
class VkBindBufferMemoryDeviceGroupInfoKHR(Structure):
    pass
class VkBindImageMemoryInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO
class VkBindImageMemoryInfoKHR(Structure):
    pass
class VkBindImageMemoryDeviceGroupInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_DEVICE_GROUP_INFO
class VkBindImageMemoryDeviceGroupInfoKHR(Structure):
    pass
class VkDeviceGroupRenderPassBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_RENDER_PASS_BEGIN_INFO
class VkDeviceGroupRenderPassBeginInfoKHR(Structure):
    pass
class VkDeviceGroupCommandBufferBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_COMMAND_BUFFER_BEGIN_INFO
class VkDeviceGroupCommandBufferBeginInfoKHR(Structure):
    pass
class VkDeviceGroupSubmitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO
class VkDeviceGroupSubmitInfoKHR(Structure):
    pass
class VkDeviceGroupBindSparseInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO
class VkDeviceGroupBindSparseInfoKHR(Structure):
    pass
class VkDeviceGroupPresentCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_CAPABILITIES_KHR
class VkImageSwapchainCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_SWAPCHAIN_CREATE_INFO_KHR
class VkBindImageMemorySwapchainInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_SWAPCHAIN_INFO_KHR
class VkAcquireNextImageInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR
class VkDeviceGroupPresentInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_PRESENT_INFO_KHR
class VkDeviceGroupDeviceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_DEVICE_CREATE_INFO
class VkDeviceGroupDeviceCreateInfoKHR(Structure):
    pass
class VkDeviceGroupSwapchainCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_GROUP_SWAPCHAIN_CREATE_INFO_KHR
class VkDescriptorUpdateTemplateEntry(Structure):
    pass
class VkDescriptorUpdateTemplateEntryKHR(Structure):
    pass
class VkDescriptorUpdateTemplateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO
class VkDescriptorUpdateTemplateCreateInfoKHR(Structure):
    pass
class VkXYColorEXT(Structure):
    pass
class VkPhysicalDevicePresentIdFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_ID_FEATURES_KHR
class VkPresentIdKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_ID_KHR
class VkPhysicalDevicePresentId2FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_ID_2_FEATURES_KHR
class VkPresentId2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_ID_2_KHR
class VkPresentWait2InfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_WAIT_2_INFO_KHR
class VkPhysicalDevicePresentWaitFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_WAIT_FEATURES_KHR
class VkPhysicalDevicePresentWait2FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_WAIT_2_FEATURES_KHR
class VkPhysicalDevicePresentTimingFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_TIMING_FEATURES_EXT
class VkPresentTimingSurfaceCapabilitiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_TIMING_SURFACE_CAPABILITIES_EXT
class VkSwapchainTimingPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_TIMING_PROPERTIES_EXT
class VkSwapchainTimeDomainPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_TIME_DOMAIN_PROPERTIES_EXT
class VkPresentStageTimeEXT(Structure):
    pass
class VkPastPresentationTimingInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PAST_PRESENTATION_TIMING_INFO_EXT
class VkPastPresentationTimingPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PAST_PRESENTATION_TIMING_PROPERTIES_EXT
class VkPastPresentationTimingEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PAST_PRESENTATION_TIMING_EXT
class VkPresentTimingsInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_TIMINGS_INFO_EXT
class VkPresentTimingInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_TIMING_INFO_EXT
class VkSwapchainCalibratedTimestampInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_CALIBRATED_TIMESTAMP_INFO_EXT
class VkHdrMetadataEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_HDR_METADATA_EXT
class VkHdrVividDynamicMetadataHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_HDR_VIVID_DYNAMIC_METADATA_HUAWEI
class VkDisplayNativeHdrSurfaceCapabilitiesAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_NATIVE_HDR_SURFACE_CAPABILITIES_AMD
class VkSwapchainDisplayNativeHdrCreateInfoAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_DISPLAY_NATIVE_HDR_CREATE_INFO_AMD
class VkRefreshCycleDurationGOOGLE(Structure):
    pass
class VkPastPresentationTimingGOOGLE(Structure):
    pass
class VkPresentTimesInfoGOOGLE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE
class VkPresentTimeGOOGLE(Structure):
    pass
class VkIOSSurfaceCreateInfoMVK(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IOS_SURFACE_CREATE_INFO_MVK
class VkMacOSSurfaceCreateInfoMVK(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MACOS_SURFACE_CREATE_INFO_MVK
class VkMetalSurfaceCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_METAL_SURFACE_CREATE_INFO_EXT
class VkViewportWScalingNV(Structure):
    pass
class VkPipelineViewportWScalingStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_W_SCALING_STATE_CREATE_INFO_NV
class VkViewportSwizzleNV(Structure):
    pass
class VkPipelineViewportSwizzleStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SWIZZLE_STATE_CREATE_INFO_NV
class VkPhysicalDeviceDiscardRectanglePropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DISCARD_RECTANGLE_PROPERTIES_EXT
class VkPipelineDiscardRectangleStateCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_DISCARD_RECTANGLE_STATE_CREATE_INFO_EXT
class VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PER_VIEW_ATTRIBUTES_PROPERTIES_NVX
class VkInputAttachmentAspectReference(Structure):
    pass
class VkInputAttachmentAspectReferenceKHR(Structure):
    pass
class VkRenderPassInputAttachmentAspectCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO
class VkRenderPassInputAttachmentAspectCreateInfoKHR(Structure):
    pass
class VkPhysicalDeviceSurfaceInfo2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR
class VkSurfaceCapabilities2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR
class VkSurfaceFormat2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR
class VkDisplayProperties2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR
class VkDisplayPlaneProperties2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PLANE_PROPERTIES_2_KHR
class VkDisplayModeProperties2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_MODE_PROPERTIES_2_KHR
class VkDisplayModeStereoPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_MODE_STEREO_PROPERTIES_NV
class VkDisplayPlaneInfo2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PLANE_INFO_2_KHR
class VkDisplayPlaneCapabilities2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPLAY_PLANE_CAPABILITIES_2_KHR
class VkSharedPresentSurfaceCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHARED_PRESENT_SURFACE_CAPABILITIES_KHR
class VkPhysicalDevice16BitStorageFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES
class VkPhysicalDevice16BitStorageFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceSubgroupProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_PROPERTIES
class VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_EXTENDED_TYPES_FEATURES
class VkPhysicalDeviceShaderSubgroupExtendedTypesFeaturesKHR(Structure):
    pass
class VkBufferMemoryRequirementsInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_MEMORY_REQUIREMENTS_INFO_2
class VkBufferMemoryRequirementsInfo2KHR(Structure):
    pass
class VkDeviceBufferMemoryRequirements(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_BUFFER_MEMORY_REQUIREMENTS
class VkDeviceBufferMemoryRequirementsKHR(Structure):
    pass
class VkImageMemoryRequirementsInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2
class VkImageMemoryRequirementsInfo2KHR(Structure):
    pass
class VkImageSparseMemoryRequirementsInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_SPARSE_MEMORY_REQUIREMENTS_INFO_2
class VkImageSparseMemoryRequirementsInfo2KHR(Structure):
    pass
class VkDeviceImageMemoryRequirements(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_IMAGE_MEMORY_REQUIREMENTS
class VkDeviceImageMemoryRequirementsKHR(Structure):
    pass
class VkMemoryRequirements2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_REQUIREMENTS_2
class VkMemoryRequirements2KHR(Structure):
    pass
class VkSparseImageMemoryRequirements2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SPARSE_IMAGE_MEMORY_REQUIREMENTS_2
class VkSparseImageMemoryRequirements2KHR(Structure):
    pass
class VkPhysicalDevicePointClippingProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_POINT_CLIPPING_PROPERTIES
class VkPhysicalDevicePointClippingPropertiesKHR(Structure):
    pass
class VkMemoryDedicatedRequirements(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_DEDICATED_REQUIREMENTS
class VkMemoryDedicatedRequirementsKHR(Structure):
    pass
class VkMemoryDedicatedAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO
class VkMemoryDedicatedAllocateInfoKHR(Structure):
    pass
class VkImageViewUsageCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_USAGE_CREATE_INFO
class VkImageViewSlicedCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_SLICED_CREATE_INFO_EXT
class VkImageViewUsageCreateInfoKHR(Structure):
    pass
class VkPipelineTessellationDomainOriginStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_DOMAIN_ORIGIN_STATE_CREATE_INFO
class VkPipelineTessellationDomainOriginStateCreateInfoKHR(Structure):
    pass
class VkSamplerYcbcrConversionInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO
class VkSamplerYcbcrConversionInfoKHR(Structure):
    pass
class VkSamplerYcbcrConversionCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO
class VkSamplerYcbcrConversionCreateInfoKHR(Structure):
    pass
class VkBindImagePlaneMemoryInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_IMAGE_PLANE_MEMORY_INFO
class VkBindImagePlaneMemoryInfoKHR(Structure):
    pass
class VkImagePlaneMemoryRequirementsInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_PLANE_MEMORY_REQUIREMENTS_INFO
class VkImagePlaneMemoryRequirementsInfoKHR(Structure):
    pass
class VkPhysicalDeviceSamplerYcbcrConversionFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_YCBCR_CONVERSION_FEATURES
class VkPhysicalDeviceSamplerYcbcrConversionFeaturesKHR(Structure):
    pass
class VkSamplerYcbcrConversionImageFormatProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_IMAGE_FORMAT_PROPERTIES
class VkSamplerYcbcrConversionImageFormatPropertiesKHR(Structure):
    pass
class VkTextureLODGatherFormatPropertiesAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TEXTURE_LOD_GATHER_FORMAT_PROPERTIES_AMD
class VkConditionalRenderingBeginInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT
class VkProtectedSubmitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PROTECTED_SUBMIT_INFO
class VkPhysicalDeviceProtectedMemoryFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROTECTED_MEMORY_FEATURES
class VkPhysicalDeviceProtectedMemoryProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROTECTED_MEMORY_PROPERTIES
class VkDeviceQueueInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_QUEUE_INFO_2
class VkPipelineCoverageToColorStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_TO_COLOR_STATE_CREATE_INFO_NV
class VkPhysicalDeviceSamplerFilterMinmaxProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLER_FILTER_MINMAX_PROPERTIES
class VkPhysicalDeviceSamplerFilterMinmaxPropertiesEXT(Structure):
    pass
class VkSampleLocationEXT(Structure):
    pass
class VkSampleLocationsInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT
class VkAttachmentSampleLocationsEXT(Structure):
    pass
class VkSubpassSampleLocationsEXT(Structure):
    pass
class VkRenderPassSampleLocationsBeginInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT
class VkPipelineSampleLocationsStateCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT
class VkPhysicalDeviceSampleLocationsPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT
class VkMultisamplePropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MULTISAMPLE_PROPERTIES_EXT
class VkSamplerReductionModeCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO
class VkSamplerReductionModeCreateInfoEXT(Structure):
    pass
class VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_FEATURES_EXT
class VkPhysicalDeviceMultiDrawFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTI_DRAW_FEATURES_EXT
class VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BLEND_OPERATION_ADVANCED_PROPERTIES_EXT
class VkPipelineColorBlendAdvancedStateCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_ADVANCED_STATE_CREATE_INFO_EXT
class VkPhysicalDeviceInlineUniformBlockFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_FEATURES
class VkPhysicalDeviceInlineUniformBlockFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceInlineUniformBlockProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES
class VkPhysicalDeviceInlineUniformBlockPropertiesEXT(Structure):
    pass
class VkWriteDescriptorSetInlineUniformBlock(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_INLINE_UNIFORM_BLOCK
class VkWriteDescriptorSetInlineUniformBlockEXT(Structure):
    pass
class VkDescriptorPoolInlineUniformBlockCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_INLINE_UNIFORM_BLOCK_CREATE_INFO
class VkDescriptorPoolInlineUniformBlockCreateInfoEXT(Structure):
    pass
class VkPipelineCoverageModulationStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_MODULATION_STATE_CREATE_INFO_NV
class VkImageFormatListCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO
class VkImageFormatListCreateInfoKHR(Structure):
    pass
class VkValidationCacheCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT
class VkShaderModuleValidationCacheCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_MODULE_VALIDATION_CACHE_CREATE_INFO_EXT
class VkPhysicalDeviceMaintenance3Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_3_PROPERTIES
class VkPhysicalDeviceMaintenance3PropertiesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance4Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_4_FEATURES
class VkPhysicalDeviceMaintenance4FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance4Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_4_PROPERTIES
class VkPhysicalDeviceMaintenance4PropertiesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance5Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_5_FEATURES
class VkPhysicalDeviceMaintenance5FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance5Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_5_PROPERTIES
class VkPhysicalDeviceMaintenance5PropertiesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance6Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_6_FEATURES
class VkPhysicalDeviceMaintenance6FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance6Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_6_PROPERTIES
class VkPhysicalDeviceMaintenance6PropertiesKHR(Structure):
    pass
class VkPhysicalDeviceMaintenance7FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_7_FEATURES_KHR
class VkPhysicalDeviceMaintenance7PropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_7_PROPERTIES_KHR
class VkPhysicalDeviceLayeredApiPropertiesListKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_PROPERTIES_LIST_KHR
class VkPhysicalDeviceLayeredApiPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_PROPERTIES_KHR
class VkPhysicalDeviceLayeredApiVulkanPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_API_VULKAN_PROPERTIES_KHR
class VkPhysicalDeviceMaintenance8FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_8_FEATURES_KHR
class VkPhysicalDeviceMaintenance9FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_9_FEATURES_KHR
class VkPhysicalDeviceMaintenance9PropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_9_PROPERTIES_KHR
class VkPhysicalDeviceMaintenance11FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_11_FEATURES_KHR
class VkPhysicalDeviceMaintenance10PropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_10_PROPERTIES_KHR
class VkPhysicalDeviceMaintenance10FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_10_FEATURES_KHR
class VkQueueFamilyOwnershipTransferPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_OWNERSHIP_TRANSFER_PROPERTIES_KHR
class VkQueueFamilyOptimalImageTransferGranularityPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_OPTIMAL_IMAGE_TRANSFER_GRANULARITY_PROPERTIES_KHR
class VkRenderingAreaInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_AREA_INFO
class VkRenderingAreaInfoKHR(Structure):
    pass
class VkDescriptorSetLayoutSupport(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT
class VkDescriptorSetLayoutSupportKHR(Structure):
    pass
class VkPhysicalDeviceShaderDrawParametersFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DRAW_PARAMETERS_FEATURES
class VkPhysicalDeviceShaderDrawParameterFeatures(Structure):
    pass
class VkPhysicalDeviceShaderFloat16Int8Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT16_INT8_FEATURES
class VkPhysicalDeviceShaderFloat16Int8FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceFloat16Int8FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceFloatControlsProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT_CONTROLS_PROPERTIES
class VkPhysicalDeviceFloatControlsPropertiesKHR(Structure):
    pass
class VkPhysicalDeviceHostQueryResetFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_QUERY_RESET_FEATURES
class VkPhysicalDeviceHostQueryResetFeaturesEXT(Structure):
    pass
class VkNativeBufferUsage2ANDROID(Structure):
    pass
class VkNativeBufferANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_NATIVE_BUFFER_ANDROID
class VkSwapchainImageCreateInfoANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_IMAGE_CREATE_INFO_ANDROID
class VkPhysicalDevicePresentationPropertiesANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENTATION_PROPERTIES_ANDROID
class VkShaderResourceUsageAMD(Structure):
    pass
class VkShaderStatisticsInfoAMD(Structure):
    pass
class VkDeviceQueueGlobalPriorityCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_QUEUE_GLOBAL_PRIORITY_CREATE_INFO
class VkDeviceQueueGlobalPriorityCreateInfoKHR(Structure):
    pass
class VkDeviceQueueGlobalPriorityCreateInfoEXT(Structure):
    pass
class VkPhysicalDeviceGlobalPriorityQueryFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GLOBAL_PRIORITY_QUERY_FEATURES
class VkPhysicalDeviceGlobalPriorityQueryFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceGlobalPriorityQueryFeaturesEXT(Structure):
    pass
class VkQueueFamilyGlobalPriorityProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_GLOBAL_PRIORITY_PROPERTIES
class VkQueueFamilyGlobalPriorityPropertiesKHR(Structure):
    pass
class VkQueueFamilyGlobalPriorityPropertiesEXT(Structure):
    pass
class VkDebugUtilsObjectNameInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_NAME_INFO_EXT
class VkDebugUtilsObjectTagInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_TAG_INFO_EXT
class VkDebugUtilsLabelEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT
class VkDebugUtilsMessengerCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT
class VkDebugUtilsMessengerCallbackDataEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT
class VkPhysicalDeviceDeviceMemoryReportFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_MEMORY_REPORT_FEATURES_EXT
class VkDeviceDeviceMemoryReportCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_DEVICE_MEMORY_REPORT_CREATE_INFO_EXT
class VkDeviceMemoryReportCallbackDataEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT
class VkImportMemoryHostPointerInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_HOST_POINTER_INFO_EXT
class VkMemoryHostPointerPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_HOST_POINTER_PROPERTIES_EXT
class VkPhysicalDeviceExternalMemoryHostPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_HOST_PROPERTIES_EXT
class VkPhysicalDeviceConservativeRasterizationPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT
class VkCalibratedTimestampInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CALIBRATED_TIMESTAMP_INFO_KHR
class VkCalibratedTimestampInfoEXT(Structure):
    pass
class VkPhysicalDeviceShaderCorePropertiesAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_AMD
class VkPhysicalDeviceShaderCoreProperties2AMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_2_AMD
class VkPipelineRasterizationConservativeStateCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_CONSERVATIVE_STATE_CREATE_INFO_EXT
class VkPhysicalDeviceDescriptorIndexingFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_FEATURES
class VkPhysicalDeviceDescriptorIndexingFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceDescriptorIndexingProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_INDEXING_PROPERTIES
class VkPhysicalDeviceDescriptorIndexingPropertiesEXT(Structure):
    pass
class VkDescriptorSetLayoutBindingFlagsCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO
class VkDescriptorSetLayoutBindingFlagsCreateInfoEXT(Structure):
    pass
class VkDescriptorSetVariableDescriptorCountAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO
class VkDescriptorSetVariableDescriptorCountAllocateInfoEXT(Structure):
    pass
class VkDescriptorSetVariableDescriptorCountLayoutSupport(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT
class VkDescriptorSetVariableDescriptorCountLayoutSupportEXT(Structure):
    pass
class VkAttachmentDescription2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2
class VkAttachmentDescription2KHR(Structure):
    pass
class VkAttachmentReference2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2
class VkAttachmentReference2KHR(Structure):
    pass
class VkSubpassDescription2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2
class VkSubpassDescription2KHR(Structure):
    pass
class VkSubpassDependency2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2
class VkSubpassDependency2KHR(Structure):
    pass
class VkRenderPassCreateInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2
class VkRenderPassCreateInfo2KHR(Structure):
    pass
class VkSubpassBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_BEGIN_INFO
class VkSubpassBeginInfoKHR(Structure):
    pass
class VkSubpassEndInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_END_INFO
class VkSubpassEndInfoKHR(Structure):
    pass
class VkPhysicalDeviceTimelineSemaphoreFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_FEATURES
class VkPhysicalDeviceTimelineSemaphoreFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceTimelineSemaphoreProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TIMELINE_SEMAPHORE_PROPERTIES
class VkPhysicalDeviceTimelineSemaphorePropertiesKHR(Structure):
    pass
class VkSemaphoreTypeCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO
class VkSemaphoreTypeCreateInfoKHR(Structure):
    pass
class VkTimelineSemaphoreSubmitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO
class VkTimelineSemaphoreSubmitInfoKHR(Structure):
    pass
class VkSemaphoreWaitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO
class VkSemaphoreWaitInfoKHR(Structure):
    pass
class VkSemaphoreSignalInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO
class VkSemaphoreSignalInfoKHR(Structure):
    pass
class VkVertexInputBindingDivisorDescription(Structure):
    pass
class VkVertexInputBindingDivisorDescriptionKHR(Structure):
    pass
class VkVertexInputBindingDivisorDescriptionEXT(Structure):
    pass
class VkPipelineVertexInputDivisorStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_DIVISOR_STATE_CREATE_INFO
class VkPipelineVertexInputDivisorStateCreateInfoKHR(Structure):
    pass
class VkPipelineVertexInputDivisorStateCreateInfoEXT(Structure):
    pass
class VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_PROPERTIES_EXT
class VkPhysicalDeviceVertexAttributeDivisorProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_PROPERTIES
class VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR(Structure):
    pass
class VkPhysicalDevicePCIBusInfoPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PCI_BUS_INFO_PROPERTIES_EXT
class VkImportAndroidHardwareBufferInfoANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_ANDROID_HARDWARE_BUFFER_INFO_ANDROID
class VkAndroidHardwareBufferUsageANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID
class VkAndroidHardwareBufferPropertiesANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_PROPERTIES_ANDROID
class VkMemoryGetAndroidHardwareBufferInfoANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_ANDROID_HARDWARE_BUFFER_INFO_ANDROID
class VkAndroidHardwareBufferFormatPropertiesANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_ANDROID
class VkCommandBufferInheritanceConditionalRenderingInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_CONDITIONAL_RENDERING_INFO_EXT
class VkExternalFormatANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_ANDROID
class VkPhysicalDevice8BitStorageFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_8BIT_STORAGE_FEATURES
class VkPhysicalDevice8BitStorageFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceConditionalRenderingFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONDITIONAL_RENDERING_FEATURES_EXT
class VkPhysicalDeviceVulkanMemoryModelFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES
class VkPhysicalDeviceVulkanMemoryModelFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceShaderAtomicInt64Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_INT64_FEATURES
class VkPhysicalDeviceShaderAtomicInt64FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceShaderAtomicFloatFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT
class VkPhysicalDeviceShaderAtomicFloat2FeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_2_FEATURES_EXT
class VkPhysicalDeviceVertexAttributeDivisorFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_FEATURES
class VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceVertexAttributeDivisorFeaturesEXT(Structure):
    pass
class VkQueueFamilyCheckpointPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_NV
class VkCheckpointDataNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CHECKPOINT_DATA_NV
class VkPhysicalDeviceDepthStencilResolveProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES
class VkPhysicalDeviceDepthStencilResolvePropertiesKHR(Structure):
    pass
class VkSubpassDescriptionDepthStencilResolve(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_DEPTH_STENCIL_RESOLVE
class VkSubpassDescriptionDepthStencilResolveKHR(Structure):
    pass
class VkImageViewASTCDecodeModeEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_ASTC_DECODE_MODE_EXT
class VkPhysicalDeviceASTCDecodeFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ASTC_DECODE_FEATURES_EXT
class VkPhysicalDeviceTransformFeedbackFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_FEATURES_EXT
class VkPhysicalDeviceTransformFeedbackPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TRANSFORM_FEEDBACK_PROPERTIES_EXT
class VkPipelineRasterizationStateStreamCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_STREAM_CREATE_INFO_EXT
class VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_REPRESENTATIVE_FRAGMENT_TEST_FEATURES_NV
class VkPipelineRepresentativeFragmentTestStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_REPRESENTATIVE_FRAGMENT_TEST_STATE_CREATE_INFO_NV
class VkPhysicalDeviceExclusiveScissorFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXCLUSIVE_SCISSOR_FEATURES_NV
class VkPipelineViewportExclusiveScissorStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV
class VkPhysicalDeviceCornerSampledImageFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CORNER_SAMPLED_IMAGE_FEATURES_NV
class VkPhysicalDeviceComputeShaderDerivativesFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMPUTE_SHADER_DERIVATIVES_FEATURES_KHR
class VkPhysicalDeviceComputeShaderDerivativesFeaturesNV(Structure):
    pass
class VkPhysicalDeviceComputeShaderDerivativesPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMPUTE_SHADER_DERIVATIVES_PROPERTIES_KHR
class VkPhysicalDeviceFragmentShaderBarycentricFeaturesNV(Structure):
    pass
class VkPhysicalDeviceShaderImageFootprintFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_IMAGE_FOOTPRINT_FEATURES_NV
class VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEDICATED_ALLOCATION_IMAGE_ALIASING_FEATURES_NV
class VkPhysicalDeviceCopyMemoryIndirectFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COPY_MEMORY_INDIRECT_FEATURES_KHR
class VkPhysicalDeviceCopyMemoryIndirectFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COPY_MEMORY_INDIRECT_FEATURES_NV
class VkPhysicalDeviceCopyMemoryIndirectPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COPY_MEMORY_INDIRECT_PROPERTIES_KHR
class VkPhysicalDeviceCopyMemoryIndirectPropertiesNV(Structure):
    pass
class VkPhysicalDeviceMemoryDecompressionFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_DECOMPRESSION_FEATURES_EXT
class VkPhysicalDeviceMemoryDecompressionFeaturesNV(Structure):
    pass
class VkPhysicalDeviceMemoryDecompressionPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_DECOMPRESSION_PROPERTIES_EXT
class VkPhysicalDeviceMemoryDecompressionPropertiesNV(Structure):
    pass
class VkShadingRatePaletteNV(Structure):
    pass
class VkPipelineViewportShadingRateImageStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV
class VkPhysicalDeviceShadingRateImageFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_FEATURES_NV
class VkPhysicalDeviceShadingRateImagePropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV
class VkPhysicalDeviceInvocationMaskFeaturesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INVOCATION_MASK_FEATURES_HUAWEI
class VkCoarseSampleLocationNV(Structure):
    pass
class VkCoarseSampleOrderCustomNV(Structure):
    pass
class VkPipelineViewportCoarseSampleOrderStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_COARSE_SAMPLE_ORDER_STATE_CREATE_INFO_NV
class VkPhysicalDeviceMeshShaderFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_FEATURES_NV
class VkPhysicalDeviceMeshShaderPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_NV
class VkDrawMeshTasksIndirectCommandNV(Structure):
    pass
class VkPhysicalDeviceMeshShaderFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_FEATURES_EXT
class VkPhysicalDeviceMeshShaderPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MESH_SHADER_PROPERTIES_EXT
class VkDrawMeshTasksIndirectCommandEXT(Structure):
    pass
class VkRayTracingShaderGroupCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_NV
class VkRayTracingShaderGroupCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_KHR
class VkRayTracingPipelineCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV
class VkRayTracingPipelineCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR
class VkGeometryTrianglesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GEOMETRY_TRIANGLES_NV
class VkGeometryAABBNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GEOMETRY_AABB_NV
class VkGeometryDataNV(Structure):
    pass
class VkGeometryNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GEOMETRY_NV
class VkAccelerationStructureInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV
class VkAccelerationStructureCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_NV
class VkBindAccelerationStructureMemoryInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_ACCELERATION_STRUCTURE_MEMORY_INFO_NV
class VkWriteDescriptorSetAccelerationStructureKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_KHR
class VkWriteDescriptorSetAccelerationStructureNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_ACCELERATION_STRUCTURE_NV
class VkAccelerationStructureMemoryRequirementsInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_INFO_NV
class VkPhysicalDeviceAccelerationStructureFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR
class VkPhysicalDeviceRayTracingPipelineFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR
class VkPhysicalDeviceRayQueryFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_QUERY_FEATURES_KHR
class VkPhysicalDeviceAccelerationStructurePropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_PROPERTIES_KHR
class VkPhysicalDeviceRayTracingPipelinePropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR
class VkPhysicalDeviceRayTracingPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV
class VkTraceRaysIndirectCommandKHR(Structure):
    pass
class VkTraceRaysIndirectCommand2KHR(Structure):
    pass
class VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_MAINTENANCE_1_FEATURES_KHR
class VkDrmFormatModifierPropertiesListEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_EXT
class VkDrmFormatModifierPropertiesEXT(Structure):
    pass
class VkPhysicalDeviceImageDrmFormatModifierInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT
class VkImageDrmFormatModifierListCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_LIST_CREATE_INFO_EXT
class VkImageDrmFormatModifierExplicitCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT
class VkImageDrmFormatModifierPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_PROPERTIES_EXT
class VkImageStencilUsageCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO
class VkImageStencilUsageCreateInfoEXT(Structure):
    pass
class VkDeviceMemoryOverallocationCreateInfoAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD
class VkPhysicalDeviceFragmentDensityMapFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_FEATURES_EXT
class VkPhysicalDeviceFragmentDensityMap2FeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_FEATURES_EXT
class VkPhysicalDeviceFragmentDensityMapOffsetFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_OFFSET_FEATURES_EXT
class VkPhysicalDeviceFragmentDensityMapOffsetFeaturesQCOM(Structure):
    pass
class VkPhysicalDeviceFragmentDensityMapPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_PROPERTIES_EXT
class VkPhysicalDeviceFragmentDensityMap2PropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_2_PROPERTIES_EXT
class VkPhysicalDeviceFragmentDensityMapOffsetPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_OFFSET_PROPERTIES_EXT
class VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM(Structure):
    pass
class VkRenderPassFragmentDensityMapCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_FRAGMENT_DENSITY_MAP_CREATE_INFO_EXT
class VkRenderPassFragmentDensityMapOffsetEndInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_FRAGMENT_DENSITY_MAP_OFFSET_END_INFO_EXT
class VkSubpassFragmentDensityMapOffsetEndInfoQCOM(Structure):
    pass
class VkPhysicalDeviceScalarBlockLayoutFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCALAR_BLOCK_LAYOUT_FEATURES
class VkPhysicalDeviceScalarBlockLayoutFeaturesEXT(Structure):
    pass
class VkSurfaceProtectedCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_PROTECTED_CAPABILITIES_KHR
class VkPhysicalDeviceUniformBufferStandardLayoutFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_UNIFORM_BUFFER_STANDARD_LAYOUT_FEATURES
class VkPhysicalDeviceUniformBufferStandardLayoutFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceDepthClipEnableFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_CLIP_ENABLE_FEATURES_EXT
class VkPipelineRasterizationDepthClipStateCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_DEPTH_CLIP_STATE_CREATE_INFO_EXT
class VkPhysicalDeviceMemoryBudgetPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_BUDGET_PROPERTIES_EXT
class VkPhysicalDeviceMemoryPriorityFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PRIORITY_FEATURES_EXT
class VkMemoryPriorityAllocateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_PRIORITY_ALLOCATE_INFO_EXT
class VkPhysicalDevicePageableDeviceLocalMemoryFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PAGEABLE_DEVICE_LOCAL_MEMORY_FEATURES_EXT
class VkPhysicalDeviceBufferDeviceAddressFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES
class VkPhysicalDeviceBufferDeviceAddressFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceBufferDeviceAddressFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BUFFER_DEVICE_ADDRESS_FEATURES_EXT
class VkPhysicalDeviceBufferAddressFeaturesEXT(Structure):
    pass
class VkBufferDeviceAddressInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO
class VkBufferDeviceAddressInfoKHR(Structure):
    pass
class VkBufferDeviceAddressInfoEXT(Structure):
    pass
class VkBufferOpaqueCaptureAddressCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_OPAQUE_CAPTURE_ADDRESS_CREATE_INFO
class VkBufferOpaqueCaptureAddressCreateInfoKHR(Structure):
    pass
class VkBufferDeviceAddressCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_CREATE_INFO_EXT
class VkPhysicalDeviceImageViewImageFormatInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_IMAGE_FORMAT_INFO_EXT
class VkFilterCubicImageViewImageFormatPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FILTER_CUBIC_IMAGE_VIEW_IMAGE_FORMAT_PROPERTIES_EXT
class VkPhysicalDeviceImagelessFramebufferFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGELESS_FRAMEBUFFER_FEATURES
class VkPhysicalDeviceImagelessFramebufferFeaturesKHR(Structure):
    pass
class VkFramebufferAttachmentsCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO
class VkFramebufferAttachmentsCreateInfoKHR(Structure):
    pass
class VkFramebufferAttachmentImageInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO
class VkFramebufferAttachmentImageInfoKHR(Structure):
    pass
class VkRenderPassAttachmentBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO
class VkRenderPassAttachmentBeginInfoKHR(Structure):
    pass
class VkPhysicalDeviceTextureCompressionASTCHDRFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXTURE_COMPRESSION_ASTC_HDR_FEATURES
class VkPhysicalDeviceTextureCompressionASTCHDRFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceCooperativeMatrixFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_FEATURES_NV
class VkPhysicalDeviceCooperativeMatrixPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_PROPERTIES_NV
class VkCooperativeMatrixPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_NV
class VkPhysicalDeviceYcbcrImageArraysFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_YCBCR_IMAGE_ARRAYS_FEATURES_EXT
class VkImageViewHandleInfoNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX
class VkImageViewAddressPropertiesNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_ADDRESS_PROPERTIES_NVX
class VkPresentFrameTokenGGP(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_FRAME_TOKEN_GGP
class VkPipelineCreationFeedback(Structure):
    pass
class VkPipelineCreationFeedbackEXT(Structure):
    pass
class VkPipelineCreationFeedbackCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_CREATION_FEEDBACK_CREATE_INFO
class VkPipelineCreationFeedbackCreateInfoEXT(Structure):
    pass
class VkSurfaceFullScreenExclusiveInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_INFO_EXT
class VkSurfaceFullScreenExclusiveWin32InfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_FULL_SCREEN_EXCLUSIVE_WIN32_INFO_EXT
class VkSurfaceCapabilitiesFullScreenExclusiveEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_FULL_SCREEN_EXCLUSIVE_EXT
class VkPhysicalDevicePresentBarrierFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_BARRIER_FEATURES_NV
class VkSurfaceCapabilitiesPresentBarrierNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_PRESENT_BARRIER_NV
class VkSwapchainPresentBarrierCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_BARRIER_CREATE_INFO_NV
class VkPhysicalDevicePerformanceQueryFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_FEATURES_KHR
class VkPhysicalDevicePerformanceQueryPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_PROPERTIES_KHR
class VkPerformanceCounterKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR
class VkPerformanceCounterDescriptionKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR
class VkQueryPoolPerformanceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR
class VkPerformanceCounterResultKHR(Union):
    pass
class VkAcquireProfilingLockInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACQUIRE_PROFILING_LOCK_INFO_KHR
class VkPerformanceQuerySubmitInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_QUERY_SUBMIT_INFO_KHR
class VkPerformanceQueryReservationInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_QUERY_RESERVATION_INFO_KHR
class VkHeadlessSurfaceCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_HEADLESS_SURFACE_CREATE_INFO_EXT
class VkPhysicalDeviceCoverageReductionModeFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COVERAGE_REDUCTION_MODE_FEATURES_NV
class VkPipelineCoverageReductionStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV
class VkFramebufferMixedSamplesCombinationNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV
class VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_FUNCTIONS_2_FEATURES_INTEL
class VkPerformanceValueDataINTEL(Union):
    pass
class VkPerformanceValueINTEL(Structure):
    pass
class VkInitializePerformanceApiInfoINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INITIALIZE_PERFORMANCE_API_INFO_INTEL
class VkQueryPoolPerformanceQueryCreateInfoINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL
class VkQueryPoolCreateInfoINTEL(Structure):
    pass
class VkPerformanceMarkerInfoINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_MARKER_INFO_INTEL
class VkPerformanceStreamMarkerInfoINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_STREAM_MARKER_INFO_INTEL
class VkPerformanceOverrideInfoINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_OVERRIDE_INFO_INTEL
class VkPerformanceConfigurationAcquireInfoINTEL(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_CONFIGURATION_ACQUIRE_INFO_INTEL
class VkPhysicalDeviceShaderClockFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CLOCK_FEATURES_KHR
class VkPhysicalDeviceIndexTypeUint8Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INDEX_TYPE_UINT8_FEATURES
class VkPhysicalDeviceIndexTypeUint8FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceIndexTypeUint8FeaturesEXT(Structure):
    pass
class VkPhysicalDeviceShaderSMBuiltinsPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SM_BUILTINS_PROPERTIES_NV
class VkPhysicalDeviceShaderSMBuiltinsFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SM_BUILTINS_FEATURES_NV
class VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_INTERLOCK_FEATURES_EXT
class VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SEPARATE_DEPTH_STENCIL_LAYOUTS_FEATURES
class VkPhysicalDeviceSeparateDepthStencilLayoutsFeaturesKHR(Structure):
    pass
class VkAttachmentReferenceStencilLayout(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT
class VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVE_TOPOLOGY_LIST_RESTART_FEATURES_EXT
class VkAttachmentReferenceStencilLayoutKHR(Structure):
    pass
class VkAttachmentDescriptionStencilLayout(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT
class VkAttachmentDescriptionStencilLayoutKHR(Structure):
    pass
class VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_EXECUTABLE_PROPERTIES_FEATURES_KHR
class VkPipelineInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_INFO_KHR
class VkPipelineInfoEXT(Structure):
    pass
class VkPipelineExecutablePropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR
class VkPipelineExecutableInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INFO_KHR
class VkPipelineExecutableStatisticValueKHR(Union):
    pass
class VkPipelineExecutableStatisticKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_STATISTIC_KHR
class VkPipelineExecutableInternalRepresentationKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR
class VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_DEMOTE_TO_HELPER_INVOCATION_FEATURES
class VkPhysicalDeviceShaderDemoteToHelperInvocationFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_FEATURES_EXT
class VkPhysicalDeviceTexelBufferAlignmentProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_PROPERTIES
class VkPhysicalDeviceTexelBufferAlignmentPropertiesEXT(Structure):
    pass
class VkPhysicalDeviceSubgroupSizeControlFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_FEATURES
class VkPhysicalDeviceSubgroupSizeControlFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceSubgroupSizeControlProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_SIZE_CONTROL_PROPERTIES
class VkPhysicalDeviceSubgroupSizeControlPropertiesEXT(Structure):
    pass
class VkPipelineShaderStageRequiredSubgroupSizeCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_REQUIRED_SUBGROUP_SIZE_CREATE_INFO
class VkPipelineShaderStageRequiredSubgroupSizeCreateInfoEXT(Structure):
    pass
class VkShaderRequiredSubgroupSizeCreateInfoEXT(Structure):
    pass
class VkSubpassShadingPipelineCreateInfoHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_SHADING_PIPELINE_CREATE_INFO_HUAWEI
class VkPhysicalDeviceSubpassShadingPropertiesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBPASS_SHADING_PROPERTIES_HUAWEI
class VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_PROPERTIES_HUAWEI
class VkMemoryOpaqueCaptureAddressAllocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_OPAQUE_CAPTURE_ADDRESS_ALLOCATE_INFO
class VkMemoryOpaqueCaptureAddressAllocateInfoKHR(Structure):
    pass
class VkDeviceMemoryOpaqueCaptureAddressInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_OPAQUE_CAPTURE_ADDRESS_INFO
class VkDeviceMemoryOpaqueCaptureAddressInfoKHR(Structure):
    pass
class VkPhysicalDeviceLineRasterizationFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_FEATURES
class VkPhysicalDeviceLineRasterizationFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceLineRasterizationFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceLineRasterizationProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINE_RASTERIZATION_PROPERTIES
class VkPhysicalDeviceLineRasterizationPropertiesKHR(Structure):
    pass
class VkPhysicalDeviceLineRasterizationPropertiesEXT(Structure):
    pass
class VkPipelineRasterizationLineStateCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO
class VkPipelineRasterizationLineStateCreateInfoKHR(Structure):
    pass
class VkPipelineRasterizationLineStateCreateInfoEXT(Structure):
    pass
class VkPhysicalDevicePipelineCreationCacheControlFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_CREATION_CACHE_CONTROL_FEATURES
class VkPhysicalDevicePipelineCreationCacheControlFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceVulkan11Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_FEATURES
class VkPhysicalDeviceVulkan11Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES
class VkPhysicalDeviceVulkan12Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_FEATURES
class VkPhysicalDeviceVulkan12Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_2_PROPERTIES
class VkPhysicalDeviceVulkan13Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_FEATURES
class VkPhysicalDeviceVulkan13Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_3_PROPERTIES
class VkPhysicalDeviceVulkan14Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_4_FEATURES
class VkPhysicalDeviceVulkan14Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_4_PROPERTIES
class VkPipelineCompilerControlCreateInfoAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COMPILER_CONTROL_CREATE_INFO_AMD
class VkPhysicalDeviceCoherentMemoryFeaturesAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COHERENT_MEMORY_FEATURES_AMD
class VkFaultData(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FAULT_DATA
class VkFaultCallbackInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FAULT_CALLBACK_INFO
class VkPhysicalDeviceToolProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TOOL_PROPERTIES
class VkPhysicalDeviceToolPropertiesEXT(Structure):
    pass
class VkSamplerCustomBorderColorCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_CUSTOM_BORDER_COLOR_CREATE_INFO_EXT
class VkPhysicalDeviceCustomBorderColorPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_PROPERTIES_EXT
class VkPhysicalDeviceCustomBorderColorFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_BORDER_COLOR_FEATURES_EXT
class VkSamplerBorderColorComponentMappingCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_BORDER_COLOR_COMPONENT_MAPPING_CREATE_INFO_EXT
class VkPhysicalDeviceBorderColorSwizzleFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_BORDER_COLOR_SWIZZLE_FEATURES_EXT
class VkDeviceOrHostAddressKHR(Union):
    pass
class VkDeviceOrHostAddressConstKHR(Union):
    pass
class VkDeviceOrHostAddressConstAMDX(Union):
    pass
class VkAccelerationStructureGeometryTrianglesDataKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_TRIANGLES_DATA_KHR
class VkAccelerationStructureGeometryAabbsDataKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_AABBS_DATA_KHR
class VkAccelerationStructureGeometryInstancesDataKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_INSTANCES_DATA_KHR
class VkAccelerationStructureGeometryLinearSweptSpheresDataNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_LINEAR_SWEPT_SPHERES_DATA_NV
class VkAccelerationStructureGeometrySpheresDataNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_SPHERES_DATA_NV
class VkAccelerationStructureGeometryDataKHR(Union):
    pass
class VkAccelerationStructureGeometryKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_KHR
class VkAccelerationStructureBuildGeometryInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_GEOMETRY_INFO_KHR
class VkAccelerationStructureBuildRangeInfoKHR(Structure):
    pass
class VkAccelerationStructureCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_KHR
class VkAabbPositionsKHR(Structure):
    pass
class VkAabbPositionsNV(Structure):
    pass
class VkTransformMatrixKHR(Structure):
    pass
class VkTransformMatrixNV(Structure):
    pass
class VkAccelerationStructureInstanceKHR(Structure):
    pass
class VkAccelerationStructureInstanceNV(Structure):
    pass
class VkAccelerationStructureDeviceAddressInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_DEVICE_ADDRESS_INFO_KHR
class VkAccelerationStructureVersionInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_VERSION_INFO_KHR
class VkCopyAccelerationStructureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_INFO_KHR
class VkCopyAccelerationStructureToMemoryInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_ACCELERATION_STRUCTURE_TO_MEMORY_INFO_KHR
class VkCopyMemoryToAccelerationStructureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_TO_ACCELERATION_STRUCTURE_INFO_KHR
class VkRayTracingPipelineInterfaceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR
class VkPipelineLibraryCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_LIBRARY_CREATE_INFO_KHR
class VkRefreshObjectKHR(Structure):
    pass
class VkRefreshObjectListKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_REFRESH_OBJECT_LIST_KHR
class VkPhysicalDeviceExtendedDynamicStateFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_FEATURES_EXT
class VkPhysicalDeviceExtendedDynamicState2FeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_2_FEATURES_EXT
class VkPhysicalDeviceExtendedDynamicState3FeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_3_FEATURES_EXT
class VkPhysicalDeviceExtendedDynamicState3PropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_DYNAMIC_STATE_3_PROPERTIES_EXT
class VkColorBlendEquationEXT(Structure):
    pass
class VkColorBlendAdvancedEXT(Structure):
    pass
class VkRenderPassTransformBeginInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_TRANSFORM_BEGIN_INFO_QCOM
class VkCopyCommandTransformInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_COMMAND_TRANSFORM_INFO_QCOM
class VkCommandBufferInheritanceRenderPassTransformInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDER_PASS_TRANSFORM_INFO_QCOM
class VkPhysicalDevicePartitionedAccelerationStructureFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PARTITIONED_ACCELERATION_STRUCTURE_FEATURES_NV
class VkPhysicalDevicePartitionedAccelerationStructurePropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PARTITIONED_ACCELERATION_STRUCTURE_PROPERTIES_NV
class VkBuildPartitionedAccelerationStructureIndirectCommandNV(Structure):
    pass
class VkPartitionedAccelerationStructureFlagsNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PARTITIONED_ACCELERATION_STRUCTURE_FLAGS_NV
class VkPartitionedAccelerationStructureWriteInstanceDataNV(Structure):
    pass
class VkPartitionedAccelerationStructureUpdateInstanceDataNV(Structure):
    pass
class VkPartitionedAccelerationStructureWritePartitionTranslationDataNV(Structure):
    pass
class VkWriteDescriptorSetPartitionedAccelerationStructureNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_PARTITIONED_ACCELERATION_STRUCTURE_NV
class VkPartitionedAccelerationStructureInstancesInputNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PARTITIONED_ACCELERATION_STRUCTURE_INSTANCES_INPUT_NV
class VkBuildPartitionedAccelerationStructureInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUILD_PARTITIONED_ACCELERATION_STRUCTURE_INFO_NV
class VkPhysicalDeviceDiagnosticsConfigFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DIAGNOSTICS_CONFIG_FEATURES_NV
class VkDeviceDiagnosticsConfigCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_DIAGNOSTICS_CONFIG_CREATE_INFO_NV
class VkPipelineOfflineCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_OFFLINE_CREATE_INFO
class VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ZERO_INITIALIZE_WORKGROUP_MEMORY_FEATURES
class VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceShaderSubgroupUniformControlFlowFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_UNIFORM_CONTROL_FLOW_FEATURES_KHR
class VkPhysicalDeviceRobustness2FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_FEATURES_KHR
class VkPhysicalDeviceRobustness2FeaturesEXT(Structure):
    pass
class VkPhysicalDeviceRobustness2PropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_PROPERTIES_KHR
class VkPhysicalDeviceRobustness2PropertiesEXT(Structure):
    pass
class VkPhysicalDeviceImageRobustnessFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ROBUSTNESS_FEATURES
class VkPhysicalDeviceImageRobustnessFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_WORKGROUP_MEMORY_EXPLICIT_LAYOUT_FEATURES_KHR
class VkPhysicalDevicePortabilitySubsetFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR
class VkPhysicalDevicePortabilitySubsetPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_PROPERTIES_KHR
class VkPhysicalDevice4444FormatsFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_4444_FORMATS_FEATURES_EXT
class VkPhysicalDeviceSubpassShadingFeaturesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBPASS_SHADING_FEATURES_HUAWEI
class VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_FEATURES_HUAWEI
class VkPhysicalDeviceClusterCullingShaderVrsFeaturesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CLUSTER_CULLING_SHADER_VRS_FEATURES_HUAWEI
class VkBufferCopy2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COPY_2
class VkBufferCopy2KHR(Structure):
    pass
class VkImageCopy2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_COPY_2
class VkImageCopy2KHR(Structure):
    pass
class VkImageBlit2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_BLIT_2
class VkImageBlit2KHR(Structure):
    pass
class VkBufferImageCopy2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2
class VkBufferImageCopy2KHR(Structure):
    pass
class VkImageResolve2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_RESOLVE_2
class VkImageResolve2KHR(Structure):
    pass
class VkCopyBufferInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_BUFFER_INFO_2
class VkCopyBufferInfo2KHR(Structure):
    pass
class VkCopyImageInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_IMAGE_INFO_2
class VkCopyImageInfo2KHR(Structure):
    pass
class VkBlitImageInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BLIT_IMAGE_INFO_2
class VkBlitImageInfo2KHR(Structure):
    pass
class VkCopyBufferToImageInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_BUFFER_TO_IMAGE_INFO_2
class VkCopyBufferToImageInfo2KHR(Structure):
    pass
class VkCopyImageToBufferInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_IMAGE_TO_BUFFER_INFO_2
class VkCopyImageToBufferInfo2KHR(Structure):
    pass
class VkResolveImageInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RESOLVE_IMAGE_INFO_2
class VkResolveImageInfo2KHR(Structure):
    pass
class VkPhysicalDeviceShaderImageAtomicInt64FeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_IMAGE_ATOMIC_INT64_FEATURES_EXT
class VkFragmentShadingRateAttachmentInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR
class VkPipelineFragmentShadingRateStateCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_STATE_CREATE_INFO_KHR
class VkPhysicalDeviceFragmentShadingRateFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_FEATURES_KHR
class VkPhysicalDeviceFragmentShadingRatePropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR
class VkPhysicalDeviceFragmentShadingRateKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_KHR
class VkPhysicalDeviceShaderTerminateInvocationFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TERMINATE_INVOCATION_FEATURES
class VkPhysicalDeviceShaderTerminateInvocationFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV
class VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_PROPERTIES_NV
class VkPipelineFragmentShadingRateEnumStateCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV
class VkAccelerationStructureBuildSizesInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_SIZES_INFO_KHR
class VkPhysicalDeviceImage2DViewOf3DFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_2D_VIEW_OF_3D_FEATURES_EXT
class VkPhysicalDeviceImageSlicedViewOf3DFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_SLICED_VIEW_OF_3D_FEATURES_EXT
class VkPhysicalDeviceAttachmentFeedbackLoopDynamicStateFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ATTACHMENT_FEEDBACK_LOOP_DYNAMIC_STATE_FEATURES_EXT
class VkPhysicalDeviceLegacyVertexAttributesFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LEGACY_VERTEX_ATTRIBUTES_FEATURES_EXT
class VkPhysicalDeviceLegacyVertexAttributesPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LEGACY_VERTEX_ATTRIBUTES_PROPERTIES_EXT
class VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MUTABLE_DESCRIPTOR_TYPE_FEATURES_EXT
class VkPhysicalDeviceMutableDescriptorTypeFeaturesVALVE(Structure):
    pass
class VkMutableDescriptorTypeListEXT(Structure):
    pass
class VkMutableDescriptorTypeListVALVE(Structure):
    pass
class VkMutableDescriptorTypeCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MUTABLE_DESCRIPTOR_TYPE_CREATE_INFO_EXT
class VkMutableDescriptorTypeCreateInfoVALVE(Structure):
    pass
class VkPhysicalDeviceDepthClipControlFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_CLIP_CONTROL_FEATURES_EXT
class VkPhysicalDeviceZeroInitializeDeviceMemoryFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ZERO_INITIALIZE_DEVICE_MEMORY_FEATURES_EXT
class VkBeginCustomResolveInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BEGIN_CUSTOM_RESOLVE_INFO_EXT
class VkPhysicalDeviceCustomResolveFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUSTOM_RESOLVE_FEATURES_EXT
class VkCustomResolveCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUSTOM_RESOLVE_CREATE_INFO_EXT
class VkPhysicalDeviceDeviceGeneratedCommandsFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_FEATURES_EXT
class VkPhysicalDeviceDeviceGeneratedCommandsPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_EXT
class VkGeneratedCommandsPipelineInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_PIPELINE_INFO_EXT
class VkGeneratedCommandsShaderInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_SHADER_INFO_EXT
class VkGeneratedCommandsMemoryRequirementsInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_EXT
class VkIndirectExecutionSetPipelineInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_EXECUTION_SET_PIPELINE_INFO_EXT
class VkIndirectExecutionSetShaderLayoutInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_EXECUTION_SET_SHADER_LAYOUT_INFO_EXT
class VkIndirectExecutionSetShaderInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_EXECUTION_SET_SHADER_INFO_EXT
class VkIndirectExecutionSetInfoEXT(Union):
    pass
class VkIndirectExecutionSetCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_EXECUTION_SET_CREATE_INFO_EXT
class VkGeneratedCommandsInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_EXT
class VkWriteIndirectExecutionSetPipelineEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_INDIRECT_EXECUTION_SET_PIPELINE_EXT
class VkWriteIndirectExecutionSetShaderEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_INDIRECT_EXECUTION_SET_SHADER_EXT
class VkIndirectCommandsLayoutCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_EXT
class VkIndirectCommandsTokenDataEXT(Union):
    pass
class VkIndirectCommandsLayoutTokenEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_EXT
class VkDrawIndirectCountIndirectCommandEXT(Structure):
    pass
class VkIndirectCommandsVertexBufferTokenEXT(Structure):
    pass
class VkBindVertexBufferIndirectCommandEXT(Structure):
    pass
class VkIndirectCommandsIndexBufferTokenEXT(Structure):
    pass
class VkBindIndexBufferIndirectCommandEXT(Structure):
    pass
class VkIndirectCommandsPushConstantTokenEXT(Structure):
    pass
class VkIndirectCommandsExecutionSetTokenEXT(Structure):
    pass
class VkPipelineViewportDepthClipControlCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_DEPTH_CLIP_CONTROL_CREATE_INFO_EXT
class VkPhysicalDeviceDepthClampControlFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_CLAMP_CONTROL_FEATURES_EXT
class VkPipelineViewportDepthClampControlCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_DEPTH_CLAMP_CONTROL_CREATE_INFO_EXT
class VkPhysicalDeviceVertexInputDynamicStateFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_INPUT_DYNAMIC_STATE_FEATURES_EXT
class VkPhysicalDeviceExternalMemoryRDMAFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_RDMA_FEATURES_NV
class VkPhysicalDeviceShaderRelaxedExtendedInstructionFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_RELAXED_EXTENDED_INSTRUCTION_FEATURES_KHR
class VkVertexInputBindingDescription2EXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VERTEX_INPUT_BINDING_DESCRIPTION_2_EXT
class VkVertexInputAttributeDescription2EXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VERTEX_INPUT_ATTRIBUTE_DESCRIPTION_2_EXT
class VkPhysicalDeviceColorWriteEnableFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COLOR_WRITE_ENABLE_FEATURES_EXT
class VkPipelineColorWriteCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COLOR_WRITE_CREATE_INFO_EXT
class VkMemoryBarrier2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_BARRIER_2
class VkMemoryBarrier2KHR(Structure):
    pass
class VkImageMemoryBarrier2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER_2
class VkImageMemoryBarrier2KHR(Structure):
    pass
class VkBufferMemoryBarrier2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER_2
class VkBufferMemoryBarrier2KHR(Structure):
    pass
class VkMemoryBarrierAccessFlags3KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_BARRIER_ACCESS_FLAGS_3_KHR
class VkDependencyInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEPENDENCY_INFO
class VkDependencyInfoKHR(Structure):
    pass
class VkSemaphoreSubmitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_SUBMIT_INFO
class VkSemaphoreSubmitInfoKHR(Structure):
    pass
class VkCommandBufferSubmitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_SUBMIT_INFO
class VkCommandBufferSubmitInfoKHR(Structure):
    pass
class VkSubmitInfo2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBMIT_INFO_2
class VkSubmitInfo2KHR(Structure):
    pass
class VkQueueFamilyCheckpointProperties2NV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_2_NV
class VkCheckpointData2NV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CHECKPOINT_DATA_2_NV
class VkPhysicalDeviceSynchronization2Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SYNCHRONIZATION_2_FEATURES
class VkPhysicalDeviceSynchronization2FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceUnifiedImageLayoutsFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_UNIFIED_IMAGE_LAYOUTS_FEATURES_KHR
class VkPhysicalDeviceHostImageCopyFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_IMAGE_COPY_FEATURES
class VkPhysicalDeviceHostImageCopyFeaturesEXT(Structure):
    pass
class VkPhysicalDeviceHostImageCopyProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_IMAGE_COPY_PROPERTIES
class VkPhysicalDeviceHostImageCopyPropertiesEXT(Structure):
    pass
class VkMemoryToImageCopy(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_TO_IMAGE_COPY
class VkMemoryToImageCopyEXT(Structure):
    pass
class VkImageToMemoryCopy(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_TO_MEMORY_COPY
class VkImageToMemoryCopyEXT(Structure):
    pass
class VkCopyMemoryToImageInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_TO_IMAGE_INFO
class VkCopyMemoryToImageInfoEXT(Structure):
    pass
class VkCopyImageToMemoryInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_IMAGE_TO_MEMORY_INFO
class VkCopyImageToMemoryInfoEXT(Structure):
    pass
class VkCopyImageToImageInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_IMAGE_TO_IMAGE_INFO
class VkCopyImageToImageInfoEXT(Structure):
    pass
class VkHostImageLayoutTransitionInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_HOST_IMAGE_LAYOUT_TRANSITION_INFO
class VkHostImageLayoutTransitionInfoEXT(Structure):
    pass
class VkSubresourceHostMemcpySize(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBRESOURCE_HOST_MEMCPY_SIZE
class VkSubresourceHostMemcpySizeEXT(Structure):
    pass
class VkHostImageCopyDevicePerformanceQuery(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_HOST_IMAGE_COPY_DEVICE_PERFORMANCE_QUERY
class VkHostImageCopyDevicePerformanceQueryEXT(Structure):
    pass
class VkPhysicalDeviceVulkanSC10Properties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_SC_1_0_PROPERTIES
class VkPipelinePoolSize(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_POOL_SIZE
class VkDeviceObjectReservationCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_OBJECT_RESERVATION_CREATE_INFO
class VkCommandPoolMemoryReservationCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_POOL_MEMORY_RESERVATION_CREATE_INFO
class VkCommandPoolMemoryConsumption(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_POOL_MEMORY_CONSUMPTION
class VkPhysicalDeviceVulkanSC10Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_SC_1_0_FEATURES
class VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVES_GENERATED_QUERY_FEATURES_EXT
class VkPhysicalDeviceLegacyDitheringFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LEGACY_DITHERING_FEATURES_EXT
class VkPhysicalDeviceMultisampledRenderToSingleSampledFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_FEATURES_EXT
class VkSurfaceCapabilitiesPresentId2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_PRESENT_ID_2_KHR
class VkSurfaceCapabilitiesPresentWait2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_PRESENT_WAIT_2_KHR
class VkSubpassResolvePerformanceQueryEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_RESOLVE_PERFORMANCE_QUERY_EXT
class VkMultisampledRenderToSingleSampledInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_INFO_EXT
class VkPhysicalDevicePipelineProtectedAccessFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_PROTECTED_ACCESS_FEATURES
class VkPhysicalDevicePipelineProtectedAccessFeaturesEXT(Structure):
    pass
class VkQueueFamilyVideoPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_VIDEO_PROPERTIES_KHR
class VkQueueFamilyQueryResultStatusPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_QUERY_RESULT_STATUS_PROPERTIES_KHR
class VkVideoProfileListInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_PROFILE_LIST_INFO_KHR
class VkPhysicalDeviceVideoFormatInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_FORMAT_INFO_KHR
class VkVideoFormatPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_FORMAT_PROPERTIES_KHR
class VkVideoEncodeQuantizationMapCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUANTIZATION_MAP_CAPABILITIES_KHR
class VkVideoEncodeH264QuantizationMapCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_QUANTIZATION_MAP_CAPABILITIES_KHR
class VkVideoEncodeH265QuantizationMapCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_QUANTIZATION_MAP_CAPABILITIES_KHR
class VkVideoEncodeAV1QuantizationMapCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_QUANTIZATION_MAP_CAPABILITIES_KHR
class VkVideoFormatQuantizationMapPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_FORMAT_QUANTIZATION_MAP_PROPERTIES_KHR
class VkVideoFormatH265QuantizationMapPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_FORMAT_H265_QUANTIZATION_MAP_PROPERTIES_KHR
class VkVideoFormatAV1QuantizationMapPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_FORMAT_AV1_QUANTIZATION_MAP_PROPERTIES_KHR
class VkVideoProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_PROFILE_INFO_KHR
class VkVideoCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_CAPABILITIES_KHR
class VkVideoSessionMemoryRequirementsKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_MEMORY_REQUIREMENTS_KHR
class VkBindVideoSessionMemoryInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_VIDEO_SESSION_MEMORY_INFO_KHR
class VkVideoPictureResourceInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_PICTURE_RESOURCE_INFO_KHR
class VkVideoReferenceSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_REFERENCE_SLOT_INFO_KHR
class VkVideoDecodeCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_CAPABILITIES_KHR
class VkVideoDecodeUsageInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_USAGE_INFO_KHR
class VkVideoDecodeInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_INFO_KHR
class VkPhysicalDeviceVideoMaintenance1FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_MAINTENANCE_1_FEATURES_KHR
class VkPhysicalDeviceVideoMaintenance2FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_MAINTENANCE_2_FEATURES_KHR
class VkVideoInlineQueryInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_INLINE_QUERY_INFO_KHR
class VkVideoDecodeH264ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PROFILE_INFO_KHR
class VkVideoDecodeH264CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_CAPABILITIES_KHR
class VkVideoDecodeH264SessionParametersAddInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_SESSION_PARAMETERS_ADD_INFO_KHR
class VkVideoDecodeH264SessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoDecodeH264InlineSessionParametersInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_INLINE_SESSION_PARAMETERS_INFO_KHR
class VkVideoDecodeH264PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PICTURE_INFO_KHR
class VkVideoDecodeH264DpbSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_DPB_SLOT_INFO_KHR
class VkVideoDecodeH265ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PROFILE_INFO_KHR
class VkVideoDecodeH265CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_CAPABILITIES_KHR
class VkVideoDecodeH265SessionParametersAddInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_ADD_INFO_KHR
class VkVideoDecodeH265SessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoDecodeH265InlineSessionParametersInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_INLINE_SESSION_PARAMETERS_INFO_KHR
class VkVideoDecodeH265PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PICTURE_INFO_KHR
class VkVideoDecodeH265DpbSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_DPB_SLOT_INFO_KHR
class VkPhysicalDeviceVideoDecodeVP9FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_DECODE_VP9_FEATURES_KHR
class VkVideoDecodeVP9ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_VP9_PROFILE_INFO_KHR
class VkVideoDecodeVP9CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_VP9_CAPABILITIES_KHR
class VkVideoDecodeVP9PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_VP9_PICTURE_INFO_KHR
class VkVideoDecodeAV1ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PROFILE_INFO_KHR
class VkVideoDecodeAV1CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_CAPABILITIES_KHR
class VkVideoDecodeAV1SessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoDecodeAV1InlineSessionParametersInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_INLINE_SESSION_PARAMETERS_INFO_KHR
class VkVideoDecodeAV1PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PICTURE_INFO_KHR
class VkVideoDecodeAV1DpbSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_DPB_SLOT_INFO_KHR
class VkVideoSessionCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_CREATE_INFO_KHR
class VkVideoSessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoSessionParametersUpdateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_UPDATE_INFO_KHR
class VkVideoEncodeSessionParametersGetInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_GET_INFO_KHR
class VkVideoEncodeSessionParametersFeedbackInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_FEEDBACK_INFO_KHR
class VkVideoBeginCodingInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_BEGIN_CODING_INFO_KHR
class VkVideoEndCodingInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_END_CODING_INFO_KHR
class VkVideoCodingControlInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_CODING_CONTROL_INFO_KHR
class VkVideoEncodeUsageInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_USAGE_INFO_KHR
class VkVideoEncodeInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_INFO_KHR
class VkVideoEncodeQuantizationMapInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUANTIZATION_MAP_INFO_KHR
class VkVideoEncodeQuantizationMapSessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUANTIZATION_MAP_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkPhysicalDeviceVideoEncodeQuantizationMapFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_QUANTIZATION_MAP_FEATURES_KHR
class VkQueryPoolVideoEncodeFeedbackCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_POOL_VIDEO_ENCODE_FEEDBACK_CREATE_INFO_KHR
class VkVideoEncodeQualityLevelInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUALITY_LEVEL_INFO_KHR
class VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_QUALITY_LEVEL_INFO_KHR
class VkVideoEncodeQualityLevelPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUALITY_LEVEL_PROPERTIES_KHR
class VkVideoEncodeRateControlInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_INFO_KHR
class VkVideoEncodeRateControlLayerInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_LAYER_INFO_KHR
class VkVideoEncodeCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_CAPABILITIES_KHR
class VkVideoEncodeH264CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_CAPABILITIES_KHR
class VkVideoEncodeH264QpKHR(Structure):
    pass
class VkVideoEncodeH264QualityLevelPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_QUALITY_LEVEL_PROPERTIES_KHR
class VkVideoEncodeH264SessionCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_CREATE_INFO_KHR
class VkVideoEncodeH264SessionParametersAddInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_ADD_INFO_KHR
class VkVideoEncodeH264SessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoEncodeH264SessionParametersGetInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_GET_INFO_KHR
class VkVideoEncodeH264SessionParametersFeedbackInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_FEEDBACK_INFO_KHR
class VkVideoEncodeH264DpbSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_DPB_SLOT_INFO_KHR
class VkVideoEncodeH264PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PICTURE_INFO_KHR
class VkVideoEncodeH264ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PROFILE_INFO_KHR
class VkVideoEncodeH264NaluSliceInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_NALU_SLICE_INFO_KHR
class VkVideoEncodeH264RateControlInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_INFO_KHR
class VkVideoEncodeH264FrameSizeKHR(Structure):
    pass
class VkVideoEncodeH264GopRemainingFrameInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_GOP_REMAINING_FRAME_INFO_KHR
class VkVideoEncodeH264RateControlLayerInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_LAYER_INFO_KHR
class VkVideoEncodeH265CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_CAPABILITIES_KHR
class VkVideoEncodeH265QpKHR(Structure):
    pass
class VkVideoEncodeH265QualityLevelPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_QUALITY_LEVEL_PROPERTIES_KHR
class VkVideoEncodeH265SessionCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_CREATE_INFO_KHR
class VkVideoEncodeH265SessionParametersAddInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_ADD_INFO_KHR
class VkVideoEncodeH265SessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoEncodeH265SessionParametersGetInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_GET_INFO_KHR
class VkVideoEncodeH265SessionParametersFeedbackInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_FEEDBACK_INFO_KHR
class VkVideoEncodeH265PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_PICTURE_INFO_KHR
class VkVideoEncodeH265NaluSliceSegmentInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_NALU_SLICE_SEGMENT_INFO_KHR
class VkVideoEncodeH265RateControlInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_INFO_KHR
class VkVideoEncodeH265FrameSizeKHR(Structure):
    pass
class VkVideoEncodeH265GopRemainingFrameInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_GOP_REMAINING_FRAME_INFO_KHR
class VkVideoEncodeH265RateControlLayerInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_LAYER_INFO_KHR
class VkVideoEncodeH265ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_PROFILE_INFO_KHR
class VkVideoEncodeH265DpbSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_DPB_SLOT_INFO_KHR
class VkVideoEncodeAV1CapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_CAPABILITIES_KHR
class VkVideoEncodeAV1QIndexKHR(Structure):
    pass
class VkVideoEncodeAV1QualityLevelPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_QUALITY_LEVEL_PROPERTIES_KHR
class VkPhysicalDeviceVideoEncodeAV1FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_AV1_FEATURES_KHR
class VkVideoEncodeAV1SessionCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_SESSION_CREATE_INFO_KHR
class VkVideoEncodeAV1SessionParametersCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_SESSION_PARAMETERS_CREATE_INFO_KHR
class VkVideoEncodeAV1DpbSlotInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_DPB_SLOT_INFO_KHR
class VkVideoEncodeAV1PictureInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_PICTURE_INFO_KHR
class VkVideoEncodeAV1ProfileInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_PROFILE_INFO_KHR
class VkVideoEncodeAV1RateControlInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_RATE_CONTROL_INFO_KHR
class VkVideoEncodeAV1FrameSizeKHR(Structure):
    pass
class VkVideoEncodeAV1GopRemainingFrameInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_GOP_REMAINING_FRAME_INFO_KHR
class VkVideoEncodeAV1RateControlLayerInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_AV1_RATE_CONTROL_LAYER_INFO_KHR
class VkPhysicalDeviceInheritedViewportScissorFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INHERITED_VIEWPORT_SCISSOR_FEATURES_NV
class VkCommandBufferInheritanceViewportScissorInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_VIEWPORT_SCISSOR_INFO_NV
class VkPhysicalDeviceYcbcr2Plane444FormatsFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_YCBCR_2_PLANE_444_FORMATS_FEATURES_EXT
class VkPhysicalDeviceProvokingVertexFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROVOKING_VERTEX_FEATURES_EXT
class VkPhysicalDeviceProvokingVertexPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PROVOKING_VERTEX_PROPERTIES_EXT
class VkPipelineRasterizationProvokingVertexStateCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_PROVOKING_VERTEX_STATE_CREATE_INFO_EXT
class VkVideoEncodeIntraRefreshCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_INTRA_REFRESH_CAPABILITIES_KHR
class VkVideoEncodeSessionIntraRefreshCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_INTRA_REFRESH_CREATE_INFO_KHR
class VkVideoEncodeIntraRefreshInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_INTRA_REFRESH_INFO_KHR
class VkVideoReferenceIntraRefreshInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_REFERENCE_INTRA_REFRESH_INFO_KHR
class VkPhysicalDeviceVideoEncodeIntraRefreshFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_INTRA_REFRESH_FEATURES_KHR
class VkCuModuleCreateInfoNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CU_MODULE_CREATE_INFO_NVX
class VkCuModuleTexturingModeCreateInfoNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CU_MODULE_TEXTURING_MODE_CREATE_INFO_NVX
class VkCuFunctionCreateInfoNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CU_FUNCTION_CREATE_INFO_NVX
class VkCuLaunchInfoNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CU_LAUNCH_INFO_NVX
class VkPhysicalDeviceDescriptorBufferFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_FEATURES_EXT
class VkPhysicalDeviceDescriptorBufferPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_PROPERTIES_EXT
class VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_DENSITY_MAP_PROPERTIES_EXT
class VkDescriptorAddressInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_ADDRESS_INFO_EXT
class VkDescriptorBufferBindingInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_BUFFER_BINDING_INFO_EXT
class VkDescriptorBufferBindingPushDescriptorBufferHandleEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_BUFFER_BINDING_PUSH_DESCRIPTOR_BUFFER_HANDLE_EXT
class VkDescriptorDataEXT(Union):
    pass
class VkDescriptorGetInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_GET_INFO_EXT
class VkBufferCaptureDescriptorDataInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_CAPTURE_DESCRIPTOR_DATA_INFO_EXT
class VkImageCaptureDescriptorDataInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_CAPTURE_DESCRIPTOR_DATA_INFO_EXT
class VkImageViewCaptureDescriptorDataInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_CAPTURE_DESCRIPTOR_DATA_INFO_EXT
class VkSamplerCaptureDescriptorDataInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_CAPTURE_DESCRIPTOR_DATA_INFO_EXT
class VkAccelerationStructureCaptureDescriptorDataInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CAPTURE_DESCRIPTOR_DATA_INFO_EXT
class VkOpaqueCaptureDescriptorDataCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPAQUE_CAPTURE_DESCRIPTOR_DATA_CREATE_INFO_EXT
class VkPhysicalDeviceShaderIntegerDotProductFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_DOT_PRODUCT_FEATURES
class VkPhysicalDeviceShaderIntegerDotProductFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceShaderIntegerDotProductProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INTEGER_DOT_PRODUCT_PROPERTIES
class VkPhysicalDeviceShaderIntegerDotProductPropertiesKHR(Structure):
    pass
class VkPhysicalDeviceDrmPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DRM_PROPERTIES_EXT
class VkPhysicalDeviceFragmentShaderBarycentricFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_BARYCENTRIC_FEATURES_KHR
class VkPhysicalDeviceFragmentShaderBarycentricPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_BARYCENTRIC_PROPERTIES_KHR
class VkPhysicalDeviceShaderFmaFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FMA_FEATURES_KHR
class VkPhysicalDeviceRayTracingMotionBlurFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_MOTION_BLUR_FEATURES_NV
class VkPhysicalDeviceRayTracingValidationFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_VALIDATION_FEATURES_NV
class VkPhysicalDeviceRayTracingLinearSweptSpheresFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_LINEAR_SWEPT_SPHERES_FEATURES_NV
class VkAccelerationStructureGeometryMotionTrianglesDataNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_MOTION_TRIANGLES_DATA_NV
class VkAccelerationStructureMotionInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_MOTION_INFO_NV
class VkSRTDataNV(Structure):
    pass
class VkAccelerationStructureSRTMotionInstanceNV(Structure):
    pass
class VkAccelerationStructureMatrixMotionInstanceNV(Structure):
    pass
class VkAccelerationStructureMotionInstanceDataNV(Union):
    pass
class VkAccelerationStructureMotionInstanceNV(Structure):
    pass
class VkMemoryGetRemoteAddressInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_REMOTE_ADDRESS_INFO_NV
class VkImportMemoryBufferCollectionFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_MEMORY_BUFFER_COLLECTION_FUCHSIA
class VkBufferCollectionImageCreateInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_IMAGE_CREATE_INFO_FUCHSIA
class VkBufferCollectionBufferCreateInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_BUFFER_CREATE_INFO_FUCHSIA
class VkBufferCollectionCreateInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_CREATE_INFO_FUCHSIA
class VkSysmemColorSpaceFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SYSMEM_COLOR_SPACE_FUCHSIA
class VkBufferCollectionPropertiesFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_PROPERTIES_FUCHSIA
class VkBufferCollectionConstraintsInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_COLLECTION_CONSTRAINTS_INFO_FUCHSIA
class VkBufferConstraintsInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BUFFER_CONSTRAINTS_INFO_FUCHSIA
class VkImageFormatConstraintsInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_FORMAT_CONSTRAINTS_INFO_FUCHSIA
class VkImageConstraintsInfoFUCHSIA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_CONSTRAINTS_INFO_FUCHSIA
class VkCudaModuleCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUDA_MODULE_CREATE_INFO_NV
class VkCudaFunctionCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUDA_FUNCTION_CREATE_INFO_NV
class VkCudaLaunchInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CUDA_LAUNCH_INFO_NV
class VkPhysicalDeviceRGBA10X6FormatsFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RGBA10X6_FORMATS_FEATURES_EXT
class VkFormatProperties3(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_3
class VkFormatProperties3KHR(Structure):
    pass
class VkDrmFormatModifierPropertiesList2EXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_2_EXT
class VkDrmFormatModifierProperties2EXT(Structure):
    pass
class VkAndroidHardwareBufferFormatProperties2ANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_PROPERTIES_2_ANDROID
class VkPipelineRenderingCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RENDERING_CREATE_INFO
class VkPipelineRenderingCreateInfoKHR(Structure):
    pass
class VkRenderingInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_INFO
class VkRenderingInfoKHR(Structure):
    pass
class VkRenderingEndInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_END_INFO_KHR
class VkRenderingEndInfoEXT(Structure):
    pass
class VkRenderingAttachmentInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_INFO
class VkRenderingAttachmentInfoKHR(Structure):
    pass
class VkRenderingFragmentShadingRateAttachmentInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR
class VkRenderingFragmentDensityMapAttachmentInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_DENSITY_MAP_ATTACHMENT_INFO_EXT
class VkPhysicalDeviceDynamicRenderingFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DYNAMIC_RENDERING_FEATURES
class VkPhysicalDeviceDynamicRenderingFeaturesKHR(Structure):
    pass
class VkCommandBufferInheritanceRenderingInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_RENDERING_INFO
class VkCommandBufferInheritanceRenderingInfoKHR(Structure):
    pass
class VkAttachmentSampleCountInfoAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_SAMPLE_COUNT_INFO_AMD
class VkAttachmentSampleCountInfoNV(Structure):
    pass
class VkMultiviewPerViewAttributesInfoNVX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_ATTRIBUTES_INFO_NVX
class VkPhysicalDeviceImageViewMinLodFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_VIEW_MIN_LOD_FEATURES_EXT
class VkImageViewMinLodCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_MIN_LOD_CREATE_INFO_EXT
class VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RASTERIZATION_ORDER_ATTACHMENT_ACCESS_FEATURES_EXT
class VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesARM(Structure):
    pass
class VkPhysicalDeviceLinearColorAttachmentFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LINEAR_COLOR_ATTACHMENT_FEATURES_NV
class VkPhysicalDeviceGraphicsPipelineLibraryFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GRAPHICS_PIPELINE_LIBRARY_FEATURES_EXT
class VkPhysicalDevicePipelineBinaryFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_BINARY_FEATURES_KHR
class VkDevicePipelineBinaryInternalCacheControlKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_PIPELINE_BINARY_INTERNAL_CACHE_CONTROL_KHR
class VkPhysicalDevicePipelineBinaryPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_BINARY_PROPERTIES_KHR
class VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_GRAPHICS_PIPELINE_LIBRARY_PROPERTIES_EXT
class VkGraphicsPipelineLibraryCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_LIBRARY_CREATE_INFO_EXT
class VkPhysicalDeviceDataGraphNeuralAcceleratorStatisticsFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DATA_GRAPH_NEURAL_ACCELERATOR_STATISTICS_FEATURES_ARM
class VkDataGraphPipelineNeuralStatisticsCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_NEURAL_STATISTICS_CREATE_INFO_ARM
class VkDataGraphPipelineSessionNeuralStatisticsCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SESSION_NEURAL_STATISTICS_CREATE_INFO_ARM
class VkPhysicalDeviceDescriptorSetHostMappingFeaturesVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_SET_HOST_MAPPING_FEATURES_VALVE
class VkDescriptorSetBindingReferenceVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_BINDING_REFERENCE_VALVE
class VkDescriptorSetLayoutHostMappingInfoVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_HOST_MAPPING_INFO_VALVE
class VkPhysicalDeviceNestedCommandBufferFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_NESTED_COMMAND_BUFFER_FEATURES_EXT
class VkPhysicalDeviceNestedCommandBufferPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_NESTED_COMMAND_BUFFER_PROPERTIES_EXT
class VkPhysicalDeviceShaderModuleIdentifierFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_MODULE_IDENTIFIER_FEATURES_EXT
class VkPhysicalDeviceShaderModuleIdentifierPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_MODULE_IDENTIFIER_PROPERTIES_EXT
class VkPipelineShaderStageModuleIdentifierCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_MODULE_IDENTIFIER_CREATE_INFO_EXT
class VkShaderModuleIdentifierEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_MODULE_IDENTIFIER_EXT
class VkImageCompressionControlEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT
class VkPhysicalDeviceImageCompressionControlFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_COMPRESSION_CONTROL_FEATURES_EXT
class VkImageCompressionPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT
class VkPhysicalDeviceImageCompressionControlSwapchainFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_COMPRESSION_CONTROL_SWAPCHAIN_FEATURES_EXT
class VkImageSubresource2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_SUBRESOURCE_2
class VkImageSubresource2KHR(Structure):
    pass
class VkImageSubresource2EXT(Structure):
    pass
class VkSubresourceLayout2(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBRESOURCE_LAYOUT_2
class VkSubresourceLayout2KHR(Structure):
    pass
class VkSubresourceLayout2EXT(Structure):
    pass
class VkRenderPassCreationControlEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_CONTROL_EXT
class VkRenderPassCreationFeedbackInfoEXT(Structure):
    pass
class VkRenderPassCreationFeedbackCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_FEEDBACK_CREATE_INFO_EXT
class VkRenderPassSubpassFeedbackInfoEXT(Structure):
    pass
class VkRenderPassSubpassFeedbackCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_SUBPASS_FEEDBACK_CREATE_INFO_EXT
class VkPhysicalDeviceSubpassMergeFeedbackFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBPASS_MERGE_FEEDBACK_FEATURES_EXT
class VkMicromapBuildInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MICROMAP_BUILD_INFO_EXT
class VkMicromapCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MICROMAP_CREATE_INFO_EXT
class VkMicromapVersionInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MICROMAP_VERSION_INFO_EXT
class VkCopyMicromapInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MICROMAP_INFO_EXT
class VkCopyMicromapToMemoryInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MICROMAP_TO_MEMORY_INFO_EXT
class VkCopyMemoryToMicromapInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_MEMORY_TO_MICROMAP_INFO_EXT
class VkMicromapBuildSizesInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MICROMAP_BUILD_SIZES_INFO_EXT
class VkMicromapUsageEXT(Structure):
    pass
class VkMicromapTriangleEXT(Structure):
    pass
class VkPhysicalDeviceOpacityMicromapFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPACITY_MICROMAP_FEATURES_EXT
class VkPhysicalDeviceOpacityMicromapPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPACITY_MICROMAP_PROPERTIES_EXT
class VkAccelerationStructureTrianglesOpacityMicromapEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_OPACITY_MICROMAP_EXT
class VkPhysicalDeviceDisplacementMicromapFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DISPLACEMENT_MICROMAP_FEATURES_NV
class VkPhysicalDeviceDisplacementMicromapPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DISPLACEMENT_MICROMAP_PROPERTIES_NV
class VkAccelerationStructureTrianglesDisplacementMicromapNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_TRIANGLES_DISPLACEMENT_MICROMAP_NV
class VkPipelinePropertiesIdentifierEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_PROPERTIES_IDENTIFIER_EXT
class VkPhysicalDevicePipelinePropertiesFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_PROPERTIES_FEATURES_EXT
class VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_EARLY_AND_LATE_FRAGMENT_TESTS_FEATURES_AMD
class VkExternalMemoryAcquireUnmodifiedEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_ACQUIRE_UNMODIFIED_EXT
class VkExportMetalObjectCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_OBJECT_CREATE_INFO_EXT
class VkExportMetalObjectsInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_OBJECTS_INFO_EXT
class VkExportMetalDeviceInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_DEVICE_INFO_EXT
class VkExportMetalCommandQueueInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_COMMAND_QUEUE_INFO_EXT
class VkExportMetalBufferInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_BUFFER_INFO_EXT
class VkImportMetalBufferInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_METAL_BUFFER_INFO_EXT
class VkExportMetalTextureInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_TEXTURE_INFO_EXT
class VkImportMetalTextureInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_METAL_TEXTURE_INFO_EXT
class VkExportMetalIOSurfaceInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_IO_SURFACE_INFO_EXT
class VkImportMetalIOSurfaceInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_METAL_IO_SURFACE_INFO_EXT
class VkExportMetalSharedEventInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXPORT_METAL_SHARED_EVENT_INFO_EXT
class VkImportMetalSharedEventInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_METAL_SHARED_EVENT_INFO_EXT
class VkPhysicalDeviceNonSeamlessCubeMapFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_NON_SEAMLESS_CUBE_MAP_FEATURES_EXT
class VkPhysicalDevicePipelineRobustnessFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_ROBUSTNESS_FEATURES
class VkPhysicalDevicePipelineRobustnessFeaturesEXT(Structure):
    pass
class VkPipelineRobustnessCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_ROBUSTNESS_CREATE_INFO
class VkPipelineRobustnessCreateInfoEXT(Structure):
    pass
class VkPhysicalDevicePipelineRobustnessProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_ROBUSTNESS_PROPERTIES
class VkPhysicalDevicePipelineRobustnessPropertiesEXT(Structure):
    pass
class VkImageViewSampleWeightCreateInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_VIEW_SAMPLE_WEIGHT_CREATE_INFO_QCOM
class VkPhysicalDeviceImageProcessingFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_FEATURES_QCOM
class VkPhysicalDeviceImageProcessingPropertiesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_PROPERTIES_QCOM
class VkPhysicalDeviceTilePropertiesFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TILE_PROPERTIES_FEATURES_QCOM
class VkTilePropertiesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TILE_PROPERTIES_QCOM
class VkTileMemoryBindInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TILE_MEMORY_BIND_INFO_QCOM
class VkPhysicalDeviceAmigoProfilingFeaturesSEC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_AMIGO_PROFILING_FEATURES_SEC
class VkAmigoProfilingSubmitInfoSEC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_AMIGO_PROFILING_SUBMIT_INFO_SEC
class VkPhysicalDeviceAttachmentFeedbackLoopLayoutFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ATTACHMENT_FEEDBACK_LOOP_LAYOUT_FEATURES_EXT
class VkPhysicalDeviceDepthClampZeroOneFeaturesEXT(Structure):
    pass
class VkAttachmentFeedbackLoopInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_FEEDBACK_LOOP_INFO_EXT
class VkPhysicalDeviceAddressBindingReportFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ADDRESS_BINDING_REPORT_FEATURES_EXT
class VkRenderingAttachmentFlagsInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_FLAGS_INFO_KHR
class VkResolveImageModeInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RESOLVE_IMAGE_MODE_INFO_KHR
class VkDeviceAddressBindingCallbackDataEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_ADDRESS_BINDING_CALLBACK_DATA_EXT
class VkPhysicalDeviceOpticalFlowFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPTICAL_FLOW_FEATURES_NV
class VkPhysicalDeviceOpticalFlowPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_OPTICAL_FLOW_PROPERTIES_NV
class VkOpticalFlowImageFormatInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_INFO_NV
class VkOpticalFlowImageFormatPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_PROPERTIES_NV
class VkOpticalFlowSessionCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_INFO_NV
class VkOpticalFlowSessionCreatePrivateDataInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_PRIVATE_DATA_INFO_NV
class VkOpticalFlowExecuteInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPTICAL_FLOW_EXECUTE_INFO_NV
class VkPhysicalDeviceFaultFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FAULT_FEATURES_EXT
class VkDeviceFaultAddressInfoKHR(Structure):
    pass
class VkDeviceFaultAddressInfoEXT(Structure):
    pass
class VkDeviceFaultVendorInfoKHR(Structure):
    pass
class VkDeviceFaultVendorInfoEXT(Structure):
    pass
class VkDeviceFaultInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_KHR
class VkDeviceFaultDebugInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_DEBUG_INFO_KHR
class VkDeviceFaultCountsEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_COUNTS_EXT
class VkDeviceFaultInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_EXT
class VkDeviceFaultVendorBinaryHeaderVersionOneKHR(Structure):
    pass
class VkDeviceFaultVendorBinaryHeaderVersionOneEXT(Structure):
    pass
class VkPhysicalDeviceFaultFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FAULT_FEATURES_KHR
class VkPhysicalDeviceFaultPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FAULT_PROPERTIES_KHR
class VkPhysicalDevicePipelineLibraryGroupHandlesFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_LIBRARY_GROUP_HANDLES_FEATURES_EXT
class VkDepthBiasInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEPTH_BIAS_INFO_EXT
class VkDepthBiasRepresentationInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEPTH_BIAS_REPRESENTATION_INFO_EXT
class VkDecompressMemoryRegionNV(Structure):
    pass
class VkDecompressMemoryRegionEXT(Structure):
    pass
class VkDecompressMemoryInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DECOMPRESS_MEMORY_INFO_EXT
class VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_BUILTINS_PROPERTIES_ARM
class VkPhysicalDeviceShaderCoreBuiltinsFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_BUILTINS_FEATURES_ARM
class VkFrameBoundaryEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAME_BOUNDARY_EXT
class VkPhysicalDeviceFrameBoundaryFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAME_BOUNDARY_FEATURES_EXT
class VkPhysicalDeviceDynamicRenderingUnusedAttachmentsFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DYNAMIC_RENDERING_UNUSED_ATTACHMENTS_FEATURES_EXT
class VkPhysicalDeviceInternallySynchronizedQueuesFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INTERNALLY_SYNCHRONIZED_QUEUES_FEATURES_KHR
class VkSurfacePresentModeKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_PRESENT_MODE_KHR
class VkSurfacePresentModeEXT(Structure):
    pass
class VkSurfacePresentScalingCapabilitiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_PRESENT_SCALING_CAPABILITIES_KHR
class VkSurfacePresentScalingCapabilitiesEXT(Structure):
    pass
class VkSurfacePresentModeCompatibilityKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_PRESENT_MODE_COMPATIBILITY_KHR
class VkSurfacePresentModeCompatibilityEXT(Structure):
    pass
class VkPhysicalDeviceSwapchainMaintenance1FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SWAPCHAIN_MAINTENANCE_1_FEATURES_KHR
class VkPhysicalDeviceSwapchainMaintenance1FeaturesEXT(Structure):
    pass
class VkSwapchainPresentFenceInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_FENCE_INFO_KHR
class VkSwapchainPresentFenceInfoEXT(Structure):
    pass
class VkSwapchainPresentModesCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_MODES_CREATE_INFO_KHR
class VkSwapchainPresentModesCreateInfoEXT(Structure):
    pass
class VkSwapchainPresentModeInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_MODE_INFO_KHR
class VkSwapchainPresentModeInfoEXT(Structure):
    pass
class VkSwapchainPresentScalingCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_SCALING_CREATE_INFO_KHR
class VkSwapchainPresentScalingCreateInfoEXT(Structure):
    pass
class VkReleaseSwapchainImagesInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RELEASE_SWAPCHAIN_IMAGES_INFO_KHR
class VkReleaseSwapchainImagesInfoEXT(Structure):
    pass
class VkPhysicalDeviceDepthBiasControlFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_BIAS_CONTROL_FEATURES_EXT
class VkPhysicalDeviceRayTracingInvocationReorderFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_FEATURES_EXT
class VkPhysicalDeviceRayTracingInvocationReorderFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_FEATURES_NV
class VkPhysicalDeviceRayTracingInvocationReorderPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_PROPERTIES_EXT
class VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_INVOCATION_REORDER_PROPERTIES_NV
class VkPhysicalDeviceExtendedSparseAddressSpaceFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_SPARSE_ADDRESS_SPACE_FEATURES_NV
class VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_SPARSE_ADDRESS_SPACE_PROPERTIES_NV
class VkDirectDriverLoadingInfoLUNARG(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_INFO_LUNARG
class VkDirectDriverLoadingListLUNARG(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DIRECT_DRIVER_LOADING_LIST_LUNARG
class VkPhysicalDeviceMultiviewPerViewViewportsFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PER_VIEW_VIEWPORTS_FEATURES_QCOM
class VkPhysicalDeviceRayTracingPositionFetchFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_POSITION_FETCH_FEATURES_KHR
class VkDeviceImageSubresourceInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_IMAGE_SUBRESOURCE_INFO
class VkDeviceImageSubresourceInfoKHR(Structure):
    pass
class VkPhysicalDeviceShaderCorePropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_PROPERTIES_ARM
class VkPhysicalDeviceMultiviewPerViewRenderAreasFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MULTIVIEW_PER_VIEW_RENDER_AREAS_FEATURES_QCOM
class VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_RENDER_AREAS_RENDER_PASS_BEGIN_INFO_QCOM
class VkQueryLowLatencySupportNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_LOW_LATENCY_SUPPORT_NV
class VkMemoryMapInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_MAP_INFO
class VkMemoryMapInfoKHR(Structure):
    pass
class VkMemoryUnmapInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_UNMAP_INFO
class VkMemoryUnmapInfoKHR(Structure):
    pass
class VkPhysicalDeviceShaderObjectFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_OBJECT_FEATURES_EXT
class VkPhysicalDeviceShaderObjectPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_OBJECT_PROPERTIES_EXT
class VkShaderCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_CREATE_INFO_EXT
class VkPhysicalDeviceShaderTileImageFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_FEATURES_EXT
class VkPhysicalDeviceShaderTileImagePropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_TILE_IMAGE_PROPERTIES_EXT
class VkImportScreenBufferInfoQNX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_SCREEN_BUFFER_INFO_QNX
class VkScreenBufferPropertiesQNX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SCREEN_BUFFER_PROPERTIES_QNX
class VkScreenBufferFormatPropertiesQNX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SCREEN_BUFFER_FORMAT_PROPERTIES_QNX
class VkExternalFormatQNX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_QNX
class VkPhysicalDeviceExternalMemoryScreenBufferFeaturesQNX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_MEMORY_SCREEN_BUFFER_FEATURES_QNX
class VkPhysicalDeviceCooperativeMatrixFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_FEATURES_KHR
class VkCooperativeMatrixPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_PROPERTIES_KHR
class VkPhysicalDeviceCooperativeMatrixPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_PROPERTIES_KHR
class VkPhysicalDeviceCooperativeMatrixConversionFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_CONVERSION_FEATURES_QCOM
class VkPhysicalDeviceShaderEnqueuePropertiesAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ENQUEUE_PROPERTIES_AMDX
class VkPhysicalDeviceShaderEnqueueFeaturesAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ENQUEUE_FEATURES_AMDX
class VkExecutionGraphPipelineCreateInfoAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXECUTION_GRAPH_PIPELINE_CREATE_INFO_AMDX
class VkPipelineShaderStageNodeCreateInfoAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_NODE_CREATE_INFO_AMDX
class VkExecutionGraphPipelineScratchSizeAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXECUTION_GRAPH_PIPELINE_SCRATCH_SIZE_AMDX
class VkDispatchGraphInfoAMDX(Structure):
    pass
class VkDispatchGraphCountInfoAMDX(Structure):
    pass
class VkPhysicalDeviceAntiLagFeaturesAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ANTI_LAG_FEATURES_AMD
class VkAntiLagDataAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANTI_LAG_DATA_AMD
class VkAntiLagPresentationInfoAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANTI_LAG_PRESENTATION_INFO_AMD
class VkBindMemoryStatus(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_MEMORY_STATUS
class VkPhysicalDeviceTileMemoryHeapFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TILE_MEMORY_HEAP_FEATURES_QCOM
class VkPhysicalDeviceTileMemoryHeapPropertiesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TILE_MEMORY_HEAP_PROPERTIES_QCOM
class VkTileMemorySizeInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TILE_MEMORY_SIZE_INFO_QCOM
class VkTileMemoryRequirementsQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TILE_MEMORY_REQUIREMENTS_QCOM
class VkBindMemoryStatusKHR(Structure):
    pass
class VkBindDescriptorSetsInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_SETS_INFO
class VkBindDescriptorSetsInfoKHR(Structure):
    pass
class VkPushConstantsInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_CONSTANTS_INFO
class VkPushConstantsInfoKHR(Structure):
    pass
class VkPushDescriptorSetInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_INFO
class VkPushDescriptorSetInfoKHR(Structure):
    pass
class VkPushDescriptorSetWithTemplateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_WITH_TEMPLATE_INFO
class VkPushDescriptorSetWithTemplateInfoKHR(Structure):
    pass
class VkSetDescriptorBufferOffsetsInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SET_DESCRIPTOR_BUFFER_OFFSETS_INFO_EXT
class VkBindDescriptorBufferEmbeddedSamplersInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_BUFFER_EMBEDDED_SAMPLERS_INFO_EXT
class VkPhysicalDeviceCubicClampFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUBIC_CLAMP_FEATURES_QCOM
class VkPhysicalDeviceYcbcrDegammaFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_YCBCR_DEGAMMA_FEATURES_QCOM
class VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_YCBCR_DEGAMMA_CREATE_INFO_QCOM
class VkPhysicalDeviceCubicWeightsFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUBIC_WEIGHTS_FEATURES_QCOM
class VkSamplerCubicWeightsCreateInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_CUBIC_WEIGHTS_CREATE_INFO_QCOM
class VkBlitImageCubicWeightsInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BLIT_IMAGE_CUBIC_WEIGHTS_INFO_QCOM
class VkPhysicalDeviceImageProcessing2FeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_2_FEATURES_QCOM
class VkPhysicalDeviceImageProcessing2PropertiesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_PROCESSING_2_PROPERTIES_QCOM
class VkSamplerBlockMatchWindowCreateInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_BLOCK_MATCH_WINDOW_CREATE_INFO_QCOM
class VkPhysicalDeviceDescriptorPoolOverallocationFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_POOL_OVERALLOCATION_FEATURES_NV
class VkPhysicalDeviceLayeredDriverPropertiesMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_LAYERED_DRIVER_PROPERTIES_MSFT
class VkPhysicalDevicePerStageDescriptorSetFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PER_STAGE_DESCRIPTOR_SET_FEATURES_NV
class VkPhysicalDeviceExternalFormatResolveFeaturesANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FORMAT_RESOLVE_FEATURES_ANDROID
class VkPhysicalDeviceExternalFormatResolvePropertiesANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_FORMAT_RESOLVE_PROPERTIES_ANDROID
class VkAndroidHardwareBufferFormatResolvePropertiesANDROID(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_FORMAT_RESOLVE_PROPERTIES_ANDROID
class VkLatencySleepModeInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_SLEEP_MODE_INFO_NV
class VkLatencySleepInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_SLEEP_INFO_NV
class VkSetLatencyMarkerInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SET_LATENCY_MARKER_INFO_NV
class VkGetLatencyMarkerInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_GET_LATENCY_MARKER_INFO_NV
class VkLatencyTimingsFrameReportNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_TIMINGS_FRAME_REPORT_NV
class VkOutOfBandQueueTypeInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OUT_OF_BAND_QUEUE_TYPE_INFO_NV
class VkLatencySubmissionPresentIdNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_SUBMISSION_PRESENT_ID_NV
class VkSwapchainLatencyCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_LATENCY_CREATE_INFO_NV
class VkLatencySurfaceCapabilitiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_LATENCY_SURFACE_CAPABILITIES_NV
class VkPhysicalDeviceCudaKernelLaunchFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUDA_KERNEL_LAUNCH_FEATURES_NV
class VkPhysicalDeviceCudaKernelLaunchPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CUDA_KERNEL_LAUNCH_PROPERTIES_NV
class VkDeviceQueueShaderCoreControlCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_QUEUE_SHADER_CORE_CONTROL_CREATE_INFO_ARM
class VkPhysicalDeviceSchedulingControlsFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_FEATURES_ARM
class VkPhysicalDeviceSchedulingControlsPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_PROPERTIES_ARM
class VkPhysicalDeviceSchedulingControlsDispatchParametersPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SCHEDULING_CONTROLS_DISPATCH_PARAMETERS_PROPERTIES_ARM
class VkDispatchParametersARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPATCH_PARAMETERS_ARM
class VkPhysicalDeviceRelaxedLineRasterizationFeaturesIMG(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RELAXED_LINE_RASTERIZATION_FEATURES_IMG
class VkPhysicalDeviceRenderPassStripedFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RENDER_PASS_STRIPED_FEATURES_ARM
class VkPhysicalDeviceRenderPassStripedPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RENDER_PASS_STRIPED_PROPERTIES_ARM
class VkRenderPassStripeInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_INFO_ARM
class VkRenderPassStripeBeginInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_BEGIN_INFO_ARM
class VkRenderPassStripeSubmitInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_STRIPE_SUBMIT_INFO_ARM
class VkPhysicalDevicePipelineOpacityMicromapFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_OPACITY_MICROMAP_FEATURES_ARM
class VkPhysicalDeviceShaderMaximalReconvergenceFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_MAXIMAL_RECONVERGENCE_FEATURES_KHR
class VkPhysicalDeviceShaderSubgroupRotateFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_ROTATE_FEATURES
class VkPhysicalDeviceShaderSubgroupRotateFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceShaderExpectAssumeFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_EXPECT_ASSUME_FEATURES
class VkPhysicalDeviceShaderExpectAssumeFeaturesKHR(Structure):
    pass
class VkPhysicalDeviceShaderFloatControls2Features(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT_CONTROLS_2_FEATURES
class VkPhysicalDeviceShaderFloatControls2FeaturesKHR(Structure):
    pass
class VkPhysicalDeviceDynamicRenderingLocalReadFeatures(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DYNAMIC_RENDERING_LOCAL_READ_FEATURES
class VkPhysicalDeviceDynamicRenderingLocalReadFeaturesKHR(Structure):
    pass
class VkRenderingAttachmentLocationInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_LOCATION_INFO
class VkRenderingAttachmentLocationInfoKHR(Structure):
    pass
class VkRenderingInputAttachmentIndexInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_INPUT_ATTACHMENT_INDEX_INFO
class VkRenderingInputAttachmentIndexInfoKHR(Structure):
    pass
class VkPhysicalDeviceShaderQuadControlFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_QUAD_CONTROL_FEATURES_KHR
class VkPhysicalDeviceShaderAtomicFloat16VectorFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT16_VECTOR_FEATURES_NV
class VkPhysicalDeviceMapMemoryPlacedFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAP_MEMORY_PLACED_FEATURES_EXT
class VkPhysicalDeviceMapMemoryPlacedPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAP_MEMORY_PLACED_PROPERTIES_EXT
class VkMemoryMapPlacedInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_MAP_PLACED_INFO_EXT
class VkPhysicalDeviceShaderBfloat16FeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_BFLOAT16_FEATURES_KHR
class VkPhysicalDeviceRawAccessChainsFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAW_ACCESS_CHAINS_FEATURES_NV
class VkPhysicalDeviceCommandBufferInheritanceFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMMAND_BUFFER_INHERITANCE_FEATURES_NV
class VkPhysicalDeviceImageAlignmentControlFeaturesMESA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ALIGNMENT_CONTROL_FEATURES_MESA
class VkPhysicalDeviceImageAlignmentControlPropertiesMESA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_ALIGNMENT_CONTROL_PROPERTIES_MESA
class VkImageAlignmentControlCreateInfoMESA(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_ALIGNMENT_CONTROL_CREATE_INFO_MESA
class VkPhysicalDeviceShaderReplicatedCompositesFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_REPLICATED_COMPOSITES_FEATURES_EXT
class VkPhysicalDevicePresentModeFifoLatestReadyFeaturesEXT(Structure):
    pass
class VkPhysicalDevicePresentModeFifoLatestReadyFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_MODE_FIFO_LATEST_READY_FEATURES_KHR
class VkDepthClampRangeEXT(Structure):
    pass
class VkPhysicalDeviceCooperativeMatrix2FeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_2_FEATURES_NV
class VkPhysicalDeviceCooperativeMatrix2PropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_MATRIX_2_PROPERTIES_NV
class VkCooperativeMatrixFlexibleDimensionsPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COOPERATIVE_MATRIX_FLEXIBLE_DIMENSIONS_PROPERTIES_NV
class VkPhysicalDeviceHdrVividFeaturesHUAWEI(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HDR_VIVID_FEATURES_HUAWEI
class VkPhysicalDeviceVertexAttributeRobustnessFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_ROBUSTNESS_FEATURES_EXT
class VkPhysicalDeviceDenseGeometryFormatFeaturesAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DENSE_GEOMETRY_FORMAT_FEATURES_AMDX
class VkAccelerationStructureDenseGeometryFormatTrianglesDataAMDX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_DENSE_GEOMETRY_FORMAT_TRIANGLES_DATA_AMDX
class VkPhysicalDeviceDepthClampZeroOneFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_CLAMP_ZERO_ONE_FEATURES_KHR
class VkPhysicalDeviceCooperativeVectorFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_VECTOR_FEATURES_NV
class VkCooperativeVectorPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COOPERATIVE_VECTOR_PROPERTIES_NV
class VkPhysicalDeviceCooperativeVectorPropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COOPERATIVE_VECTOR_PROPERTIES_NV
class VkConvertCooperativeVectorMatrixInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CONVERT_COOPERATIVE_VECTOR_MATRIX_INFO_NV
class VkPhysicalDeviceTileShadingFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TILE_SHADING_FEATURES_QCOM
class VkPhysicalDeviceTileShadingPropertiesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TILE_SHADING_PROPERTIES_QCOM
class VkRenderPassTileShadingCreateInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_TILE_SHADING_CREATE_INFO_QCOM
class VkPerTileBeginInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PER_TILE_BEGIN_INFO_QCOM
class VkPerTileEndInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PER_TILE_END_INFO_QCOM
class VkDispatchTileInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPATCH_TILE_INFO_QCOM
class VkPhysicalDeviceFragmentDensityMapLayeredPropertiesVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_LAYERED_PROPERTIES_VALVE
class VkPhysicalDeviceFragmentDensityMapLayeredFeaturesVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_LAYERED_FEATURES_VALVE
class VkPipelineFragmentDensityMapLayeredCreateInfoVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_DENSITY_MAP_LAYERED_CREATE_INFO_VALVE
class VkSetPresentConfigNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SET_PRESENT_CONFIG_NV
class VkPhysicalDevicePresentMeteringFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_METERING_FEATURES_NV
class VkExternalComputeQueueDeviceCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_COMPUTE_QUEUE_DEVICE_CREATE_INFO_NV
class VkExternalComputeQueueCreateInfoNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_COMPUTE_QUEUE_CREATE_INFO_NV
class VkExternalComputeQueueDataParamsNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_COMPUTE_QUEUE_DATA_PARAMS_NV
class VkPhysicalDeviceExternalComputeQueuePropertiesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_COMPUTE_QUEUE_PROPERTIES_NV
class VkPhysicalDeviceShaderUniformBufferUnsizedArrayFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_UNIFORM_BUFFER_UNSIZED_ARRAY_FEATURES_EXT
class VkPhysicalDeviceShaderMixedFloatDotProductFeaturesVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_MIXED_FLOAT_DOT_PRODUCT_FEATURES_VALVE
class VkPhysicalDevicePrimitiveRestartIndexFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVE_RESTART_INDEX_FEATURES_EXT
class VkPhysicalDeviceFormatPackFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FORMAT_PACK_FEATURES_ARM
class VkPhysicalDeviceThrottleHintFeaturesSEC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_THROTTLE_HINT_FEATURES_SEC
class VkThrottleHintSubmitInfoSEC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_THROTTLE_HINT_SUBMIT_INFO_SEC
class VkTensorDescriptionARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_DESCRIPTION_ARM
class VkTensorCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_CREATE_INFO_ARM
class VkTensorViewCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_VIEW_CREATE_INFO_ARM
class VkTensorMemoryRequirementsInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_MEMORY_REQUIREMENTS_INFO_ARM
class VkBindTensorMemoryInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_TENSOR_MEMORY_INFO_ARM
class VkWriteDescriptorSetTensorARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_TENSOR_ARM
class VkTensorFormatPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_FORMAT_PROPERTIES_ARM
class VkPhysicalDeviceTensorPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TENSOR_PROPERTIES_ARM
class VkTensorMemoryBarrierARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_MEMORY_BARRIER_ARM
class VkTensorDependencyInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_DEPENDENCY_INFO_ARM
class VkPhysicalDeviceTensorFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TENSOR_FEATURES_ARM
class VkDeviceTensorMemoryRequirementsARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_TENSOR_MEMORY_REQUIREMENTS_ARM
class VkCopyTensorInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_TENSOR_INFO_ARM
class VkTensorCopyARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_COPY_ARM
class VkMemoryDedicatedAllocateInfoTensorARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO_TENSOR_ARM
class VkPhysicalDeviceDescriptorBufferTensorPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_TENSOR_PROPERTIES_ARM
class VkPhysicalDeviceDescriptorBufferTensorFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_BUFFER_TENSOR_FEATURES_ARM
class VkTensorCaptureDescriptorDataInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_CAPTURE_DESCRIPTOR_DATA_INFO_ARM
class VkTensorViewCaptureDescriptorDataInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TENSOR_VIEW_CAPTURE_DESCRIPTOR_DATA_INFO_ARM
class VkDescriptorGetTensorInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_GET_TENSOR_INFO_ARM
class VkFrameBoundaryTensorsARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAME_BOUNDARY_TENSORS_ARM
class VkPhysicalDeviceExternalTensorInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_TENSOR_INFO_ARM
class VkExternalTensorPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_TENSOR_PROPERTIES_ARM
class VkExternalMemoryTensorCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_TENSOR_CREATE_INFO_ARM
class VkPhysicalDeviceShaderFloat8FeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_FLOAT8_FEATURES_EXT
class VkSurfaceCreateInfoOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS
class VkPhysicalDeviceDataGraphFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DATA_GRAPH_FEATURES_ARM
class VkDataGraphPipelineConstantTensorSemiStructuredSparsityInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_CONSTANT_TENSOR_SEMI_STRUCTURED_SPARSITY_INFO_ARM
class VkDataGraphPipelineConstantARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_CONSTANT_ARM
class VkDataGraphPipelineResourceInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_RESOURCE_INFO_ARM
class VkDataGraphPipelineResourceInfoImageLayoutARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_RESOURCE_INFO_IMAGE_LAYOUT_ARM
class VkDataGraphPipelineCompilerControlCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_COMPILER_CONTROL_CREATE_INFO_ARM
class VkDataGraphPipelineCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_CREATE_INFO_ARM
class VkDataGraphPipelineShaderModuleCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SHADER_MODULE_CREATE_INFO_ARM
class VkDataGraphPipelineSessionCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SESSION_CREATE_INFO_ARM
class VkDataGraphPipelineSessionBindPointRequirementsInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SESSION_BIND_POINT_REQUIREMENTS_INFO_ARM
class VkDataGraphPipelineSessionBindPointRequirementARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SESSION_BIND_POINT_REQUIREMENT_ARM
class VkDataGraphPipelineSessionMemoryRequirementsInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SESSION_MEMORY_REQUIREMENTS_INFO_ARM
class VkBindDataGraphPipelineSessionMemoryInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_DATA_GRAPH_PIPELINE_SESSION_MEMORY_INFO_ARM
class VkDataGraphPipelineInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_INFO_ARM
class VkDataGraphPipelinePropertyQueryResultARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_PROPERTY_QUERY_RESULT_ARM
class VkDataGraphPipelineIdentifierCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_IDENTIFIER_CREATE_INFO_ARM
class VkDataGraphPipelineDispatchInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_DISPATCH_INFO_ARM
class VkPhysicalDeviceDataGraphProcessingEngineARM(Structure):
    pass
class VkPhysicalDeviceDataGraphOperationSupportARM(Structure):
    pass
class VkQueueFamilyDataGraphPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_DATA_GRAPH_PROPERTIES_ARM
class VkPhysicalDeviceQueueFamilyDataGraphProcessingEngineInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_QUEUE_FAMILY_DATA_GRAPH_PROCESSING_ENGINE_INFO_ARM
class VkQueueFamilyDataGraphProcessingEnginePropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_DATA_GRAPH_PROCESSING_ENGINE_PROPERTIES_ARM
class VkDataGraphProcessingEngineCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PROCESSING_ENGINE_CREATE_INFO_ARM
class VkPhysicalDevicePipelineCacheIncrementalModeFeaturesSEC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_CACHE_INCREMENTAL_MODE_FEATURES_SEC
class VkDataGraphPipelineBuiltinModelCreateInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_BUILTIN_MODEL_CREATE_INFO_QCOM
class VkPhysicalDeviceDataGraphModelFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DATA_GRAPH_MODEL_FEATURES_QCOM
class VkPhysicalDeviceShaderUntypedPointersFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_UNTYPED_POINTERS_FEATURES_KHR
class VkNativeBufferOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_NATIVE_BUFFER_OHOS
class VkSwapchainImageCreateInfoOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_IMAGE_CREATE_INFO_OHOS
class VkPhysicalDevicePresentationPropertiesOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENTATION_PROPERTIES_OHOS
class VkPhysicalDeviceVideoEncodeRgbConversionFeaturesVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_RGB_CONVERSION_FEATURES_VALVE
class VkVideoEncodeRgbConversionCapabilitiesVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_RGB_CONVERSION_CAPABILITIES_VALVE
class VkVideoEncodeProfileRgbConversionInfoVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_PROFILE_RGB_CONVERSION_INFO_VALVE
class VkVideoEncodeSessionRgbConversionCreateInfoVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_RGB_CONVERSION_CREATE_INFO_VALVE
class VkPhysicalDeviceShader64BitIndexingFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_64_BIT_INDEXING_FEATURES_EXT
class VkNativeBufferUsageOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_NATIVE_BUFFER_USAGE_OHOS
class VkNativeBufferPropertiesOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_NATIVE_BUFFER_PROPERTIES_OHOS
class VkNativeBufferFormatPropertiesOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_NATIVE_BUFFER_FORMAT_PROPERTIES_OHOS
class VkImportNativeBufferInfoOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMPORT_NATIVE_BUFFER_INFO_OHOS
class VkMemoryGetNativeBufferInfoOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_GET_NATIVE_BUFFER_INFO_OHOS
class VkExternalFormatOHOS(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_OHOS
class VkPerfHintInfoQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERF_HINT_INFO_QCOM
class VkPhysicalDeviceQueuePerfHintFeaturesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_QUEUE_PERF_HINT_FEATURES_QCOM
class VkPhysicalDeviceQueuePerfHintPropertiesQCOM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_QUEUE_PERF_HINT_PROPERTIES_QCOM
class VkPhysicalDevicePerformanceCountersByRegionFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_COUNTERS_BY_REGION_FEATURES_ARM
class VkPhysicalDevicePerformanceCountersByRegionPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_COUNTERS_BY_REGION_PROPERTIES_ARM
class VkPerformanceCounterARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_ARM
class VkPerformanceCounterDescriptionARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_ARM
class VkRenderPassPerformanceCountersByRegionBeginInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_PERFORMANCE_COUNTERS_BY_REGION_BEGIN_INFO_ARM
class VkComputeOccupancyPriorityParametersNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMPUTE_OCCUPANCY_PRIORITY_PARAMETERS_NV
class VkPhysicalDeviceComputeOccupancyPriorityFeaturesNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMPUTE_OCCUPANCY_PRIORITY_FEATURES_NV
class VkPhysicalDeviceShaderLongVectorFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_LONG_VECTOR_FEATURES_EXT
class VkPhysicalDeviceShaderLongVectorPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_LONG_VECTOR_PROPERTIES_EXT
class VkPhysicalDeviceTextureCompressionASTC3DFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXTURE_COMPRESSION_ASTC_3D_FEATURES_EXT
class VkPhysicalDeviceShaderSubgroupPartitionedFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_SUBGROUP_PARTITIONED_FEATURES_EXT
class VkHostAddressRangeEXT(Structure):
    pass
class VkHostAddressRangeConstEXT(Structure):
    pass
class VkDeviceAddressRangeEXT(Structure):
    pass
class VkTexelBufferDescriptorInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_TEXEL_BUFFER_DESCRIPTOR_INFO_EXT
class VkImageDescriptorInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_DESCRIPTOR_INFO_EXT
class VkResourceDescriptorDataEXT(Union):
    pass
class VkResourceDescriptorInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_RESOURCE_DESCRIPTOR_INFO_EXT
class VkBindHeapInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_HEAP_INFO_EXT
class VkPushDataInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_DATA_INFO_EXT
class VkDescriptorMappingSourceConstantOffsetEXT(Structure):
    pass
class VkDescriptorMappingSourcePushIndexEXT(Structure):
    pass
class VkDescriptorMappingSourceIndirectIndexEXT(Structure):
    pass
class VkDescriptorMappingSourceIndirectIndexArrayEXT(Structure):
    pass
class VkDescriptorMappingSourceHeapDataEXT(Structure):
    pass
class VkDescriptorMappingSourceShaderRecordIndexEXT(Structure):
    pass
class VkDescriptorMappingSourceIndirectAddressEXT(Structure):
    pass
class VkDescriptorMappingSourceDataEXT(Union):
    pass
class VkDescriptorSetAndBindingMappingEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_AND_BINDING_MAPPING_EXT
class VkShaderDescriptorSetAndBindingMappingInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_DESCRIPTOR_SET_AND_BINDING_MAPPING_INFO_EXT
class VkSamplerCustomBorderColorIndexCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SAMPLER_CUSTOM_BORDER_COLOR_INDEX_CREATE_INFO_EXT
class VkOpaqueCaptureDataCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_OPAQUE_CAPTURE_DATA_CREATE_INFO_EXT
class VkIndirectCommandsLayoutPushDataTokenNV(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_PUSH_DATA_TOKEN_NV
class VkSubsampledImageFormatPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBSAMPLED_IMAGE_FORMAT_PROPERTIES_EXT
class VkPhysicalDeviceDescriptorHeapFeaturesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_HEAP_FEATURES_EXT
class VkPhysicalDeviceDescriptorHeapPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_HEAP_PROPERTIES_EXT
class VkCommandBufferInheritanceDescriptorHeapInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_DESCRIPTOR_HEAP_INFO_EXT
class VkPhysicalDeviceDescriptorHeapTensorPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DESCRIPTOR_HEAP_TENSOR_PROPERTIES_ARM
class VkPhysicalDeviceShaderInstrumentationFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INSTRUMENTATION_FEATURES_ARM
class VkPhysicalDeviceShaderInstrumentationPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_INSTRUMENTATION_PROPERTIES_ARM
class VkShaderInstrumentationCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_INSTRUMENTATION_CREATE_INFO_ARM
class VkShaderInstrumentationMetricDescriptionARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_INSTRUMENTATION_METRIC_DESCRIPTION_ARM
class VkShaderInstrumentationMetricDataHeaderARM(Structure):
    pass
class VkDeviceAddressRangeKHR(Structure):
    pass
class VkDeviceMemoryCopyKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_COPY_KHR
class VkCopyDeviceMemoryInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_DEVICE_MEMORY_INFO_KHR
class VkDeviceMemoryImageCopyKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_IMAGE_COPY_KHR
class VkCopyDeviceMemoryImageInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_COPY_DEVICE_MEMORY_IMAGE_INFO_KHR
class VkMemoryRangeBarriersInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_RANGE_BARRIERS_INFO_KHR
class VkMemoryRangeBarrierKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_RANGE_BARRIER_KHR
class VkPhysicalDeviceDeviceAddressCommandsFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_ADDRESS_COMMANDS_FEATURES_KHR
class VkConditionalRenderingBeginInfo2EXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_2_EXT
class VkAccelerationStructureCreateInfo2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_CREATE_INFO_2_KHR
class VkBindIndexBuffer3InfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_INDEX_BUFFER_3_INFO_KHR
class VkBindVertexBuffer3InfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_VERTEX_BUFFER_3_INFO_KHR
class VkDrawIndirect2InfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DRAW_INDIRECT_2_INFO_KHR
class VkDrawIndirectCount2InfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DRAW_INDIRECT_COUNT_2_INFO_KHR
class VkDispatchIndirect2InfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DISPATCH_INDIRECT_2_INFO_KHR
class VkBindTransformFeedbackBuffer2InfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_TRANSFORM_FEEDBACK_BUFFER_2_INFO_EXT
class VkMemoryMarkerInfoAMD(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_MARKER_INFO_AMD
class VkPhysicalDeviceShaderConstantDataFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CONSTANT_DATA_FEATURES_KHR
class VkPhysicalDeviceShaderAbortFeaturesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ABORT_FEATURES_KHR
class VkPhysicalDeviceShaderAbortPropertiesKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ABORT_PROPERTIES_KHR
class VkDeviceFaultShaderAbortMessageInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_FAULT_SHADER_ABORT_MESSAGE_INFO_KHR
class VkDataGraphTOSANameQualityARM(Structure):
    pass
class VkQueueFamilyDataGraphTOSAPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_DATA_GRAPH_TOSA_PROPERTIES_ARM
class VkDataGraphPipelineSingleNodeConnectionARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SINGLE_NODE_CONNECTION_ARM
class VkPhysicalDeviceDataGraphOpticalFlowFeaturesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DATA_GRAPH_OPTICAL_FLOW_FEATURES_ARM
class VkQueueFamilyDataGraphOpticalFlowPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_DATA_GRAPH_OPTICAL_FLOW_PROPERTIES_ARM
class VkDataGraphOpticalFlowImageFormatInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_OPTICAL_FLOW_IMAGE_FORMAT_INFO_ARM
class VkDataGraphOpticalFlowImageFormatPropertiesARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_OPTICAL_FLOW_IMAGE_FORMAT_PROPERTIES_ARM
class VkDataGraphPipelineSingleNodeCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_SINGLE_NODE_CREATE_INFO_ARM
class VkDataGraphPipelineOpticalFlowCreateInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_OPTICAL_FLOW_CREATE_INFO_ARM
class VkDataGraphPipelineOpticalFlowDispatchInfoARM(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'sType' not in kwargs:
            self.sType = VkStructureType.VK_STRUCTURE_TYPE_DATA_GRAPH_PIPELINE_OPTICAL_FLOW_DISPATCH_INFO_ARM

PFN_vkInternalAllocationNotification = CFUNCTYPE(None, c_void_p, c_size_t, c_int32, c_int32)
PFN_vkInternalFreeNotification = CFUNCTYPE(None, c_void_p, c_size_t, c_int32, c_int32)
PFN_vkReallocationFunction = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_size_t, c_size_t, c_int32)
PFN_vkAllocationFunction = CFUNCTYPE(c_void_p, c_void_p, c_size_t, c_size_t, c_int32)
PFN_vkFreeFunction = CFUNCTYPE(None, c_void_p, c_void_p)
PFN_vkVoidFunction = CFUNCTYPE(None)
PFN_vkDebugReportCallbackEXT = CFUNCTYPE(c_uint32, c_uint32, c_int32, c_uint64, c_size_t, c_int32, c_char_p, c_char_p, c_void_p)
PFN_vkDebugUtilsMessengerCallbackEXT = CFUNCTYPE(c_uint32, c_int32, c_uint32, POINTER(VkDebugUtilsMessengerCallbackDataEXT), c_void_p)
PFN_vkFaultCallbackFunction = CFUNCTYPE(None, c_uint32, c_uint32, POINTER(VkFaultData))
PFN_vkDeviceMemoryReportCallbackEXT = CFUNCTYPE(None, POINTER(VkDeviceMemoryReportCallbackDataEXT), c_void_p)
PFN_vkGetInstanceProcAddrLUNARG = CFUNCTYPE(PFN_vkVoidFunction, c_void_p, c_char_p)

VkBaseOutStructure._fields_ = [
    ("sType", c_int32),
    ("pNext", POINTER(VkBaseOutStructure)),
]

VkBaseInStructure._fields_ = [
    ("sType", c_int32),
    ("pNext", POINTER(VkBaseInStructure)),
]

VkOffset2D._fields_ = [
    ("x", c_int32),
    ("y", c_int32),
]

VkOffset3D._fields_ = [
    ("x", c_int32),
    ("y", c_int32),
    ("z", c_int32),
]

VkExtent2D._fields_ = [
    ("width", c_uint32),
    ("height", c_uint32),
]

VkExtent3D._fields_ = [
    ("width", c_uint32),
    ("height", c_uint32),
    ("depth", c_uint32),
]

VkViewport._fields_ = [
    ("x", c_float),
    ("y", c_float),
    ("width", c_float),
    ("height", c_float),
    ("minDepth", c_float),
    ("maxDepth", c_float),
]

VkRect2D._fields_ = [
    ("offset", VkOffset2D),
    ("extent", VkExtent2D),
]

VkClearRect._fields_ = [
    ("rect", VkRect2D),
    ("baseArrayLayer", c_uint32),
    ("layerCount", c_uint32),
]

VkComponentMapping._fields_ = [
    ("r", c_int32),
    ("g", c_int32),
    ("b", c_int32),
    ("a", c_int32),
]

VkPhysicalDeviceLimits._fields_ = [
    ("maxImageDimension1D", c_uint32),
    ("maxImageDimension2D", c_uint32),
    ("maxImageDimension3D", c_uint32),
    ("maxImageDimensionCube", c_uint32),
    ("maxImageArrayLayers", c_uint32),
    ("maxTexelBufferElements", c_uint32),
    ("maxUniformBufferRange", c_uint32),
    ("maxStorageBufferRange", c_uint32),
    ("maxPushConstantsSize", c_uint32),
    ("maxMemoryAllocationCount", c_uint32),
    ("maxSamplerAllocationCount", c_uint32),
    ("bufferImageGranularity", c_uint64),
    ("sparseAddressSpaceSize", c_uint64),
    ("maxBoundDescriptorSets", c_uint32),
    ("maxPerStageDescriptorSamplers", c_uint32),
    ("maxPerStageDescriptorUniformBuffers", c_uint32),
    ("maxPerStageDescriptorStorageBuffers", c_uint32),
    ("maxPerStageDescriptorSampledImages", c_uint32),
    ("maxPerStageDescriptorStorageImages", c_uint32),
    ("maxPerStageDescriptorInputAttachments", c_uint32),
    ("maxPerStageResources", c_uint32),
    ("maxDescriptorSetSamplers", c_uint32),
    ("maxDescriptorSetUniformBuffers", c_uint32),
    ("maxDescriptorSetUniformBuffersDynamic", c_uint32),
    ("maxDescriptorSetStorageBuffers", c_uint32),
    ("maxDescriptorSetStorageBuffersDynamic", c_uint32),
    ("maxDescriptorSetSampledImages", c_uint32),
    ("maxDescriptorSetStorageImages", c_uint32),
    ("maxDescriptorSetInputAttachments", c_uint32),
    ("maxVertexInputAttributes", c_uint32),
    ("maxVertexInputBindings", c_uint32),
    ("maxVertexInputAttributeOffset", c_uint32),
    ("maxVertexInputBindingStride", c_uint32),
    ("maxVertexOutputComponents", c_uint32),
    ("maxTessellationGenerationLevel", c_uint32),
    ("maxTessellationPatchSize", c_uint32),
    ("maxTessellationControlPerVertexInputComponents", c_uint32),
    ("maxTessellationControlPerVertexOutputComponents", c_uint32),
    ("maxTessellationControlPerPatchOutputComponents", c_uint32),
    ("maxTessellationControlTotalOutputComponents", c_uint32),
    ("maxTessellationEvaluationInputComponents", c_uint32),
    ("maxTessellationEvaluationOutputComponents", c_uint32),
    ("maxGeometryShaderInvocations", c_uint32),
    ("maxGeometryInputComponents", c_uint32),
    ("maxGeometryOutputComponents", c_uint32),
    ("maxGeometryOutputVertices", c_uint32),
    ("maxGeometryTotalOutputComponents", c_uint32),
    ("maxFragmentInputComponents", c_uint32),
    ("maxFragmentOutputAttachments", c_uint32),
    ("maxFragmentDualSrcAttachments", c_uint32),
    ("maxFragmentCombinedOutputResources", c_uint32),
    ("maxComputeSharedMemorySize", c_uint32),
    ("maxComputeWorkGroupCount", (c_uint32 * 3)),
    ("maxComputeWorkGroupInvocations", c_uint32),
    ("maxComputeWorkGroupSize", (c_uint32 * 3)),
    ("subPixelPrecisionBits", c_uint32),
    ("subTexelPrecisionBits", c_uint32),
    ("mipmapPrecisionBits", c_uint32),
    ("maxDrawIndexedIndexValue", c_uint32),
    ("maxDrawIndirectCount", c_uint32),
    ("maxSamplerLodBias", c_float),
    ("maxSamplerAnisotropy", c_float),
    ("maxViewports", c_uint32),
    ("maxViewportDimensions", (c_uint32 * 2)),
    ("viewportBoundsRange", (c_float * 2)),
    ("viewportSubPixelBits", c_uint32),
    ("minMemoryMapAlignment", c_size_t),
    ("minTexelBufferOffsetAlignment", c_uint64),
    ("minUniformBufferOffsetAlignment", c_uint64),
    ("minStorageBufferOffsetAlignment", c_uint64),
    ("minTexelOffset", c_int32),
    ("maxTexelOffset", c_uint32),
    ("minTexelGatherOffset", c_int32),
    ("maxTexelGatherOffset", c_uint32),
    ("minInterpolationOffset", c_float),
    ("maxInterpolationOffset", c_float),
    ("subPixelInterpolationOffsetBits", c_uint32),
    ("maxFramebufferWidth", c_uint32),
    ("maxFramebufferHeight", c_uint32),
    ("maxFramebufferLayers", c_uint32),
    ("framebufferColorSampleCounts", c_uint32),
    ("framebufferDepthSampleCounts", c_uint32),
    ("framebufferStencilSampleCounts", c_uint32),
    ("framebufferNoAttachmentsSampleCounts", c_uint32),
    ("maxColorAttachments", c_uint32),
    ("sampledImageColorSampleCounts", c_uint32),
    ("sampledImageIntegerSampleCounts", c_uint32),
    ("sampledImageDepthSampleCounts", c_uint32),
    ("sampledImageStencilSampleCounts", c_uint32),
    ("storageImageSampleCounts", c_uint32),
    ("maxSampleMaskWords", c_uint32),
    ("timestampComputeAndGraphics", c_uint32),
    ("timestampPeriod", c_float),
    ("maxClipDistances", c_uint32),
    ("maxCullDistances", c_uint32),
    ("maxCombinedClipAndCullDistances", c_uint32),
    ("discreteQueuePriorities", c_uint32),
    ("pointSizeRange", (c_float * 2)),
    ("lineWidthRange", (c_float * 2)),
    ("pointSizeGranularity", c_float),
    ("lineWidthGranularity", c_float),
    ("strictLines", c_uint32),
    ("standardSampleLocations", c_uint32),
    ("optimalBufferCopyOffsetAlignment", c_uint64),
    ("optimalBufferCopyRowPitchAlignment", c_uint64),
    ("nonCoherentAtomSize", c_uint64),
]

VkPhysicalDeviceSparseProperties._fields_ = [
    ("residencyStandard2DBlockShape", c_uint32),
    ("residencyStandard2DMultisampleBlockShape", c_uint32),
    ("residencyStandard3DBlockShape", c_uint32),
    ("residencyAlignedMipSize", c_uint32),
    ("residencyNonResidentStrict", c_uint32),
]

VkPhysicalDeviceProperties._fields_ = [
    ("apiVersion", c_uint32),
    ("driverVersion", c_uint32),
    ("vendorID", c_uint32),
    ("deviceID", c_uint32),
    ("deviceType", c_int32),
    ("deviceName", (c_char * VK_MAX_PHYSICAL_DEVICE_NAME_SIZE)),
    ("pipelineCacheUUID", (c_uint8 * VK_UUID_SIZE)),
    ("limits", VkPhysicalDeviceLimits),
    ("sparseProperties", VkPhysicalDeviceSparseProperties),
]

VkExtensionProperties._fields_ = [
    ("extensionName", (c_char * VK_MAX_EXTENSION_NAME_SIZE)),
    ("specVersion", c_uint32),
]

VkLayerProperties._fields_ = [
    ("layerName", (c_char * VK_MAX_EXTENSION_NAME_SIZE)),
    ("specVersion", c_uint32),
    ("implementationVersion", c_uint32),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
]

VkApplicationInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pApplicationName", c_char_p),
    ("applicationVersion", c_uint32),
    ("pEngineName", c_char_p),
    ("engineVersion", c_uint32),
    ("apiVersion", c_uint32),
]

VkAllocationCallbacks._fields_ = [
    ("pUserData", c_void_p),
    ("pfnAllocation", PFN_vkAllocationFunction),
    ("pfnReallocation", PFN_vkReallocationFunction),
    ("pfnFree", PFN_vkFreeFunction),
    ("pfnInternalAllocation", PFN_vkInternalAllocationNotification),
    ("pfnInternalFree", PFN_vkInternalFreeNotification),
]

VkDeviceQueueCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("queueFamilyIndex", c_uint32),
    ("queueCount", c_uint32),
    ("pQueuePriorities", POINTER(c_float)),
]

VkDeviceCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("queueCreateInfoCount", c_uint32),
    ("pQueueCreateInfos", POINTER(VkDeviceQueueCreateInfo)),
    ("enabledLayerCount", c_uint32),
    ("ppEnabledLayerNames", POINTER(c_char_p)),
    ("enabledExtensionCount", c_uint32),
    ("ppEnabledExtensionNames", POINTER(c_char_p)),
    ("pEnabledFeatures", POINTER(VkPhysicalDeviceFeatures)),
]

VkInstanceCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pApplicationInfo", POINTER(VkApplicationInfo)),
    ("enabledLayerCount", c_uint32),
    ("ppEnabledLayerNames", POINTER(c_char_p)),
    ("enabledExtensionCount", c_uint32),
    ("ppEnabledExtensionNames", POINTER(c_char_p)),
]

VkQueueFamilyProperties._fields_ = [
    ("queueFlags", c_uint32),
    ("queueCount", c_uint32),
    ("timestampValidBits", c_uint32),
    ("minImageTransferGranularity", VkExtent3D),
]

VkMemoryType._fields_ = [
    ("propertyFlags", c_uint32),
    ("heapIndex", c_uint32),
]

VkMemoryHeap._fields_ = [
    ("size", c_uint64),
    ("flags", c_uint32),
]

VkPhysicalDeviceMemoryProperties._fields_ = [
    ("memoryTypeCount", c_uint32),
    ("memoryTypes", (VkMemoryType * VK_MAX_MEMORY_TYPES)),
    ("memoryHeapCount", c_uint32),
    ("memoryHeaps", (VkMemoryHeap * VK_MAX_MEMORY_HEAPS)),
]

VkMemoryAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allocationSize", c_uint64),
    ("memoryTypeIndex", c_uint32),
]

VkMemoryRequirements._fields_ = [
    ("size", c_uint64),
    ("alignment", c_uint64),
    ("memoryTypeBits", c_uint32),
]

VkSparseImageFormatProperties._fields_ = [
    ("aspectMask", c_uint32),
    ("imageGranularity", VkExtent3D),
    ("flags", c_uint32),
]

VkSparseImageMemoryRequirements._fields_ = [
    ("formatProperties", VkSparseImageFormatProperties),
    ("imageMipTailFirstLod", c_uint32),
    ("imageMipTailSize", c_uint64),
    ("imageMipTailOffset", c_uint64),
    ("imageMipTailStride", c_uint64),
]

VkMappedMemoryRange._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("offset", c_uint64),
    ("size", c_uint64),
]

VkFormatProperties._fields_ = [
    ("linearTilingFeatures", c_uint32),
    ("optimalTilingFeatures", c_uint32),
    ("bufferFeatures", c_uint32),
]

VkImageFormatProperties._fields_ = [
    ("maxExtent", VkExtent3D),
    ("maxMipLevels", c_uint32),
    ("maxArrayLayers", c_uint32),
    ("sampleCounts", c_uint32),
    ("maxResourceSize", c_uint64),
]

VkDescriptorBufferInfo._fields_ = [
    ("buffer", c_void_p),
    ("offset", c_uint64),
    ("range", c_uint64),
]

VkDescriptorImageInfo._fields_ = [
    ("sampler", c_void_p),
    ("imageView", c_void_p),
    ("imageLayout", c_int32),
]

VkWriteDescriptorSet._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dstSet", c_void_p),
    ("dstBinding", c_uint32),
    ("dstArrayElement", c_uint32),
    ("descriptorCount", c_uint32),
    ("descriptorType", c_int32),
    ("pImageInfo", POINTER(VkDescriptorImageInfo)),
    ("pBufferInfo", POINTER(VkDescriptorBufferInfo)),
    ("pTexelBufferView", POINTER(c_void_p)),
]

VkCopyDescriptorSet._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcSet", c_void_p),
    ("srcBinding", c_uint32),
    ("srcArrayElement", c_uint32),
    ("dstSet", c_void_p),
    ("dstBinding", c_uint32),
    ("dstArrayElement", c_uint32),
    ("descriptorCount", c_uint32),
]

VkBufferUsageFlags2CreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("usage", c_uint64),
]

VkBufferUsageFlags2CreateInfoKHR._fields_ = [
]

VkBufferCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("size", c_uint64),
    ("usage", c_uint32),
    ("sharingMode", c_int32),
    ("queueFamilyIndexCount", c_uint32),
    ("pQueueFamilyIndices", POINTER(c_uint32)),
]

VkBufferViewCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("buffer", c_void_p),
    ("format", c_int32),
    ("offset", c_uint64),
    ("range", c_uint64),
]

VkImageSubresource._fields_ = [
    ("aspectMask", c_uint32),
    ("mipLevel", c_uint32),
    ("arrayLayer", c_uint32),
]

VkImageSubresourceLayers._fields_ = [
    ("aspectMask", c_uint32),
    ("mipLevel", c_uint32),
    ("baseArrayLayer", c_uint32),
    ("layerCount", c_uint32),
]

VkImageSubresourceRange._fields_ = [
    ("aspectMask", c_uint32),
    ("baseMipLevel", c_uint32),
    ("levelCount", c_uint32),
    ("baseArrayLayer", c_uint32),
    ("layerCount", c_uint32),
]

VkMemoryBarrier._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcAccessMask", c_uint32),
    ("dstAccessMask", c_uint32),
]

VkBufferMemoryBarrier._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcAccessMask", c_uint32),
    ("dstAccessMask", c_uint32),
    ("srcQueueFamilyIndex", c_uint32),
    ("dstQueueFamilyIndex", c_uint32),
    ("buffer", c_void_p),
    ("offset", c_uint64),
    ("size", c_uint64),
]

VkImageMemoryBarrier._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcAccessMask", c_uint32),
    ("dstAccessMask", c_uint32),
    ("oldLayout", c_int32),
    ("newLayout", c_int32),
    ("srcQueueFamilyIndex", c_uint32),
    ("dstQueueFamilyIndex", c_uint32),
    ("image", c_void_p),
    ("subresourceRange", VkImageSubresourceRange),
]

VkImageCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("imageType", c_int32),
    ("format", c_int32),
    ("extent", VkExtent3D),
    ("mipLevels", c_uint32),
    ("arrayLayers", c_uint32),
    ("samples", c_int32),
    ("tiling", c_int32),
    ("usage", c_uint32),
    ("sharingMode", c_int32),
    ("queueFamilyIndexCount", c_uint32),
    ("pQueueFamilyIndices", POINTER(c_uint32)),
    ("initialLayout", c_int32),
]

VkSubresourceLayout._fields_ = [
    ("offset", c_uint64),
    ("size", c_uint64),
    ("rowPitch", c_uint64),
    ("arrayPitch", c_uint64),
    ("depthPitch", c_uint64),
]

VkImageViewCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("image", c_void_p),
    ("viewType", c_int32),
    ("format", c_int32),
    ("components", VkComponentMapping),
    ("subresourceRange", VkImageSubresourceRange),
]

VkBufferCopy._fields_ = [
    ("srcOffset", c_uint64),
    ("dstOffset", c_uint64),
    ("size", c_uint64),
]

VkSparseMemoryBind._fields_ = [
    ("resourceOffset", c_uint64),
    ("size", c_uint64),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
    ("flags", c_uint32),
]

VkSparseImageMemoryBind._fields_ = [
    ("subresource", VkImageSubresource),
    ("offset", VkOffset3D),
    ("extent", VkExtent3D),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
    ("flags", c_uint32),
]

VkSparseBufferMemoryBindInfo._fields_ = [
    ("buffer", c_void_p),
    ("bindCount", c_uint32),
    ("pBinds", POINTER(VkSparseMemoryBind)),
]

VkSparseImageOpaqueMemoryBindInfo._fields_ = [
    ("image", c_void_p),
    ("bindCount", c_uint32),
    ("pBinds", POINTER(VkSparseMemoryBind)),
]

VkSparseImageMemoryBindInfo._fields_ = [
    ("image", c_void_p),
    ("bindCount", c_uint32),
    ("pBinds", POINTER(VkSparseImageMemoryBind)),
]

VkBindSparseInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("waitSemaphoreCount", c_uint32),
    ("pWaitSemaphores", POINTER(c_void_p)),
    ("bufferBindCount", c_uint32),
    ("pBufferBinds", POINTER(VkSparseBufferMemoryBindInfo)),
    ("imageOpaqueBindCount", c_uint32),
    ("pImageOpaqueBinds", POINTER(VkSparseImageOpaqueMemoryBindInfo)),
    ("imageBindCount", c_uint32),
    ("pImageBinds", POINTER(VkSparseImageMemoryBindInfo)),
    ("signalSemaphoreCount", c_uint32),
    ("pSignalSemaphores", POINTER(c_void_p)),
]

VkImageCopy._fields_ = [
    ("srcSubresource", VkImageSubresourceLayers),
    ("srcOffset", VkOffset3D),
    ("dstSubresource", VkImageSubresourceLayers),
    ("dstOffset", VkOffset3D),
    ("extent", VkExtent3D),
]

VkImageBlit._fields_ = [
    ("srcSubresource", VkImageSubresourceLayers),
    ("srcOffsets", (VkOffset3D * 2)),
    ("dstSubresource", VkImageSubresourceLayers),
    ("dstOffsets", (VkOffset3D * 2)),
]

VkBufferImageCopy._fields_ = [
    ("bufferOffset", c_uint64),
    ("bufferRowLength", c_uint32),
    ("bufferImageHeight", c_uint32),
    ("imageSubresource", VkImageSubresourceLayers),
    ("imageOffset", VkOffset3D),
    ("imageExtent", VkExtent3D),
]

VkStridedDeviceAddressRangeKHR._fields_ = [
    ("address", c_uint64),
    ("size", c_uint64),
    ("stride", c_uint64),
]

VkCopyMemoryIndirectCommandKHR._fields_ = [
    ("srcAddress", c_uint64),
    ("dstAddress", c_uint64),
    ("size", c_uint64),
]

VkCopyMemoryIndirectCommandNV._fields_ = [
]

VkCopyMemoryIndirectInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcCopyFlags", c_uint32),
    ("dstCopyFlags", c_uint32),
    ("copyCount", c_uint32),
    ("copyAddressRange", VkStridedDeviceAddressRangeKHR),
]

VkCopyMemoryToImageIndirectCommandKHR._fields_ = [
    ("srcAddress", c_uint64),
    ("bufferRowLength", c_uint32),
    ("bufferImageHeight", c_uint32),
    ("imageSubresource", VkImageSubresourceLayers),
    ("imageOffset", VkOffset3D),
    ("imageExtent", VkExtent3D),
]

VkCopyMemoryToImageIndirectCommandNV._fields_ = [
]

VkCopyMemoryToImageIndirectInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcCopyFlags", c_uint32),
    ("copyCount", c_uint32),
    ("copyAddressRange", VkStridedDeviceAddressRangeKHR),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("pImageSubresources", POINTER(VkImageSubresourceLayers)),
]

VkImageResolve._fields_ = [
    ("srcSubresource", VkImageSubresourceLayers),
    ("srcOffset", VkOffset3D),
    ("dstSubresource", VkImageSubresourceLayers),
    ("dstOffset", VkOffset3D),
    ("extent", VkExtent3D),
]

VkShaderModuleCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("codeSize", c_size_t),
    ("pCode", POINTER(c_uint32)),
]

VkDescriptorSetLayoutBinding._fields_ = [
    ("binding", c_uint32),
    ("descriptorType", c_int32),
    ("descriptorCount", c_uint32),
    ("stageFlags", c_uint32),
    ("pImmutableSamplers", POINTER(c_void_p)),
]

VkDescriptorSetLayoutCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("bindingCount", c_uint32),
    ("pBindings", POINTER(VkDescriptorSetLayoutBinding)),
]

VkDescriptorPoolSize._fields_ = [
    ("type", c_int32),
    ("descriptorCount", c_uint32),
]

VkDescriptorPoolCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("maxSets", c_uint32),
    ("poolSizeCount", c_uint32),
    ("pPoolSizes", POINTER(VkDescriptorPoolSize)),
]

VkDescriptorSetAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorPool", c_void_p),
    ("descriptorSetCount", c_uint32),
    ("pSetLayouts", POINTER(c_void_p)),
]

VkSpecializationMapEntry._fields_ = [
    ("constantID", c_uint32),
    ("offset", c_uint32),
    ("size", c_size_t),
]

VkSpecializationInfo._fields_ = [
    ("mapEntryCount", c_uint32),
    ("pMapEntries", POINTER(VkSpecializationMapEntry)),
    ("dataSize", c_size_t),
    ("pData", c_void_p),
]

VkPipelineShaderStageCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stage", c_int32),
    ("module", c_void_p),
    ("pName", c_char_p),
    ("pName", c_char_p),
    ("pSpecializationInfo", POINTER(VkSpecializationInfo)),
]

VkComputePipelineCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stage", VkPipelineShaderStageCreateInfo),
    ("layout", c_void_p),
    ("basePipelineHandle", c_void_p),
    ("basePipelineIndex", c_int32),
]

VkComputePipelineIndirectBufferInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceAddress", c_uint64),
    ("size", c_uint64),
    ("pipelineDeviceAddressCaptureReplay", c_uint64),
]

VkPipelineCreateFlags2CreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
]

VkPipelineCreateFlags2CreateInfoKHR._fields_ = [
]

VkVertexInputBindingDescription._fields_ = [
    ("binding", c_uint32),
    ("stride", c_uint32),
    ("inputRate", c_int32),
]

VkVertexInputAttributeDescription._fields_ = [
    ("location", c_uint32),
    ("binding", c_uint32),
    ("format", c_int32),
    ("offset", c_uint32),
]

VkPipelineVertexInputStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("vertexBindingDescriptionCount", c_uint32),
    ("pVertexBindingDescriptions", POINTER(VkVertexInputBindingDescription)),
    ("vertexAttributeDescriptionCount", c_uint32),
    ("pVertexAttributeDescriptions", POINTER(VkVertexInputAttributeDescription)),
]

VkPipelineInputAssemblyStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("topology", c_int32),
    ("primitiveRestartEnable", c_uint32),
]

VkPipelineTessellationStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("patchControlPoints", c_uint32),
]

VkPipelineViewportStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("viewportCount", c_uint32),
    ("pViewports", POINTER(VkViewport)),
    ("scissorCount", c_uint32),
    ("pScissors", POINTER(VkRect2D)),
]

VkPipelineRasterizationStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("depthClampEnable", c_uint32),
    ("rasterizerDiscardEnable", c_uint32),
    ("polygonMode", c_int32),
    ("cullMode", c_uint32),
    ("frontFace", c_int32),
    ("depthBiasEnable", c_uint32),
    ("depthBiasConstantFactor", c_float),
    ("depthBiasClamp", c_float),
    ("depthBiasSlopeFactor", c_float),
    ("lineWidth", c_float),
]

VkPipelineMultisampleStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("rasterizationSamples", c_int32),
    ("sampleShadingEnable", c_uint32),
    ("minSampleShading", c_float),
    ("pSampleMask", POINTER(c_uint32)),
    ("alphaToCoverageEnable", c_uint32),
    ("alphaToOneEnable", c_uint32),
]

VkPipelineColorBlendAttachmentState._fields_ = [
    ("blendEnable", c_uint32),
    ("srcColorBlendFactor", c_int32),
    ("dstColorBlendFactor", c_int32),
    ("colorBlendOp", c_int32),
    ("srcAlphaBlendFactor", c_int32),
    ("dstAlphaBlendFactor", c_int32),
    ("alphaBlendOp", c_int32),
    ("colorWriteMask", c_uint32),
]

VkPipelineColorBlendStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("logicOpEnable", c_uint32),
    ("logicOp", c_int32),
    ("attachmentCount", c_uint32),
    ("pAttachments", POINTER(VkPipelineColorBlendAttachmentState)),
    ("blendConstants", (c_float * 4)),
]

VkPipelineDynamicStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("dynamicStateCount", c_uint32),
    ("pDynamicStates", POINTER(c_int32)),
]

VkStencilOpState._fields_ = [
    ("failOp", c_int32),
    ("passOp", c_int32),
    ("depthFailOp", c_int32),
    ("compareOp", c_int32),
    ("compareMask", c_uint32),
    ("writeMask", c_uint32),
    ("reference", c_uint32),
]

VkPipelineDepthStencilStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("depthTestEnable", c_uint32),
    ("depthWriteEnable", c_uint32),
    ("depthCompareOp", c_int32),
    ("depthBoundsTestEnable", c_uint32),
    ("stencilTestEnable", c_uint32),
    ("front", VkStencilOpState),
    ("back", VkStencilOpState),
    ("minDepthBounds", c_float),
    ("maxDepthBounds", c_float),
]

VkGraphicsPipelineCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stageCount", c_uint32),
    ("pStages", POINTER(VkPipelineShaderStageCreateInfo)),
    ("pStages", POINTER(VkPipelineShaderStageCreateInfo)),
    ("pVertexInputState", POINTER(VkPipelineVertexInputStateCreateInfo)),
    ("pInputAssemblyState", POINTER(VkPipelineInputAssemblyStateCreateInfo)),
    ("pTessellationState", POINTER(VkPipelineTessellationStateCreateInfo)),
    ("pViewportState", POINTER(VkPipelineViewportStateCreateInfo)),
    ("pRasterizationState", POINTER(VkPipelineRasterizationStateCreateInfo)),
    ("pMultisampleState", POINTER(VkPipelineMultisampleStateCreateInfo)),
    ("pDepthStencilState", POINTER(VkPipelineDepthStencilStateCreateInfo)),
    ("pColorBlendState", POINTER(VkPipelineColorBlendStateCreateInfo)),
    ("pDynamicState", POINTER(VkPipelineDynamicStateCreateInfo)),
    ("layout", c_void_p),
    ("renderPass", c_void_p),
    ("subpass", c_uint32),
    ("basePipelineHandle", c_void_p),
    ("basePipelineIndex", c_int32),
]

VkPipelineCacheCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("initialDataSize", c_size_t),
    ("initialDataSize", c_size_t),
    ("pInitialData", c_void_p),
]

VkPipelineCacheHeaderVersionOne._fields_ = [
    ("headerSize", c_uint32),
    ("headerVersion", c_int32),
    ("vendorID", c_uint32),
    ("deviceID", c_uint32),
    ("pipelineCacheUUID", (c_uint8 * VK_UUID_SIZE)),
]

VkPipelineCacheStageValidationIndexEntry._fields_ = [
    ("codeSize", c_uint64),
    ("codeOffset", c_uint64),
]

VkPipelineCacheSafetyCriticalIndexEntry._fields_ = [
    ("pipelineIdentifier", (c_uint8 * VK_UUID_SIZE)),
    ("pipelineMemorySize", c_uint64),
    ("jsonSize", c_uint64),
    ("jsonOffset", c_uint64),
    ("stageIndexCount", c_uint32),
    ("stageIndexStride", c_uint32),
    ("stageIndexOffset", c_uint64),
]

VkPipelineCacheHeaderVersionSafetyCriticalOne._fields_ = [
    ("headerVersionOne", VkPipelineCacheHeaderVersionOne),
    ("validationVersion", c_int32),
    ("implementationData", c_uint32),
    ("pipelineIndexCount", c_uint32),
    ("pipelineIndexStride", c_uint32),
    ("pipelineIndexOffset", c_uint64),
]

VkPipelineCacheHeaderVersionDataGraphQCOM._fields_ = [
    ("headerSize", c_uint32),
    ("headerVersion", c_int32),
    ("cacheType", c_int32),
    ("cacheVersion", c_uint32),
    ("toolchainVersion", (c_uint32 * VK_DATA_GRAPH_MODEL_TOOLCHAIN_VERSION_LENGTH_QCOM)),
]

VkPushConstantRange._fields_ = [
    ("stageFlags", c_uint32),
    ("offset", c_uint32),
    ("size", c_uint32),
]

VkPipelineBinaryCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pKeysAndDataInfo", POINTER(VkPipelineBinaryKeysAndDataKHR)),
    ("pipeline", c_void_p),
    ("pPipelineCreateInfo", POINTER(VkPipelineCreateInfoKHR)),
]

VkPipelineBinaryHandlesInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBinaryCount", c_uint32),
    ("pPipelineBinaries", POINTER(c_void_p)),
]

VkPipelineBinaryDataKHR._fields_ = [
    ("dataSize", c_size_t),
    ("pData", c_void_p),
]

VkPipelineBinaryKeysAndDataKHR._fields_ = [
    ("binaryCount", c_uint32),
    ("pPipelineBinaryKeys", POINTER(VkPipelineBinaryKeyKHR)),
    ("pPipelineBinaryData", POINTER(VkPipelineBinaryDataKHR)),
]

VkPipelineBinaryKeyKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("keySize", c_uint32),
    ("key", (c_uint8 * VK_MAX_PIPELINE_BINARY_KEY_SIZE_KHR)),
]

VkPipelineBinaryInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("binaryCount", c_uint32),
    ("pPipelineBinaries", POINTER(c_void_p)),
]

VkReleaseCapturedPipelineDataInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipeline", c_void_p),
]

VkPipelineBinaryDataInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBinary", c_void_p),
]

VkPipelineCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkPipelineLayoutCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("setLayoutCount", c_uint32),
    ("pSetLayouts", POINTER(c_void_p)),
    ("pushConstantRangeCount", c_uint32),
    ("pPushConstantRanges", POINTER(VkPushConstantRange)),
]

VkSamplerCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("magFilter", c_int32),
    ("minFilter", c_int32),
    ("mipmapMode", c_int32),
    ("addressModeU", c_int32),
    ("addressModeV", c_int32),
    ("addressModeW", c_int32),
    ("mipLodBias", c_float),
    ("anisotropyEnable", c_uint32),
    ("maxAnisotropy", c_float),
    ("compareEnable", c_uint32),
    ("compareOp", c_int32),
    ("minLod", c_float),
    ("maxLod", c_float),
    ("borderColor", c_int32),
    ("unnormalizedCoordinates", c_uint32),
]

VkCommandPoolCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("queueFamilyIndex", c_uint32),
]

VkCommandBufferAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("commandPool", c_void_p),
    ("level", c_int32),
    ("commandBufferCount", c_uint32),
]

VkCommandBufferInheritanceInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("renderPass", c_void_p),
    ("subpass", c_uint32),
    ("framebuffer", c_void_p),
    ("occlusionQueryEnable", c_uint32),
    ("queryFlags", c_uint32),
    ("pipelineStatistics", c_uint32),
]

VkCommandBufferBeginInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pInheritanceInfo", POINTER(VkCommandBufferInheritanceInfo)),
]

VkRenderPassBeginInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("renderPass", c_void_p),
    ("framebuffer", c_void_p),
    ("renderArea", VkRect2D),
    ("clearValueCount", c_uint32),
    ("pClearValues", POINTER(VkClearValue)),
]

VkClearColorValue._fields_ = [
    ("float32", (c_float * 4)),
    ("int32", (c_int32 * 4)),
    ("uint32", (c_uint32 * 4)),
]

VkClearDepthStencilValue._fields_ = [
    ("depth", c_float),
    ("stencil", c_uint32),
]

VkClearValue._fields_ = [
    ("color", VkClearColorValue),
    ("depthStencil", VkClearDepthStencilValue),
]

VkClearAttachment._fields_ = [
    ("aspectMask", c_uint32),
    ("colorAttachment", c_uint32),
    ("clearValue", VkClearValue),
]

VkAttachmentDescription._fields_ = [
    ("flags", c_uint32),
    ("format", c_int32),
    ("samples", c_int32),
    ("loadOp", c_int32),
    ("storeOp", c_int32),
    ("stencilLoadOp", c_int32),
    ("stencilStoreOp", c_int32),
    ("initialLayout", c_int32),
    ("finalLayout", c_int32),
]

VkAttachmentReference._fields_ = [
    ("attachment", c_uint32),
    ("layout", c_int32),
]

VkSubpassDescription._fields_ = [
    ("flags", c_uint32),
    ("pipelineBindPoint", c_int32),
    ("inputAttachmentCount", c_uint32),
    ("pInputAttachments", POINTER(VkAttachmentReference)),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachments", POINTER(VkAttachmentReference)),
    ("pResolveAttachments", POINTER(VkAttachmentReference)),
    ("pDepthStencilAttachment", POINTER(VkAttachmentReference)),
    ("preserveAttachmentCount", c_uint32),
    ("pPreserveAttachments", POINTER(c_uint32)),
]

VkSubpassDependency._fields_ = [
    ("srcSubpass", c_uint32),
    ("dstSubpass", c_uint32),
    ("srcStageMask", c_uint32),
    ("dstStageMask", c_uint32),
    ("srcAccessMask", c_uint32),
    ("dstAccessMask", c_uint32),
    ("dependencyFlags", c_uint32),
]

VkRenderPassCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("attachmentCount", c_uint32),
    ("pAttachments", POINTER(VkAttachmentDescription)),
    ("subpassCount", c_uint32),
    ("pSubpasses", POINTER(VkSubpassDescription)),
    ("dependencyCount", c_uint32),
    ("pDependencies", POINTER(VkSubpassDependency)),
]

VkEventCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkFenceCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkPhysicalDeviceFeatures._fields_ = [
    ("robustBufferAccess", c_uint32),
    ("fullDrawIndexUint32", c_uint32),
    ("imageCubeArray", c_uint32),
    ("independentBlend", c_uint32),
    ("geometryShader", c_uint32),
    ("tessellationShader", c_uint32),
    ("sampleRateShading", c_uint32),
    ("dualSrcBlend", c_uint32),
    ("logicOp", c_uint32),
    ("multiDrawIndirect", c_uint32),
    ("drawIndirectFirstInstance", c_uint32),
    ("depthClamp", c_uint32),
    ("depthBiasClamp", c_uint32),
    ("fillModeNonSolid", c_uint32),
    ("depthBounds", c_uint32),
    ("wideLines", c_uint32),
    ("largePoints", c_uint32),
    ("alphaToOne", c_uint32),
    ("multiViewport", c_uint32),
    ("samplerAnisotropy", c_uint32),
    ("textureCompressionETC2", c_uint32),
    ("textureCompressionASTC_LDR", c_uint32),
    ("textureCompressionBC", c_uint32),
    ("occlusionQueryPrecise", c_uint32),
    ("pipelineStatisticsQuery", c_uint32),
    ("vertexPipelineStoresAndAtomics", c_uint32),
    ("fragmentStoresAndAtomics", c_uint32),
    ("shaderTessellationAndGeometryPointSize", c_uint32),
    ("shaderImageGatherExtended", c_uint32),
    ("shaderStorageImageExtendedFormats", c_uint32),
    ("shaderStorageImageMultisample", c_uint32),
    ("shaderStorageImageReadWithoutFormat", c_uint32),
    ("shaderStorageImageWriteWithoutFormat", c_uint32),
    ("shaderUniformBufferArrayDynamicIndexing", c_uint32),
    ("shaderSampledImageArrayDynamicIndexing", c_uint32),
    ("shaderStorageBufferArrayDynamicIndexing", c_uint32),
    ("shaderStorageImageArrayDynamicIndexing", c_uint32),
    ("shaderClipDistance", c_uint32),
    ("shaderCullDistance", c_uint32),
    ("shaderFloat64", c_uint32),
    ("shaderInt64", c_uint32),
    ("shaderInt16", c_uint32),
    ("shaderResourceResidency", c_uint32),
    ("shaderResourceMinLod", c_uint32),
    ("sparseBinding", c_uint32),
    ("sparseResidencyBuffer", c_uint32),
    ("sparseResidencyImage2D", c_uint32),
    ("sparseResidencyImage3D", c_uint32),
    ("sparseResidency2Samples", c_uint32),
    ("sparseResidency4Samples", c_uint32),
    ("sparseResidency8Samples", c_uint32),
    ("sparseResidency16Samples", c_uint32),
    ("sparseResidencyAliased", c_uint32),
    ("variableMultisampleRate", c_uint32),
    ("inheritedQueries", c_uint32),
]

VkSemaphoreCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkQueryPoolCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("queryType", c_int32),
    ("queryCount", c_uint32),
    ("pipelineStatistics", c_uint32),
]

VkFramebufferCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("renderPass", c_void_p),
    ("attachmentCount", c_uint32),
    ("pAttachments", POINTER(c_void_p)),
    ("width", c_uint32),
    ("height", c_uint32),
    ("layers", c_uint32),
]

VkDrawIndirectCommand._fields_ = [
    ("vertexCount", c_uint32),
    ("instanceCount", c_uint32),
    ("firstVertex", c_uint32),
    ("firstInstance", c_uint32),
]

VkDrawIndexedIndirectCommand._fields_ = [
    ("indexCount", c_uint32),
    ("instanceCount", c_uint32),
    ("firstIndex", c_uint32),
    ("vertexOffset", c_int32),
    ("firstInstance", c_uint32),
]

VkDispatchIndirectCommand._fields_ = [
    ("x", c_uint32),
    ("y", c_uint32),
    ("z", c_uint32),
]

VkMultiDrawInfoEXT._fields_ = [
    ("firstVertex", c_uint32),
    ("vertexCount", c_uint32),
]

VkMultiDrawIndexedInfoEXT._fields_ = [
    ("firstIndex", c_uint32),
    ("indexCount", c_uint32),
    ("vertexOffset", c_int32),
]

VkSubmitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("waitSemaphoreCount", c_uint32),
    ("pWaitSemaphores", POINTER(c_void_p)),
    ("pWaitDstStageMask", POINTER(c_uint32)),
    ("commandBufferCount", c_uint32),
    ("pCommandBuffers", POINTER(c_void_p)),
    ("signalSemaphoreCount", c_uint32),
    ("pSignalSemaphores", POINTER(c_void_p)),
]

VkDisplayPropertiesKHR._fields_ = [
    ("display", c_void_p),
    ("displayName", c_char_p),
    ("physicalDimensions", VkExtent2D),
    ("physicalResolution", VkExtent2D),
    ("supportedTransforms", c_uint32),
    ("planeReorderPossible", c_uint32),
    ("persistentContent", c_uint32),
]

VkDisplayPlanePropertiesKHR._fields_ = [
    ("currentDisplay", c_void_p),
    ("currentStackIndex", c_uint32),
]

VkDisplayModeParametersKHR._fields_ = [
    ("visibleRegion", VkExtent2D),
    ("refreshRate", c_uint32),
]

VkDisplayModePropertiesKHR._fields_ = [
    ("displayMode", c_void_p),
    ("parameters", VkDisplayModeParametersKHR),
]

VkDisplayModeCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("parameters", VkDisplayModeParametersKHR),
]

VkDisplayPlaneCapabilitiesKHR._fields_ = [
    ("supportedAlpha", c_uint32),
    ("minSrcPosition", VkOffset2D),
    ("maxSrcPosition", VkOffset2D),
    ("minSrcExtent", VkExtent2D),
    ("maxSrcExtent", VkExtent2D),
    ("minDstPosition", VkOffset2D),
    ("maxDstPosition", VkOffset2D),
    ("minDstExtent", VkExtent2D),
    ("maxDstExtent", VkExtent2D),
]

VkDisplaySurfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("displayMode", c_void_p),
    ("planeIndex", c_uint32),
    ("planeStackIndex", c_uint32),
    ("transform", c_int32),
    ("globalAlpha", c_float),
    ("alphaMode", c_int32),
    ("imageExtent", VkExtent2D),
]

VkDisplaySurfaceStereoCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stereoType", c_int32),
]

VkDisplayPresentInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcRect", VkRect2D),
    ("dstRect", VkRect2D),
    ("persistent", c_uint32),
]

VkSurfaceCapabilitiesKHR._fields_ = [
    ("minImageCount", c_uint32),
    ("maxImageCount", c_uint32),
    ("currentExtent", VkExtent2D),
    ("minImageExtent", VkExtent2D),
    ("maxImageExtent", VkExtent2D),
    ("maxImageArrayLayers", c_uint32),
    ("supportedTransforms", c_uint32),
    ("currentTransform", c_int32),
    ("supportedCompositeAlpha", c_uint32),
    ("supportedUsageFlags", c_uint32),
]

VkAndroidSurfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("window", POINTER(c_void_p)),
]

VkViSurfaceCreateInfoNN._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("window", c_void_p),
]

VkWaylandSurfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("display", POINTER(c_void_p)),
    ("surface", POINTER(c_void_p)),
]

VkUbmSurfaceCreateInfoSEC._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("device", POINTER(c_void_p)),
    ("surface", POINTER(c_void_p)),
]

VkWin32SurfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("hinstance", c_void_p),
    ("hwnd", c_void_p),
]

VkXlibSurfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("dpy", POINTER(c_void_p)),
    ("window", c_ulong),
]

VkXcbSurfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("connection", POINTER(c_void_p)),
    ("window", c_uint32),
]

VkDirectFBSurfaceCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("dfb", POINTER(c_void_p)),
    ("surface", POINTER(c_void_p)),
]

VkImagePipeSurfaceCreateInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("imagePipeHandle", c_uint32),
]

VkStreamDescriptorSurfaceCreateInfoGGP._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("streamDescriptor", c_uint32),
]

VkScreenSurfaceCreateInfoQNX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("context", POINTER(c_void_p)),
    ("window", POINTER(c_void_p)),
]

VkSurfaceFormatKHR._fields_ = [
    ("format", c_int32),
    ("colorSpace", c_int32),
]

VkSwapchainCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("surface", c_void_p),
    ("minImageCount", c_uint32),
    ("imageFormat", c_int32),
    ("imageColorSpace", c_int32),
    ("imageExtent", VkExtent2D),
    ("imageArrayLayers", c_uint32),
    ("imageUsage", c_uint32),
    ("imageSharingMode", c_int32),
    ("queueFamilyIndexCount", c_uint32),
    ("pQueueFamilyIndices", POINTER(c_uint32)),
    ("preTransform", c_int32),
    ("compositeAlpha", c_int32),
    ("presentMode", c_int32),
    ("clipped", c_uint32),
    ("oldSwapchain", c_void_p),
    ("oldSwapchain", c_void_p),
]

VkPresentInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("waitSemaphoreCount", c_uint32),
    ("pWaitSemaphores", POINTER(c_void_p)),
    ("swapchainCount", c_uint32),
    ("pSwapchains", POINTER(c_void_p)),
    ("pImageIndices", POINTER(c_uint32)),
    ("pResults", POINTER(c_int32)),
]

VkDebugReportCallbackCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pfnCallback", PFN_vkDebugReportCallbackEXT),
    ("pUserData", c_void_p),
]

VkValidationFlagsEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("disabledValidationCheckCount", c_uint32),
    ("pDisabledValidationChecks", POINTER(c_int32)),
]

VkValidationFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("enabledValidationFeatureCount", c_uint32),
    ("pEnabledValidationFeatures", POINTER(c_int32)),
    ("disabledValidationFeatureCount", c_uint32),
    ("pDisabledValidationFeatures", POINTER(c_int32)),
]

VkLayerSettingsCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("settingCount", c_uint32),
    ("pSettings", POINTER(VkLayerSettingEXT)),
]

VkLayerSettingEXT._fields_ = [
    ("pLayerName", c_char_p),
    ("pSettingName", c_char_p),
    ("type", c_int32),
    ("valueCount", c_uint32),
    ("pValues", c_void_p),
]

VkApplicationParametersEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vendorID", c_uint32),
    ("deviceID", c_uint32),
    ("key", c_uint32),
    ("value", c_uint64),
]

VkPipelineRasterizationStateRasterizationOrderAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rasterizationOrder", c_int32),
]

VkDebugMarkerObjectNameInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("objectType", c_int32),
    ("object", c_uint64),
    ("pObjectName", c_char_p),
]

VkDebugMarkerObjectTagInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("objectType", c_int32),
    ("object", c_uint64),
    ("tagName", c_uint64),
    ("tagSize", c_size_t),
    ("pTag", c_void_p),
]

VkDebugMarkerMarkerInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pMarkerName", c_char_p),
    ("color", (c_float * 4)),
]

VkDedicatedAllocationImageCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dedicatedAllocation", c_uint32),
]

VkDedicatedAllocationBufferCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dedicatedAllocation", c_uint32),
]

VkDedicatedAllocationMemoryAllocateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("buffer", c_void_p),
]

VkExternalImageFormatPropertiesNV._fields_ = [
    ("imageFormatProperties", VkImageFormatProperties),
    ("externalMemoryFeatures", c_uint32),
    ("exportFromImportedHandleTypes", c_uint32),
    ("compatibleHandleTypes", c_uint32),
]

VkExternalMemoryImageCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkExportMemoryAllocateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkImportMemoryWin32HandleInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_uint32),
    ("handle", c_void_p),
]

VkExportMemoryWin32HandleInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", POINTER(c_void_p)),
    ("dwAccess", c_uint32),
]

VkExportMemorySciBufInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", c_void_p),
]

VkImportMemorySciBufInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
    ("handle", c_void_p),
]

VkMemoryGetSciBufInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("handleType", c_int32),
]

VkMemorySciBufPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
]

VkPhysicalDeviceExternalMemorySciBufFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sciBufImport", c_uint32),
    ("sciBufExport", c_uint32),
]

VkPhysicalDeviceExternalSciBufFeaturesNV._fields_ = [
]

VkWin32KeyedMutexAcquireReleaseInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("acquireCount", c_uint32),
    ("pAcquireSyncs", POINTER(c_void_p)),
    ("pAcquireKeys", POINTER(c_uint64)),
    ("pAcquireTimeoutMilliseconds", POINTER(c_uint32)),
    ("releaseCount", c_uint32),
    ("pReleaseSyncs", POINTER(c_void_p)),
    ("pReleaseKeys", POINTER(c_uint64)),
]

VkPhysicalDeviceDeviceGeneratedCommandsFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceGeneratedCommands", c_uint32),
]

VkPushConstantBankInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("bank", c_uint32),
]

VkPhysicalDevicePushConstantBankFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pushConstantBank", c_uint32),
]

VkPhysicalDevicePushConstantBankPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxGraphicsPushConstantBanks", c_uint32),
    ("maxComputePushConstantBanks", c_uint32),
    ("maxGraphicsPushDataBanks", c_uint32),
    ("maxComputePushDataBanks", c_uint32),
]

VkPhysicalDeviceDeviceGeneratedCommandsComputeFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceGeneratedCompute", c_uint32),
    ("deviceGeneratedComputePipelines", c_uint32),
    ("deviceGeneratedComputeCaptureReplay", c_uint32),
]

VkDevicePrivateDataCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("privateDataSlotRequestCount", c_uint32),
]

VkDevicePrivateDataCreateInfoEXT._fields_ = [
]

VkPrivateDataSlotCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkPrivateDataSlotCreateInfoEXT._fields_ = [
]

VkPhysicalDevicePrivateDataFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("privateData", c_uint32),
]

VkPhysicalDevicePrivateDataFeaturesEXT._fields_ = [
]

VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxGraphicsShaderGroupCount", c_uint32),
    ("maxIndirectSequenceCount", c_uint32),
    ("maxIndirectCommandsTokenCount", c_uint32),
    ("maxIndirectCommandsStreamCount", c_uint32),
    ("maxIndirectCommandsTokenOffset", c_uint32),
    ("maxIndirectCommandsStreamStride", c_uint32),
    ("minSequencesCountBufferOffsetAlignment", c_uint32),
    ("minSequencesIndexBufferOffsetAlignment", c_uint32),
    ("minIndirectCommandsBufferOffsetAlignment", c_uint32),
]

VkPhysicalDeviceClusterAccelerationStructureFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("clusterAccelerationStructure", c_uint32),
]

VkPhysicalDeviceClusterAccelerationStructurePropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxVerticesPerCluster", c_uint32),
    ("maxTrianglesPerCluster", c_uint32),
    ("clusterScratchByteAlignment", c_uint32),
    ("clusterByteAlignment", c_uint32),
    ("clusterTemplateByteAlignment", c_uint32),
    ("clusterBottomLevelByteAlignment", c_uint32),
    ("clusterTemplateBoundsByteAlignment", c_uint32),
    ("maxClusterGeometryIndex", c_uint32),
]

VkStridedDeviceAddressNV._fields_ = [
    ("startAddress", c_uint64),
    ("strideInBytes", c_uint64),
]

VkRayTracingPipelineClusterAccelerationStructureCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allowClusterAccelerationStructure", c_uint32),
]

VkClusterAccelerationStructureGeometryIndexAndGeometryFlagsNV._fields_ = [
    ("geometryIndex", c_uint32),
    ("reserved", c_uint32),
    ("geometryFlags", c_uint32),
]

VkClusterAccelerationStructureMoveObjectsInfoNV._fields_ = [
    ("srcAccelerationStructure", c_uint64),
]

VkClusterAccelerationStructureBuildClustersBottomLevelInfoNV._fields_ = [
    ("clusterReferencesCount", c_uint32),
    ("clusterReferencesStride", c_uint32),
    ("clusterReferences", c_uint64),
]

VkClusterAccelerationStructureGetTemplateIndicesInfoNV._fields_ = [
    ("clusterTemplateAddress", c_uint64),
]

VkClusterAccelerationStructureBuildTriangleClusterInfoNV._fields_ = [
    ("clusterID", c_uint32),
    ("clusterFlags", c_uint32),
    ("triangleCount", c_uint32),
    ("vertexCount", c_uint32),
    ("positionTruncateBitCount", c_uint32),
    ("indexType", c_uint32),
    ("opacityMicromapIndexType", c_uint32),
    ("baseGeometryIndexAndGeometryFlags", VkClusterAccelerationStructureGeometryIndexAndGeometryFlagsNV),
    ("indexBufferStride", c_uint16),
    ("vertexBufferStride", c_uint16),
    ("geometryIndexAndFlagsBufferStride", c_uint16),
    ("opacityMicromapIndexBufferStride", c_uint16),
    ("indexBuffer", c_uint64),
    ("vertexBuffer", c_uint64),
    ("geometryIndexAndFlagsBuffer", c_uint64),
    ("opacityMicromapArray", c_uint64),
    ("opacityMicromapIndexBuffer", c_uint64),
]

VkClusterAccelerationStructureBuildTriangleClusterTemplateInfoNV._fields_ = [
    ("clusterID", c_uint32),
    ("clusterFlags", c_uint32),
    ("triangleCount", c_uint32),
    ("vertexCount", c_uint32),
    ("positionTruncateBitCount", c_uint32),
    ("indexType", c_uint32),
    ("opacityMicromapIndexType", c_uint32),
    ("baseGeometryIndexAndGeometryFlags", VkClusterAccelerationStructureGeometryIndexAndGeometryFlagsNV),
    ("indexBufferStride", c_uint16),
    ("vertexBufferStride", c_uint16),
    ("geometryIndexAndFlagsBufferStride", c_uint16),
    ("opacityMicromapIndexBufferStride", c_uint16),
    ("indexBuffer", c_uint64),
    ("vertexBuffer", c_uint64),
    ("geometryIndexAndFlagsBuffer", c_uint64),
    ("opacityMicromapArray", c_uint64),
    ("opacityMicromapIndexBuffer", c_uint64),
    ("instantiationBoundingBoxLimit", c_uint64),
]

VkClusterAccelerationStructureInstantiateClusterInfoNV._fields_ = [
    ("clusterIdOffset", c_uint32),
    ("geometryIndexOffset", c_uint32),
    ("reserved", c_uint32),
    ("clusterTemplateAddress", c_uint64),
    ("vertexBuffer", VkStridedDeviceAddressNV),
]

VkClusterAccelerationStructureClustersBottomLevelInputNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxTotalClusterCount", c_uint32),
    ("maxClusterCountPerAccelerationStructure", c_uint32),
]

VkClusterAccelerationStructureTriangleClusterInputNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexFormat", c_int32),
    ("maxGeometryIndexValue", c_uint32),
    ("maxClusterUniqueGeometryCount", c_uint32),
    ("maxClusterTriangleCount", c_uint32),
    ("maxClusterVertexCount", c_uint32),
    ("maxTotalTriangleCount", c_uint32),
    ("maxTotalVertexCount", c_uint32),
    ("minPositionTruncateBitCount", c_uint32),
]

VkClusterAccelerationStructureMoveObjectsInputNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("noMoveOverlap", c_uint32),
    ("maxMovedBytes", c_uint64),
]

VkClusterAccelerationStructureOpInputNV._fields_ = [
    ("pClustersBottomLevel", POINTER(VkClusterAccelerationStructureClustersBottomLevelInputNV)),
    ("pTriangleClusters", POINTER(VkClusterAccelerationStructureTriangleClusterInputNV)),
    ("pMoveObjects", POINTER(VkClusterAccelerationStructureMoveObjectsInputNV)),
]

VkClusterAccelerationStructureInputInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxAccelerationStructureCount", c_uint32),
    ("flags", c_uint32),
    ("opType", c_int32),
    ("opMode", c_int32),
    ("opInput", VkClusterAccelerationStructureOpInputNV),
]

VkStridedDeviceAddressRegionKHR._fields_ = [
    ("deviceAddress", c_uint64),
    ("stride", c_uint64),
    ("size", c_uint64),
]

VkClusterAccelerationStructureCommandsInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("input", VkClusterAccelerationStructureInputInfoNV),
    ("dstImplicitData", c_uint64),
    ("scratchData", c_uint64),
    ("dstAddressesArray", VkStridedDeviceAddressRegionKHR),
    ("dstSizesArray", VkStridedDeviceAddressRegionKHR),
    ("srcInfosArray", VkStridedDeviceAddressRegionKHR),
    ("srcInfosCount", c_uint64),
    ("addressResolutionFlags", c_uint32),
]

VkPhysicalDeviceMultiDrawPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxMultiDrawCount", c_uint32),
]

VkGraphicsShaderGroupCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stageCount", c_uint32),
    ("pStages", POINTER(VkPipelineShaderStageCreateInfo)),
    ("pVertexInputState", POINTER(VkPipelineVertexInputStateCreateInfo)),
    ("pTessellationState", POINTER(VkPipelineTessellationStateCreateInfo)),
]

VkGraphicsPipelineShaderGroupsCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("groupCount", c_uint32),
    ("pGroups", POINTER(VkGraphicsShaderGroupCreateInfoNV)),
    ("pipelineCount", c_uint32),
    ("pPipelines", POINTER(c_void_p)),
]

VkBindShaderGroupIndirectCommandNV._fields_ = [
    ("groupIndex", c_uint32),
]

VkBindIndexBufferIndirectCommandNV._fields_ = [
    ("bufferAddress", c_uint64),
    ("size", c_uint32),
    ("indexType", c_int32),
]

VkBindVertexBufferIndirectCommandNV._fields_ = [
    ("bufferAddress", c_uint64),
    ("size", c_uint32),
    ("stride", c_uint32),
]

VkSetStateFlagsIndirectCommandNV._fields_ = [
    ("data", c_uint32),
]

VkIndirectCommandsStreamNV._fields_ = [
    ("buffer", c_void_p),
    ("offset", c_uint64),
]

VkIndirectCommandsLayoutTokenNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tokenType", c_int32),
    ("stream", c_uint32),
    ("offset", c_uint32),
    ("vertexBindingUnit", c_uint32),
    ("vertexDynamicStride", c_uint32),
    ("pushconstantPipelineLayout", c_void_p),
    ("pushconstantShaderStageFlags", c_uint32),
    ("pushconstantOffset", c_uint32),
    ("pushconstantSize", c_uint32),
    ("indirectStateFlags", c_uint32),
    ("indexTypeCount", c_uint32),
    ("pIndexTypes", POINTER(c_int32)),
    ("pIndexTypeValues", POINTER(c_uint32)),
]

VkIndirectCommandsLayoutCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pipelineBindPoint", c_int32),
    ("tokenCount", c_uint32),
    ("pTokens", POINTER(VkIndirectCommandsLayoutTokenNV)),
    ("streamCount", c_uint32),
    ("pStreamStrides", POINTER(c_uint32)),
]

VkGeneratedCommandsInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBindPoint", c_int32),
    ("pipeline", c_void_p),
    ("indirectCommandsLayout", c_void_p),
    ("streamCount", c_uint32),
    ("pStreams", POINTER(VkIndirectCommandsStreamNV)),
    ("sequencesCount", c_uint32),
    ("preprocessBuffer", c_void_p),
    ("preprocessOffset", c_uint64),
    ("preprocessSize", c_uint64),
    ("sequencesCountBuffer", c_void_p),
    ("sequencesCountOffset", c_uint64),
    ("sequencesIndexBuffer", c_void_p),
    ("sequencesIndexOffset", c_uint64),
]

VkGeneratedCommandsMemoryRequirementsInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBindPoint", c_int32),
    ("pipeline", c_void_p),
    ("indirectCommandsLayout", c_void_p),
    ("maxSequencesCount", c_uint32),
]

VkPipelineIndirectDeviceAddressInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBindPoint", c_int32),
    ("pipeline", c_void_p),
]

VkBindPipelineIndirectCommandNV._fields_ = [
    ("pipelineAddress", c_uint64),
]

VkPhysicalDeviceFeatures2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("features", VkPhysicalDeviceFeatures),
]

VkPhysicalDeviceFeatures2KHR._fields_ = [
]

VkPhysicalDeviceProperties2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("properties", VkPhysicalDeviceProperties),
]

VkPhysicalDeviceProperties2KHR._fields_ = [
]

VkFormatProperties2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("formatProperties", VkFormatProperties),
]

VkFormatProperties2KHR._fields_ = [
]

VkImageFormatProperties2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageFormatProperties", VkImageFormatProperties),
]

VkImageFormatProperties2KHR._fields_ = [
]

VkPhysicalDeviceImageFormatInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("type", c_int32),
    ("tiling", c_int32),
    ("usage", c_uint32),
    ("flags", c_uint32),
]

VkPhysicalDeviceImageFormatInfo2KHR._fields_ = [
]

VkQueueFamilyProperties2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queueFamilyProperties", VkQueueFamilyProperties),
]

VkQueueFamilyProperties2KHR._fields_ = [
]

VkPhysicalDeviceMemoryProperties2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryProperties", VkPhysicalDeviceMemoryProperties),
]

VkPhysicalDeviceMemoryProperties2KHR._fields_ = [
]

VkSparseImageFormatProperties2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("properties", VkSparseImageFormatProperties),
]

VkSparseImageFormatProperties2KHR._fields_ = [
]

VkPhysicalDeviceSparseImageFormatInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("type", c_int32),
    ("samples", c_int32),
    ("usage", c_uint32),
    ("tiling", c_int32),
]

VkPhysicalDeviceSparseImageFormatInfo2KHR._fields_ = [
]

VkPhysicalDevicePushDescriptorProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxPushDescriptors", c_uint32),
]

VkPhysicalDevicePushDescriptorPropertiesKHR._fields_ = [
]

VkConformanceVersion._fields_ = [
    ("major", c_uint8),
    ("minor", c_uint8),
    ("subminor", c_uint8),
    ("patch", c_uint8),
]

VkConformanceVersionKHR._fields_ = [
]

VkPhysicalDeviceDriverProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("driverID", c_int32),
    ("driverName", (c_char * VK_MAX_DRIVER_NAME_SIZE)),
    ("driverInfo", (c_char * VK_MAX_DRIVER_INFO_SIZE)),
    ("conformanceVersion", VkConformanceVersion),
]

VkPhysicalDeviceDriverPropertiesKHR._fields_ = [
]

VkPresentRegionsKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pRegions", POINTER(VkPresentRegionKHR)),
]

VkPresentRegionKHR._fields_ = [
    ("rectangleCount", c_uint32),
    ("pRectangles", POINTER(VkRectLayerKHR)),
]

VkRectLayerKHR._fields_ = [
    ("offset", VkOffset2D),
    ("extent", VkExtent2D),
    ("layer", c_uint32),
]

VkPhysicalDeviceVariablePointersFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("variablePointersStorageBuffer", c_uint32),
    ("variablePointers", c_uint32),
]

VkPhysicalDeviceVariablePointersFeaturesKHR._fields_ = [
]

VkPhysicalDeviceVariablePointerFeaturesKHR._fields_ = [
]

VkPhysicalDeviceVariablePointerFeatures._fields_ = [
]

VkExternalMemoryProperties._fields_ = [
    ("externalMemoryFeatures", c_uint32),
    ("exportFromImportedHandleTypes", c_uint32),
    ("compatibleHandleTypes", c_uint32),
]

VkExternalMemoryPropertiesKHR._fields_ = [
]

VkPhysicalDeviceExternalImageFormatInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
]

VkPhysicalDeviceExternalImageFormatInfoKHR._fields_ = [
]

VkExternalImageFormatProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalMemoryProperties", VkExternalMemoryProperties),
]

VkExternalImageFormatPropertiesKHR._fields_ = [
]

VkPhysicalDeviceExternalBufferInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("usage", c_uint32),
    ("handleType", c_int32),
]

VkPhysicalDeviceExternalBufferInfoKHR._fields_ = [
]

VkExternalBufferProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalMemoryProperties", VkExternalMemoryProperties),
]

VkExternalBufferPropertiesKHR._fields_ = [
]

VkPhysicalDeviceIDProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceUUID", (c_uint8 * VK_UUID_SIZE)),
    ("driverUUID", (c_uint8 * VK_UUID_SIZE)),
    ("deviceLUID", (c_uint8 * VK_LUID_SIZE)),
    ("deviceNodeMask", c_uint32),
    ("deviceLUIDValid", c_uint32),
]

VkPhysicalDeviceIDPropertiesKHR._fields_ = [
]

VkExternalMemoryImageCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkExternalMemoryImageCreateInfoKHR._fields_ = [
]

VkExternalMemoryBufferCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkExternalMemoryBufferCreateInfoKHR._fields_ = [
]

VkExportMemoryAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkExportMemoryAllocateInfoKHR._fields_ = [
]

VkImportMemoryWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
    ("handle", c_void_p),
    ("name", c_wchar_p),
]

VkExportMemoryWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", POINTER(c_void_p)),
    ("dwAccess", c_uint32),
    ("name", c_wchar_p),
]

VkImportMemoryZirconHandleInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
    ("handle", c_uint32),
]

VkMemoryZirconHandlePropertiesFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
]

VkMemoryGetZirconHandleInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("handleType", c_int32),
]

VkMemoryWin32HandlePropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
]

VkMemoryGetWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("handleType", c_int32),
]

VkImportMemoryFdInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
    ("fd", c_int),
]

VkMemoryFdPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
]

VkMemoryGetFdInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("handleType", c_int32),
]

VkWin32KeyedMutexAcquireReleaseInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("acquireCount", c_uint32),
    ("pAcquireSyncs", POINTER(c_void_p)),
    ("pAcquireKeys", POINTER(c_uint64)),
    ("pAcquireTimeouts", POINTER(c_uint32)),
    ("releaseCount", c_uint32),
    ("pReleaseSyncs", POINTER(c_void_p)),
    ("pReleaseKeys", POINTER(c_uint64)),
]

VkImportMemoryMetalHandleInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
    ("handle", c_void_p),
]

VkMemoryMetalHandlePropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
]

VkMemoryGetMetalHandleInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("handleType", c_int32),
]

VkPhysicalDeviceExternalSemaphoreInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
]

VkPhysicalDeviceExternalSemaphoreInfoKHR._fields_ = [
]

VkExternalSemaphoreProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("exportFromImportedHandleTypes", c_uint32),
    ("compatibleHandleTypes", c_uint32),
    ("externalSemaphoreFeatures", c_uint32),
]

VkExternalSemaphorePropertiesKHR._fields_ = [
]

VkExportSemaphoreCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkExportSemaphoreCreateInfoKHR._fields_ = [
]

VkImportSemaphoreWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("flags", c_uint32),
    ("handleType", c_int32),
    ("handle", c_void_p),
    ("name", c_wchar_p),
]

VkExportSemaphoreWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", POINTER(c_void_p)),
    ("dwAccess", c_uint32),
    ("name", c_wchar_p),
]

VkD3D12FenceSubmitInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("waitSemaphoreValuesCount", c_uint32),
    ("pWaitSemaphoreValues", POINTER(c_uint64)),
    ("signalSemaphoreValuesCount", c_uint32),
    ("pSignalSemaphoreValues", POINTER(c_uint64)),
]

VkSemaphoreGetWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("handleType", c_int32),
]

VkImportSemaphoreFdInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("flags", c_uint32),
    ("handleType", c_int32),
    ("fd", c_int),
]

VkSemaphoreGetFdInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("handleType", c_int32),
]

VkImportSemaphoreZirconHandleInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("flags", c_uint32),
    ("handleType", c_int32),
    ("zirconHandle", c_uint32),
]

VkSemaphoreGetZirconHandleInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("handleType", c_int32),
]

VkPhysicalDeviceExternalFenceInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
]

VkPhysicalDeviceExternalFenceInfoKHR._fields_ = [
]

VkExternalFenceProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("exportFromImportedHandleTypes", c_uint32),
    ("compatibleHandleTypes", c_uint32),
    ("externalFenceFeatures", c_uint32),
]

VkExternalFencePropertiesKHR._fields_ = [
]

VkExportFenceCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkExportFenceCreateInfoKHR._fields_ = [
]

VkImportFenceWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fence", c_void_p),
    ("flags", c_uint32),
    ("handleType", c_int32),
    ("handle", c_void_p),
    ("name", c_wchar_p),
]

VkExportFenceWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", POINTER(c_void_p)),
    ("dwAccess", c_uint32),
    ("name", c_wchar_p),
]

VkFenceGetWin32HandleInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fence", c_void_p),
    ("handleType", c_int32),
]

VkImportFenceFdInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fence", c_void_p),
    ("flags", c_uint32),
    ("handleType", c_int32),
    ("fd", c_int),
]

VkFenceGetFdInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fence", c_void_p),
    ("handleType", c_int32),
]

VkExportFenceSciSyncInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", c_void_p),
]

VkImportFenceSciSyncInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fence", c_void_p),
    ("handleType", c_int32),
    ("handle", c_void_p),
]

VkFenceGetSciSyncInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fence", c_void_p),
    ("handleType", c_int32),
]

VkExportSemaphoreSciSyncInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pAttributes", c_void_p),
]

VkImportSemaphoreSciSyncInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("handleType", c_int32),
    ("handle", c_void_p),
]

VkSemaphoreGetSciSyncInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("handleType", c_int32),
]

VkSciSyncAttributesInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("clientType", c_int32),
    ("primitiveType", c_int32),
]

VkPhysicalDeviceExternalSciSyncFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sciSyncFence", c_uint32),
    ("sciSyncSemaphore", c_uint32),
    ("sciSyncImport", c_uint32),
    ("sciSyncExport", c_uint32),
]

VkPhysicalDeviceExternalSciSync2FeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sciSyncFence", c_uint32),
    ("sciSyncSemaphore2", c_uint32),
    ("sciSyncImport", c_uint32),
    ("sciSyncExport", c_uint32),
]

VkSemaphoreSciSyncPoolCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handle", c_void_p),
]

VkSemaphoreSciSyncCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphorePool", c_void_p),
    ("pFence", POINTER(c_void_p)),
]

VkDeviceSemaphoreSciSyncPoolReservationCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphoreSciSyncPoolRequestCount", c_uint32),
]

VkPhysicalDeviceMultiviewFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("multiview", c_uint32),
    ("multiviewGeometryShader", c_uint32),
    ("multiviewTessellationShader", c_uint32),
]

VkPhysicalDeviceMultiviewFeaturesKHR._fields_ = [
]

VkPhysicalDeviceMultiviewProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxMultiviewViewCount", c_uint32),
    ("maxMultiviewInstanceIndex", c_uint32),
]

VkPhysicalDeviceMultiviewPropertiesKHR._fields_ = [
]

VkRenderPassMultiviewCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subpassCount", c_uint32),
    ("pViewMasks", POINTER(c_uint32)),
    ("dependencyCount", c_uint32),
    ("pViewOffsets", POINTER(c_int32)),
    ("correlationMaskCount", c_uint32),
    ("pCorrelationMasks", POINTER(c_uint32)),
]

VkRenderPassMultiviewCreateInfoKHR._fields_ = [
]

VkSurfaceCapabilities2EXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minImageCount", c_uint32),
    ("maxImageCount", c_uint32),
    ("currentExtent", VkExtent2D),
    ("minImageExtent", VkExtent2D),
    ("maxImageExtent", VkExtent2D),
    ("maxImageArrayLayers", c_uint32),
    ("supportedTransforms", c_uint32),
    ("currentTransform", c_int32),
    ("supportedCompositeAlpha", c_uint32),
    ("supportedUsageFlags", c_uint32),
    ("supportedSurfaceCounters", c_uint32),
]

VkDisplayPowerInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("powerState", c_int32),
]

VkDeviceEventInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceEvent", c_int32),
]

VkDisplayEventInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displayEvent", c_int32),
]

VkSwapchainCounterCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("surfaceCounters", c_uint32),
]

VkPhysicalDeviceGroupProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("physicalDeviceCount", c_uint32),
    ("physicalDevices", (c_void_p * VK_MAX_DEVICE_GROUP_SIZE)),
    ("subsetAllocation", c_uint32),
]

VkPhysicalDeviceGroupPropertiesKHR._fields_ = [
]

VkMemoryAllocateFlagsInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("deviceMask", c_uint32),
]

VkMemoryAllocateFlagsInfoKHR._fields_ = [
]

VkBindBufferMemoryInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", c_void_p),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
]

VkBindBufferMemoryInfoKHR._fields_ = [
]

VkBindBufferMemoryDeviceGroupInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceIndexCount", c_uint32),
    ("pDeviceIndices", POINTER(c_uint32)),
]

VkBindBufferMemoryDeviceGroupInfoKHR._fields_ = [
]

VkBindImageMemoryInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
]

VkBindImageMemoryInfoKHR._fields_ = [
]

VkBindImageMemoryDeviceGroupInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceIndexCount", c_uint32),
    ("pDeviceIndices", POINTER(c_uint32)),
    ("splitInstanceBindRegionCount", c_uint32),
    ("pSplitInstanceBindRegions", POINTER(VkRect2D)),
]

VkBindImageMemoryDeviceGroupInfoKHR._fields_ = [
]

VkDeviceGroupRenderPassBeginInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceMask", c_uint32),
    ("deviceRenderAreaCount", c_uint32),
    ("pDeviceRenderAreas", POINTER(VkRect2D)),
]

VkDeviceGroupRenderPassBeginInfoKHR._fields_ = [
]

VkDeviceGroupCommandBufferBeginInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceMask", c_uint32),
]

VkDeviceGroupCommandBufferBeginInfoKHR._fields_ = [
]

VkDeviceGroupSubmitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("waitSemaphoreCount", c_uint32),
    ("pWaitSemaphoreDeviceIndices", POINTER(c_uint32)),
    ("commandBufferCount", c_uint32),
    ("pCommandBufferDeviceMasks", POINTER(c_uint32)),
    ("signalSemaphoreCount", c_uint32),
    ("pSignalSemaphoreDeviceIndices", POINTER(c_uint32)),
]

VkDeviceGroupSubmitInfoKHR._fields_ = [
]

VkDeviceGroupBindSparseInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("resourceDeviceIndex", c_uint32),
    ("memoryDeviceIndex", c_uint32),
]

VkDeviceGroupBindSparseInfoKHR._fields_ = [
]

VkDeviceGroupPresentCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentMask", (c_uint32 * VK_MAX_DEVICE_GROUP_SIZE)),
    ("modes", c_uint32),
]

VkImageSwapchainCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchain", c_void_p),
]

VkBindImageMemorySwapchainInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchain", c_void_p),
    ("imageIndex", c_uint32),
]

VkAcquireNextImageInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchain", c_void_p),
    ("timeout", c_uint64),
    ("semaphore", c_void_p),
    ("fence", c_void_p),
    ("deviceMask", c_uint32),
]

VkDeviceGroupPresentInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pDeviceMasks", POINTER(c_uint32)),
    ("mode", c_int32),
]

VkDeviceGroupDeviceCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("physicalDeviceCount", c_uint32),
    ("pPhysicalDevices", POINTER(c_void_p)),
]

VkDeviceGroupDeviceCreateInfoKHR._fields_ = [
]

VkDeviceGroupSwapchainCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("modes", c_uint32),
]

VkDescriptorUpdateTemplateEntry._fields_ = [
    ("dstBinding", c_uint32),
    ("dstArrayElement", c_uint32),
    ("descriptorCount", c_uint32),
    ("descriptorType", c_int32),
    ("offset", c_size_t),
    ("stride", c_size_t),
]

VkDescriptorUpdateTemplateEntryKHR._fields_ = [
]

VkDescriptorUpdateTemplateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("descriptorUpdateEntryCount", c_uint32),
    ("pDescriptorUpdateEntries", POINTER(VkDescriptorUpdateTemplateEntry)),
    ("templateType", c_int32),
    ("descriptorSetLayout", c_void_p),
    ("pipelineBindPoint", c_int32),
    ("pipelineLayout", c_void_p),
    ("set", c_uint32),
]

VkDescriptorUpdateTemplateCreateInfoKHR._fields_ = [
]

VkXYColorEXT._fields_ = [
    ("x", c_float),
    ("y", c_float),
]

VkPhysicalDevicePresentIdFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentId", c_uint32),
]

VkPresentIdKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pPresentIds", POINTER(c_uint64)),
]

VkPhysicalDevicePresentId2FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentId2", c_uint32),
]

VkPresentId2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pPresentIds", POINTER(c_uint64)),
]

VkPresentWait2InfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentId", c_uint64),
    ("timeout", c_uint64),
]

VkPhysicalDevicePresentWaitFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentWait", c_uint32),
]

VkPhysicalDevicePresentWait2FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentWait2", c_uint32),
]

VkPhysicalDevicePresentTimingFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentTiming", c_uint32),
    ("presentAtAbsoluteTime", c_uint32),
    ("presentAtRelativeTime", c_uint32),
]

VkPresentTimingSurfaceCapabilitiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentTimingSupported", c_uint32),
    ("presentAtAbsoluteTimeSupported", c_uint32),
    ("presentAtRelativeTimeSupported", c_uint32),
    ("presentStageQueries", c_uint32),
]

VkSwapchainTimingPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("refreshDuration", c_uint64),
    ("refreshInterval", c_uint64),
]

VkSwapchainTimeDomainPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("timeDomainCount", c_uint32),
    ("pTimeDomains", POINTER(c_int32)),
    ("pTimeDomainIds", POINTER(c_uint64)),
]

VkPresentStageTimeEXT._fields_ = [
    ("stage", c_uint32),
    ("time", c_uint64),
]

VkPastPresentationTimingInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("swapchain", c_void_p),
]

VkPastPresentationTimingPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("timingPropertiesCounter", c_uint64),
    ("timeDomainsCounter", c_uint64),
    ("presentationTimingCount", c_uint32),
    ("pPresentationTimings", POINTER(VkPastPresentationTimingEXT)),
]

VkPastPresentationTimingEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentId", c_uint64),
    ("targetTime", c_uint64),
    ("presentStageCount", c_uint32),
    ("pPresentStages", POINTER(VkPresentStageTimeEXT)),
    ("timeDomain", c_int32),
    ("timeDomainId", c_uint64),
    ("reportComplete", c_uint32),
]

VkPresentTimingsInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pTimingInfos", POINTER(VkPresentTimingInfoEXT)),
]

VkPresentTimingInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("targetTime", c_uint64),
    ("timeDomainId", c_uint64),
    ("presentStageQueries", c_uint32),
    ("targetTimeDomainPresentStage", c_uint32),
]

VkSwapchainCalibratedTimestampInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchain", c_void_p),
    ("presentStage", c_uint32),
    ("timeDomainId", c_uint64),
]

VkHdrMetadataEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displayPrimaryRed", VkXYColorEXT),
    ("displayPrimaryGreen", VkXYColorEXT),
    ("displayPrimaryBlue", VkXYColorEXT),
    ("whitePoint", VkXYColorEXT),
    ("maxLuminance", c_float),
    ("minLuminance", c_float),
    ("maxContentLightLevel", c_float),
    ("maxFrameAverageLightLevel", c_float),
]

VkHdrVividDynamicMetadataHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dynamicMetadataSize", c_size_t),
    ("pDynamicMetadata", c_void_p),
]

VkDisplayNativeHdrSurfaceCapabilitiesAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("localDimmingSupport", c_uint32),
]

VkSwapchainDisplayNativeHdrCreateInfoAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("localDimmingEnable", c_uint32),
]

VkRefreshCycleDurationGOOGLE._fields_ = [
    ("refreshDuration", c_uint64),
]

VkPastPresentationTimingGOOGLE._fields_ = [
    ("presentID", c_uint32),
    ("desiredPresentTime", c_uint64),
    ("actualPresentTime", c_uint64),
    ("earliestPresentTime", c_uint64),
    ("presentMargin", c_uint64),
]

VkPresentTimesInfoGOOGLE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pTimes", POINTER(VkPresentTimeGOOGLE)),
]

VkPresentTimeGOOGLE._fields_ = [
    ("presentID", c_uint32),
    ("desiredPresentTime", c_uint64),
]

VkIOSSurfaceCreateInfoMVK._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pView", c_void_p),
]

VkMacOSSurfaceCreateInfoMVK._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pView", c_void_p),
]

VkMetalSurfaceCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pLayer", POINTER(c_void_p)),
]

VkViewportWScalingNV._fields_ = [
    ("xcoeff", c_float),
    ("ycoeff", c_float),
]

VkPipelineViewportWScalingStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("viewportWScalingEnable", c_uint32),
    ("viewportCount", c_uint32),
    ("pViewportWScalings", POINTER(VkViewportWScalingNV)),
]

VkViewportSwizzleNV._fields_ = [
    ("x", c_int32),
    ("y", c_int32),
    ("z", c_int32),
    ("w", c_int32),
]

VkPipelineViewportSwizzleStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("viewportCount", c_uint32),
    ("pViewportSwizzles", POINTER(VkViewportSwizzleNV)),
]

VkPhysicalDeviceDiscardRectanglePropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxDiscardRectangles", c_uint32),
]

VkPipelineDiscardRectangleStateCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("discardRectangleMode", c_int32),
    ("discardRectangleCount", c_uint32),
    ("pDiscardRectangles", POINTER(VkRect2D)),
]

VkPhysicalDeviceMultiviewPerViewAttributesPropertiesNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("perViewPositionAllComponents", c_uint32),
]

VkInputAttachmentAspectReference._fields_ = [
    ("subpass", c_uint32),
    ("inputAttachmentIndex", c_uint32),
    ("aspectMask", c_uint32),
]

VkInputAttachmentAspectReferenceKHR._fields_ = [
]

VkRenderPassInputAttachmentAspectCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("aspectReferenceCount", c_uint32),
    ("pAspectReferences", POINTER(VkInputAttachmentAspectReference)),
]

VkRenderPassInputAttachmentAspectCreateInfoKHR._fields_ = [
]

VkPhysicalDeviceSurfaceInfo2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("surface", c_void_p),
]

VkSurfaceCapabilities2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("surfaceCapabilities", VkSurfaceCapabilitiesKHR),
]

VkSurfaceFormat2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("surfaceFormat", VkSurfaceFormatKHR),
]

VkDisplayProperties2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displayProperties", VkDisplayPropertiesKHR),
]

VkDisplayPlaneProperties2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displayPlaneProperties", VkDisplayPlanePropertiesKHR),
]

VkDisplayModeProperties2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displayModeProperties", VkDisplayModePropertiesKHR),
]

VkDisplayModeStereoPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hdmi3DSupported", c_uint32),
]

VkDisplayPlaneInfo2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mode", c_void_p),
    ("planeIndex", c_uint32),
]

VkDisplayPlaneCapabilities2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("capabilities", VkDisplayPlaneCapabilitiesKHR),
]

VkSharedPresentSurfaceCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sharedPresentSupportedUsageFlags", c_uint32),
]

VkPhysicalDevice16BitStorageFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("storageBuffer16BitAccess", c_uint32),
    ("uniformAndStorageBuffer16BitAccess", c_uint32),
    ("storagePushConstant16", c_uint32),
    ("storageInputOutput16", c_uint32),
]

VkPhysicalDevice16BitStorageFeaturesKHR._fields_ = [
]

VkPhysicalDeviceSubgroupProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subgroupSize", c_uint32),
    ("supportedStages", c_uint32),
    ("supportedOperations", c_uint32),
    ("quadOperationsInAllStages", c_uint32),
]

VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSubgroupExtendedTypes", c_uint32),
]

VkPhysicalDeviceShaderSubgroupExtendedTypesFeaturesKHR._fields_ = [
]

VkBufferMemoryRequirementsInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", c_void_p),
]

VkBufferMemoryRequirementsInfo2KHR._fields_ = [
]

VkDeviceBufferMemoryRequirements._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pCreateInfo", POINTER(VkBufferCreateInfo)),
]

VkDeviceBufferMemoryRequirementsKHR._fields_ = [
]

VkImageMemoryRequirementsInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
]

VkImageMemoryRequirementsInfo2KHR._fields_ = [
]

VkImageSparseMemoryRequirementsInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
]

VkImageSparseMemoryRequirementsInfo2KHR._fields_ = [
]

VkDeviceImageMemoryRequirements._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pCreateInfo", POINTER(VkImageCreateInfo)),
    ("planeAspect", c_int32),
]

VkDeviceImageMemoryRequirementsKHR._fields_ = [
]

VkMemoryRequirements2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryRequirements", VkMemoryRequirements),
]

VkMemoryRequirements2KHR._fields_ = [
]

VkSparseImageMemoryRequirements2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryRequirements", VkSparseImageMemoryRequirements),
]

VkSparseImageMemoryRequirements2KHR._fields_ = [
]

VkPhysicalDevicePointClippingProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pointClippingBehavior", c_int32),
]

VkPhysicalDevicePointClippingPropertiesKHR._fields_ = [
]

VkMemoryDedicatedRequirements._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("prefersDedicatedAllocation", c_uint32),
    ("requiresDedicatedAllocation", c_uint32),
]

VkMemoryDedicatedRequirementsKHR._fields_ = [
]

VkMemoryDedicatedAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("buffer", c_void_p),
]

VkMemoryDedicatedAllocateInfoKHR._fields_ = [
]

VkImageViewUsageCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("usage", c_uint32),
]

VkImageViewSlicedCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sliceOffset", c_uint32),
    ("sliceCount", c_uint32),
]

VkImageViewUsageCreateInfoKHR._fields_ = [
]

VkPipelineTessellationDomainOriginStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("domainOrigin", c_int32),
]

VkPipelineTessellationDomainOriginStateCreateInfoKHR._fields_ = [
]

VkSamplerYcbcrConversionInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("conversion", c_void_p),
]

VkSamplerYcbcrConversionInfoKHR._fields_ = [
]

VkSamplerYcbcrConversionCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("ycbcrModel", c_int32),
    ("ycbcrRange", c_int32),
    ("components", VkComponentMapping),
    ("xChromaOffset", c_int32),
    ("yChromaOffset", c_int32),
    ("chromaFilter", c_int32),
    ("forceExplicitReconstruction", c_uint32),
]

VkSamplerYcbcrConversionCreateInfoKHR._fields_ = [
]

VkBindImagePlaneMemoryInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("planeAspect", c_int32),
]

VkBindImagePlaneMemoryInfoKHR._fields_ = [
]

VkImagePlaneMemoryRequirementsInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("planeAspect", c_int32),
]

VkImagePlaneMemoryRequirementsInfoKHR._fields_ = [
]

VkPhysicalDeviceSamplerYcbcrConversionFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("samplerYcbcrConversion", c_uint32),
]

VkPhysicalDeviceSamplerYcbcrConversionFeaturesKHR._fields_ = [
]

VkSamplerYcbcrConversionImageFormatProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("combinedImageSamplerDescriptorCount", c_uint32),
]

VkSamplerYcbcrConversionImageFormatPropertiesKHR._fields_ = [
]

VkTextureLODGatherFormatPropertiesAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportsTextureGatherLODBiasAMD", c_uint32),
]

VkConditionalRenderingBeginInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", c_void_p),
    ("offset", c_uint64),
    ("flags", c_uint32),
]

VkProtectedSubmitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("protectedSubmit", c_uint32),
]

VkPhysicalDeviceProtectedMemoryFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("protectedMemory", c_uint32),
]

VkPhysicalDeviceProtectedMemoryProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("protectedNoFault", c_uint32),
]

VkDeviceQueueInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("queueFamilyIndex", c_uint32),
    ("queueIndex", c_uint32),
]

VkPipelineCoverageToColorStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("coverageToColorEnable", c_uint32),
    ("coverageToColorLocation", c_uint32),
]

VkPhysicalDeviceSamplerFilterMinmaxProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("filterMinmaxSingleComponentFormats", c_uint32),
    ("filterMinmaxImageComponentMapping", c_uint32),
]

VkPhysicalDeviceSamplerFilterMinmaxPropertiesEXT._fields_ = [
]

VkSampleLocationEXT._fields_ = [
    ("x", c_float),
    ("y", c_float),
]

VkSampleLocationsInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sampleLocationsPerPixel", c_int32),
    ("sampleLocationGridSize", VkExtent2D),
    ("sampleLocationsCount", c_uint32),
    ("pSampleLocations", POINTER(VkSampleLocationEXT)),
]

VkAttachmentSampleLocationsEXT._fields_ = [
    ("attachmentIndex", c_uint32),
    ("sampleLocationsInfo", VkSampleLocationsInfoEXT),
]

VkSubpassSampleLocationsEXT._fields_ = [
    ("subpassIndex", c_uint32),
    ("sampleLocationsInfo", VkSampleLocationsInfoEXT),
]

VkRenderPassSampleLocationsBeginInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachmentInitialSampleLocationsCount", c_uint32),
    ("pAttachmentInitialSampleLocations", POINTER(VkAttachmentSampleLocationsEXT)),
    ("postSubpassSampleLocationsCount", c_uint32),
    ("pPostSubpassSampleLocations", POINTER(VkSubpassSampleLocationsEXT)),
]

VkPipelineSampleLocationsStateCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sampleLocationsEnable", c_uint32),
    ("sampleLocationsInfo", VkSampleLocationsInfoEXT),
]

VkPhysicalDeviceSampleLocationsPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sampleLocationSampleCounts", c_uint32),
    ("maxSampleLocationGridSize", VkExtent2D),
    ("sampleLocationCoordinateRange", (c_float * 2)),
    ("sampleLocationSubPixelBits", c_uint32),
    ("variableSampleLocations", c_uint32),
]

VkMultisamplePropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxSampleLocationGridSize", VkExtent2D),
]

VkSamplerReductionModeCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("reductionMode", c_int32),
]

VkSamplerReductionModeCreateInfoEXT._fields_ = [
]

VkPhysicalDeviceBlendOperationAdvancedFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("advancedBlendCoherentOperations", c_uint32),
]

VkPhysicalDeviceMultiDrawFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("multiDraw", c_uint32),
]

VkPhysicalDeviceBlendOperationAdvancedPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("advancedBlendMaxColorAttachments", c_uint32),
    ("advancedBlendIndependentBlend", c_uint32),
    ("advancedBlendNonPremultipliedSrcColor", c_uint32),
    ("advancedBlendNonPremultipliedDstColor", c_uint32),
    ("advancedBlendCorrelatedOverlap", c_uint32),
    ("advancedBlendAllOperations", c_uint32),
]

VkPipelineColorBlendAdvancedStateCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcPremultiplied", c_uint32),
    ("dstPremultiplied", c_uint32),
    ("blendOverlap", c_int32),
]

VkPhysicalDeviceInlineUniformBlockFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("inlineUniformBlock", c_uint32),
    ("descriptorBindingInlineUniformBlockUpdateAfterBind", c_uint32),
]

VkPhysicalDeviceInlineUniformBlockFeaturesEXT._fields_ = [
]

VkPhysicalDeviceInlineUniformBlockProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxInlineUniformBlockSize", c_uint32),
    ("maxPerStageDescriptorInlineUniformBlocks", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks", c_uint32),
    ("maxDescriptorSetInlineUniformBlocks", c_uint32),
    ("maxDescriptorSetUpdateAfterBindInlineUniformBlocks", c_uint32),
]

VkPhysicalDeviceInlineUniformBlockPropertiesEXT._fields_ = [
]

VkWriteDescriptorSetInlineUniformBlock._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataSize", c_uint32),
    ("pData", c_void_p),
]

VkWriteDescriptorSetInlineUniformBlockEXT._fields_ = [
]

VkDescriptorPoolInlineUniformBlockCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxInlineUniformBlockBindings", c_uint32),
]

VkDescriptorPoolInlineUniformBlockCreateInfoEXT._fields_ = [
]

VkPipelineCoverageModulationStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("coverageModulationMode", c_int32),
    ("coverageModulationTableEnable", c_uint32),
    ("coverageModulationTableCount", c_uint32),
    ("pCoverageModulationTable", POINTER(c_float)),
]

VkImageFormatListCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("viewFormatCount", c_uint32),
    ("pViewFormats", POINTER(c_int32)),
]

VkImageFormatListCreateInfoKHR._fields_ = [
]

VkValidationCacheCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("initialDataSize", c_size_t),
    ("pInitialData", c_void_p),
]

VkShaderModuleValidationCacheCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("validationCache", c_void_p),
]

VkPhysicalDeviceMaintenance3Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxPerSetDescriptors", c_uint32),
    ("maxMemoryAllocationSize", c_uint64),
]

VkPhysicalDeviceMaintenance3PropertiesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance4Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance4", c_uint32),
]

VkPhysicalDeviceMaintenance4FeaturesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance4Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxBufferSize", c_uint64),
]

VkPhysicalDeviceMaintenance4PropertiesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance5Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance5", c_uint32),
]

VkPhysicalDeviceMaintenance5FeaturesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance5Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("earlyFragmentMultisampleCoverageAfterSampleCounting", c_uint32),
    ("earlyFragmentSampleMaskTestBeforeSampleCounting", c_uint32),
    ("depthStencilSwizzleOneSupport", c_uint32),
    ("polygonModePointSize", c_uint32),
    ("nonStrictSinglePixelWideLinesUseParallelogram", c_uint32),
    ("nonStrictWideLinesUseParallelogram", c_uint32),
]

VkPhysicalDeviceMaintenance5PropertiesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance6Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance6", c_uint32),
]

VkPhysicalDeviceMaintenance6FeaturesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance6Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("blockTexelViewCompatibleMultipleLayers", c_uint32),
    ("maxCombinedImageSamplerDescriptorCount", c_uint32),
    ("fragmentShadingRateClampCombinerInputs", c_uint32),
]

VkPhysicalDeviceMaintenance6PropertiesKHR._fields_ = [
]

VkPhysicalDeviceMaintenance7FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance7", c_uint32),
]

VkPhysicalDeviceMaintenance7PropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("robustFragmentShadingRateAttachmentAccess", c_uint32),
    ("separateDepthStencilAttachmentAccess", c_uint32),
    ("maxDescriptorSetTotalUniformBuffersDynamic", c_uint32),
    ("maxDescriptorSetTotalStorageBuffersDynamic", c_uint32),
    ("maxDescriptorSetTotalBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindTotalUniformBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindTotalStorageBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindTotalBuffersDynamic", c_uint32),
]

VkPhysicalDeviceLayeredApiPropertiesListKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("layeredApiCount", c_uint32),
    ("pLayeredApis", POINTER(VkPhysicalDeviceLayeredApiPropertiesKHR)),
]

VkPhysicalDeviceLayeredApiPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vendorID", c_uint32),
    ("deviceID", c_uint32),
    ("layeredAPI", c_int32),
    ("deviceName", (c_char * VK_MAX_PHYSICAL_DEVICE_NAME_SIZE)),
]

VkPhysicalDeviceLayeredApiVulkanPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("properties", VkPhysicalDeviceProperties2),
]

VkPhysicalDeviceMaintenance8FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance8", c_uint32),
]

VkPhysicalDeviceMaintenance9FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance9", c_uint32),
]

VkPhysicalDeviceMaintenance9PropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image2DViewOf3DSparse", c_uint32),
    ("defaultVertexAttributeValue", c_int32),
]

VkPhysicalDeviceMaintenance11FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance11", c_uint32),
]

VkPhysicalDeviceMaintenance10PropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rgba4OpaqueBlackSwizzled", c_uint32),
    ("resolveSrgbFormatAppliesTransferFunction", c_uint32),
    ("resolveSrgbFormatSupportsTransferFunctionControl", c_uint32),
]

VkPhysicalDeviceMaintenance10FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maintenance10", c_uint32),
]

VkQueueFamilyOwnershipTransferPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("optimalImageTransferToQueueFamilies", c_uint32),
]

VkQueueFamilyOptimalImageTransferGranularityPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("optimalImageTransferGranularity", VkExtent3D),
]

VkRenderingAreaInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("viewMask", c_uint32),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentFormats", POINTER(c_int32)),
    ("depthAttachmentFormat", c_int32),
    ("stencilAttachmentFormat", c_int32),
]

VkRenderingAreaInfoKHR._fields_ = [
]

VkDescriptorSetLayoutSupport._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supported", c_uint32),
]

VkDescriptorSetLayoutSupportKHR._fields_ = [
]

VkPhysicalDeviceShaderDrawParametersFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderDrawParameters", c_uint32),
]

VkPhysicalDeviceShaderDrawParameterFeatures._fields_ = [
]

VkPhysicalDeviceShaderFloat16Int8Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderFloat16", c_uint32),
    ("shaderInt8", c_uint32),
]

VkPhysicalDeviceShaderFloat16Int8FeaturesKHR._fields_ = [
]

VkPhysicalDeviceFloat16Int8FeaturesKHR._fields_ = [
]

VkPhysicalDeviceFloatControlsProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("denormBehaviorIndependence", c_int32),
    ("roundingModeIndependence", c_int32),
    ("shaderSignedZeroInfNanPreserveFloat16", c_uint32),
    ("shaderSignedZeroInfNanPreserveFloat32", c_uint32),
    ("shaderSignedZeroInfNanPreserveFloat64", c_uint32),
    ("shaderDenormPreserveFloat16", c_uint32),
    ("shaderDenormPreserveFloat32", c_uint32),
    ("shaderDenormPreserveFloat64", c_uint32),
    ("shaderDenormFlushToZeroFloat16", c_uint32),
    ("shaderDenormFlushToZeroFloat32", c_uint32),
    ("shaderDenormFlushToZeroFloat64", c_uint32),
    ("shaderRoundingModeRTEFloat16", c_uint32),
    ("shaderRoundingModeRTEFloat32", c_uint32),
    ("shaderRoundingModeRTEFloat64", c_uint32),
    ("shaderRoundingModeRTZFloat16", c_uint32),
    ("shaderRoundingModeRTZFloat32", c_uint32),
    ("shaderRoundingModeRTZFloat64", c_uint32),
]

VkPhysicalDeviceFloatControlsPropertiesKHR._fields_ = [
]

VkPhysicalDeviceHostQueryResetFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hostQueryReset", c_uint32),
]

VkPhysicalDeviceHostQueryResetFeaturesEXT._fields_ = [
]

VkNativeBufferUsage2ANDROID._fields_ = [
    ("consumer", c_uint64),
    ("producer", c_uint64),
]

VkNativeBufferANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handle", c_void_p),
    ("stride", c_int),
    ("format", c_int),
    ("usage", c_int),
    ("usage2", VkNativeBufferUsage2ANDROID),
]

VkSwapchainImageCreateInfoANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("usage", c_uint32),
]

VkPhysicalDevicePresentationPropertiesANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sharedImage", c_uint32),
]

VkShaderResourceUsageAMD._fields_ = [
    ("numUsedVgprs", c_uint32),
    ("numUsedSgprs", c_uint32),
    ("ldsSizePerLocalWorkGroup", c_uint32),
    ("ldsUsageSizeInBytes", c_size_t),
    ("scratchMemUsageInBytes", c_size_t),
]

VkShaderStatisticsInfoAMD._fields_ = [
    ("shaderStageMask", c_uint32),
    ("resourceUsage", VkShaderResourceUsageAMD),
    ("numPhysicalVgprs", c_uint32),
    ("numPhysicalSgprs", c_uint32),
    ("numAvailableVgprs", c_uint32),
    ("numAvailableSgprs", c_uint32),
    ("computeWorkGroupSize", (c_uint32 * 3)),
]

VkDeviceQueueGlobalPriorityCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("globalPriority", c_int32),
]

VkDeviceQueueGlobalPriorityCreateInfoKHR._fields_ = [
]

VkDeviceQueueGlobalPriorityCreateInfoEXT._fields_ = [
]

VkPhysicalDeviceGlobalPriorityQueryFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("globalPriorityQuery", c_uint32),
]

VkPhysicalDeviceGlobalPriorityQueryFeaturesKHR._fields_ = [
]

VkPhysicalDeviceGlobalPriorityQueryFeaturesEXT._fields_ = [
]

VkQueueFamilyGlobalPriorityProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("priorityCount", c_uint32),
    ("priorities", (c_int32 * VK_MAX_GLOBAL_PRIORITY_SIZE)),
]

VkQueueFamilyGlobalPriorityPropertiesKHR._fields_ = [
]

VkQueueFamilyGlobalPriorityPropertiesEXT._fields_ = [
]

VkDebugUtilsObjectNameInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("objectType", c_int32),
    ("objectHandle", c_uint64),
    ("pObjectName", c_char_p),
]

VkDebugUtilsObjectTagInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("objectType", c_int32),
    ("objectHandle", c_uint64),
    ("tagName", c_uint64),
    ("tagSize", c_size_t),
    ("pTag", c_void_p),
]

VkDebugUtilsLabelEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pLabelName", c_char_p),
    ("color", (c_float * 4)),
]

VkDebugUtilsMessengerCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("messageSeverity", c_uint32),
    ("messageType", c_uint32),
    ("pfnUserCallback", PFN_vkDebugUtilsMessengerCallbackEXT),
    ("pUserData", c_void_p),
]

VkDebugUtilsMessengerCallbackDataEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pMessageIdName", c_char_p),
    ("messageIdNumber", c_int32),
    ("pMessage", c_char_p),
    ("queueLabelCount", c_uint32),
    ("pQueueLabels", POINTER(VkDebugUtilsLabelEXT)),
    ("cmdBufLabelCount", c_uint32),
    ("pCmdBufLabels", POINTER(VkDebugUtilsLabelEXT)),
    ("objectCount", c_uint32),
    ("pObjects", POINTER(VkDebugUtilsObjectNameInfoEXT)),
]

VkPhysicalDeviceDeviceMemoryReportFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceMemoryReport", c_uint32),
]

VkDeviceDeviceMemoryReportCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pfnUserCallback", PFN_vkDeviceMemoryReportCallbackEXT),
    ("pUserData", c_void_p),
]

VkDeviceMemoryReportCallbackDataEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("type", c_int32),
    ("memoryObjectId", c_uint64),
    ("size", c_uint64),
    ("objectType", c_int32),
    ("objectHandle", c_uint64),
    ("heapIndex", c_uint32),
]

VkImportMemoryHostPointerInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleType", c_int32),
    ("pHostPointer", c_void_p),
]

VkMemoryHostPointerPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
]

VkPhysicalDeviceExternalMemoryHostPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minImportedHostPointerAlignment", c_uint64),
]

VkPhysicalDeviceConservativeRasterizationPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("primitiveOverestimationSize", c_float),
    ("maxExtraPrimitiveOverestimationSize", c_float),
    ("extraPrimitiveOverestimationSizeGranularity", c_float),
    ("primitiveUnderestimation", c_uint32),
    ("conservativePointAndLineRasterization", c_uint32),
    ("degenerateTrianglesRasterized", c_uint32),
    ("degenerateLinesRasterized", c_uint32),
    ("fullyCoveredFragmentShaderInputVariable", c_uint32),
    ("conservativeRasterizationPostDepthCoverage", c_uint32),
]

VkCalibratedTimestampInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("timeDomain", c_int32),
]

VkCalibratedTimestampInfoEXT._fields_ = [
]

VkPhysicalDeviceShaderCorePropertiesAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderEngineCount", c_uint32),
    ("shaderArraysPerEngineCount", c_uint32),
    ("computeUnitsPerShaderArray", c_uint32),
    ("simdPerComputeUnit", c_uint32),
    ("wavefrontsPerSimd", c_uint32),
    ("wavefrontSize", c_uint32),
    ("sgprsPerSimd", c_uint32),
    ("minSgprAllocation", c_uint32),
    ("maxSgprAllocation", c_uint32),
    ("sgprAllocationGranularity", c_uint32),
    ("vgprsPerSimd", c_uint32),
    ("minVgprAllocation", c_uint32),
    ("maxVgprAllocation", c_uint32),
    ("vgprAllocationGranularity", c_uint32),
]

VkPhysicalDeviceShaderCoreProperties2AMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderCoreFeatures", c_uint32),
    ("activeComputeUnitCount", c_uint32),
]

VkPipelineRasterizationConservativeStateCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("conservativeRasterizationMode", c_int32),
    ("extraPrimitiveOverestimationSize", c_float),
]

VkPhysicalDeviceDescriptorIndexingFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderInputAttachmentArrayDynamicIndexing", c_uint32),
    ("shaderUniformTexelBufferArrayDynamicIndexing", c_uint32),
    ("shaderStorageTexelBufferArrayDynamicIndexing", c_uint32),
    ("shaderUniformBufferArrayNonUniformIndexing", c_uint32),
    ("shaderSampledImageArrayNonUniformIndexing", c_uint32),
    ("shaderStorageBufferArrayNonUniformIndexing", c_uint32),
    ("shaderStorageImageArrayNonUniformIndexing", c_uint32),
    ("shaderInputAttachmentArrayNonUniformIndexing", c_uint32),
    ("shaderUniformTexelBufferArrayNonUniformIndexing", c_uint32),
    ("shaderStorageTexelBufferArrayNonUniformIndexing", c_uint32),
    ("descriptorBindingUniformBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingSampledImageUpdateAfterBind", c_uint32),
    ("descriptorBindingStorageImageUpdateAfterBind", c_uint32),
    ("descriptorBindingStorageBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingUniformTexelBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingStorageTexelBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingUpdateUnusedWhilePending", c_uint32),
    ("descriptorBindingPartiallyBound", c_uint32),
    ("descriptorBindingVariableDescriptorCount", c_uint32),
    ("runtimeDescriptorArray", c_uint32),
]

VkPhysicalDeviceDescriptorIndexingFeaturesEXT._fields_ = [
]

VkPhysicalDeviceDescriptorIndexingProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxUpdateAfterBindDescriptorsInAllPools", c_uint32),
    ("shaderUniformBufferArrayNonUniformIndexingNative", c_uint32),
    ("shaderSampledImageArrayNonUniformIndexingNative", c_uint32),
    ("shaderStorageBufferArrayNonUniformIndexingNative", c_uint32),
    ("shaderStorageImageArrayNonUniformIndexingNative", c_uint32),
    ("shaderInputAttachmentArrayNonUniformIndexingNative", c_uint32),
    ("robustBufferAccessUpdateAfterBind", c_uint32),
    ("quadDivergentImplicitLod", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindSamplers", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindUniformBuffers", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindStorageBuffers", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindSampledImages", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindStorageImages", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindInputAttachments", c_uint32),
    ("maxPerStageUpdateAfterBindResources", c_uint32),
    ("maxDescriptorSetUpdateAfterBindSamplers", c_uint32),
    ("maxDescriptorSetUpdateAfterBindUniformBuffers", c_uint32),
    ("maxDescriptorSetUpdateAfterBindUniformBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageBuffers", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindSampledImages", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageImages", c_uint32),
    ("maxDescriptorSetUpdateAfterBindInputAttachments", c_uint32),
]

VkPhysicalDeviceDescriptorIndexingPropertiesEXT._fields_ = [
]

VkDescriptorSetLayoutBindingFlagsCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("bindingCount", c_uint32),
    ("pBindingFlags", POINTER(c_uint32)),
]

VkDescriptorSetLayoutBindingFlagsCreateInfoEXT._fields_ = [
]

VkDescriptorSetVariableDescriptorCountAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorSetCount", c_uint32),
    ("pDescriptorCounts", POINTER(c_uint32)),
]

VkDescriptorSetVariableDescriptorCountAllocateInfoEXT._fields_ = [
]

VkDescriptorSetVariableDescriptorCountLayoutSupport._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxVariableDescriptorCount", c_uint32),
]

VkDescriptorSetVariableDescriptorCountLayoutSupportEXT._fields_ = [
]

VkAttachmentDescription2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("format", c_int32),
    ("samples", c_int32),
    ("loadOp", c_int32),
    ("storeOp", c_int32),
    ("stencilLoadOp", c_int32),
    ("stencilStoreOp", c_int32),
    ("initialLayout", c_int32),
    ("finalLayout", c_int32),
]

VkAttachmentDescription2KHR._fields_ = [
]

VkAttachmentReference2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachment", c_uint32),
    ("layout", c_int32),
    ("aspectMask", c_uint32),
]

VkAttachmentReference2KHR._fields_ = [
]

VkSubpassDescription2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pipelineBindPoint", c_int32),
    ("viewMask", c_uint32),
    ("inputAttachmentCount", c_uint32),
    ("pInputAttachments", POINTER(VkAttachmentReference2)),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachments", POINTER(VkAttachmentReference2)),
    ("pResolveAttachments", POINTER(VkAttachmentReference2)),
    ("pDepthStencilAttachment", POINTER(VkAttachmentReference2)),
    ("preserveAttachmentCount", c_uint32),
    ("pPreserveAttachments", POINTER(c_uint32)),
]

VkSubpassDescription2KHR._fields_ = [
]

VkSubpassDependency2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcSubpass", c_uint32),
    ("dstSubpass", c_uint32),
    ("srcStageMask", c_uint32),
    ("dstStageMask", c_uint32),
    ("srcAccessMask", c_uint32),
    ("dstAccessMask", c_uint32),
    ("dependencyFlags", c_uint32),
    ("viewOffset", c_int32),
]

VkSubpassDependency2KHR._fields_ = [
]

VkRenderPassCreateInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("attachmentCount", c_uint32),
    ("pAttachments", POINTER(VkAttachmentDescription2)),
    ("subpassCount", c_uint32),
    ("pSubpasses", POINTER(VkSubpassDescription2)),
    ("dependencyCount", c_uint32),
    ("pDependencies", POINTER(VkSubpassDependency2)),
    ("correlatedViewMaskCount", c_uint32),
    ("pCorrelatedViewMasks", POINTER(c_uint32)),
]

VkRenderPassCreateInfo2KHR._fields_ = [
]

VkSubpassBeginInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("contents", c_int32),
]

VkSubpassBeginInfoKHR._fields_ = [
]

VkSubpassEndInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkSubpassEndInfoKHR._fields_ = [
]

VkPhysicalDeviceTimelineSemaphoreFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("timelineSemaphore", c_uint32),
]

VkPhysicalDeviceTimelineSemaphoreFeaturesKHR._fields_ = [
]

VkPhysicalDeviceTimelineSemaphoreProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxTimelineSemaphoreValueDifference", c_uint64),
]

VkPhysicalDeviceTimelineSemaphorePropertiesKHR._fields_ = [
]

VkSemaphoreTypeCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphoreType", c_int32),
    ("initialValue", c_uint64),
]

VkSemaphoreTypeCreateInfoKHR._fields_ = [
]

VkTimelineSemaphoreSubmitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("waitSemaphoreValueCount", c_uint32),
    ("pWaitSemaphoreValues", POINTER(c_uint64)),
    ("signalSemaphoreValueCount", c_uint32),
    ("pSignalSemaphoreValues", POINTER(c_uint64)),
]

VkTimelineSemaphoreSubmitInfoKHR._fields_ = [
]

VkSemaphoreWaitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("semaphoreCount", c_uint32),
    ("pSemaphores", POINTER(c_void_p)),
    ("pValues", POINTER(c_uint64)),
]

VkSemaphoreWaitInfoKHR._fields_ = [
]

VkSemaphoreSignalInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("value", c_uint64),
]

VkSemaphoreSignalInfoKHR._fields_ = [
]

VkVertexInputBindingDivisorDescription._fields_ = [
    ("binding", c_uint32),
    ("divisor", c_uint32),
]

VkVertexInputBindingDivisorDescriptionKHR._fields_ = [
]

VkVertexInputBindingDivisorDescriptionEXT._fields_ = [
]

VkPipelineVertexInputDivisorStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexBindingDivisorCount", c_uint32),
    ("pVertexBindingDivisors", POINTER(VkVertexInputBindingDivisorDescription)),
]

VkPipelineVertexInputDivisorStateCreateInfoKHR._fields_ = [
]

VkPipelineVertexInputDivisorStateCreateInfoEXT._fields_ = [
]

VkPhysicalDeviceVertexAttributeDivisorPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxVertexAttribDivisor", c_uint32),
]

VkPhysicalDeviceVertexAttributeDivisorProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxVertexAttribDivisor", c_uint32),
    ("supportsNonZeroFirstInstance", c_uint32),
]

VkPhysicalDeviceVertexAttributeDivisorPropertiesKHR._fields_ = [
]

VkPhysicalDevicePCIBusInfoPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pciDomain", c_uint32),
    ("pciBus", c_uint32),
    ("pciDevice", c_uint32),
    ("pciFunction", c_uint32),
]

VkImportAndroidHardwareBufferInfoANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", POINTER(c_void_p)),
]

VkAndroidHardwareBufferUsageANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("androidHardwareBufferUsage", c_uint64),
]

VkAndroidHardwareBufferPropertiesANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allocationSize", c_uint64),
    ("memoryTypeBits", c_uint32),
]

VkMemoryGetAndroidHardwareBufferInfoANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
]

VkAndroidHardwareBufferFormatPropertiesANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("externalFormat", c_uint64),
    ("formatFeatures", c_uint32),
    ("samplerYcbcrConversionComponents", VkComponentMapping),
    ("suggestedYcbcrModel", c_int32),
    ("suggestedYcbcrRange", c_int32),
    ("suggestedXChromaOffset", c_int32),
    ("suggestedYChromaOffset", c_int32),
]

VkCommandBufferInheritanceConditionalRenderingInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("conditionalRenderingEnable", c_uint32),
]

VkExternalFormatANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalFormat", c_uint64),
]

VkPhysicalDevice8BitStorageFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("storageBuffer8BitAccess", c_uint32),
    ("uniformAndStorageBuffer8BitAccess", c_uint32),
    ("storagePushConstant8", c_uint32),
]

VkPhysicalDevice8BitStorageFeaturesKHR._fields_ = [
]

VkPhysicalDeviceConditionalRenderingFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("conditionalRendering", c_uint32),
    ("inheritedConditionalRendering", c_uint32),
]

VkPhysicalDeviceVulkanMemoryModelFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vulkanMemoryModel", c_uint32),
    ("vulkanMemoryModelDeviceScope", c_uint32),
    ("vulkanMemoryModelAvailabilityVisibilityChains", c_uint32),
]

VkPhysicalDeviceVulkanMemoryModelFeaturesKHR._fields_ = [
]

VkPhysicalDeviceShaderAtomicInt64Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderBufferInt64Atomics", c_uint32),
    ("shaderSharedInt64Atomics", c_uint32),
]

VkPhysicalDeviceShaderAtomicInt64FeaturesKHR._fields_ = [
]

VkPhysicalDeviceShaderAtomicFloatFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderBufferFloat32Atomics", c_uint32),
    ("shaderBufferFloat32AtomicAdd", c_uint32),
    ("shaderBufferFloat64Atomics", c_uint32),
    ("shaderBufferFloat64AtomicAdd", c_uint32),
    ("shaderSharedFloat32Atomics", c_uint32),
    ("shaderSharedFloat32AtomicAdd", c_uint32),
    ("shaderSharedFloat64Atomics", c_uint32),
    ("shaderSharedFloat64AtomicAdd", c_uint32),
    ("shaderImageFloat32Atomics", c_uint32),
    ("shaderImageFloat32AtomicAdd", c_uint32),
    ("sparseImageFloat32Atomics", c_uint32),
    ("sparseImageFloat32AtomicAdd", c_uint32),
]

VkPhysicalDeviceShaderAtomicFloat2FeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderBufferFloat16Atomics", c_uint32),
    ("shaderBufferFloat16AtomicAdd", c_uint32),
    ("shaderBufferFloat16AtomicMinMax", c_uint32),
    ("shaderBufferFloat32AtomicMinMax", c_uint32),
    ("shaderBufferFloat64AtomicMinMax", c_uint32),
    ("shaderSharedFloat16Atomics", c_uint32),
    ("shaderSharedFloat16AtomicAdd", c_uint32),
    ("shaderSharedFloat16AtomicMinMax", c_uint32),
    ("shaderSharedFloat32AtomicMinMax", c_uint32),
    ("shaderSharedFloat64AtomicMinMax", c_uint32),
    ("shaderImageFloat32AtomicMinMax", c_uint32),
    ("sparseImageFloat32AtomicMinMax", c_uint32),
]

VkPhysicalDeviceVertexAttributeDivisorFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexAttributeInstanceRateDivisor", c_uint32),
    ("vertexAttributeInstanceRateZeroDivisor", c_uint32),
]

VkPhysicalDeviceVertexAttributeDivisorFeaturesKHR._fields_ = [
]

VkPhysicalDeviceVertexAttributeDivisorFeaturesEXT._fields_ = [
]

VkQueueFamilyCheckpointPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("checkpointExecutionStageMask", c_uint32),
]

VkCheckpointDataNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stage", c_int32),
    ("pCheckpointMarker", c_void_p),
]

VkPhysicalDeviceDepthStencilResolveProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedDepthResolveModes", c_uint32),
    ("supportedStencilResolveModes", c_uint32),
    ("independentResolveNone", c_uint32),
    ("independentResolve", c_uint32),
]

VkPhysicalDeviceDepthStencilResolvePropertiesKHR._fields_ = [
]

VkSubpassDescriptionDepthStencilResolve._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthResolveMode", c_int32),
    ("stencilResolveMode", c_int32),
    ("pDepthStencilResolveAttachment", POINTER(VkAttachmentReference2)),
]

VkSubpassDescriptionDepthStencilResolveKHR._fields_ = [
]

VkImageViewASTCDecodeModeEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("decodeMode", c_int32),
]

VkPhysicalDeviceASTCDecodeFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("decodeModeSharedExponent", c_uint32),
]

VkPhysicalDeviceTransformFeedbackFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("transformFeedback", c_uint32),
    ("geometryStreams", c_uint32),
]

VkPhysicalDeviceTransformFeedbackPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxTransformFeedbackStreams", c_uint32),
    ("maxTransformFeedbackBuffers", c_uint32),
    ("maxTransformFeedbackBufferSize", c_uint64),
    ("maxTransformFeedbackStreamDataSize", c_uint32),
    ("maxTransformFeedbackBufferDataSize", c_uint32),
    ("maxTransformFeedbackBufferDataStride", c_uint32),
    ("transformFeedbackQueries", c_uint32),
    ("transformFeedbackStreamsLinesTriangles", c_uint32),
    ("transformFeedbackRasterizationStreamSelect", c_uint32),
    ("transformFeedbackDraw", c_uint32),
]

VkPipelineRasterizationStateStreamCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("rasterizationStream", c_uint32),
]

VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("representativeFragmentTest", c_uint32),
]

VkPipelineRepresentativeFragmentTestStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("representativeFragmentTestEnable", c_uint32),
]

VkPhysicalDeviceExclusiveScissorFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("exclusiveScissor", c_uint32),
]

VkPipelineViewportExclusiveScissorStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("exclusiveScissorCount", c_uint32),
    ("pExclusiveScissors", POINTER(VkRect2D)),
]

VkPhysicalDeviceCornerSampledImageFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cornerSampledImage", c_uint32),
]

VkPhysicalDeviceComputeShaderDerivativesFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("computeDerivativeGroupQuads", c_uint32),
    ("computeDerivativeGroupLinear", c_uint32),
]

VkPhysicalDeviceComputeShaderDerivativesFeaturesNV._fields_ = [
]

VkPhysicalDeviceComputeShaderDerivativesPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("meshAndTaskShaderDerivatives", c_uint32),
]

VkPhysicalDeviceFragmentShaderBarycentricFeaturesNV._fields_ = [
]

VkPhysicalDeviceShaderImageFootprintFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageFootprint", c_uint32),
]

VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dedicatedAllocationImageAliasing", c_uint32),
]

VkPhysicalDeviceCopyMemoryIndirectFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("indirectMemoryCopy", c_uint32),
    ("indirectMemoryToImageCopy", c_uint32),
]

VkPhysicalDeviceCopyMemoryIndirectFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("indirectCopy", c_uint32),
]

VkPhysicalDeviceCopyMemoryIndirectPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedQueues", c_uint32),
]

VkPhysicalDeviceCopyMemoryIndirectPropertiesNV._fields_ = [
]

VkPhysicalDeviceMemoryDecompressionFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryDecompression", c_uint32),
]

VkPhysicalDeviceMemoryDecompressionFeaturesNV._fields_ = [
]

VkPhysicalDeviceMemoryDecompressionPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("decompressionMethods", c_uint64),
    ("maxDecompressionIndirectCount", c_uint64),
]

VkPhysicalDeviceMemoryDecompressionPropertiesNV._fields_ = [
]

VkShadingRatePaletteNV._fields_ = [
    ("shadingRatePaletteEntryCount", c_uint32),
    ("pShadingRatePaletteEntries", POINTER(c_int32)),
]

VkPipelineViewportShadingRateImageStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shadingRateImageEnable", c_uint32),
    ("viewportCount", c_uint32),
    ("pShadingRatePalettes", POINTER(VkShadingRatePaletteNV)),
]

VkPhysicalDeviceShadingRateImageFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shadingRateImage", c_uint32),
    ("shadingRateCoarseSampleOrder", c_uint32),
]

VkPhysicalDeviceShadingRateImagePropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shadingRateTexelSize", VkExtent2D),
    ("shadingRatePaletteSize", c_uint32),
    ("shadingRateMaxCoarseSamples", c_uint32),
]

VkPhysicalDeviceInvocationMaskFeaturesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("invocationMask", c_uint32),
]

VkCoarseSampleLocationNV._fields_ = [
    ("pixelX", c_uint32),
    ("pixelY", c_uint32),
    ("sample", c_uint32),
]

VkCoarseSampleOrderCustomNV._fields_ = [
    ("shadingRate", c_int32),
    ("sampleCount", c_uint32),
    ("sampleLocationCount", c_uint32),
    ("pSampleLocations", POINTER(VkCoarseSampleLocationNV)),
]

VkPipelineViewportCoarseSampleOrderStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sampleOrderType", c_int32),
    ("customSampleOrderCount", c_uint32),
    ("pCustomSampleOrders", POINTER(VkCoarseSampleOrderCustomNV)),
]

VkPhysicalDeviceMeshShaderFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("taskShader", c_uint32),
    ("meshShader", c_uint32),
]

VkPhysicalDeviceMeshShaderPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxDrawMeshTasksCount", c_uint32),
    ("maxTaskWorkGroupInvocations", c_uint32),
    ("maxTaskWorkGroupSize", (c_uint32 * 3)),
    ("maxTaskTotalMemorySize", c_uint32),
    ("maxTaskOutputCount", c_uint32),
    ("maxMeshWorkGroupInvocations", c_uint32),
    ("maxMeshWorkGroupSize", (c_uint32 * 3)),
    ("maxMeshTotalMemorySize", c_uint32),
    ("maxMeshOutputVertices", c_uint32),
    ("maxMeshOutputPrimitives", c_uint32),
    ("maxMeshMultiviewViewCount", c_uint32),
    ("meshOutputPerVertexGranularity", c_uint32),
    ("meshOutputPerPrimitiveGranularity", c_uint32),
]

VkDrawMeshTasksIndirectCommandNV._fields_ = [
    ("taskCount", c_uint32),
    ("firstTask", c_uint32),
]

VkPhysicalDeviceMeshShaderFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("taskShader", c_uint32),
    ("meshShader", c_uint32),
    ("multiviewMeshShader", c_uint32),
    ("primitiveFragmentShadingRateMeshShader", c_uint32),
    ("meshShaderQueries", c_uint32),
]

VkPhysicalDeviceMeshShaderPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxTaskWorkGroupTotalCount", c_uint32),
    ("maxTaskWorkGroupCount", (c_uint32 * 3)),
    ("maxTaskWorkGroupInvocations", c_uint32),
    ("maxTaskWorkGroupSize", (c_uint32 * 3)),
    ("maxTaskPayloadSize", c_uint32),
    ("maxTaskSharedMemorySize", c_uint32),
    ("maxTaskPayloadAndSharedMemorySize", c_uint32),
    ("maxMeshWorkGroupTotalCount", c_uint32),
    ("maxMeshWorkGroupCount", (c_uint32 * 3)),
    ("maxMeshWorkGroupInvocations", c_uint32),
    ("maxMeshWorkGroupSize", (c_uint32 * 3)),
    ("maxMeshSharedMemorySize", c_uint32),
    ("maxMeshPayloadAndSharedMemorySize", c_uint32),
    ("maxMeshOutputMemorySize", c_uint32),
    ("maxMeshPayloadAndOutputMemorySize", c_uint32),
    ("maxMeshOutputComponents", c_uint32),
    ("maxMeshOutputVertices", c_uint32),
    ("maxMeshOutputPrimitives", c_uint32),
    ("maxMeshOutputLayers", c_uint32),
    ("maxMeshMultiviewViewCount", c_uint32),
    ("meshOutputPerVertexGranularity", c_uint32),
    ("meshOutputPerPrimitiveGranularity", c_uint32),
    ("maxPreferredTaskWorkGroupInvocations", c_uint32),
    ("maxPreferredMeshWorkGroupInvocations", c_uint32),
    ("prefersLocalInvocationVertexOutput", c_uint32),
    ("prefersLocalInvocationPrimitiveOutput", c_uint32),
    ("prefersCompactVertexOutput", c_uint32),
    ("prefersCompactPrimitiveOutput", c_uint32),
]

VkDrawMeshTasksIndirectCommandEXT._fields_ = [
    ("groupCountX", c_uint32),
    ("groupCountY", c_uint32),
    ("groupCountZ", c_uint32),
]

VkRayTracingShaderGroupCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("generalShader", c_uint32),
    ("closestHitShader", c_uint32),
    ("anyHitShader", c_uint32),
    ("intersectionShader", c_uint32),
]

VkRayTracingShaderGroupCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("generalShader", c_uint32),
    ("closestHitShader", c_uint32),
    ("anyHitShader", c_uint32),
    ("intersectionShader", c_uint32),
    ("pShaderGroupCaptureReplayHandle", c_void_p),
]

VkRayTracingPipelineCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stageCount", c_uint32),
    ("pStages", POINTER(VkPipelineShaderStageCreateInfo)),
    ("groupCount", c_uint32),
    ("pGroups", POINTER(VkRayTracingShaderGroupCreateInfoNV)),
    ("maxRecursionDepth", c_uint32),
    ("layout", c_void_p),
    ("basePipelineHandle", c_void_p),
    ("basePipelineIndex", c_int32),
]

VkRayTracingPipelineCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stageCount", c_uint32),
    ("pStages", POINTER(VkPipelineShaderStageCreateInfo)),
    ("groupCount", c_uint32),
    ("pGroups", POINTER(VkRayTracingShaderGroupCreateInfoKHR)),
    ("maxPipelineRayRecursionDepth", c_uint32),
    ("pLibraryInfo", POINTER(VkPipelineLibraryCreateInfoKHR)),
    ("pLibraryInterface", POINTER(VkRayTracingPipelineInterfaceCreateInfoKHR)),
    ("pDynamicState", POINTER(VkPipelineDynamicStateCreateInfo)),
    ("layout", c_void_p),
    ("basePipelineHandle", c_void_p),
    ("basePipelineIndex", c_int32),
]

VkGeometryTrianglesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexData", c_void_p),
    ("vertexOffset", c_uint64),
    ("vertexCount", c_uint32),
    ("vertexStride", c_uint64),
    ("vertexFormat", c_int32),
    ("indexData", c_void_p),
    ("indexOffset", c_uint64),
    ("indexCount", c_uint32),
    ("indexType", c_int32),
    ("transformData", c_void_p),
    ("transformOffset", c_uint64),
]

VkGeometryAABBNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("aabbData", c_void_p),
    ("numAABBs", c_uint32),
    ("stride", c_uint32),
    ("offset", c_uint64),
]

VkGeometryDataNV._fields_ = [
    ("triangles", VkGeometryTrianglesNV),
    ("aabbs", VkGeometryAABBNV),
]

VkGeometryNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("geometryType", c_int32),
    ("geometry", VkGeometryDataNV),
    ("flags", c_uint32),
]

VkAccelerationStructureCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("compactedSize", c_uint64),
    ("info", VkAccelerationStructureInfoNV),
]

VkBindAccelerationStructureMemoryInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructure", c_void_p),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
    ("deviceIndexCount", c_uint32),
    ("pDeviceIndices", POINTER(c_uint32)),
]

VkWriteDescriptorSetAccelerationStructureKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructureCount", c_uint32),
    ("pAccelerationStructures", POINTER(c_void_p)),
]

VkWriteDescriptorSetAccelerationStructureNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructureCount", c_uint32),
    ("pAccelerationStructures", POINTER(c_void_p)),
]

VkAccelerationStructureMemoryRequirementsInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("accelerationStructure", c_void_p),
]

VkPhysicalDeviceAccelerationStructureFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructure", c_uint32),
    ("accelerationStructureCaptureReplay", c_uint32),
    ("accelerationStructureIndirectBuild", c_uint32),
    ("accelerationStructureHostCommands", c_uint32),
    ("descriptorBindingAccelerationStructureUpdateAfterBind", c_uint32),
]

VkPhysicalDeviceRayTracingPipelineFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingPipeline", c_uint32),
    ("rayTracingPipelineShaderGroupHandleCaptureReplay", c_uint32),
    ("rayTracingPipelineShaderGroupHandleCaptureReplayMixed", c_uint32),
    ("rayTracingPipelineTraceRaysIndirect", c_uint32),
    ("rayTraversalPrimitiveCulling", c_uint32),
]

VkPhysicalDeviceRayQueryFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayQuery", c_uint32),
]

VkPhysicalDeviceAccelerationStructurePropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxGeometryCount", c_uint64),
    ("maxInstanceCount", c_uint64),
    ("maxPrimitiveCount", c_uint64),
    ("maxPerStageDescriptorAccelerationStructures", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindAccelerationStructures", c_uint32),
    ("maxDescriptorSetAccelerationStructures", c_uint32),
    ("maxDescriptorSetUpdateAfterBindAccelerationStructures", c_uint32),
    ("minAccelerationStructureScratchOffsetAlignment", c_uint32),
]

VkPhysicalDeviceRayTracingPipelinePropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderGroupHandleSize", c_uint32),
    ("maxRayRecursionDepth", c_uint32),
    ("maxShaderGroupStride", c_uint32),
    ("shaderGroupBaseAlignment", c_uint32),
    ("shaderGroupHandleCaptureReplaySize", c_uint32),
    ("maxRayDispatchInvocationCount", c_uint32),
    ("shaderGroupHandleAlignment", c_uint32),
    ("maxRayHitAttributeSize", c_uint32),
]

VkPhysicalDeviceRayTracingPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderGroupHandleSize", c_uint32),
    ("maxRecursionDepth", c_uint32),
    ("maxShaderGroupStride", c_uint32),
    ("shaderGroupBaseAlignment", c_uint32),
    ("maxGeometryCount", c_uint64),
    ("maxInstanceCount", c_uint64),
    ("maxTriangleCount", c_uint64),
    ("maxDescriptorSetAccelerationStructures", c_uint32),
]

VkTraceRaysIndirectCommandKHR._fields_ = [
    ("width", c_uint32),
    ("height", c_uint32),
    ("depth", c_uint32),
]

VkTraceRaysIndirectCommand2KHR._fields_ = [
    ("raygenShaderRecordAddress", c_uint64),
    ("raygenShaderRecordSize", c_uint64),
    ("missShaderBindingTableAddress", c_uint64),
    ("missShaderBindingTableSize", c_uint64),
    ("missShaderBindingTableStride", c_uint64),
    ("hitShaderBindingTableAddress", c_uint64),
    ("hitShaderBindingTableSize", c_uint64),
    ("hitShaderBindingTableStride", c_uint64),
    ("callableShaderBindingTableAddress", c_uint64),
    ("callableShaderBindingTableSize", c_uint64),
    ("callableShaderBindingTableStride", c_uint64),
    ("width", c_uint32),
    ("height", c_uint32),
    ("depth", c_uint32),
]

VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingMaintenance1", c_uint32),
    ("rayTracingPipelineTraceRaysIndirect2", c_uint32),
]

VkDrmFormatModifierPropertiesListEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("drmFormatModifierCount", c_uint32),
    ("pDrmFormatModifierProperties", POINTER(VkDrmFormatModifierPropertiesEXT)),
]

VkDrmFormatModifierPropertiesEXT._fields_ = [
    ("drmFormatModifier", c_uint64),
    ("drmFormatModifierPlaneCount", c_uint32),
    ("drmFormatModifierTilingFeatures", c_uint32),
]

VkPhysicalDeviceImageDrmFormatModifierInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("drmFormatModifier", c_uint64),
    ("sharingMode", c_int32),
    ("queueFamilyIndexCount", c_uint32),
    ("pQueueFamilyIndices", POINTER(c_uint32)),
]

VkImageDrmFormatModifierListCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("drmFormatModifierCount", c_uint32),
    ("pDrmFormatModifiers", POINTER(c_uint64)),
]

VkImageDrmFormatModifierExplicitCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("drmFormatModifier", c_uint64),
    ("drmFormatModifierPlaneCount", c_uint32),
    ("pPlaneLayouts", POINTER(VkSubresourceLayout)),
]

VkImageDrmFormatModifierPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("drmFormatModifier", c_uint64),
]

VkImageStencilUsageCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stencilUsage", c_uint32),
]

VkImageStencilUsageCreateInfoEXT._fields_ = [
]

VkDeviceMemoryOverallocationCreateInfoAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("overallocationBehavior", c_int32),
]

VkPhysicalDeviceFragmentDensityMapFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityMap", c_uint32),
    ("fragmentDensityMapDynamic", c_uint32),
    ("fragmentDensityMapNonSubsampledImages", c_uint32),
]

VkPhysicalDeviceFragmentDensityMap2FeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityMapDeferred", c_uint32),
]

VkPhysicalDeviceFragmentDensityMapOffsetFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityMapOffset", c_uint32),
]

VkPhysicalDeviceFragmentDensityMapOffsetFeaturesQCOM._fields_ = [
]

VkPhysicalDeviceFragmentDensityMapPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minFragmentDensityTexelSize", VkExtent2D),
    ("maxFragmentDensityTexelSize", VkExtent2D),
    ("fragmentDensityInvocations", c_uint32),
]

VkPhysicalDeviceFragmentDensityMap2PropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subsampledLoads", c_uint32),
    ("subsampledCoarseReconstructionEarlyAccess", c_uint32),
    ("maxSubsampledArrayLayers", c_uint32),
    ("maxDescriptorSetSubsampledSamplers", c_uint32),
]

VkPhysicalDeviceFragmentDensityMapOffsetPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityOffsetGranularity", VkExtent2D),
]

VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM._fields_ = [
]

VkRenderPassFragmentDensityMapCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityMapAttachment", VkAttachmentReference),
]

VkRenderPassFragmentDensityMapOffsetEndInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityOffsetCount", c_uint32),
    ("pFragmentDensityOffsets", POINTER(VkOffset2D)),
]

VkSubpassFragmentDensityMapOffsetEndInfoQCOM._fields_ = [
]

VkPhysicalDeviceScalarBlockLayoutFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("scalarBlockLayout", c_uint32),
]

VkPhysicalDeviceScalarBlockLayoutFeaturesEXT._fields_ = [
]

VkSurfaceProtectedCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportsProtected", c_uint32),
]

VkPhysicalDeviceUniformBufferStandardLayoutFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("uniformBufferStandardLayout", c_uint32),
]

VkPhysicalDeviceUniformBufferStandardLayoutFeaturesKHR._fields_ = [
]

VkPhysicalDeviceDepthClipEnableFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthClipEnable", c_uint32),
]

VkPipelineRasterizationDepthClipStateCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("depthClipEnable", c_uint32),
]

VkPhysicalDeviceMemoryBudgetPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("heapBudget", (c_uint64 * VK_MAX_MEMORY_HEAPS)),
    ("heapUsage", (c_uint64 * VK_MAX_MEMORY_HEAPS)),
]

VkPhysicalDeviceMemoryPriorityFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryPriority", c_uint32),
]

VkMemoryPriorityAllocateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("priority", c_float),
]

VkPhysicalDevicePageableDeviceLocalMemoryFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pageableDeviceLocalMemory", c_uint32),
]

VkPhysicalDeviceBufferDeviceAddressFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("bufferDeviceAddress", c_uint32),
    ("bufferDeviceAddressCaptureReplay", c_uint32),
    ("bufferDeviceAddressMultiDevice", c_uint32),
]

VkPhysicalDeviceBufferDeviceAddressFeaturesKHR._fields_ = [
]

VkPhysicalDeviceBufferDeviceAddressFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("bufferDeviceAddress", c_uint32),
    ("bufferDeviceAddressCaptureReplay", c_uint32),
    ("bufferDeviceAddressMultiDevice", c_uint32),
]

VkPhysicalDeviceBufferAddressFeaturesEXT._fields_ = [
]

VkBufferDeviceAddressInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", c_void_p),
]

VkBufferDeviceAddressInfoKHR._fields_ = [
]

VkBufferDeviceAddressInfoEXT._fields_ = [
]

VkBufferOpaqueCaptureAddressCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("opaqueCaptureAddress", c_uint64),
]

VkBufferOpaqueCaptureAddressCreateInfoKHR._fields_ = [
]

VkBufferDeviceAddressCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceAddress", c_uint64),
]

VkPhysicalDeviceImageViewImageFormatInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageViewType", c_int32),
]

VkFilterCubicImageViewImageFormatPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("filterCubic", c_uint32),
    ("filterCubicMinmax", c_uint32),
]

VkPhysicalDeviceImagelessFramebufferFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imagelessFramebuffer", c_uint32),
]

VkPhysicalDeviceImagelessFramebufferFeaturesKHR._fields_ = [
]

VkFramebufferAttachmentsCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachmentImageInfoCount", c_uint32),
    ("pAttachmentImageInfos", POINTER(VkFramebufferAttachmentImageInfo)),
]

VkFramebufferAttachmentsCreateInfoKHR._fields_ = [
]

VkFramebufferAttachmentImageInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("usage", c_uint32),
    ("width", c_uint32),
    ("height", c_uint32),
    ("layerCount", c_uint32),
    ("viewFormatCount", c_uint32),
    ("pViewFormats", POINTER(c_int32)),
]

VkFramebufferAttachmentImageInfoKHR._fields_ = [
]

VkRenderPassAttachmentBeginInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachmentCount", c_uint32),
    ("pAttachments", POINTER(c_void_p)),
]

VkRenderPassAttachmentBeginInfoKHR._fields_ = [
]

VkPhysicalDeviceTextureCompressionASTCHDRFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("textureCompressionASTC_HDR", c_uint32),
]

VkPhysicalDeviceTextureCompressionASTCHDRFeaturesEXT._fields_ = [
]

VkPhysicalDeviceCooperativeMatrixFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrix", c_uint32),
    ("cooperativeMatrixRobustBufferAccess", c_uint32),
]

VkPhysicalDeviceCooperativeMatrixPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrixSupportedStages", c_uint32),
]

VkPhysicalDeviceYcbcrImageArraysFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("ycbcrImageArrays", c_uint32),
]

VkImageViewHandleInfoNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageView", c_void_p),
    ("descriptorType", c_int32),
    ("sampler", c_void_p),
]

VkImageViewAddressPropertiesNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceAddress", c_uint64),
    ("size", c_uint64),
]

VkPresentFrameTokenGGP._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("frameToken", c_uint32),
]

VkPipelineCreationFeedback._fields_ = [
    ("flags", c_uint32),
    ("duration", c_uint64),
]

VkPipelineCreationFeedbackEXT._fields_ = [
]

VkPipelineCreationFeedbackCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pPipelineCreationFeedback", POINTER(VkPipelineCreationFeedback)),
    ("pipelineStageCreationFeedbackCount", c_uint32),
    ("pPipelineStageCreationFeedbacks", POINTER(VkPipelineCreationFeedback)),
]

VkPipelineCreationFeedbackCreateInfoEXT._fields_ = [
]

VkSurfaceFullScreenExclusiveInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fullScreenExclusive", c_int32),
]

VkSurfaceFullScreenExclusiveWin32InfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hmonitor", c_void_p),
]

VkSurfaceCapabilitiesFullScreenExclusiveEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fullScreenExclusiveSupported", c_uint32),
]

VkPhysicalDevicePresentBarrierFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentBarrier", c_uint32),
]

VkSurfaceCapabilitiesPresentBarrierNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentBarrierSupported", c_uint32),
]

VkSwapchainPresentBarrierCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentBarrierEnable", c_uint32),
]

VkPhysicalDevicePerformanceQueryFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("performanceCounterQueryPools", c_uint32),
    ("performanceCounterMultipleQueryPools", c_uint32),
]

VkPhysicalDevicePerformanceQueryPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allowCommandBufferQueryCopies", c_uint32),
]

VkPerformanceCounterKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("unit", c_int32),
    ("scope", c_int32),
    ("storage", c_int32),
    ("uuid", (c_uint8 * VK_UUID_SIZE)),
]

VkPerformanceCounterDescriptionKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("name", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("category", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
]

VkQueryPoolPerformanceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queueFamilyIndex", c_uint32),
    ("counterIndexCount", c_uint32),
    ("pCounterIndices", POINTER(c_uint32)),
]

VkPerformanceCounterResultKHR._fields_ = [
    ("int32", c_int32),
    ("int64", c_int64),
    ("uint32", c_uint32),
    ("uint64", c_uint64),
    ("float32", c_float),
    ("float64", c_double),
]

VkAcquireProfilingLockInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("timeout", c_uint64),
]

VkPerformanceQuerySubmitInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("counterPassIndex", c_uint32),
]

VkPerformanceQueryReservationInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxPerformanceQueriesPerPool", c_uint32),
]

VkHeadlessSurfaceCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkPhysicalDeviceCoverageReductionModeFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("coverageReductionMode", c_uint32),
]

VkPipelineCoverageReductionStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("coverageReductionMode", c_int32),
]

VkFramebufferMixedSamplesCombinationNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("coverageReductionMode", c_int32),
    ("rasterizationSamples", c_int32),
    ("depthStencilSamples", c_uint32),
    ("colorSamples", c_uint32),
]

VkPhysicalDeviceShaderIntegerFunctions2FeaturesINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderIntegerFunctions2", c_uint32),
]

VkPerformanceValueDataINTEL._fields_ = [
    ("value32", c_uint32),
    ("value64", c_uint64),
    ("valueFloat", c_float),
    ("valueBool", c_uint32),
    ("valueString", c_char_p),
]

VkPerformanceValueINTEL._fields_ = [
    ("type", c_int32),
    ("data", VkPerformanceValueDataINTEL),
]

VkInitializePerformanceApiInfoINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pUserData", c_void_p),
]

VkQueryPoolPerformanceQueryCreateInfoINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("performanceCountersSampling", c_int32),
]

VkQueryPoolCreateInfoINTEL._fields_ = [
]

VkPerformanceMarkerInfoINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("marker", c_uint64),
]

VkPerformanceStreamMarkerInfoINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("marker", c_uint32),
]

VkPerformanceOverrideInfoINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("enable", c_uint32),
    ("parameter", c_uint64),
]

VkPerformanceConfigurationAcquireInfoINTEL._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
]

VkPhysicalDeviceShaderClockFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSubgroupClock", c_uint32),
    ("shaderDeviceClock", c_uint32),
]

VkPhysicalDeviceIndexTypeUint8Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("indexTypeUint8", c_uint32),
]

VkPhysicalDeviceIndexTypeUint8FeaturesKHR._fields_ = [
]

VkPhysicalDeviceIndexTypeUint8FeaturesEXT._fields_ = [
]

VkPhysicalDeviceShaderSMBuiltinsPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSMCount", c_uint32),
    ("shaderWarpsPerSM", c_uint32),
]

VkPhysicalDeviceShaderSMBuiltinsFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSMBuiltins", c_uint32),
]

VkPhysicalDeviceFragmentShaderInterlockFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentShaderSampleInterlock", c_uint32),
    ("fragmentShaderPixelInterlock", c_uint32),
    ("fragmentShaderShadingRateInterlock", c_uint32),
]

VkPhysicalDeviceSeparateDepthStencilLayoutsFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("separateDepthStencilLayouts", c_uint32),
]

VkPhysicalDeviceSeparateDepthStencilLayoutsFeaturesKHR._fields_ = [
]

VkAttachmentReferenceStencilLayout._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stencilLayout", c_int32),
]

VkPhysicalDevicePrimitiveTopologyListRestartFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("primitiveTopologyListRestart", c_uint32),
    ("primitiveTopologyPatchListRestart", c_uint32),
]

VkAttachmentReferenceStencilLayoutKHR._fields_ = [
]

VkAttachmentDescriptionStencilLayout._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stencilInitialLayout", c_int32),
    ("stencilFinalLayout", c_int32),
]

VkAttachmentDescriptionStencilLayoutKHR._fields_ = [
]

VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineExecutableInfo", c_uint32),
]

VkPipelineInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipeline", c_void_p),
]

VkPipelineInfoEXT._fields_ = [
]

VkPipelineExecutablePropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stages", c_uint32),
    ("name", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("subgroupSize", c_uint32),
]

VkPipelineExecutableInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipeline", c_void_p),
    ("executableIndex", c_uint32),
]

VkPipelineExecutableStatisticValueKHR._fields_ = [
    ("b32", c_uint32),
    ("i64", c_int64),
    ("u64", c_uint64),
    ("f64", c_double),
]

VkPipelineExecutableStatisticKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("name", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("format", c_int32),
    ("value", VkPipelineExecutableStatisticValueKHR),
]

VkPipelineExecutableInternalRepresentationKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("name", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("isText", c_uint32),
    ("dataSize", c_size_t),
    ("pData", c_void_p),
]

VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderDemoteToHelperInvocation", c_uint32),
]

VkPhysicalDeviceShaderDemoteToHelperInvocationFeaturesEXT._fields_ = [
]

VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("texelBufferAlignment", c_uint32),
]

VkPhysicalDeviceTexelBufferAlignmentProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("storageTexelBufferOffsetAlignmentBytes", c_uint64),
    ("storageTexelBufferOffsetSingleTexelAlignment", c_uint32),
    ("uniformTexelBufferOffsetAlignmentBytes", c_uint64),
    ("uniformTexelBufferOffsetSingleTexelAlignment", c_uint32),
]

VkPhysicalDeviceTexelBufferAlignmentPropertiesEXT._fields_ = [
]

VkPhysicalDeviceSubgroupSizeControlFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subgroupSizeControl", c_uint32),
    ("computeFullSubgroups", c_uint32),
]

VkPhysicalDeviceSubgroupSizeControlFeaturesEXT._fields_ = [
]

VkPhysicalDeviceSubgroupSizeControlProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minSubgroupSize", c_uint32),
    ("maxSubgroupSize", c_uint32),
    ("maxComputeWorkgroupSubgroups", c_uint32),
    ("requiredSubgroupSizeStages", c_uint32),
]

VkPhysicalDeviceSubgroupSizeControlPropertiesEXT._fields_ = [
]

VkPipelineShaderStageRequiredSubgroupSizeCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("requiredSubgroupSize", c_uint32),
]

VkPipelineShaderStageRequiredSubgroupSizeCreateInfoEXT._fields_ = [
]

VkShaderRequiredSubgroupSizeCreateInfoEXT._fields_ = [
]

VkSubpassShadingPipelineCreateInfoHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("renderPass", c_void_p),
    ("subpass", c_uint32),
]

VkPhysicalDeviceSubpassShadingPropertiesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxSubpassShadingWorkgroupSizeAspectRatio", c_uint32),
]

VkPhysicalDeviceClusterCullingShaderPropertiesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxWorkGroupCount", (c_uint32 * 3)),
    ("maxWorkGroupSize", (c_uint32 * 3)),
    ("maxOutputClusterCount", c_uint32),
    ("indirectBufferOffsetAlignment", c_uint64),
]

VkMemoryOpaqueCaptureAddressAllocateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("opaqueCaptureAddress", c_uint64),
]

VkMemoryOpaqueCaptureAddressAllocateInfoKHR._fields_ = [
]

VkDeviceMemoryOpaqueCaptureAddressInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
]

VkDeviceMemoryOpaqueCaptureAddressInfoKHR._fields_ = [
]

VkPhysicalDeviceLineRasterizationFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rectangularLines", c_uint32),
    ("bresenhamLines", c_uint32),
    ("smoothLines", c_uint32),
    ("stippledRectangularLines", c_uint32),
    ("stippledBresenhamLines", c_uint32),
    ("stippledSmoothLines", c_uint32),
]

VkPhysicalDeviceLineRasterizationFeaturesKHR._fields_ = [
]

VkPhysicalDeviceLineRasterizationFeaturesEXT._fields_ = [
]

VkPhysicalDeviceLineRasterizationProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("lineSubPixelPrecisionBits", c_uint32),
]

VkPhysicalDeviceLineRasterizationPropertiesKHR._fields_ = [
]

VkPhysicalDeviceLineRasterizationPropertiesEXT._fields_ = [
]

VkPipelineRasterizationLineStateCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("lineRasterizationMode", c_int32),
    ("stippledLineEnable", c_uint32),
    ("lineStippleFactor", c_uint32),
    ("lineStipplePattern", c_uint16),
]

VkPipelineRasterizationLineStateCreateInfoKHR._fields_ = [
]

VkPipelineRasterizationLineStateCreateInfoEXT._fields_ = [
]

VkPhysicalDevicePipelineCreationCacheControlFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineCreationCacheControl", c_uint32),
]

VkPhysicalDevicePipelineCreationCacheControlFeaturesEXT._fields_ = [
]

VkPhysicalDeviceVulkan11Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("storageBuffer16BitAccess", c_uint32),
    ("uniformAndStorageBuffer16BitAccess", c_uint32),
    ("storagePushConstant16", c_uint32),
    ("storageInputOutput16", c_uint32),
    ("multiview", c_uint32),
    ("multiviewGeometryShader", c_uint32),
    ("multiviewTessellationShader", c_uint32),
    ("variablePointersStorageBuffer", c_uint32),
    ("variablePointers", c_uint32),
    ("protectedMemory", c_uint32),
    ("samplerYcbcrConversion", c_uint32),
    ("shaderDrawParameters", c_uint32),
]

VkPhysicalDeviceVulkan11Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceUUID", (c_uint8 * VK_UUID_SIZE)),
    ("driverUUID", (c_uint8 * VK_UUID_SIZE)),
    ("deviceLUID", (c_uint8 * VK_LUID_SIZE)),
    ("deviceNodeMask", c_uint32),
    ("deviceLUIDValid", c_uint32),
    ("subgroupSize", c_uint32),
    ("subgroupSupportedStages", c_uint32),
    ("subgroupSupportedOperations", c_uint32),
    ("subgroupQuadOperationsInAllStages", c_uint32),
    ("pointClippingBehavior", c_int32),
    ("maxMultiviewViewCount", c_uint32),
    ("maxMultiviewInstanceIndex", c_uint32),
    ("protectedNoFault", c_uint32),
    ("maxPerSetDescriptors", c_uint32),
    ("maxMemoryAllocationSize", c_uint64),
]

VkPhysicalDeviceVulkan12Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("samplerMirrorClampToEdge", c_uint32),
    ("drawIndirectCount", c_uint32),
    ("storageBuffer8BitAccess", c_uint32),
    ("uniformAndStorageBuffer8BitAccess", c_uint32),
    ("storagePushConstant8", c_uint32),
    ("shaderBufferInt64Atomics", c_uint32),
    ("shaderSharedInt64Atomics", c_uint32),
    ("shaderFloat16", c_uint32),
    ("shaderInt8", c_uint32),
    ("descriptorIndexing", c_uint32),
    ("shaderInputAttachmentArrayDynamicIndexing", c_uint32),
    ("shaderUniformTexelBufferArrayDynamicIndexing", c_uint32),
    ("shaderStorageTexelBufferArrayDynamicIndexing", c_uint32),
    ("shaderUniformBufferArrayNonUniformIndexing", c_uint32),
    ("shaderSampledImageArrayNonUniformIndexing", c_uint32),
    ("shaderStorageBufferArrayNonUniformIndexing", c_uint32),
    ("shaderStorageImageArrayNonUniformIndexing", c_uint32),
    ("shaderInputAttachmentArrayNonUniformIndexing", c_uint32),
    ("shaderUniformTexelBufferArrayNonUniformIndexing", c_uint32),
    ("shaderStorageTexelBufferArrayNonUniformIndexing", c_uint32),
    ("descriptorBindingUniformBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingSampledImageUpdateAfterBind", c_uint32),
    ("descriptorBindingStorageImageUpdateAfterBind", c_uint32),
    ("descriptorBindingStorageBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingUniformTexelBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingStorageTexelBufferUpdateAfterBind", c_uint32),
    ("descriptorBindingUpdateUnusedWhilePending", c_uint32),
    ("descriptorBindingPartiallyBound", c_uint32),
    ("descriptorBindingVariableDescriptorCount", c_uint32),
    ("runtimeDescriptorArray", c_uint32),
    ("samplerFilterMinmax", c_uint32),
    ("scalarBlockLayout", c_uint32),
    ("imagelessFramebuffer", c_uint32),
    ("uniformBufferStandardLayout", c_uint32),
    ("shaderSubgroupExtendedTypes", c_uint32),
    ("separateDepthStencilLayouts", c_uint32),
    ("hostQueryReset", c_uint32),
    ("timelineSemaphore", c_uint32),
    ("bufferDeviceAddress", c_uint32),
    ("bufferDeviceAddressCaptureReplay", c_uint32),
    ("bufferDeviceAddressMultiDevice", c_uint32),
    ("vulkanMemoryModel", c_uint32),
    ("vulkanMemoryModelDeviceScope", c_uint32),
    ("vulkanMemoryModelAvailabilityVisibilityChains", c_uint32),
    ("shaderOutputViewportIndex", c_uint32),
    ("shaderOutputLayer", c_uint32),
    ("subgroupBroadcastDynamicId", c_uint32),
]

VkPhysicalDeviceVulkan12Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("driverID", c_int32),
    ("driverName", (c_char * VK_MAX_DRIVER_NAME_SIZE)),
    ("driverInfo", (c_char * VK_MAX_DRIVER_INFO_SIZE)),
    ("conformanceVersion", VkConformanceVersion),
    ("denormBehaviorIndependence", c_int32),
    ("roundingModeIndependence", c_int32),
    ("shaderSignedZeroInfNanPreserveFloat16", c_uint32),
    ("shaderSignedZeroInfNanPreserveFloat32", c_uint32),
    ("shaderSignedZeroInfNanPreserveFloat64", c_uint32),
    ("shaderDenormPreserveFloat16", c_uint32),
    ("shaderDenormPreserveFloat32", c_uint32),
    ("shaderDenormPreserveFloat64", c_uint32),
    ("shaderDenormFlushToZeroFloat16", c_uint32),
    ("shaderDenormFlushToZeroFloat32", c_uint32),
    ("shaderDenormFlushToZeroFloat64", c_uint32),
    ("shaderRoundingModeRTEFloat16", c_uint32),
    ("shaderRoundingModeRTEFloat32", c_uint32),
    ("shaderRoundingModeRTEFloat64", c_uint32),
    ("shaderRoundingModeRTZFloat16", c_uint32),
    ("shaderRoundingModeRTZFloat32", c_uint32),
    ("shaderRoundingModeRTZFloat64", c_uint32),
    ("maxUpdateAfterBindDescriptorsInAllPools", c_uint32),
    ("shaderUniformBufferArrayNonUniformIndexingNative", c_uint32),
    ("shaderSampledImageArrayNonUniformIndexingNative", c_uint32),
    ("shaderStorageBufferArrayNonUniformIndexingNative", c_uint32),
    ("shaderStorageImageArrayNonUniformIndexingNative", c_uint32),
    ("shaderInputAttachmentArrayNonUniformIndexingNative", c_uint32),
    ("robustBufferAccessUpdateAfterBind", c_uint32),
    ("quadDivergentImplicitLod", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindSamplers", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindUniformBuffers", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindStorageBuffers", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindSampledImages", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindStorageImages", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindInputAttachments", c_uint32),
    ("maxPerStageUpdateAfterBindResources", c_uint32),
    ("maxDescriptorSetUpdateAfterBindSamplers", c_uint32),
    ("maxDescriptorSetUpdateAfterBindUniformBuffers", c_uint32),
    ("maxDescriptorSetUpdateAfterBindUniformBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageBuffers", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageBuffersDynamic", c_uint32),
    ("maxDescriptorSetUpdateAfterBindSampledImages", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageImages", c_uint32),
    ("maxDescriptorSetUpdateAfterBindInputAttachments", c_uint32),
    ("supportedDepthResolveModes", c_uint32),
    ("supportedStencilResolveModes", c_uint32),
    ("independentResolveNone", c_uint32),
    ("independentResolve", c_uint32),
    ("filterMinmaxSingleComponentFormats", c_uint32),
    ("filterMinmaxImageComponentMapping", c_uint32),
    ("maxTimelineSemaphoreValueDifference", c_uint64),
    ("framebufferIntegerColorSampleCounts", c_uint32),
]

VkPhysicalDeviceVulkan13Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("robustImageAccess", c_uint32),
    ("inlineUniformBlock", c_uint32),
    ("descriptorBindingInlineUniformBlockUpdateAfterBind", c_uint32),
    ("pipelineCreationCacheControl", c_uint32),
    ("privateData", c_uint32),
    ("shaderDemoteToHelperInvocation", c_uint32),
    ("shaderTerminateInvocation", c_uint32),
    ("subgroupSizeControl", c_uint32),
    ("computeFullSubgroups", c_uint32),
    ("synchronization2", c_uint32),
    ("textureCompressionASTC_HDR", c_uint32),
    ("shaderZeroInitializeWorkgroupMemory", c_uint32),
    ("dynamicRendering", c_uint32),
    ("shaderIntegerDotProduct", c_uint32),
    ("maintenance4", c_uint32),
]

VkPhysicalDeviceVulkan13Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minSubgroupSize", c_uint32),
    ("maxSubgroupSize", c_uint32),
    ("maxComputeWorkgroupSubgroups", c_uint32),
    ("requiredSubgroupSizeStages", c_uint32),
    ("maxInlineUniformBlockSize", c_uint32),
    ("maxPerStageDescriptorInlineUniformBlocks", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks", c_uint32),
    ("maxDescriptorSetInlineUniformBlocks", c_uint32),
    ("maxDescriptorSetUpdateAfterBindInlineUniformBlocks", c_uint32),
    ("maxInlineUniformTotalSize", c_uint32),
    ("integerDotProduct8BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct8BitSignedAccelerated", c_uint32),
    ("integerDotProduct8BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct4x8BitPackedUnsignedAccelerated", c_uint32),
    ("integerDotProduct4x8BitPackedSignedAccelerated", c_uint32),
    ("integerDotProduct4x8BitPackedMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct16BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct16BitSignedAccelerated", c_uint32),
    ("integerDotProduct16BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct32BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct32BitSignedAccelerated", c_uint32),
    ("integerDotProduct32BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct64BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct64BitSignedAccelerated", c_uint32),
    ("integerDotProduct64BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating8BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating8BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating16BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating16BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating32BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating32BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating64BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating64BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated", c_uint32),
    ("storageTexelBufferOffsetAlignmentBytes", c_uint64),
    ("storageTexelBufferOffsetSingleTexelAlignment", c_uint32),
    ("uniformTexelBufferOffsetAlignmentBytes", c_uint64),
    ("uniformTexelBufferOffsetSingleTexelAlignment", c_uint32),
    ("maxBufferSize", c_uint64),
]

VkPhysicalDeviceVulkan14Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("globalPriorityQuery", c_uint32),
    ("shaderSubgroupRotate", c_uint32),
    ("shaderSubgroupRotateClustered", c_uint32),
    ("shaderFloatControls2", c_uint32),
    ("shaderExpectAssume", c_uint32),
    ("rectangularLines", c_uint32),
    ("bresenhamLines", c_uint32),
    ("smoothLines", c_uint32),
    ("stippledRectangularLines", c_uint32),
    ("stippledBresenhamLines", c_uint32),
    ("stippledSmoothLines", c_uint32),
    ("vertexAttributeInstanceRateDivisor", c_uint32),
    ("vertexAttributeInstanceRateZeroDivisor", c_uint32),
    ("indexTypeUint8", c_uint32),
    ("dynamicRenderingLocalRead", c_uint32),
    ("maintenance5", c_uint32),
    ("maintenance6", c_uint32),
    ("pipelineProtectedAccess", c_uint32),
    ("pipelineRobustness", c_uint32),
    ("hostImageCopy", c_uint32),
    ("pushDescriptor", c_uint32),
]

VkPhysicalDeviceVulkan14Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("lineSubPixelPrecisionBits", c_uint32),
    ("maxVertexAttribDivisor", c_uint32),
    ("supportsNonZeroFirstInstance", c_uint32),
    ("maxPushDescriptors", c_uint32),
    ("dynamicRenderingLocalReadDepthStencilAttachments", c_uint32),
    ("dynamicRenderingLocalReadMultisampledAttachments", c_uint32),
    ("earlyFragmentMultisampleCoverageAfterSampleCounting", c_uint32),
    ("earlyFragmentSampleMaskTestBeforeSampleCounting", c_uint32),
    ("depthStencilSwizzleOneSupport", c_uint32),
    ("polygonModePointSize", c_uint32),
    ("nonStrictSinglePixelWideLinesUseParallelogram", c_uint32),
    ("nonStrictWideLinesUseParallelogram", c_uint32),
    ("blockTexelViewCompatibleMultipleLayers", c_uint32),
    ("maxCombinedImageSamplerDescriptorCount", c_uint32),
    ("fragmentShadingRateClampCombinerInputs", c_uint32),
    ("defaultRobustnessStorageBuffers", c_int32),
    ("defaultRobustnessUniformBuffers", c_int32),
    ("defaultRobustnessVertexInputs", c_int32),
    ("defaultRobustnessImages", c_int32),
    ("copySrcLayoutCount", c_uint32),
    ("pCopySrcLayouts", POINTER(c_int32)),
    ("copyDstLayoutCount", c_uint32),
    ("pCopyDstLayouts", POINTER(c_int32)),
    ("optimalTilingLayoutUUID", (c_uint8 * VK_UUID_SIZE)),
    ("identicalMemoryTypeRequirements", c_uint32),
]

VkPipelineCompilerControlCreateInfoAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("compilerControlFlags", c_uint32),
]

VkPhysicalDeviceCoherentMemoryFeaturesAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceCoherentMemory", c_uint32),
]

VkFaultData._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("faultLevel", c_int32),
    ("faultType", c_int32),
]

VkFaultCallbackInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("faultCount", c_uint32),
    ("pFaults", POINTER(VkFaultData)),
    ("pfnFaultCallback", PFN_vkFaultCallbackFunction),
]

VkPhysicalDeviceToolProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("name", (c_char * VK_MAX_EXTENSION_NAME_SIZE)),
    ("version", (c_char * VK_MAX_EXTENSION_NAME_SIZE)),
    ("purposes", c_uint32),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("layer", (c_char * VK_MAX_EXTENSION_NAME_SIZE)),
]

VkPhysicalDeviceToolPropertiesEXT._fields_ = [
]

VkSamplerCustomBorderColorCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("customBorderColor", VkClearColorValue),
    ("format", c_int32),
]

VkPhysicalDeviceCustomBorderColorPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxCustomBorderColorSamplers", c_uint32),
]

VkPhysicalDeviceCustomBorderColorFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("customBorderColors", c_uint32),
    ("customBorderColorWithoutFormat", c_uint32),
]

VkSamplerBorderColorComponentMappingCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("components", VkComponentMapping),
    ("srgb", c_uint32),
]

VkPhysicalDeviceBorderColorSwizzleFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("borderColorSwizzle", c_uint32),
    ("borderColorSwizzleFromImage", c_uint32),
]

VkDeviceOrHostAddressKHR._fields_ = [
    ("deviceAddress", c_uint64),
    ("hostAddress", c_void_p),
]

VkDeviceOrHostAddressConstKHR._fields_ = [
    ("deviceAddress", c_uint64),
    ("hostAddress", c_void_p),
]

VkDeviceOrHostAddressConstAMDX._fields_ = [
    ("deviceAddress", c_uint64),
    ("hostAddress", c_void_p),
]

VkAccelerationStructureGeometryTrianglesDataKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexFormat", c_int32),
    ("vertexData", VkDeviceOrHostAddressConstKHR),
    ("vertexStride", c_uint64),
    ("maxVertex", c_uint32),
    ("indexType", c_int32),
    ("indexData", VkDeviceOrHostAddressConstKHR),
    ("transformData", VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryAabbsDataKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("data", VkDeviceOrHostAddressConstKHR),
    ("stride", c_uint64),
]

VkAccelerationStructureGeometryInstancesDataKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("arrayOfPointers", c_uint32),
    ("data", VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryLinearSweptSpheresDataNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexFormat", c_int32),
    ("vertexData", VkDeviceOrHostAddressConstKHR),
    ("vertexStride", c_uint64),
    ("radiusFormat", c_int32),
    ("radiusData", VkDeviceOrHostAddressConstKHR),
    ("radiusStride", c_uint64),
    ("indexType", c_int32),
    ("indexData", VkDeviceOrHostAddressConstKHR),
    ("indexStride", c_uint64),
    ("indexingMode", c_int32),
    ("endCapsMode", c_int32),
]

VkAccelerationStructureGeometrySpheresDataNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexFormat", c_int32),
    ("vertexData", VkDeviceOrHostAddressConstKHR),
    ("vertexStride", c_uint64),
    ("radiusFormat", c_int32),
    ("radiusData", VkDeviceOrHostAddressConstKHR),
    ("radiusStride", c_uint64),
    ("indexType", c_int32),
    ("indexData", VkDeviceOrHostAddressConstKHR),
    ("indexStride", c_uint64),
]

VkAccelerationStructureGeometryDataKHR._fields_ = [
    ("triangles", VkAccelerationStructureGeometryTrianglesDataKHR),
    ("aabbs", VkAccelerationStructureGeometryAabbsDataKHR),
    ("instances", VkAccelerationStructureGeometryInstancesDataKHR),
]

VkAccelerationStructureGeometryKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("geometryType", c_int32),
    ("geometry", VkAccelerationStructureGeometryDataKHR),
    ("flags", c_uint32),
]

VkAccelerationStructureBuildGeometryInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("flags", c_uint32),
    ("mode", c_int32),
    ("srcAccelerationStructure", c_void_p),
    ("dstAccelerationStructure", c_void_p),
    ("geometryCount", c_uint32),
    ("pGeometries", POINTER(VkAccelerationStructureGeometryKHR)),
    ("ppGeometries", POINTER(POINTER(VkAccelerationStructureGeometryKHR))),
    ("scratchData", VkDeviceOrHostAddressKHR),
]

VkAccelerationStructureBuildRangeInfoKHR._fields_ = [
    ("primitiveCount", c_uint32),
    ("primitiveOffset", c_uint32),
    ("firstVertex", c_uint32),
    ("transformOffset", c_uint32),
]

VkAccelerationStructureCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("createFlags", c_uint32),
    ("buffer", c_void_p),
    ("offset", c_uint64),
    ("size", c_uint64),
    ("type", c_int32),
    ("deviceAddress", c_uint64),
]

VkAabbPositionsKHR._fields_ = [
    ("minX", c_float),
    ("minY", c_float),
    ("minZ", c_float),
    ("maxX", c_float),
    ("maxY", c_float),
    ("maxZ", c_float),
]

VkAabbPositionsNV._fields_ = [
]

VkTransformMatrixKHR._fields_ = [
    ("matrix", ((c_float * 4) * 3)),
]

VkTransformMatrixNV._fields_ = [
]

VkAccelerationStructureInstanceKHR._fields_ = [
    ("transform", VkTransformMatrixKHR),
    ("instanceCustomIndex", c_uint32),
    ("mask", c_uint32),
    ("instanceShaderBindingTableRecordOffset", c_uint32),
    ("flags", c_uint32),
    ("accelerationStructureReference", c_uint64),
]

VkAccelerationStructureInstanceNV._fields_ = [
]

VkAccelerationStructureDeviceAddressInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructure", c_void_p),
]

VkAccelerationStructureVersionInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pVersionData", POINTER(c_uint8)),
]

VkCopyAccelerationStructureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("src", c_void_p),
    ("dst", c_void_p),
    ("mode", c_int32),
]

VkCopyAccelerationStructureToMemoryInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("src", c_void_p),
    ("dst", VkDeviceOrHostAddressKHR),
    ("mode", c_int32),
]

VkCopyMemoryToAccelerationStructureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("src", VkDeviceOrHostAddressConstKHR),
    ("dst", c_void_p),
    ("mode", c_int32),
]

VkRayTracingPipelineInterfaceCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxPipelineRayPayloadSize", c_uint32),
    ("maxPipelineRayHitAttributeSize", c_uint32),
]

VkPipelineLibraryCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("libraryCount", c_uint32),
    ("pLibraries", POINTER(c_void_p)),
]

VkRefreshObjectKHR._fields_ = [
    ("objectType", c_int32),
    ("objectHandle", c_uint64),
    ("flags", c_uint32),
]

VkRefreshObjectListKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("objectCount", c_uint32),
    ("pObjects", POINTER(VkRefreshObjectKHR)),
]

VkPhysicalDeviceExtendedDynamicStateFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("extendedDynamicState", c_uint32),
]

VkPhysicalDeviceExtendedDynamicState2FeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("extendedDynamicState2", c_uint32),
    ("extendedDynamicState2LogicOp", c_uint32),
    ("extendedDynamicState2PatchControlPoints", c_uint32),
]

VkPhysicalDeviceExtendedDynamicState3FeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("extendedDynamicState3TessellationDomainOrigin", c_uint32),
    ("extendedDynamicState3DepthClampEnable", c_uint32),
    ("extendedDynamicState3PolygonMode", c_uint32),
    ("extendedDynamicState3RasterizationSamples", c_uint32),
    ("extendedDynamicState3SampleMask", c_uint32),
    ("extendedDynamicState3AlphaToCoverageEnable", c_uint32),
    ("extendedDynamicState3AlphaToOneEnable", c_uint32),
    ("extendedDynamicState3LogicOpEnable", c_uint32),
    ("extendedDynamicState3ColorBlendEnable", c_uint32),
    ("extendedDynamicState3ColorBlendEquation", c_uint32),
    ("extendedDynamicState3ColorWriteMask", c_uint32),
    ("extendedDynamicState3RasterizationStream", c_uint32),
    ("extendedDynamicState3ConservativeRasterizationMode", c_uint32),
    ("extendedDynamicState3ExtraPrimitiveOverestimationSize", c_uint32),
    ("extendedDynamicState3DepthClipEnable", c_uint32),
    ("extendedDynamicState3SampleLocationsEnable", c_uint32),
    ("extendedDynamicState3ColorBlendAdvanced", c_uint32),
    ("extendedDynamicState3ProvokingVertexMode", c_uint32),
    ("extendedDynamicState3LineRasterizationMode", c_uint32),
    ("extendedDynamicState3LineStippleEnable", c_uint32),
    ("extendedDynamicState3DepthClipNegativeOneToOne", c_uint32),
    ("extendedDynamicState3ViewportWScalingEnable", c_uint32),
    ("extendedDynamicState3ViewportSwizzle", c_uint32),
    ("extendedDynamicState3CoverageToColorEnable", c_uint32),
    ("extendedDynamicState3CoverageToColorLocation", c_uint32),
    ("extendedDynamicState3CoverageModulationMode", c_uint32),
    ("extendedDynamicState3CoverageModulationTableEnable", c_uint32),
    ("extendedDynamicState3CoverageModulationTable", c_uint32),
    ("extendedDynamicState3CoverageReductionMode", c_uint32),
    ("extendedDynamicState3RepresentativeFragmentTestEnable", c_uint32),
    ("extendedDynamicState3ShadingRateImageEnable", c_uint32),
]

VkPhysicalDeviceExtendedDynamicState3PropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dynamicPrimitiveTopologyUnrestricted", c_uint32),
]

VkColorBlendEquationEXT._fields_ = [
    ("srcColorBlendFactor", c_int32),
    ("dstColorBlendFactor", c_int32),
    ("colorBlendOp", c_int32),
    ("srcAlphaBlendFactor", c_int32),
    ("dstAlphaBlendFactor", c_int32),
    ("alphaBlendOp", c_int32),
]

VkColorBlendAdvancedEXT._fields_ = [
    ("advancedBlendOp", c_int32),
    ("srcPremultiplied", c_uint32),
    ("dstPremultiplied", c_uint32),
    ("blendOverlap", c_int32),
    ("clampResults", c_uint32),
]

VkRenderPassTransformBeginInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("transform", c_int32),
]

VkCopyCommandTransformInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("transform", c_int32),
]

VkCommandBufferInheritanceRenderPassTransformInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("transform", c_int32),
    ("renderArea", VkRect2D),
]

VkPhysicalDevicePartitionedAccelerationStructureFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("partitionedAccelerationStructure", c_uint32),
]

VkPhysicalDevicePartitionedAccelerationStructurePropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxPartitionCount", c_uint32),
]

VkBuildPartitionedAccelerationStructureIndirectCommandNV._fields_ = [
    ("opType", c_int32),
    ("argCount", c_uint32),
    ("argData", VkStridedDeviceAddressNV),
]

VkPartitionedAccelerationStructureFlagsNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("enablePartitionTranslation", c_uint32),
]

VkPartitionedAccelerationStructureWriteInstanceDataNV._fields_ = [
    ("transform", VkTransformMatrixKHR),
    ("explicitAABB", (c_float * 6)),
    ("instanceID", c_uint32),
    ("instanceMask", c_uint32),
    ("instanceContributionToHitGroupIndex", c_uint32),
    ("instanceFlags", c_uint32),
    ("instanceIndex", c_uint32),
    ("partitionIndex", c_uint32),
    ("accelerationStructure", c_uint64),
]

VkPartitionedAccelerationStructureUpdateInstanceDataNV._fields_ = [
    ("instanceIndex", c_uint32),
    ("instanceContributionToHitGroupIndex", c_uint32),
    ("accelerationStructure", c_uint64),
]

VkPartitionedAccelerationStructureWritePartitionTranslationDataNV._fields_ = [
    ("partitionIndex", c_uint32),
    ("partitionTranslation", (c_float * 3)),
]

VkWriteDescriptorSetPartitionedAccelerationStructureNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructureCount", c_uint32),
    ("pAccelerationStructures", POINTER(c_uint64)),
]

VkPartitionedAccelerationStructureInstancesInputNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("instanceCount", c_uint32),
    ("maxInstancePerPartitionCount", c_uint32),
    ("partitionCount", c_uint32),
    ("maxInstanceInGlobalPartitionCount", c_uint32),
]

VkBuildPartitionedAccelerationStructureInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("input", VkPartitionedAccelerationStructureInstancesInputNV),
    ("srcAccelerationStructureData", c_uint64),
    ("dstAccelerationStructureData", c_uint64),
    ("scratchData", c_uint64),
    ("srcInfos", c_uint64),
    ("srcInfosCount", c_uint64),
]

VkPhysicalDeviceDiagnosticsConfigFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("diagnosticsConfig", c_uint32),
]

VkDeviceDiagnosticsConfigCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkPipelineOfflineCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineIdentifier", (c_uint8 * VK_UUID_SIZE)),
    ("matchControl", c_int32),
    ("poolEntrySize", c_uint64),
]

VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderZeroInitializeWorkgroupMemory", c_uint32),
]

VkPhysicalDeviceZeroInitializeWorkgroupMemoryFeaturesKHR._fields_ = [
]

VkPhysicalDeviceShaderSubgroupUniformControlFlowFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSubgroupUniformControlFlow", c_uint32),
]

VkPhysicalDeviceRobustness2FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("robustBufferAccess2", c_uint32),
    ("robustImageAccess2", c_uint32),
    ("nullDescriptor", c_uint32),
]

VkPhysicalDeviceRobustness2FeaturesEXT._fields_ = [
]

VkPhysicalDeviceRobustness2PropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("robustStorageBufferAccessSizeAlignment", c_uint64),
    ("robustUniformBufferAccessSizeAlignment", c_uint64),
]

VkPhysicalDeviceRobustness2PropertiesEXT._fields_ = [
]

VkPhysicalDeviceImageRobustnessFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("robustImageAccess", c_uint32),
]

VkPhysicalDeviceImageRobustnessFeaturesEXT._fields_ = [
]

VkPhysicalDeviceWorkgroupMemoryExplicitLayoutFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("workgroupMemoryExplicitLayout", c_uint32),
    ("workgroupMemoryExplicitLayoutScalarBlockLayout", c_uint32),
    ("workgroupMemoryExplicitLayout8BitAccess", c_uint32),
    ("workgroupMemoryExplicitLayout16BitAccess", c_uint32),
]

VkPhysicalDevicePortabilitySubsetFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("constantAlphaColorBlendFactors", c_uint32),
    ("events", c_uint32),
    ("imageViewFormatReinterpretation", c_uint32),
    ("imageViewFormatSwizzle", c_uint32),
    ("imageView2DOn3DImage", c_uint32),
    ("multisampleArrayImage", c_uint32),
    ("mutableComparisonSamplers", c_uint32),
    ("pointPolygons", c_uint32),
    ("samplerMipLodBias", c_uint32),
    ("separateStencilMaskRef", c_uint32),
    ("shaderSampleRateInterpolationFunctions", c_uint32),
    ("tessellationIsolines", c_uint32),
    ("tessellationPointMode", c_uint32),
    ("triangleFans", c_uint32),
    ("vertexAttributeAccessBeyondStride", c_uint32),
]

VkPhysicalDevicePortabilitySubsetPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minVertexInputBindingStrideAlignment", c_uint32),
]

VkPhysicalDevice4444FormatsFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("formatA4R4G4B4", c_uint32),
    ("formatA4B4G4R4", c_uint32),
]

VkPhysicalDeviceSubpassShadingFeaturesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subpassShading", c_uint32),
]

VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("clustercullingShader", c_uint32),
    ("multiviewClusterCullingShader", c_uint32),
]

VkPhysicalDeviceClusterCullingShaderVrsFeaturesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("clusterShadingRate", c_uint32),
]

VkBufferCopy2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcOffset", c_uint64),
    ("dstOffset", c_uint64),
    ("size", c_uint64),
]

VkBufferCopy2KHR._fields_ = [
]

VkImageCopy2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcSubresource", VkImageSubresourceLayers),
    ("srcOffset", VkOffset3D),
    ("dstSubresource", VkImageSubresourceLayers),
    ("dstOffset", VkOffset3D),
    ("extent", VkExtent3D),
]

VkImageCopy2KHR._fields_ = [
]

VkImageBlit2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcSubresource", VkImageSubresourceLayers),
    ("srcOffsets", (VkOffset3D * 2)),
    ("dstSubresource", VkImageSubresourceLayers),
    ("dstOffsets", (VkOffset3D * 2)),
]

VkImageBlit2KHR._fields_ = [
]

VkBufferImageCopy2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("bufferOffset", c_uint64),
    ("bufferRowLength", c_uint32),
    ("bufferImageHeight", c_uint32),
    ("imageSubresource", VkImageSubresourceLayers),
    ("imageOffset", VkOffset3D),
    ("imageExtent", VkExtent3D),
]

VkBufferImageCopy2KHR._fields_ = [
]

VkImageResolve2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcSubresource", VkImageSubresourceLayers),
    ("srcOffset", VkOffset3D),
    ("dstSubresource", VkImageSubresourceLayers),
    ("dstOffset", VkOffset3D),
    ("extent", VkExtent3D),
]

VkImageResolve2KHR._fields_ = [
]

VkCopyBufferInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcBuffer", c_void_p),
    ("dstBuffer", c_void_p),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkBufferCopy2)),
]

VkCopyBufferInfo2KHR._fields_ = [
]

VkCopyImageInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcImage", c_void_p),
    ("srcImageLayout", c_int32),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkImageCopy2)),
]

VkCopyImageInfo2KHR._fields_ = [
]

VkBlitImageInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcImage", c_void_p),
    ("srcImageLayout", c_int32),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkImageBlit2)),
    ("filter", c_int32),
]

VkBlitImageInfo2KHR._fields_ = [
]

VkCopyBufferToImageInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcBuffer", c_void_p),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkBufferImageCopy2)),
]

VkCopyBufferToImageInfo2KHR._fields_ = [
]

VkCopyImageToBufferInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcImage", c_void_p),
    ("srcImageLayout", c_int32),
    ("dstBuffer", c_void_p),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkBufferImageCopy2)),
]

VkCopyImageToBufferInfo2KHR._fields_ = [
]

VkResolveImageInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcImage", c_void_p),
    ("srcImageLayout", c_int32),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkImageResolve2)),
]

VkResolveImageInfo2KHR._fields_ = [
]

VkPhysicalDeviceShaderImageAtomicInt64FeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderImageInt64Atomics", c_uint32),
    ("sparseImageInt64Atomics", c_uint32),
]

VkFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pFragmentShadingRateAttachment", POINTER(VkAttachmentReference2)),
    ("shadingRateAttachmentTexelSize", VkExtent2D),
]

VkPipelineFragmentShadingRateStateCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentSize", VkExtent2D),
    ("combinerOps", (c_int32 * 2)),
]

VkPhysicalDeviceFragmentShadingRateFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineFragmentShadingRate", c_uint32),
    ("primitiveFragmentShadingRate", c_uint32),
    ("attachmentFragmentShadingRate", c_uint32),
]

VkPhysicalDeviceFragmentShadingRatePropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minFragmentShadingRateAttachmentTexelSize", VkExtent2D),
    ("maxFragmentShadingRateAttachmentTexelSize", VkExtent2D),
    ("maxFragmentShadingRateAttachmentTexelSizeAspectRatio", c_uint32),
    ("primitiveFragmentShadingRateWithMultipleViewports", c_uint32),
    ("layeredShadingRateAttachments", c_uint32),
    ("fragmentShadingRateNonTrivialCombinerOps", c_uint32),
    ("maxFragmentSize", VkExtent2D),
    ("maxFragmentSizeAspectRatio", c_uint32),
    ("maxFragmentShadingRateCoverageSamples", c_uint32),
    ("maxFragmentShadingRateRasterizationSamples", c_int32),
    ("fragmentShadingRateWithShaderDepthStencilWrites", c_uint32),
    ("fragmentShadingRateWithSampleMask", c_uint32),
    ("fragmentShadingRateWithShaderSampleMask", c_uint32),
    ("fragmentShadingRateWithConservativeRasterization", c_uint32),
    ("fragmentShadingRateWithFragmentShaderInterlock", c_uint32),
    ("fragmentShadingRateWithCustomSampleLocations", c_uint32),
    ("fragmentShadingRateStrictMultiplyCombiner", c_uint32),
]

VkPhysicalDeviceFragmentShadingRateKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sampleCounts", c_uint32),
    ("fragmentSize", VkExtent2D),
]

VkPhysicalDeviceShaderTerminateInvocationFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderTerminateInvocation", c_uint32),
]

VkPhysicalDeviceShaderTerminateInvocationFeaturesKHR._fields_ = [
]

VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentShadingRateEnums", c_uint32),
    ("supersampleFragmentShadingRates", c_uint32),
    ("noInvocationFragmentShadingRates", c_uint32),
]

VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxFragmentShadingRateInvocationCount", c_int32),
]

VkPipelineFragmentShadingRateEnumStateCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shadingRateType", c_int32),
    ("shadingRate", c_int32),
    ("combinerOps", (c_int32 * 2)),
]

VkAccelerationStructureBuildSizesInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructureSize", c_uint64),
    ("updateScratchSize", c_uint64),
    ("buildScratchSize", c_uint64),
]

VkPhysicalDeviceImage2DViewOf3DFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image2DViewOf3D", c_uint32),
    ("sampler2DViewOf3D", c_uint32),
]

VkPhysicalDeviceImageSlicedViewOf3DFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageSlicedViewOf3D", c_uint32),
]

VkPhysicalDeviceAttachmentFeedbackLoopDynamicStateFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachmentFeedbackLoopDynamicState", c_uint32),
]

VkPhysicalDeviceLegacyVertexAttributesFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("legacyVertexAttributes", c_uint32),
]

VkPhysicalDeviceLegacyVertexAttributesPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("nativeUnalignedPerformance", c_uint32),
]

VkPhysicalDeviceMutableDescriptorTypeFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mutableDescriptorType", c_uint32),
]

VkPhysicalDeviceMutableDescriptorTypeFeaturesVALVE._fields_ = [
]

VkMutableDescriptorTypeListEXT._fields_ = [
    ("descriptorTypeCount", c_uint32),
    ("pDescriptorTypes", POINTER(c_int32)),
]

VkMutableDescriptorTypeListVALVE._fields_ = [
]

VkMutableDescriptorTypeCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mutableDescriptorTypeListCount", c_uint32),
    ("pMutableDescriptorTypeLists", POINTER(VkMutableDescriptorTypeListEXT)),
]

VkMutableDescriptorTypeCreateInfoVALVE._fields_ = [
]

VkPhysicalDeviceDepthClipControlFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthClipControl", c_uint32),
]

VkPhysicalDeviceZeroInitializeDeviceMemoryFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("zeroInitializeDeviceMemory", c_uint32),
]

VkBeginCustomResolveInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkPhysicalDeviceCustomResolveFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("customResolve", c_uint32),
]

VkCustomResolveCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("customResolve", c_uint32),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentFormats", POINTER(c_int32)),
    ("depthAttachmentFormat", c_int32),
    ("stencilAttachmentFormat", c_int32),
]

VkPhysicalDeviceDeviceGeneratedCommandsFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceGeneratedCommands", c_uint32),
    ("dynamicGeneratedPipelineLayout", c_uint32),
]

VkPhysicalDeviceDeviceGeneratedCommandsPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxIndirectPipelineCount", c_uint32),
    ("maxIndirectShaderObjectCount", c_uint32),
    ("maxIndirectSequenceCount", c_uint32),
    ("maxIndirectCommandsTokenCount", c_uint32),
    ("maxIndirectCommandsTokenOffset", c_uint32),
    ("maxIndirectCommandsIndirectStride", c_uint32),
    ("supportedIndirectCommandsInputModes", c_uint32),
    ("supportedIndirectCommandsShaderStages", c_uint32),
    ("supportedIndirectCommandsShaderStagesPipelineBinding", c_uint32),
    ("supportedIndirectCommandsShaderStagesShaderBinding", c_uint32),
    ("deviceGeneratedCommandsTransformFeedback", c_uint32),
    ("deviceGeneratedCommandsMultiDrawIndirectCount", c_uint32),
]

VkGeneratedCommandsPipelineInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipeline", c_void_p),
]

VkGeneratedCommandsShaderInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderCount", c_uint32),
    ("pShaders", POINTER(c_void_p)),
]

VkGeneratedCommandsMemoryRequirementsInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("indirectExecutionSet", c_void_p),
    ("indirectCommandsLayout", c_void_p),
    ("maxSequenceCount", c_uint32),
    ("maxDrawCount", c_uint32),
]

VkIndirectExecutionSetPipelineInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("initialPipeline", c_void_p),
    ("maxPipelineCount", c_uint32),
]

VkIndirectExecutionSetShaderLayoutInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("setLayoutCount", c_uint32),
    ("pSetLayouts", POINTER(c_void_p)),
]

VkIndirectExecutionSetShaderInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderCount", c_uint32),
    ("pInitialShaders", POINTER(c_void_p)),
    ("pSetLayoutInfos", POINTER(VkIndirectExecutionSetShaderLayoutInfoEXT)),
    ("maxShaderCount", c_uint32),
    ("pushConstantRangeCount", c_uint32),
    ("pPushConstantRanges", POINTER(VkPushConstantRange)),
]

VkIndirectExecutionSetInfoEXT._fields_ = [
    ("pPipelineInfo", POINTER(VkIndirectExecutionSetPipelineInfoEXT)),
    ("pShaderInfo", POINTER(VkIndirectExecutionSetShaderInfoEXT)),
]

VkIndirectExecutionSetCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("info", VkIndirectExecutionSetInfoEXT),
]

VkGeneratedCommandsInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderStages", c_uint32),
    ("indirectExecutionSet", c_void_p),
    ("indirectCommandsLayout", c_void_p),
    ("indirectAddress", c_uint64),
    ("indirectAddressSize", c_uint64),
    ("preprocessAddress", c_uint64),
    ("preprocessSize", c_uint64),
    ("maxSequenceCount", c_uint32),
    ("sequenceCountAddress", c_uint64),
    ("maxDrawCount", c_uint32),
]

VkWriteIndirectExecutionSetPipelineEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("index", c_uint32),
    ("pipeline", c_void_p),
]

VkWriteIndirectExecutionSetShaderEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("index", c_uint32),
    ("shader", c_void_p),
]

VkIndirectCommandsLayoutCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("shaderStages", c_uint32),
    ("indirectStride", c_uint32),
    ("pipelineLayout", c_void_p),
    ("tokenCount", c_uint32),
    ("pTokens", POINTER(VkIndirectCommandsLayoutTokenEXT)),
]

VkIndirectCommandsTokenDataEXT._fields_ = [
    ("pPushConstant", POINTER(VkIndirectCommandsPushConstantTokenEXT)),
    ("pVertexBuffer", POINTER(VkIndirectCommandsVertexBufferTokenEXT)),
    ("pIndexBuffer", POINTER(VkIndirectCommandsIndexBufferTokenEXT)),
    ("pExecutionSet", POINTER(VkIndirectCommandsExecutionSetTokenEXT)),
]

VkIndirectCommandsLayoutTokenEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("data", VkIndirectCommandsTokenDataEXT),
    ("offset", c_uint32),
]

VkDrawIndirectCountIndirectCommandEXT._fields_ = [
    ("bufferAddress", c_uint64),
    ("stride", c_uint32),
    ("commandCount", c_uint32),
]

VkIndirectCommandsVertexBufferTokenEXT._fields_ = [
    ("vertexBindingUnit", c_uint32),
]

VkBindVertexBufferIndirectCommandEXT._fields_ = [
    ("bufferAddress", c_uint64),
    ("size", c_uint32),
    ("stride", c_uint32),
]

VkIndirectCommandsIndexBufferTokenEXT._fields_ = [
    ("mode", c_int32),
]

VkBindIndexBufferIndirectCommandEXT._fields_ = [
    ("bufferAddress", c_uint64),
    ("size", c_uint32),
    ("indexType", c_int32),
]

VkIndirectCommandsPushConstantTokenEXT._fields_ = [
    ("updateRange", VkPushConstantRange),
]

VkIndirectCommandsExecutionSetTokenEXT._fields_ = [
    ("type", c_int32),
    ("shaderStages", c_uint32),
]

VkPipelineViewportDepthClipControlCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("negativeOneToOne", c_uint32),
]

VkPhysicalDeviceDepthClampControlFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthClampControl", c_uint32),
]

VkPipelineViewportDepthClampControlCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthClampMode", c_int32),
    ("pDepthClampRange", POINTER(VkDepthClampRangeEXT)),
]

VkPhysicalDeviceVertexInputDynamicStateFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexInputDynamicState", c_uint32),
]

VkPhysicalDeviceExternalMemoryRDMAFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalMemoryRDMA", c_uint32),
]

VkPhysicalDeviceShaderRelaxedExtendedInstructionFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderRelaxedExtendedInstruction", c_uint32),
]

VkVertexInputBindingDescription2EXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("binding", c_uint32),
    ("stride", c_uint32),
    ("inputRate", c_int32),
    ("divisor", c_uint32),
]

VkVertexInputAttributeDescription2EXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("location", c_uint32),
    ("binding", c_uint32),
    ("format", c_int32),
    ("offset", c_uint32),
]

VkPhysicalDeviceColorWriteEnableFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("colorWriteEnable", c_uint32),
]

VkPipelineColorWriteCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachmentCount", c_uint32),
    ("pColorWriteEnables", POINTER(c_uint32)),
]

VkMemoryBarrier2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcStageMask", c_uint64),
    ("srcAccessMask", c_uint64),
    ("dstStageMask", c_uint64),
    ("dstAccessMask", c_uint64),
]

VkMemoryBarrier2KHR._fields_ = [
]

VkImageMemoryBarrier2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcStageMask", c_uint64),
    ("srcAccessMask", c_uint64),
    ("dstStageMask", c_uint64),
    ("dstAccessMask", c_uint64),
    ("oldLayout", c_int32),
    ("newLayout", c_int32),
    ("srcQueueFamilyIndex", c_uint32),
    ("dstQueueFamilyIndex", c_uint32),
    ("image", c_void_p),
    ("subresourceRange", VkImageSubresourceRange),
]

VkImageMemoryBarrier2KHR._fields_ = [
]

VkBufferMemoryBarrier2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcStageMask", c_uint64),
    ("srcAccessMask", c_uint64),
    ("dstStageMask", c_uint64),
    ("dstAccessMask", c_uint64),
    ("srcQueueFamilyIndex", c_uint32),
    ("dstQueueFamilyIndex", c_uint32),
    ("buffer", c_void_p),
    ("offset", c_uint64),
    ("size", c_uint64),
]

VkBufferMemoryBarrier2KHR._fields_ = [
]

VkMemoryBarrierAccessFlags3KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcAccessMask3", c_uint64),
    ("dstAccessMask3", c_uint64),
]

VkDependencyInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dependencyFlags", c_uint32),
    ("memoryBarrierCount", c_uint32),
    ("pMemoryBarriers", POINTER(VkMemoryBarrier2)),
    ("bufferMemoryBarrierCount", c_uint32),
    ("pBufferMemoryBarriers", POINTER(VkBufferMemoryBarrier2)),
    ("imageMemoryBarrierCount", c_uint32),
    ("pImageMemoryBarriers", POINTER(VkImageMemoryBarrier2)),
]

VkDependencyInfoKHR._fields_ = [
]

VkSemaphoreSubmitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("value", c_uint64),
    ("stageMask", c_uint64),
    ("deviceIndex", c_uint32),
]

VkSemaphoreSubmitInfoKHR._fields_ = [
]

VkCommandBufferSubmitInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("commandBuffer", c_void_p),
    ("deviceMask", c_uint32),
]

VkCommandBufferSubmitInfoKHR._fields_ = [
]

VkSubmitInfo2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("waitSemaphoreInfoCount", c_uint32),
    ("pWaitSemaphoreInfos", POINTER(VkSemaphoreSubmitInfo)),
    ("commandBufferInfoCount", c_uint32),
    ("pCommandBufferInfos", POINTER(VkCommandBufferSubmitInfo)),
    ("signalSemaphoreInfoCount", c_uint32),
    ("pSignalSemaphoreInfos", POINTER(VkSemaphoreSubmitInfo)),
]

VkSubmitInfo2KHR._fields_ = [
]

VkQueueFamilyCheckpointProperties2NV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("checkpointExecutionStageMask", c_uint64),
]

VkCheckpointData2NV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stage", c_uint64),
    ("pCheckpointMarker", c_void_p),
]

VkPhysicalDeviceSynchronization2Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("synchronization2", c_uint32),
]

VkPhysicalDeviceSynchronization2FeaturesKHR._fields_ = [
]

VkPhysicalDeviceUnifiedImageLayoutsFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("unifiedImageLayouts", c_uint32),
    ("unifiedImageLayoutsVideo", c_uint32),
]

VkPhysicalDeviceHostImageCopyFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hostImageCopy", c_uint32),
]

VkPhysicalDeviceHostImageCopyFeaturesEXT._fields_ = [
]

VkPhysicalDeviceHostImageCopyProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("copySrcLayoutCount", c_uint32),
    ("pCopySrcLayouts", POINTER(c_int32)),
    ("copyDstLayoutCount", c_uint32),
    ("pCopyDstLayouts", POINTER(c_int32)),
    ("optimalTilingLayoutUUID", (c_uint8 * VK_UUID_SIZE)),
    ("identicalMemoryTypeRequirements", c_uint32),
]

VkPhysicalDeviceHostImageCopyPropertiesEXT._fields_ = [
]

VkMemoryToImageCopy._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pHostPointer", c_void_p),
    ("memoryRowLength", c_uint32),
    ("memoryImageHeight", c_uint32),
    ("imageSubresource", VkImageSubresourceLayers),
    ("imageOffset", VkOffset3D),
    ("imageExtent", VkExtent3D),
]

VkMemoryToImageCopyEXT._fields_ = [
]

VkImageToMemoryCopy._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pHostPointer", c_void_p),
    ("memoryRowLength", c_uint32),
    ("memoryImageHeight", c_uint32),
    ("imageSubresource", VkImageSubresourceLayers),
    ("imageOffset", VkOffset3D),
    ("imageExtent", VkExtent3D),
]

VkImageToMemoryCopyEXT._fields_ = [
]

VkCopyMemoryToImageInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkMemoryToImageCopy)),
]

VkCopyMemoryToImageInfoEXT._fields_ = [
]

VkCopyImageToMemoryInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("srcImage", c_void_p),
    ("srcImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkImageToMemoryCopy)),
]

VkCopyImageToMemoryInfoEXT._fields_ = [
]

VkCopyImageToImageInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("srcImage", c_void_p),
    ("srcImageLayout", c_int32),
    ("dstImage", c_void_p),
    ("dstImageLayout", c_int32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkImageCopy2)),
]

VkCopyImageToImageInfoEXT._fields_ = [
]

VkHostImageLayoutTransitionInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("oldLayout", c_int32),
    ("newLayout", c_int32),
    ("subresourceRange", VkImageSubresourceRange),
]

VkHostImageLayoutTransitionInfoEXT._fields_ = [
]

VkSubresourceHostMemcpySize._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("size", c_uint64),
]

VkSubresourceHostMemcpySizeEXT._fields_ = [
]

VkHostImageCopyDevicePerformanceQuery._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("optimalDeviceAccess", c_uint32),
    ("identicalMemoryLayout", c_uint32),
]

VkHostImageCopyDevicePerformanceQueryEXT._fields_ = [
]

VkPhysicalDeviceVulkanSC10Properties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceNoDynamicHostAllocations", c_uint32),
    ("deviceDestroyFreesMemory", c_uint32),
    ("commandPoolMultipleCommandBuffersRecording", c_uint32),
    ("commandPoolResetCommandBuffer", c_uint32),
    ("commandBufferSimultaneousUse", c_uint32),
    ("secondaryCommandBufferNullOrImagelessFramebuffer", c_uint32),
    ("recycleDescriptorSetMemory", c_uint32),
    ("recyclePipelineMemory", c_uint32),
    ("maxRenderPassSubpasses", c_uint32),
    ("maxRenderPassDependencies", c_uint32),
    ("maxSubpassInputAttachments", c_uint32),
    ("maxSubpassPreserveAttachments", c_uint32),
    ("maxFramebufferAttachments", c_uint32),
    ("maxDescriptorSetLayoutBindings", c_uint32),
    ("maxQueryFaultCount", c_uint32),
    ("maxCallbackFaultCount", c_uint32),
    ("maxCommandPoolCommandBuffers", c_uint32),
    ("maxCommandBufferSize", c_uint64),
]

VkPipelinePoolSize._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("poolEntrySize", c_uint64),
    ("poolEntryCount", c_uint32),
]

VkDeviceObjectReservationCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineCacheCreateInfoCount", c_uint32),
    ("pPipelineCacheCreateInfos", POINTER(VkPipelineCacheCreateInfo)),
    ("pipelinePoolSizeCount", c_uint32),
    ("pPipelinePoolSizes", POINTER(VkPipelinePoolSize)),
    ("semaphoreRequestCount", c_uint32),
    ("commandBufferRequestCount", c_uint32),
    ("fenceRequestCount", c_uint32),
    ("deviceMemoryRequestCount", c_uint32),
    ("bufferRequestCount", c_uint32),
    ("imageRequestCount", c_uint32),
    ("eventRequestCount", c_uint32),
    ("queryPoolRequestCount", c_uint32),
    ("bufferViewRequestCount", c_uint32),
    ("imageViewRequestCount", c_uint32),
    ("layeredImageViewRequestCount", c_uint32),
    ("pipelineCacheRequestCount", c_uint32),
    ("pipelineLayoutRequestCount", c_uint32),
    ("renderPassRequestCount", c_uint32),
    ("graphicsPipelineRequestCount", c_uint32),
    ("computePipelineRequestCount", c_uint32),
    ("descriptorSetLayoutRequestCount", c_uint32),
    ("samplerRequestCount", c_uint32),
    ("descriptorPoolRequestCount", c_uint32),
    ("descriptorSetRequestCount", c_uint32),
    ("framebufferRequestCount", c_uint32),
    ("commandPoolRequestCount", c_uint32),
    ("samplerYcbcrConversionRequestCount", c_uint32),
    ("surfaceRequestCount", c_uint32),
    ("swapchainRequestCount", c_uint32),
    ("displayModeRequestCount", c_uint32),
    ("subpassDescriptionRequestCount", c_uint32),
    ("attachmentDescriptionRequestCount", c_uint32),
    ("descriptorSetLayoutBindingRequestCount", c_uint32),
    ("descriptorSetLayoutBindingLimit", c_uint32),
    ("maxImageViewMipLevels", c_uint32),
    ("maxImageViewArrayLayers", c_uint32),
    ("maxLayeredImageViewMipLevels", c_uint32),
    ("maxOcclusionQueriesPerPool", c_uint32),
    ("maxPipelineStatisticsQueriesPerPool", c_uint32),
    ("maxTimestampQueriesPerPool", c_uint32),
    ("maxImmutableSamplersPerDescriptorSetLayout", c_uint32),
]

VkCommandPoolMemoryReservationCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("commandPoolReservedSize", c_uint64),
    ("commandPoolMaxCommandBuffers", c_uint32),
]

VkCommandPoolMemoryConsumption._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("commandPoolAllocated", c_uint64),
    ("commandPoolReservedSize", c_uint64),
    ("commandBufferAllocated", c_uint64),
]

VkPhysicalDeviceVulkanSC10Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderAtomicInstructions", c_uint32),
]

VkPhysicalDevicePrimitivesGeneratedQueryFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("primitivesGeneratedQuery", c_uint32),
    ("primitivesGeneratedQueryWithRasterizerDiscard", c_uint32),
    ("primitivesGeneratedQueryWithNonZeroStreams", c_uint32),
]

VkPhysicalDeviceLegacyDitheringFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("legacyDithering", c_uint32),
]

VkPhysicalDeviceMultisampledRenderToSingleSampledFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("multisampledRenderToSingleSampled", c_uint32),
]

VkSurfaceCapabilitiesPresentId2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentId2Supported", c_uint32),
]

VkSurfaceCapabilitiesPresentWait2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentWait2Supported", c_uint32),
]

VkSubpassResolvePerformanceQueryEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("optimal", c_uint32),
]

VkMultisampledRenderToSingleSampledInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("multisampledRenderToSingleSampledEnable", c_uint32),
    ("rasterizationSamples", c_int32),
]

VkPhysicalDevicePipelineProtectedAccessFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineProtectedAccess", c_uint32),
]

VkPhysicalDevicePipelineProtectedAccessFeaturesEXT._fields_ = [
]

VkQueueFamilyVideoPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoCodecOperations", c_uint32),
]

VkQueueFamilyQueryResultStatusPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queryResultStatusSupport", c_uint32),
]

VkVideoProfileListInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("profileCount", c_uint32),
    ("pProfiles", POINTER(VkVideoProfileInfoKHR)),
]

VkPhysicalDeviceVideoFormatInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageUsage", c_uint32),
]

VkVideoFormatPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("componentMapping", VkComponentMapping),
    ("imageCreateFlags", c_uint32),
    ("imageType", c_int32),
    ("imageTiling", c_int32),
    ("imageUsageFlags", c_uint32),
]

VkVideoEncodeQuantizationMapCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxQuantizationMapExtent", VkExtent2D),
]

VkVideoEncodeH264QuantizationMapCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minQpDelta", c_int32),
    ("maxQpDelta", c_int32),
]

VkVideoEncodeH265QuantizationMapCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minQpDelta", c_int32),
    ("maxQpDelta", c_int32),
]

VkVideoEncodeAV1QuantizationMapCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minQIndexDelta", c_int32),
    ("maxQIndexDelta", c_int32),
]

VkVideoFormatQuantizationMapPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("quantizationMapTexelSize", VkExtent2D),
]

VkVideoFormatH265QuantizationMapPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("compatibleCtbSizes", c_uint32),
]

VkVideoFormatAV1QuantizationMapPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("compatibleSuperblockSizes", c_uint32),
]

VkVideoProfileInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoCodecOperation", c_int32),
    ("chromaSubsampling", c_uint32),
    ("lumaBitDepth", c_uint32),
    ("chromaBitDepth", c_uint32),
]

VkVideoCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("minBitstreamBufferOffsetAlignment", c_uint64),
    ("minBitstreamBufferSizeAlignment", c_uint64),
    ("pictureAccessGranularity", VkExtent2D),
    ("minCodedExtent", VkExtent2D),
    ("maxCodedExtent", VkExtent2D),
    ("maxDpbSlots", c_uint32),
    ("maxActiveReferencePictures", c_uint32),
    ("stdHeaderVersion", VkExtensionProperties),
]

VkVideoSessionMemoryRequirementsKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryBindIndex", c_uint32),
    ("memoryRequirements", VkMemoryRequirements),
]

VkBindVideoSessionMemoryInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryBindIndex", c_uint32),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
    ("memorySize", c_uint64),
]

VkVideoPictureResourceInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("codedOffset", VkOffset2D),
    ("codedExtent", VkExtent2D),
    ("baseArrayLayer", c_uint32),
    ("imageViewBinding", c_void_p),
]

VkVideoReferenceSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("slotIndex", c_int32),
    ("pPictureResource", POINTER(VkVideoPictureResourceInfoKHR)),
]

VkVideoDecodeCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkVideoDecodeUsageInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoUsageHints", c_uint32),
]

VkVideoDecodeInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("srcBuffer", c_void_p),
    ("srcBufferOffset", c_uint64),
    ("srcBufferRange", c_uint64),
    ("dstPictureResource", VkVideoPictureResourceInfoKHR),
    ("pSetupReferenceSlot", POINTER(VkVideoReferenceSlotInfoKHR)),
    ("referenceSlotCount", c_uint32),
    ("pReferenceSlots", POINTER(VkVideoReferenceSlotInfoKHR)),
]

VkPhysicalDeviceVideoMaintenance1FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoMaintenance1", c_uint32),
]

VkPhysicalDeviceVideoMaintenance2FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoMaintenance2", c_uint32),
]

VkVideoInlineQueryInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queryPool", c_void_p),
    ("firstQuery", c_uint32),
    ("queryCount", c_uint32),
]

VkVideoDecodeH264SessionParametersAddInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stdSPSCount", c_uint32),
    ("pStdSPSs", POINTER(c_void_p)),
    ("stdPPSCount", c_uint32),
    ("pStdPPSs", POINTER(c_void_p)),
]

VkVideoDecodeH264SessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxStdSPSCount", c_uint32),
    ("maxStdPPSCount", c_uint32),
    ("pParametersAddInfo", POINTER(VkVideoDecodeH264SessionParametersAddInfoKHR)),
]

VkVideoDecodeH264InlineSessionParametersInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdSPS", POINTER(c_void_p)),
    ("pStdPPS", POINTER(c_void_p)),
]

VkVideoDecodeH264PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdPictureInfo", POINTER(c_void_p)),
    ("sliceCount", c_uint32),
    ("pSliceOffsets", POINTER(c_uint32)),
]

VkVideoDecodeH264DpbSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdReferenceInfo", POINTER(c_void_p)),
]

VkVideoDecodeH265SessionParametersAddInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stdVPSCount", c_uint32),
    ("pStdVPSs", POINTER(c_void_p)),
    ("stdSPSCount", c_uint32),
    ("pStdSPSs", POINTER(c_void_p)),
    ("stdPPSCount", c_uint32),
    ("pStdPPSs", POINTER(c_void_p)),
]

VkVideoDecodeH265SessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxStdVPSCount", c_uint32),
    ("maxStdSPSCount", c_uint32),
    ("maxStdPPSCount", c_uint32),
    ("pParametersAddInfo", POINTER(VkVideoDecodeH265SessionParametersAddInfoKHR)),
]

VkVideoDecodeH265InlineSessionParametersInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdVPS", POINTER(c_void_p)),
    ("pStdSPS", POINTER(c_void_p)),
    ("pStdPPS", POINTER(c_void_p)),
]

VkVideoDecodeH265PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdPictureInfo", POINTER(c_void_p)),
    ("sliceSegmentCount", c_uint32),
    ("pSliceSegmentOffsets", POINTER(c_uint32)),
]

VkVideoDecodeH265DpbSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdReferenceInfo", POINTER(c_void_p)),
]

VkPhysicalDeviceVideoDecodeVP9FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoDecodeVP9", c_uint32),
]

VkVideoDecodeVP9PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdPictureInfo", POINTER(c_void_p)),
    ("referenceNameSlotIndices", (c_int32 * VK_MAX_VIDEO_VP9_REFERENCES_PER_FRAME_KHR)),
    ("uncompressedHeaderOffset", c_uint32),
    ("compressedHeaderOffset", c_uint32),
    ("tilesOffset", c_uint32),
]

VkVideoDecodeAV1SessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdSequenceHeader", POINTER(c_void_p)),
]

VkVideoDecodeAV1InlineSessionParametersInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdSequenceHeader", POINTER(c_void_p)),
]

VkVideoDecodeAV1PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdPictureInfo", POINTER(c_void_p)),
    ("referenceNameSlotIndices", (c_int32 * VK_MAX_VIDEO_AV1_REFERENCES_PER_FRAME_KHR)),
    ("frameHeaderOffset", c_uint32),
    ("tileCount", c_uint32),
    ("pTileOffsets", POINTER(c_uint32)),
    ("pTileSizes", POINTER(c_uint32)),
]

VkVideoDecodeAV1DpbSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdReferenceInfo", POINTER(c_void_p)),
]

VkVideoSessionCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queueFamilyIndex", c_uint32),
    ("flags", c_uint32),
    ("pVideoProfile", POINTER(VkVideoProfileInfoKHR)),
    ("pictureFormat", c_int32),
    ("maxCodedExtent", VkExtent2D),
    ("referencePictureFormat", c_int32),
    ("maxDpbSlots", c_uint32),
    ("maxActiveReferencePictures", c_uint32),
    ("pStdHeaderVersion", POINTER(VkExtensionProperties)),
]

VkVideoSessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("videoSessionParametersTemplate", c_void_p),
    ("videoSession", c_void_p),
]

VkVideoSessionParametersUpdateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("updateSequenceCount", c_uint32),
]

VkVideoEncodeSessionParametersGetInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoSessionParameters", c_void_p),
]

VkVideoEncodeSessionParametersFeedbackInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hasOverrides", c_uint32),
]

VkVideoBeginCodingInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("videoSession", c_void_p),
    ("videoSessionParameters", c_void_p),
    ("referenceSlotCount", c_uint32),
    ("pReferenceSlots", POINTER(VkVideoReferenceSlotInfoKHR)),
]

VkVideoEndCodingInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkVideoCodingControlInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkVideoEncodeUsageInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoUsageHints", c_uint32),
    ("videoContentHints", c_uint32),
    ("tuningMode", c_int32),
]

VkVideoEncodeInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("dstBuffer", c_void_p),
    ("dstBufferOffset", c_uint64),
    ("dstBufferRange", c_uint64),
    ("srcPictureResource", VkVideoPictureResourceInfoKHR),
    ("pSetupReferenceSlot", POINTER(VkVideoReferenceSlotInfoKHR)),
    ("referenceSlotCount", c_uint32),
    ("pReferenceSlots", POINTER(VkVideoReferenceSlotInfoKHR)),
    ("precedingExternallyEncodedBytes", c_uint32),
]

VkVideoEncodeQuantizationMapInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("quantizationMap", c_void_p),
    ("quantizationMapExtent", VkExtent2D),
]

VkVideoEncodeQuantizationMapSessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("quantizationMapTexelSize", VkExtent2D),
]

VkPhysicalDeviceVideoEncodeQuantizationMapFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoEncodeQuantizationMap", c_uint32),
]

VkQueryPoolVideoEncodeFeedbackCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("encodeFeedbackFlags", c_uint32),
]

VkVideoEncodeQualityLevelInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("qualityLevel", c_uint32),
]

VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pVideoProfile", POINTER(VkVideoProfileInfoKHR)),
    ("qualityLevel", c_uint32),
]

VkVideoEncodeQualityLevelPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("preferredRateControlMode", c_int32),
    ("preferredRateControlLayerCount", c_uint32),
]

VkVideoEncodeRateControlInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("rateControlMode", c_int32),
    ("layerCount", c_uint32),
    ("pLayers", POINTER(VkVideoEncodeRateControlLayerInfoKHR)),
    ("virtualBufferSizeInMs", c_uint32),
    ("initialVirtualBufferSizeInMs", c_uint32),
]

VkVideoEncodeRateControlLayerInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("averageBitrate", c_uint64),
    ("maxBitrate", c_uint64),
    ("frameRateNumerator", c_uint32),
    ("frameRateDenominator", c_uint32),
]

VkVideoEncodeCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("rateControlModes", c_uint32),
    ("maxRateControlLayers", c_uint32),
    ("maxBitrate", c_uint64),
    ("maxQualityLevels", c_uint32),
    ("encodeInputPictureGranularity", VkExtent2D),
    ("supportedEncodeFeedbackFlags", c_uint32),
]

VkVideoEncodeH264QpKHR._fields_ = [
    ("qpI", c_int32),
    ("qpP", c_int32),
    ("qpB", c_int32),
]

VkVideoEncodeH264QualityLevelPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("preferredRateControlFlags", c_uint32),
    ("preferredGopFrameCount", c_uint32),
    ("preferredIdrPeriod", c_uint32),
    ("preferredConsecutiveBFrameCount", c_uint32),
    ("preferredTemporalLayerCount", c_uint32),
    ("preferredConstantQp", VkVideoEncodeH264QpKHR),
    ("preferredMaxL0ReferenceCount", c_uint32),
    ("preferredMaxL1ReferenceCount", c_uint32),
    ("preferredStdEntropyCodingModeFlag", c_uint32),
]

VkVideoEncodeH264SessionParametersAddInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stdSPSCount", c_uint32),
    ("pStdSPSs", POINTER(c_void_p)),
    ("stdPPSCount", c_uint32),
    ("pStdPPSs", POINTER(c_void_p)),
]

VkVideoEncodeH264SessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxStdSPSCount", c_uint32),
    ("maxStdPPSCount", c_uint32),
    ("pParametersAddInfo", POINTER(VkVideoEncodeH264SessionParametersAddInfoKHR)),
]

VkVideoEncodeH264SessionParametersGetInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("writeStdSPS", c_uint32),
    ("writeStdPPS", c_uint32),
    ("stdSPSId", c_uint32),
    ("stdPPSId", c_uint32),
]

VkVideoEncodeH264SessionParametersFeedbackInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hasStdSPSOverrides", c_uint32),
    ("hasStdPPSOverrides", c_uint32),
]

VkVideoEncodeH264DpbSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdReferenceInfo", POINTER(c_void_p)),
]

VkVideoEncodeH264PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("naluSliceEntryCount", c_uint32),
    ("pNaluSliceEntries", POINTER(VkVideoEncodeH264NaluSliceInfoKHR)),
    ("pStdPictureInfo", POINTER(c_void_p)),
    ("generatePrefixNalu", c_uint32),
]

VkVideoEncodeH264NaluSliceInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("constantQp", c_int32),
    ("pStdSliceHeader", POINTER(c_void_p)),
]

VkVideoEncodeH264RateControlInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("gopFrameCount", c_uint32),
    ("idrPeriod", c_uint32),
    ("consecutiveBFrameCount", c_uint32),
    ("temporalLayerCount", c_uint32),
]

VkVideoEncodeH264FrameSizeKHR._fields_ = [
    ("frameISize", c_uint32),
    ("framePSize", c_uint32),
    ("frameBSize", c_uint32),
]

VkVideoEncodeH264GopRemainingFrameInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("useGopRemainingFrames", c_uint32),
    ("gopRemainingI", c_uint32),
    ("gopRemainingP", c_uint32),
    ("gopRemainingB", c_uint32),
]

VkVideoEncodeH264RateControlLayerInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("useMinQp", c_uint32),
    ("minQp", VkVideoEncodeH264QpKHR),
    ("useMaxQp", c_uint32),
    ("maxQp", VkVideoEncodeH264QpKHR),
    ("useMaxFrameSize", c_uint32),
    ("maxFrameSize", VkVideoEncodeH264FrameSizeKHR),
]

VkVideoEncodeH265QpKHR._fields_ = [
    ("qpI", c_int32),
    ("qpP", c_int32),
    ("qpB", c_int32),
]

VkVideoEncodeH265QualityLevelPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("preferredRateControlFlags", c_uint32),
    ("preferredGopFrameCount", c_uint32),
    ("preferredIdrPeriod", c_uint32),
    ("preferredConsecutiveBFrameCount", c_uint32),
    ("preferredSubLayerCount", c_uint32),
    ("preferredConstantQp", VkVideoEncodeH265QpKHR),
    ("preferredMaxL0ReferenceCount", c_uint32),
    ("preferredMaxL1ReferenceCount", c_uint32),
]

VkVideoEncodeH265SessionParametersAddInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stdVPSCount", c_uint32),
    ("pStdVPSs", POINTER(c_void_p)),
    ("stdSPSCount", c_uint32),
    ("pStdSPSs", POINTER(c_void_p)),
    ("stdPPSCount", c_uint32),
    ("pStdPPSs", POINTER(c_void_p)),
]

VkVideoEncodeH265SessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxStdVPSCount", c_uint32),
    ("maxStdSPSCount", c_uint32),
    ("maxStdPPSCount", c_uint32),
    ("pParametersAddInfo", POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR)),
]

VkVideoEncodeH265SessionParametersGetInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("writeStdVPS", c_uint32),
    ("writeStdSPS", c_uint32),
    ("writeStdPPS", c_uint32),
    ("stdVPSId", c_uint32),
    ("stdSPSId", c_uint32),
    ("stdPPSId", c_uint32),
]

VkVideoEncodeH265SessionParametersFeedbackInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hasStdVPSOverrides", c_uint32),
    ("hasStdSPSOverrides", c_uint32),
    ("hasStdPPSOverrides", c_uint32),
]

VkVideoEncodeH265PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("naluSliceSegmentEntryCount", c_uint32),
    ("pNaluSliceSegmentEntries", POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR)),
    ("pStdPictureInfo", POINTER(c_void_p)),
]

VkVideoEncodeH265NaluSliceSegmentInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("constantQp", c_int32),
    ("pStdSliceSegmentHeader", POINTER(c_void_p)),
]

VkVideoEncodeH265RateControlInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("gopFrameCount", c_uint32),
    ("idrPeriod", c_uint32),
    ("consecutiveBFrameCount", c_uint32),
    ("subLayerCount", c_uint32),
]

VkVideoEncodeH265FrameSizeKHR._fields_ = [
    ("frameISize", c_uint32),
    ("framePSize", c_uint32),
    ("frameBSize", c_uint32),
]

VkVideoEncodeH265GopRemainingFrameInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("useGopRemainingFrames", c_uint32),
    ("gopRemainingI", c_uint32),
    ("gopRemainingP", c_uint32),
    ("gopRemainingB", c_uint32),
]

VkVideoEncodeH265RateControlLayerInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("useMinQp", c_uint32),
    ("minQp", VkVideoEncodeH265QpKHR),
    ("useMaxQp", c_uint32),
    ("maxQp", VkVideoEncodeH265QpKHR),
    ("useMaxFrameSize", c_uint32),
    ("maxFrameSize", VkVideoEncodeH265FrameSizeKHR),
]

VkVideoEncodeH265DpbSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdReferenceInfo", POINTER(c_void_p)),
]

VkVideoEncodeAV1QIndexKHR._fields_ = [
    ("intraQIndex", c_uint32),
    ("predictiveQIndex", c_uint32),
    ("bipredictiveQIndex", c_uint32),
]

VkVideoEncodeAV1QualityLevelPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("preferredRateControlFlags", c_uint32),
    ("preferredGopFrameCount", c_uint32),
    ("preferredKeyFramePeriod", c_uint32),
    ("preferredConsecutiveBipredictiveFrameCount", c_uint32),
    ("preferredTemporalLayerCount", c_uint32),
    ("preferredConstantQIndex", VkVideoEncodeAV1QIndexKHR),
    ("preferredMaxSingleReferenceCount", c_uint32),
    ("preferredSingleReferenceNameMask", c_uint32),
    ("preferredMaxUnidirectionalCompoundReferenceCount", c_uint32),
    ("preferredMaxUnidirectionalCompoundGroup1ReferenceCount", c_uint32),
    ("preferredUnidirectionalCompoundReferenceNameMask", c_uint32),
    ("preferredMaxBidirectionalCompoundReferenceCount", c_uint32),
    ("preferredMaxBidirectionalCompoundGroup1ReferenceCount", c_uint32),
    ("preferredMaxBidirectionalCompoundGroup2ReferenceCount", c_uint32),
    ("preferredBidirectionalCompoundReferenceNameMask", c_uint32),
]

VkPhysicalDeviceVideoEncodeAV1FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoEncodeAV1", c_uint32),
]

VkVideoEncodeAV1SessionParametersCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdSequenceHeader", POINTER(c_void_p)),
    ("pStdDecoderModelInfo", POINTER(c_void_p)),
    ("stdOperatingPointCount", c_uint32),
    ("pStdOperatingPoints", POINTER(c_void_p)),
]

VkVideoEncodeAV1DpbSlotInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pStdReferenceInfo", POINTER(c_void_p)),
]

VkVideoEncodeAV1PictureInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("predictionMode", c_int32),
    ("rateControlGroup", c_int32),
    ("constantQIndex", c_uint32),
    ("pStdPictureInfo", POINTER(c_void_p)),
    ("referenceNameSlotIndices", (c_int32 * VK_MAX_VIDEO_AV1_REFERENCES_PER_FRAME_KHR)),
    ("primaryReferenceCdfOnly", c_uint32),
    ("generateObuExtensionHeader", c_uint32),
]

VkVideoEncodeAV1RateControlInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("gopFrameCount", c_uint32),
    ("keyFramePeriod", c_uint32),
    ("consecutiveBipredictiveFrameCount", c_uint32),
    ("temporalLayerCount", c_uint32),
]

VkVideoEncodeAV1FrameSizeKHR._fields_ = [
    ("intraFrameSize", c_uint32),
    ("predictiveFrameSize", c_uint32),
    ("bipredictiveFrameSize", c_uint32),
]

VkVideoEncodeAV1GopRemainingFrameInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("useGopRemainingFrames", c_uint32),
    ("gopRemainingIntra", c_uint32),
    ("gopRemainingPredictive", c_uint32),
    ("gopRemainingBipredictive", c_uint32),
]

VkVideoEncodeAV1RateControlLayerInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("useMinQIndex", c_uint32),
    ("minQIndex", VkVideoEncodeAV1QIndexKHR),
    ("useMaxQIndex", c_uint32),
    ("maxQIndex", VkVideoEncodeAV1QIndexKHR),
    ("useMaxFrameSize", c_uint32),
    ("maxFrameSize", VkVideoEncodeAV1FrameSizeKHR),
]

VkPhysicalDeviceInheritedViewportScissorFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("inheritedViewportScissor2D", c_uint32),
]

VkCommandBufferInheritanceViewportScissorInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("viewportScissor2D", c_uint32),
    ("viewportDepthCount", c_uint32),
    ("pViewportDepths", POINTER(VkViewport)),
]

VkPhysicalDeviceYcbcr2Plane444FormatsFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("ycbcr2plane444Formats", c_uint32),
]

VkPhysicalDeviceProvokingVertexFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("provokingVertexLast", c_uint32),
    ("transformFeedbackPreservesProvokingVertex", c_uint32),
]

VkPhysicalDeviceProvokingVertexPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("provokingVertexModePerPipeline", c_uint32),
    ("transformFeedbackPreservesTriangleFanProvokingVertex", c_uint32),
]

VkPipelineRasterizationProvokingVertexStateCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("provokingVertexMode", c_int32),
]

VkVideoEncodeIntraRefreshCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("intraRefreshModes", c_uint32),
    ("maxIntraRefreshCycleDuration", c_uint32),
    ("maxIntraRefreshActiveReferencePictures", c_uint32),
    ("partitionIndependentIntraRefreshRegions", c_uint32),
    ("nonRectangularIntraRefreshRegions", c_uint32),
]

VkVideoEncodeSessionIntraRefreshCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("intraRefreshMode", c_int32),
]

VkVideoEncodeIntraRefreshInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("intraRefreshCycleDuration", c_uint32),
    ("intraRefreshIndex", c_uint32),
]

VkVideoReferenceIntraRefreshInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dirtyIntraRefreshRegions", c_uint32),
]

VkPhysicalDeviceVideoEncodeIntraRefreshFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoEncodeIntraRefresh", c_uint32),
]

VkCuModuleCreateInfoNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataSize", c_size_t),
    ("pData", c_void_p),
]

VkCuModuleTexturingModeCreateInfoNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("use64bitTexturing", c_uint32),
]

VkCuFunctionCreateInfoNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("module", c_void_p),
    ("pName", c_char_p),
]

VkCuLaunchInfoNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("function", c_void_p),
    ("gridDimX", c_uint32),
    ("gridDimY", c_uint32),
    ("gridDimZ", c_uint32),
    ("blockDimX", c_uint32),
    ("blockDimY", c_uint32),
    ("blockDimZ", c_uint32),
    ("sharedMemBytes", c_uint32),
    ("paramCount", c_size_t),
    ("pParams", POINTER(c_void_p)),
    ("extraCount", c_size_t),
    ("pExtras", POINTER(c_void_p)),
]

VkPhysicalDeviceDescriptorBufferFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorBuffer", c_uint32),
    ("descriptorBufferCaptureReplay", c_uint32),
    ("descriptorBufferImageLayoutIgnored", c_uint32),
    ("descriptorBufferPushDescriptors", c_uint32),
]

VkPhysicalDeviceDescriptorBufferPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("combinedImageSamplerDescriptorSingleArray", c_uint32),
    ("bufferlessPushDescriptors", c_uint32),
    ("allowSamplerImageViewPostSubmitCreation", c_uint32),
    ("descriptorBufferOffsetAlignment", c_uint64),
    ("maxDescriptorBufferBindings", c_uint32),
    ("maxResourceDescriptorBufferBindings", c_uint32),
    ("maxSamplerDescriptorBufferBindings", c_uint32),
    ("maxEmbeddedImmutableSamplerBindings", c_uint32),
    ("maxEmbeddedImmutableSamplers", c_uint32),
    ("bufferCaptureReplayDescriptorDataSize", c_size_t),
    ("imageCaptureReplayDescriptorDataSize", c_size_t),
    ("imageViewCaptureReplayDescriptorDataSize", c_size_t),
    ("samplerCaptureReplayDescriptorDataSize", c_size_t),
    ("accelerationStructureCaptureReplayDescriptorDataSize", c_size_t),
    ("samplerDescriptorSize", c_size_t),
    ("combinedImageSamplerDescriptorSize", c_size_t),
    ("sampledImageDescriptorSize", c_size_t),
    ("storageImageDescriptorSize", c_size_t),
    ("uniformTexelBufferDescriptorSize", c_size_t),
    ("robustUniformTexelBufferDescriptorSize", c_size_t),
    ("storageTexelBufferDescriptorSize", c_size_t),
    ("robustStorageTexelBufferDescriptorSize", c_size_t),
    ("uniformBufferDescriptorSize", c_size_t),
    ("robustUniformBufferDescriptorSize", c_size_t),
    ("storageBufferDescriptorSize", c_size_t),
    ("robustStorageBufferDescriptorSize", c_size_t),
    ("inputAttachmentDescriptorSize", c_size_t),
    ("accelerationStructureDescriptorSize", c_size_t),
    ("maxSamplerDescriptorBufferRange", c_uint64),
    ("maxResourceDescriptorBufferRange", c_uint64),
    ("samplerDescriptorBufferAddressSpaceSize", c_uint64),
    ("resourceDescriptorBufferAddressSpaceSize", c_uint64),
    ("descriptorBufferAddressSpaceSize", c_uint64),
]

VkPhysicalDeviceDescriptorBufferDensityMapPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("combinedImageSamplerDensityMapDescriptorSize", c_size_t),
]

VkDescriptorAddressInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("address", c_uint64),
    ("range", c_uint64),
    ("format", c_int32),
]

VkDescriptorBufferBindingInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("address", c_uint64),
    ("usage", c_uint32),
]

VkDescriptorBufferBindingPushDescriptorBufferHandleEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", c_void_p),
]

VkDescriptorDataEXT._fields_ = [
    ("pSampler", POINTER(c_void_p)),
    ("pCombinedImageSampler", POINTER(VkDescriptorImageInfo)),
    ("pInputAttachmentImage", POINTER(VkDescriptorImageInfo)),
    ("pSampledImage", POINTER(VkDescriptorImageInfo)),
    ("pStorageImage", POINTER(VkDescriptorImageInfo)),
    ("pUniformTexelBuffer", POINTER(VkDescriptorAddressInfoEXT)),
    ("pStorageTexelBuffer", POINTER(VkDescriptorAddressInfoEXT)),
    ("pUniformBuffer", POINTER(VkDescriptorAddressInfoEXT)),
    ("pStorageBuffer", POINTER(VkDescriptorAddressInfoEXT)),
    ("accelerationStructure", c_uint64),
]

VkDescriptorGetInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("data", VkDescriptorDataEXT),
]

VkBufferCaptureDescriptorDataInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", c_void_p),
]

VkImageCaptureDescriptorDataInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
]

VkImageViewCaptureDescriptorDataInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageView", c_void_p),
]

VkSamplerCaptureDescriptorDataInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sampler", c_void_p),
]

VkAccelerationStructureCaptureDescriptorDataInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("accelerationStructure", c_void_p),
    ("accelerationStructureNV", c_void_p),
]

VkOpaqueCaptureDescriptorDataCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("opaqueCaptureDescriptorData", c_void_p),
]

VkPhysicalDeviceShaderIntegerDotProductFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderIntegerDotProduct", c_uint32),
]

VkPhysicalDeviceShaderIntegerDotProductFeaturesKHR._fields_ = [
]

VkPhysicalDeviceShaderIntegerDotProductProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("integerDotProduct8BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct8BitSignedAccelerated", c_uint32),
    ("integerDotProduct8BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct4x8BitPackedUnsignedAccelerated", c_uint32),
    ("integerDotProduct4x8BitPackedSignedAccelerated", c_uint32),
    ("integerDotProduct4x8BitPackedMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct16BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct16BitSignedAccelerated", c_uint32),
    ("integerDotProduct16BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct32BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct32BitSignedAccelerated", c_uint32),
    ("integerDotProduct32BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProduct64BitUnsignedAccelerated", c_uint32),
    ("integerDotProduct64BitSignedAccelerated", c_uint32),
    ("integerDotProduct64BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating8BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating8BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating8BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating4x8BitPackedUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating4x8BitPackedSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating4x8BitPackedMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating16BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating16BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating16BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating32BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating32BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating32BitMixedSignednessAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating64BitUnsignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating64BitSignedAccelerated", c_uint32),
    ("integerDotProductAccumulatingSaturating64BitMixedSignednessAccelerated", c_uint32),
]

VkPhysicalDeviceShaderIntegerDotProductPropertiesKHR._fields_ = [
]

VkPhysicalDeviceDrmPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hasPrimary", c_uint32),
    ("hasRender", c_uint32),
    ("primaryMajor", c_int64),
    ("primaryMinor", c_int64),
    ("renderMajor", c_int64),
    ("renderMinor", c_int64),
]

VkPhysicalDeviceFragmentShaderBarycentricFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentShaderBarycentric", c_uint32),
]

VkPhysicalDeviceFragmentShaderBarycentricPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("triStripVertexOrderIndependentOfProvokingVertex", c_uint32),
]

VkPhysicalDeviceShaderFmaFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderFmaFloat16", c_uint32),
    ("shaderFmaFloat32", c_uint32),
    ("shaderFmaFloat64", c_uint32),
]

VkPhysicalDeviceRayTracingMotionBlurFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingMotionBlur", c_uint32),
    ("rayTracingMotionBlurPipelineTraceRaysIndirect", c_uint32),
]

VkPhysicalDeviceRayTracingValidationFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingValidation", c_uint32),
]

VkPhysicalDeviceRayTracingLinearSweptSpheresFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("spheres", c_uint32),
    ("linearSweptSpheres", c_uint32),
]

VkAccelerationStructureGeometryMotionTrianglesDataNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexData", VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureMotionInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxInstances", c_uint32),
    ("flags", c_uint32),
]

VkSRTDataNV._fields_ = [
    ("sx", c_float),
    ("a", c_float),
    ("b", c_float),
    ("pvx", c_float),
    ("sy", c_float),
    ("c", c_float),
    ("pvy", c_float),
    ("sz", c_float),
    ("pvz", c_float),
    ("qx", c_float),
    ("qy", c_float),
    ("qz", c_float),
    ("qw", c_float),
    ("tx", c_float),
    ("ty", c_float),
    ("tz", c_float),
]

VkAccelerationStructureSRTMotionInstanceNV._fields_ = [
    ("transformT0", VkSRTDataNV),
    ("transformT1", VkSRTDataNV),
    ("instanceCustomIndex", c_uint32),
    ("mask", c_uint32),
    ("instanceShaderBindingTableRecordOffset", c_uint32),
    ("flags", c_uint32),
    ("accelerationStructureReference", c_uint64),
]

VkAccelerationStructureMatrixMotionInstanceNV._fields_ = [
    ("transformT0", VkTransformMatrixKHR),
    ("transformT1", VkTransformMatrixKHR),
    ("instanceCustomIndex", c_uint32),
    ("mask", c_uint32),
    ("instanceShaderBindingTableRecordOffset", c_uint32),
    ("flags", c_uint32),
    ("accelerationStructureReference", c_uint64),
]

VkAccelerationStructureMotionInstanceDataNV._fields_ = [
    ("staticInstance", VkAccelerationStructureInstanceKHR),
    ("matrixMotionInstance", VkAccelerationStructureMatrixMotionInstanceNV),
    ("srtMotionInstance", VkAccelerationStructureSRTMotionInstanceNV),
]

VkAccelerationStructureMotionInstanceNV._fields_ = [
    ("type", c_int32),
    ("flags", c_uint32),
    ("data", VkAccelerationStructureMotionInstanceDataNV),
]

VkMemoryGetRemoteAddressInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("handleType", c_int32),
]

VkImportMemoryBufferCollectionFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("collection", c_void_p),
    ("index", c_uint32),
]

VkBufferCollectionImageCreateInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("collection", c_void_p),
    ("index", c_uint32),
]

VkBufferCollectionBufferCreateInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("collection", c_void_p),
    ("index", c_uint32),
]

VkBufferCollectionCreateInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("collectionToken", c_uint32),
]

VkSysmemColorSpaceFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("colorSpace", c_uint32),
]

VkBufferCollectionPropertiesFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryTypeBits", c_uint32),
    ("bufferCount", c_uint32),
    ("createInfoIndex", c_uint32),
    ("sysmemPixelFormat", c_uint64),
    ("formatFeatures", c_uint32),
    ("sysmemColorSpaceIndex", VkSysmemColorSpaceFUCHSIA),
    ("samplerYcbcrConversionComponents", VkComponentMapping),
    ("suggestedYcbcrModel", c_int32),
    ("suggestedYcbcrRange", c_int32),
    ("suggestedXChromaOffset", c_int32),
    ("suggestedYChromaOffset", c_int32),
]

VkBufferCollectionConstraintsInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minBufferCount", c_uint32),
    ("maxBufferCount", c_uint32),
    ("minBufferCountForCamping", c_uint32),
    ("minBufferCountForDedicatedSlack", c_uint32),
    ("minBufferCountForSharedSlack", c_uint32),
]

VkBufferConstraintsInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("createInfo", VkBufferCreateInfo),
    ("requiredFormatFeatures", c_uint32),
    ("bufferCollectionConstraints", VkBufferCollectionConstraintsInfoFUCHSIA),
]

VkImageFormatConstraintsInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageCreateInfo", VkImageCreateInfo),
    ("requiredFormatFeatures", c_uint32),
    ("flags", c_uint32),
    ("sysmemPixelFormat", c_uint64),
    ("colorSpaceCount", c_uint32),
    ("pColorSpaces", POINTER(VkSysmemColorSpaceFUCHSIA)),
]

VkImageConstraintsInfoFUCHSIA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("formatConstraintsCount", c_uint32),
    ("pFormatConstraints", POINTER(VkImageFormatConstraintsInfoFUCHSIA)),
    ("bufferCollectionConstraints", VkBufferCollectionConstraintsInfoFUCHSIA),
    ("flags", c_uint32),
]

VkCudaModuleCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataSize", c_size_t),
    ("pData", c_void_p),
]

VkCudaFunctionCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("module", c_void_p),
    ("pName", c_char_p),
]

VkCudaLaunchInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("function", c_void_p),
    ("gridDimX", c_uint32),
    ("gridDimY", c_uint32),
    ("gridDimZ", c_uint32),
    ("blockDimX", c_uint32),
    ("blockDimY", c_uint32),
    ("blockDimZ", c_uint32),
    ("sharedMemBytes", c_uint32),
    ("paramCount", c_size_t),
    ("pParams", POINTER(c_void_p)),
    ("extraCount", c_size_t),
    ("pExtras", POINTER(c_void_p)),
]

VkPhysicalDeviceRGBA10X6FormatsFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("formatRgba10x6WithoutYCbCrSampler", c_uint32),
]

VkFormatProperties3._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("linearTilingFeatures", c_uint64),
    ("optimalTilingFeatures", c_uint64),
    ("bufferFeatures", c_uint64),
]

VkFormatProperties3KHR._fields_ = [
]

VkDrmFormatModifierPropertiesList2EXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("drmFormatModifierCount", c_uint32),
    ("pDrmFormatModifierProperties", POINTER(VkDrmFormatModifierProperties2EXT)),
]

VkDrmFormatModifierProperties2EXT._fields_ = [
    ("drmFormatModifier", c_uint64),
    ("drmFormatModifierPlaneCount", c_uint32),
    ("drmFormatModifierTilingFeatures", c_uint64),
]

VkAndroidHardwareBufferFormatProperties2ANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("externalFormat", c_uint64),
    ("formatFeatures", c_uint64),
    ("samplerYcbcrConversionComponents", VkComponentMapping),
    ("suggestedYcbcrModel", c_int32),
    ("suggestedYcbcrRange", c_int32),
    ("suggestedXChromaOffset", c_int32),
    ("suggestedYChromaOffset", c_int32),
]

VkPipelineRenderingCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("viewMask", c_uint32),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentFormats", POINTER(c_int32)),
    ("depthAttachmentFormat", c_int32),
    ("stencilAttachmentFormat", c_int32),
]

VkPipelineRenderingCreateInfoKHR._fields_ = [
]

VkRenderingInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("renderArea", VkRect2D),
    ("layerCount", c_uint32),
    ("viewMask", c_uint32),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachments", POINTER(VkRenderingAttachmentInfo)),
    ("pDepthAttachment", POINTER(VkRenderingAttachmentInfo)),
    ("pStencilAttachment", POINTER(VkRenderingAttachmentInfo)),
]

VkRenderingInfoKHR._fields_ = [
]

VkRenderingEndInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkRenderingEndInfoEXT._fields_ = [
]

VkRenderingAttachmentInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageView", c_void_p),
    ("imageLayout", c_int32),
    ("resolveMode", c_int32),
    ("resolveImageView", c_void_p),
    ("resolveImageLayout", c_int32),
    ("loadOp", c_int32),
    ("storeOp", c_int32),
    ("clearValue", VkClearValue),
]

VkRenderingAttachmentInfoKHR._fields_ = [
]

VkRenderingFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageView", c_void_p),
    ("imageLayout", c_int32),
    ("shadingRateAttachmentTexelSize", VkExtent2D),
]

VkRenderingFragmentDensityMapAttachmentInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageView", c_void_p),
    ("imageLayout", c_int32),
]

VkPhysicalDeviceDynamicRenderingFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dynamicRendering", c_uint32),
]

VkPhysicalDeviceDynamicRenderingFeaturesKHR._fields_ = [
]

VkCommandBufferInheritanceRenderingInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("viewMask", c_uint32),
    ("colorAttachmentCount", c_uint32),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentFormats", POINTER(c_int32)),
    ("depthAttachmentFormat", c_int32),
    ("stencilAttachmentFormat", c_int32),
    ("rasterizationSamples", c_int32),
]

VkCommandBufferInheritanceRenderingInfoKHR._fields_ = [
]

VkAttachmentSampleCountInfoAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentSamples", POINTER(c_int32)),
    ("depthStencilAttachmentSamples", c_int32),
]

VkAttachmentSampleCountInfoNV._fields_ = [
]

VkMultiviewPerViewAttributesInfoNVX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("perViewAttributes", c_uint32),
    ("perViewAttributesPositionXOnly", c_uint32),
]

VkPhysicalDeviceImageViewMinLodFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minLod", c_uint32),
]

VkImageViewMinLodCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minLod", c_float),
]

VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rasterizationOrderColorAttachmentAccess", c_uint32),
    ("rasterizationOrderDepthAttachmentAccess", c_uint32),
    ("rasterizationOrderStencilAttachmentAccess", c_uint32),
]

VkPhysicalDeviceRasterizationOrderAttachmentAccessFeaturesARM._fields_ = [
]

VkPhysicalDeviceLinearColorAttachmentFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("linearColorAttachment", c_uint32),
]

VkPhysicalDeviceGraphicsPipelineLibraryFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("graphicsPipelineLibrary", c_uint32),
]

VkPhysicalDevicePipelineBinaryFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBinaries", c_uint32),
]

VkDevicePipelineBinaryInternalCacheControlKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("disableInternalCache", c_uint32),
]

VkPhysicalDevicePipelineBinaryPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineBinaryInternalCache", c_uint32),
    ("pipelineBinaryInternalCacheControl", c_uint32),
    ("pipelineBinaryPrefersInternalCache", c_uint32),
    ("pipelineBinaryPrecompiledInternalCache", c_uint32),
    ("pipelineBinaryCompressedData", c_uint32),
]

VkPhysicalDeviceGraphicsPipelineLibraryPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("graphicsPipelineLibraryFastLinking", c_uint32),
    ("graphicsPipelineLibraryIndependentInterpolationDecoration", c_uint32),
]

VkGraphicsPipelineLibraryCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkPhysicalDeviceDataGraphNeuralAcceleratorStatisticsFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataGraphNeuralAcceleratorStatistics", c_uint32),
]

VkDataGraphPipelineNeuralStatisticsCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allowNeuralStatistics", c_uint32),
]

VkDataGraphPipelineSessionNeuralStatisticsCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mode", c_int32),
]

VkPhysicalDeviceDescriptorSetHostMappingFeaturesVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorSetHostMapping", c_uint32),
]

VkDescriptorSetBindingReferenceVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorSetLayout", c_void_p),
    ("binding", c_uint32),
]

VkDescriptorSetLayoutHostMappingInfoVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorOffset", c_size_t),
    ("descriptorSize", c_uint32),
]

VkPhysicalDeviceNestedCommandBufferFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("nestedCommandBuffer", c_uint32),
    ("nestedCommandBufferRendering", c_uint32),
    ("nestedCommandBufferSimultaneousUse", c_uint32),
]

VkPhysicalDeviceNestedCommandBufferPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxCommandBufferNestingLevel", c_uint32),
]

VkPhysicalDeviceShaderModuleIdentifierFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderModuleIdentifier", c_uint32),
]

VkPhysicalDeviceShaderModuleIdentifierPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderModuleIdentifierAlgorithmUUID", (c_uint8 * VK_UUID_SIZE)),
]

VkPipelineShaderStageModuleIdentifierCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("identifierSize", c_uint32),
    ("pIdentifier", POINTER(c_uint8)),
]

VkShaderModuleIdentifierEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("identifierSize", c_uint32),
    ("identifier", (c_uint8 * VK_MAX_SHADER_MODULE_IDENTIFIER_SIZE_EXT)),
]

VkImageCompressionControlEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("compressionControlPlaneCount", c_uint32),
    ("pFixedRateFlags", POINTER(c_uint32)),
]

VkPhysicalDeviceImageCompressionControlFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageCompressionControl", c_uint32),
]

VkImageCompressionPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageCompressionFlags", c_uint32),
    ("imageCompressionFixedRateFlags", c_uint32),
]

VkPhysicalDeviceImageCompressionControlSwapchainFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageCompressionControlSwapchain", c_uint32),
]

VkImageSubresource2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageSubresource", VkImageSubresource),
]

VkImageSubresource2KHR._fields_ = [
]

VkImageSubresource2EXT._fields_ = [
]

VkSubresourceLayout2._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subresourceLayout", VkSubresourceLayout),
]

VkSubresourceLayout2KHR._fields_ = [
]

VkSubresourceLayout2EXT._fields_ = [
]

VkRenderPassCreationControlEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("disallowMerging", c_uint32),
]

VkRenderPassCreationFeedbackInfoEXT._fields_ = [
    ("postMergeSubpassCount", c_uint32),
]

VkRenderPassCreationFeedbackCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pRenderPassFeedback", POINTER(VkRenderPassCreationFeedbackInfoEXT)),
]

VkRenderPassSubpassFeedbackInfoEXT._fields_ = [
    ("subpassMergeStatus", c_int32),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("postMergeIndex", c_uint32),
]

VkRenderPassSubpassFeedbackCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pSubpassFeedback", POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]

VkPhysicalDeviceSubpassMergeFeedbackFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subpassMergeFeedback", c_uint32),
]

VkMicromapBuildInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("flags", c_uint32),
    ("mode", c_int32),
    ("dstMicromap", c_void_p),
    ("usageCountsCount", c_uint32),
    ("pUsageCounts", POINTER(VkMicromapUsageEXT)),
    ("ppUsageCounts", POINTER(POINTER(VkMicromapUsageEXT))),
    ("data", VkDeviceOrHostAddressConstKHR),
    ("scratchData", VkDeviceOrHostAddressKHR),
    ("triangleArray", VkDeviceOrHostAddressConstKHR),
    ("triangleArrayStride", c_uint64),
]

VkMicromapCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("createFlags", c_uint32),
    ("buffer", c_void_p),
    ("offset", c_uint64),
    ("size", c_uint64),
    ("type", c_int32),
    ("deviceAddress", c_uint64),
]

VkMicromapVersionInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pVersionData", POINTER(c_uint8)),
]

VkCopyMicromapInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("src", c_void_p),
    ("dst", c_void_p),
    ("mode", c_int32),
]

VkCopyMicromapToMemoryInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("src", c_void_p),
    ("dst", VkDeviceOrHostAddressKHR),
    ("mode", c_int32),
]

VkCopyMemoryToMicromapInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("src", VkDeviceOrHostAddressConstKHR),
    ("dst", c_void_p),
    ("mode", c_int32),
]

VkMicromapBuildSizesInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("micromapSize", c_uint64),
    ("buildScratchSize", c_uint64),
    ("discardable", c_uint32),
]

VkMicromapUsageEXT._fields_ = [
    ("count", c_uint32),
    ("subdivisionLevel", c_uint32),
    ("format", c_uint32),
]

VkMicromapTriangleEXT._fields_ = [
    ("dataOffset", c_uint32),
    ("subdivisionLevel", c_uint16),
    ("format", c_uint16),
]

VkPhysicalDeviceOpacityMicromapFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("micromap", c_uint32),
    ("micromapCaptureReplay", c_uint32),
    ("micromapHostCommands", c_uint32),
]

VkPhysicalDeviceOpacityMicromapPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxOpacity2StateSubdivisionLevel", c_uint32),
    ("maxOpacity4StateSubdivisionLevel", c_uint32),
]

VkAccelerationStructureTrianglesOpacityMicromapEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("indexType", c_int32),
    ("indexBuffer", VkDeviceOrHostAddressConstKHR),
    ("indexStride", c_uint64),
    ("baseTriangle", c_uint32),
    ("usageCountsCount", c_uint32),
    ("pUsageCounts", POINTER(VkMicromapUsageEXT)),
    ("ppUsageCounts", POINTER(POINTER(VkMicromapUsageEXT))),
    ("micromap", c_void_p),
]

VkPhysicalDeviceDisplacementMicromapFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displacementMicromap", c_uint32),
]

VkPhysicalDeviceDisplacementMicromapPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxDisplacementMicromapSubdivisionLevel", c_uint32),
]

VkAccelerationStructureTrianglesDisplacementMicromapNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("displacementBiasAndScaleFormat", c_int32),
    ("displacementVectorFormat", c_int32),
    ("displacementBiasAndScaleBuffer", VkDeviceOrHostAddressConstKHR),
    ("displacementBiasAndScaleStride", c_uint64),
    ("displacementVectorBuffer", VkDeviceOrHostAddressConstKHR),
    ("displacementVectorStride", c_uint64),
    ("displacedMicromapPrimitiveFlags", VkDeviceOrHostAddressConstKHR),
    ("displacedMicromapPrimitiveFlagsStride", c_uint64),
    ("indexType", c_int32),
    ("indexBuffer", VkDeviceOrHostAddressConstKHR),
    ("indexStride", c_uint64),
    ("baseTriangle", c_uint32),
    ("usageCountsCount", c_uint32),
    ("pUsageCounts", POINTER(VkMicromapUsageEXT)),
    ("ppUsageCounts", POINTER(POINTER(VkMicromapUsageEXT))),
    ("micromap", c_void_p),
]

VkPipelinePropertiesIdentifierEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineIdentifier", (c_uint8 * VK_UUID_SIZE)),
]

VkPhysicalDevicePipelinePropertiesFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelinePropertiesIdentifier", c_uint32),
]

VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderEarlyAndLateFragmentTests", c_uint32),
]

VkExternalMemoryAcquireUnmodifiedEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("acquireUnmodifiedMemory", c_uint32),
]

VkExportMetalObjectCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("exportObjectType", c_int32),
]

VkExportMetalObjectsInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkExportMetalDeviceInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mtlDevice", c_void_p),
]

VkExportMetalCommandQueueInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queue", c_void_p),
    ("mtlCommandQueue", c_void_p),
]

VkExportMetalBufferInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
    ("mtlBuffer", c_void_p),
]

VkImportMetalBufferInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mtlBuffer", c_void_p),
]

VkExportMetalTextureInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("imageView", c_void_p),
    ("bufferView", c_void_p),
    ("plane", c_int32),
    ("mtlTexture", c_void_p),
]

VkImportMetalTextureInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("plane", c_int32),
    ("mtlTexture", c_void_p),
]

VkExportMetalIOSurfaceInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("ioSurface", c_void_p),
]

VkImportMetalIOSurfaceInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("ioSurface", c_void_p),
]

VkExportMetalSharedEventInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("semaphore", c_void_p),
    ("event", c_void_p),
    ("mtlSharedEvent", c_void_p),
]

VkImportMetalSharedEventInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mtlSharedEvent", c_void_p),
]

VkPhysicalDeviceNonSeamlessCubeMapFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("nonSeamlessCubeMap", c_uint32),
]

VkPhysicalDevicePipelineRobustnessFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineRobustness", c_uint32),
]

VkPhysicalDevicePipelineRobustnessFeaturesEXT._fields_ = [
]

VkPipelineRobustnessCreateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("storageBuffers", c_int32),
    ("uniformBuffers", c_int32),
    ("vertexInputs", c_int32),
    ("images", c_int32),
]

VkPipelineRobustnessCreateInfoEXT._fields_ = [
]

VkPhysicalDevicePipelineRobustnessProperties._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("defaultRobustnessStorageBuffers", c_int32),
    ("defaultRobustnessUniformBuffers", c_int32),
    ("defaultRobustnessVertexInputs", c_int32),
    ("defaultRobustnessImages", c_int32),
]

VkPhysicalDevicePipelineRobustnessPropertiesEXT._fields_ = [
]

VkImageViewSampleWeightCreateInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("filterCenter", VkOffset2D),
    ("filterSize", VkExtent2D),
    ("numPhases", c_uint32),
]

VkPhysicalDeviceImageProcessingFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("textureSampleWeighted", c_uint32),
    ("textureBoxFilter", c_uint32),
    ("textureBlockMatch", c_uint32),
]

VkPhysicalDeviceImageProcessingPropertiesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxWeightFilterPhases", c_uint32),
    ("maxWeightFilterDimension", VkExtent2D),
    ("maxBlockMatchRegion", VkExtent2D),
    ("maxBoxFilterBlockSize", VkExtent2D),
]

VkPhysicalDeviceTilePropertiesFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tileProperties", c_uint32),
]

VkTilePropertiesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tileSize", VkExtent3D),
    ("apronSize", VkExtent2D),
    ("origin", VkOffset2D),
]

VkTileMemoryBindInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
]

VkPhysicalDeviceAmigoProfilingFeaturesSEC._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("amigoProfiling", c_uint32),
]

VkAmigoProfilingSubmitInfoSEC._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("firstDrawTimestamp", c_uint64),
    ("swapBufferTimestamp", c_uint64),
]

VkPhysicalDeviceAttachmentFeedbackLoopLayoutFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("attachmentFeedbackLoopLayout", c_uint32),
]

VkPhysicalDeviceDepthClampZeroOneFeaturesEXT._fields_ = [
]

VkAttachmentFeedbackLoopInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("feedbackLoopEnable", c_uint32),
]

VkPhysicalDeviceAddressBindingReportFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("reportAddressBinding", c_uint32),
]

VkRenderingAttachmentFlagsInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
]

VkResolveImageModeInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("resolveMode", c_int32),
    ("stencilResolveMode", c_int32),
]

VkDeviceAddressBindingCallbackDataEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("baseAddress", c_uint64),
    ("size", c_uint64),
    ("bindingType", c_int32),
]

VkPhysicalDeviceOpticalFlowFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("opticalFlow", c_uint32),
]

VkPhysicalDeviceOpticalFlowPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedOutputGridSizes", c_uint32),
    ("supportedHintGridSizes", c_uint32),
    ("hintSupported", c_uint32),
    ("costSupported", c_uint32),
    ("bidirectionalFlowSupported", c_uint32),
    ("globalFlowSupported", c_uint32),
    ("minWidth", c_uint32),
    ("minHeight", c_uint32),
    ("maxWidth", c_uint32),
    ("maxHeight", c_uint32),
    ("maxNumRegionsOfInterest", c_uint32),
]

VkOpticalFlowImageFormatInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("usage", c_uint32),
]

VkOpticalFlowImageFormatPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
]

VkOpticalFlowSessionCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("width", c_uint32),
    ("height", c_uint32),
    ("imageFormat", c_int32),
    ("flowVectorFormat", c_int32),
    ("costFormat", c_int32),
    ("outputGridSize", c_uint32),
    ("hintGridSize", c_uint32),
    ("performanceLevel", c_int32),
    ("flags", c_uint32),
]

VkOpticalFlowSessionCreatePrivateDataInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("id", c_uint32),
    ("size", c_uint32),
    ("pPrivateData", c_void_p),
]

VkOpticalFlowExecuteInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkRect2D)),
]

VkPhysicalDeviceFaultFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceFault", c_uint32),
    ("deviceFaultVendorBinary", c_uint32),
]

VkDeviceFaultAddressInfoKHR._fields_ = [
    ("addressType", c_int32),
    ("reportedAddress", c_uint64),
    ("addressPrecision", c_uint64),
]

VkDeviceFaultAddressInfoEXT._fields_ = [
]

VkDeviceFaultVendorInfoKHR._fields_ = [
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("vendorFaultCode", c_uint64),
    ("vendorFaultData", c_uint64),
]

VkDeviceFaultVendorInfoEXT._fields_ = [
]

VkDeviceFaultInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("groupId", c_uint64),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("faultAddressInfo", VkDeviceFaultAddressInfoKHR),
    ("instructionAddressInfo", VkDeviceFaultAddressInfoKHR),
    ("vendorInfo", VkDeviceFaultVendorInfoKHR),
]

VkDeviceFaultDebugInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vendorBinarySize", c_uint32),
    ("pVendorBinaryData", c_void_p),
]

VkDeviceFaultCountsEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressInfoCount", c_uint32),
    ("vendorInfoCount", c_uint32),
    ("vendorBinarySize", c_uint64),
]

VkDeviceFaultInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("pAddressInfos", POINTER(VkDeviceFaultAddressInfoKHR)),
    ("pVendorInfos", POINTER(VkDeviceFaultVendorInfoKHR)),
    ("pVendorBinaryData", c_void_p),
]

VkDeviceFaultVendorBinaryHeaderVersionOneKHR._fields_ = [
    ("headerSize", c_uint32),
    ("headerVersion", c_int32),
    ("vendorID", c_uint32),
    ("deviceID", c_uint32),
    ("driverVersion", c_uint32),
    ("pipelineCacheUUID", (c_uint8 * VK_UUID_SIZE)),
    ("applicationNameOffset", c_uint32),
    ("applicationVersion", c_uint32),
    ("engineNameOffset", c_uint32),
    ("engineVersion", c_uint32),
    ("apiVersion", c_uint32),
]

VkDeviceFaultVendorBinaryHeaderVersionOneEXT._fields_ = [
]

VkPhysicalDeviceFaultFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceFault", c_uint32),
    ("deviceFaultVendorBinary", c_uint32),
    ("deviceFaultReportMasked", c_uint32),
    ("deviceFaultDeviceLostOnMasked", c_uint32),
]

VkPhysicalDeviceFaultPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxDeviceFaultCount", c_uint32),
]

VkPhysicalDevicePipelineLibraryGroupHandlesFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineLibraryGroupHandles", c_uint32),
]

VkDepthBiasInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthBiasConstantFactor", c_float),
    ("depthBiasClamp", c_float),
    ("depthBiasSlopeFactor", c_float),
]

VkDepthBiasRepresentationInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthBiasRepresentation", c_int32),
    ("depthBiasExact", c_uint32),
]

VkDecompressMemoryRegionNV._fields_ = [
    ("srcAddress", c_uint64),
    ("dstAddress", c_uint64),
    ("compressedSize", c_uint64),
    ("decompressedSize", c_uint64),
    ("decompressionMethod", c_uint64),
]

VkDecompressMemoryRegionEXT._fields_ = [
    ("srcAddress", c_uint64),
    ("dstAddress", c_uint64),
    ("compressedSize", c_uint64),
    ("decompressedSize", c_uint64),
]

VkDecompressMemoryInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("decompressionMethod", c_uint64),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkDecompressMemoryRegionEXT)),
]

VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderCoreMask", c_uint64),
    ("shaderCoreCount", c_uint32),
    ("shaderWarpsPerCore", c_uint32),
]

VkPhysicalDeviceShaderCoreBuiltinsFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderCoreBuiltins", c_uint32),
]

VkFrameBoundaryEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("frameID", c_uint64),
    ("imageCount", c_uint32),
    ("pImages", POINTER(c_void_p)),
    ("bufferCount", c_uint32),
    ("pBuffers", POINTER(c_void_p)),
    ("tagName", c_uint64),
    ("tagSize", c_size_t),
    ("pTag", c_void_p),
]

VkPhysicalDeviceFrameBoundaryFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("frameBoundary", c_uint32),
]

VkPhysicalDeviceDynamicRenderingUnusedAttachmentsFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dynamicRenderingUnusedAttachments", c_uint32),
]

VkPhysicalDeviceInternallySynchronizedQueuesFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("internallySynchronizedQueues", c_uint32),
]

VkSurfacePresentModeKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentMode", c_int32),
]

VkSurfacePresentModeEXT._fields_ = [
]

VkSurfacePresentScalingCapabilitiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedPresentScaling", c_uint32),
    ("supportedPresentGravityX", c_uint32),
    ("supportedPresentGravityY", c_uint32),
    ("minScaledImageExtent", VkExtent2D),
    ("maxScaledImageExtent", VkExtent2D),
]

VkSurfacePresentScalingCapabilitiesEXT._fields_ = [
]

VkSurfacePresentModeCompatibilityKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentModeCount", c_uint32),
    ("pPresentModes", POINTER(c_int32)),
]

VkSurfacePresentModeCompatibilityEXT._fields_ = [
]

VkPhysicalDeviceSwapchainMaintenance1FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainMaintenance1", c_uint32),
]

VkPhysicalDeviceSwapchainMaintenance1FeaturesEXT._fields_ = [
]

VkSwapchainPresentFenceInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pFences", POINTER(c_void_p)),
]

VkSwapchainPresentFenceInfoEXT._fields_ = [
]

VkSwapchainPresentModesCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentModeCount", c_uint32),
    ("pPresentModes", POINTER(c_int32)),
]

VkSwapchainPresentModesCreateInfoEXT._fields_ = [
]

VkSwapchainPresentModeInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchainCount", c_uint32),
    ("pPresentModes", POINTER(c_int32)),
]

VkSwapchainPresentModeInfoEXT._fields_ = [
]

VkSwapchainPresentScalingCreateInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("scalingBehavior", c_uint32),
    ("presentGravityX", c_uint32),
    ("presentGravityY", c_uint32),
]

VkSwapchainPresentScalingCreateInfoEXT._fields_ = [
]

VkReleaseSwapchainImagesInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("swapchain", c_void_p),
    ("imageIndexCount", c_uint32),
    ("pImageIndices", POINTER(c_uint32)),
]

VkReleaseSwapchainImagesInfoEXT._fields_ = [
]

VkPhysicalDeviceDepthBiasControlFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthBiasControl", c_uint32),
    ("leastRepresentableValueForceUnormRepresentation", c_uint32),
    ("floatRepresentation", c_uint32),
    ("depthBiasExact", c_uint32),
]

VkPhysicalDeviceRayTracingInvocationReorderFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingInvocationReorder", c_uint32),
]

VkPhysicalDeviceRayTracingInvocationReorderFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingInvocationReorder", c_uint32),
]

VkPhysicalDeviceRayTracingInvocationReorderPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingInvocationReorderReorderingHint", c_int32),
    ("maxShaderBindingTableRecordIndex", c_uint32),
]

VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingInvocationReorderReorderingHint", c_int32),
]

VkPhysicalDeviceExtendedSparseAddressSpaceFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("extendedSparseAddressSpace", c_uint32),
]

VkPhysicalDeviceExtendedSparseAddressSpacePropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("extendedSparseAddressSpaceSize", c_uint64),
    ("extendedSparseImageUsageFlags", c_uint32),
    ("extendedSparseBufferUsageFlags", c_uint32),
]

VkDirectDriverLoadingInfoLUNARG._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("pfnGetInstanceProcAddr", PFN_vkGetInstanceProcAddrLUNARG),
]

VkDirectDriverLoadingListLUNARG._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mode", c_int32),
    ("driverCount", c_uint32),
    ("pDrivers", POINTER(VkDirectDriverLoadingInfoLUNARG)),
]

VkPhysicalDeviceMultiviewPerViewViewportsFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("multiviewPerViewViewports", c_uint32),
]

VkPhysicalDeviceRayTracingPositionFetchFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rayTracingPositionFetch", c_uint32),
]

VkDeviceImageSubresourceInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pCreateInfo", POINTER(VkImageCreateInfo)),
    ("pSubresource", POINTER(VkImageSubresource2)),
]

VkDeviceImageSubresourceInfoKHR._fields_ = [
]

VkPhysicalDeviceShaderCorePropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pixelRate", c_uint32),
    ("texelRate", c_uint32),
    ("fmaRate", c_uint32),
]

VkPhysicalDeviceMultiviewPerViewRenderAreasFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("multiviewPerViewRenderAreas", c_uint32),
]

VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("perViewRenderAreaCount", c_uint32),
    ("pPerViewRenderAreas", POINTER(VkRect2D)),
]

VkQueryLowLatencySupportNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pQueriedLowLatencyData", c_void_p),
]

VkMemoryMapInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("memory", c_void_p),
    ("offset", c_uint64),
    ("size", c_uint64),
]

VkMemoryMapInfoKHR._fields_ = [
]

VkMemoryUnmapInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("memory", c_void_p),
]

VkMemoryUnmapInfoKHR._fields_ = [
]

VkPhysicalDeviceShaderObjectFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderObject", c_uint32),
]

VkPhysicalDeviceShaderObjectPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderBinaryUUID", (c_uint8 * VK_UUID_SIZE)),
    ("shaderBinaryVersion", c_uint32),
]

VkShaderCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stage", c_int32),
    ("nextStage", c_uint32),
    ("codeType", c_int32),
    ("codeSize", c_size_t),
    ("pCode", c_void_p),
    ("pName", c_char_p),
    ("setLayoutCount", c_uint32),
    ("pSetLayouts", POINTER(c_void_p)),
    ("pushConstantRangeCount", c_uint32),
    ("pPushConstantRanges", POINTER(VkPushConstantRange)),
    ("pSpecializationInfo", POINTER(VkSpecializationInfo)),
]

VkPhysicalDeviceShaderTileImageFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderTileImageColorReadAccess", c_uint32),
    ("shaderTileImageDepthReadAccess", c_uint32),
    ("shaderTileImageStencilReadAccess", c_uint32),
]

VkPhysicalDeviceShaderTileImagePropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderTileImageCoherentReadAccelerated", c_uint32),
    ("shaderTileImageReadSampleFromPixelRateInvocation", c_uint32),
    ("shaderTileImageReadFromHelperInvocation", c_uint32),
]

VkImportScreenBufferInfoQNX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", POINTER(c_void_p)),
]

VkScreenBufferPropertiesQNX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allocationSize", c_uint64),
    ("memoryTypeBits", c_uint32),
]

VkScreenBufferFormatPropertiesQNX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("externalFormat", c_uint64),
    ("screenUsage", c_uint64),
    ("formatFeatures", c_uint32),
    ("samplerYcbcrConversionComponents", VkComponentMapping),
    ("suggestedYcbcrModel", c_int32),
    ("suggestedYcbcrRange", c_int32),
    ("suggestedXChromaOffset", c_int32),
    ("suggestedYChromaOffset", c_int32),
]

VkExternalFormatQNX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalFormat", c_uint64),
]

VkPhysicalDeviceExternalMemoryScreenBufferFeaturesQNX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("screenBufferImport", c_uint32),
]

VkPhysicalDeviceCooperativeMatrixFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrix", c_uint32),
    ("cooperativeMatrixRobustBufferAccess", c_uint32),
]

VkCooperativeMatrixPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("MSize", c_uint32),
    ("NSize", c_uint32),
    ("KSize", c_uint32),
    ("AType", c_int32),
    ("BType", c_int32),
    ("CType", c_int32),
    ("ResultType", c_int32),
    ("saturatingAccumulation", c_uint32),
    ("scope", c_int32),
]

VkPhysicalDeviceCooperativeMatrixPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrixSupportedStages", c_uint32),
]

VkPhysicalDeviceCooperativeMatrixConversionFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrixConversion", c_uint32),
]

VkPhysicalDeviceShaderEnqueuePropertiesAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxExecutionGraphDepth", c_uint32),
    ("maxExecutionGraphShaderOutputNodes", c_uint32),
    ("maxExecutionGraphShaderPayloadSize", c_uint32),
    ("maxExecutionGraphShaderPayloadCount", c_uint32),
    ("executionGraphDispatchAddressAlignment", c_uint32),
    ("maxExecutionGraphWorkgroupCount", (c_uint32 * 3)),
    ("maxExecutionGraphWorkgroups", c_uint32),
]

VkPhysicalDeviceShaderEnqueueFeaturesAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderEnqueue", c_uint32),
    ("shaderMeshEnqueue", c_uint32),
]

VkExecutionGraphPipelineCreateInfoAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("stageCount", c_uint32),
    ("pStages", POINTER(VkPipelineShaderStageCreateInfo)),
    ("pLibraryInfo", POINTER(VkPipelineLibraryCreateInfoKHR)),
    ("layout", c_void_p),
    ("basePipelineHandle", c_void_p),
    ("basePipelineIndex", c_int32),
]

VkPipelineShaderStageNodeCreateInfoAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pName", c_char_p),
    ("index", c_uint32),
]

VkExecutionGraphPipelineScratchSizeAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minSize", c_uint64),
    ("maxSize", c_uint64),
    ("sizeGranularity", c_uint64),
]

VkDispatchGraphInfoAMDX._fields_ = [
    ("nodeIndex", c_uint32),
    ("payloadCount", c_uint32),
    ("payloads", VkDeviceOrHostAddressConstAMDX),
    ("payloadStride", c_uint64),
]

VkDispatchGraphCountInfoAMDX._fields_ = [
    ("count", c_uint32),
    ("infos", VkDeviceOrHostAddressConstAMDX),
    ("stride", c_uint64),
]

VkPhysicalDeviceAntiLagFeaturesAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("antiLag", c_uint32),
]

VkAntiLagDataAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mode", c_int32),
    ("maxFPS", c_uint32),
    ("pPresentationInfo", POINTER(VkAntiLagPresentationInfoAMD)),
]

VkAntiLagPresentationInfoAMD._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stage", c_int32),
    ("frameIndex", c_uint64),
]

VkBindMemoryStatus._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pResult", POINTER(c_int32)),
]

VkPhysicalDeviceTileMemoryHeapFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tileMemoryHeap", c_uint32),
]

VkPhysicalDeviceTileMemoryHeapPropertiesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queueSubmitBoundary", c_uint32),
    ("tileBufferTransfers", c_uint32),
]

VkTileMemorySizeInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("size", c_uint64),
]

VkTileMemoryRequirementsQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("size", c_uint64),
    ("alignment", c_uint64),
]

VkBindMemoryStatusKHR._fields_ = [
]

VkBindDescriptorSetsInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stageFlags", c_uint32),
    ("layout", c_void_p),
    ("firstSet", c_uint32),
    ("descriptorSetCount", c_uint32),
    ("pDescriptorSets", POINTER(c_void_p)),
    ("dynamicOffsetCount", c_uint32),
    ("pDynamicOffsets", POINTER(c_uint32)),
]

VkBindDescriptorSetsInfoKHR._fields_ = [
]

VkPushConstantsInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("layout", c_void_p),
    ("stageFlags", c_uint32),
    ("offset", c_uint32),
    ("size", c_uint32),
    ("pValues", c_void_p),
]

VkPushConstantsInfoKHR._fields_ = [
]

VkPushDescriptorSetInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stageFlags", c_uint32),
    ("layout", c_void_p),
    ("set", c_uint32),
    ("descriptorWriteCount", c_uint32),
    ("pDescriptorWrites", POINTER(VkWriteDescriptorSet)),
]

VkPushDescriptorSetInfoKHR._fields_ = [
]

VkPushDescriptorSetWithTemplateInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorUpdateTemplate", c_void_p),
    ("layout", c_void_p),
    ("set", c_uint32),
    ("pData", c_void_p),
]

VkPushDescriptorSetWithTemplateInfoKHR._fields_ = [
]

VkSetDescriptorBufferOffsetsInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stageFlags", c_uint32),
    ("layout", c_void_p),
    ("firstSet", c_uint32),
    ("setCount", c_uint32),
    ("pBufferIndices", POINTER(c_uint32)),
    ("pOffsets", POINTER(c_uint64)),
]

VkBindDescriptorBufferEmbeddedSamplersInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stageFlags", c_uint32),
    ("layout", c_void_p),
    ("set", c_uint32),
]

VkPhysicalDeviceCubicClampFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cubicRangeClamp", c_uint32),
]

VkPhysicalDeviceYcbcrDegammaFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("ycbcrDegamma", c_uint32),
]

VkSamplerYcbcrConversionYcbcrDegammaCreateInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("enableYDegamma", c_uint32),
    ("enableCbCrDegamma", c_uint32),
]

VkPhysicalDeviceCubicWeightsFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("selectableCubicWeights", c_uint32),
]

VkSamplerCubicWeightsCreateInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cubicWeights", c_int32),
]

VkBlitImageCubicWeightsInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cubicWeights", c_int32),
]

VkPhysicalDeviceImageProcessing2FeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("textureBlockMatch2", c_uint32),
]

VkPhysicalDeviceImageProcessing2PropertiesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxBlockMatchWindow", VkExtent2D),
]

VkSamplerBlockMatchWindowCreateInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("windowExtent", VkExtent2D),
    ("windowCompareMode", c_int32),
]

VkPhysicalDeviceDescriptorPoolOverallocationFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorPoolOverallocation", c_uint32),
]

VkPhysicalDeviceLayeredDriverPropertiesMSFT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("underlyingAPI", c_int32),
]

VkPhysicalDevicePerStageDescriptorSetFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("perStageDescriptorSet", c_uint32),
    ("dynamicPipelineLayout", c_uint32),
]

VkPhysicalDeviceExternalFormatResolveFeaturesANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalFormatResolve", c_uint32),
]

VkPhysicalDeviceExternalFormatResolvePropertiesANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("nullColorAttachmentWithExternalFormatResolve", c_uint32),
    ("externalFormatResolveChromaOffsetX", c_int32),
    ("externalFormatResolveChromaOffsetY", c_int32),
]

VkAndroidHardwareBufferFormatResolvePropertiesANDROID._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("colorAttachmentFormat", c_int32),
]

VkLatencySleepModeInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("lowLatencyMode", c_uint32),
    ("lowLatencyBoost", c_uint32),
    ("minimumIntervalUs", c_uint32),
]

VkLatencySleepInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("signalSemaphore", c_void_p),
    ("value", c_uint64),
]

VkSetLatencyMarkerInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentID", c_uint64),
    ("marker", c_int32),
]

VkGetLatencyMarkerInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("timingCount", c_uint32),
    ("pTimings", POINTER(VkLatencyTimingsFrameReportNV)),
]

VkLatencyTimingsFrameReportNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentID", c_uint64),
    ("inputSampleTimeUs", c_uint64),
    ("simStartTimeUs", c_uint64),
    ("simEndTimeUs", c_uint64),
    ("renderSubmitStartTimeUs", c_uint64),
    ("renderSubmitEndTimeUs", c_uint64),
    ("presentStartTimeUs", c_uint64),
    ("presentEndTimeUs", c_uint64),
    ("driverStartTimeUs", c_uint64),
    ("driverEndTimeUs", c_uint64),
    ("osRenderQueueStartTimeUs", c_uint64),
    ("osRenderQueueEndTimeUs", c_uint64),
    ("gpuRenderStartTimeUs", c_uint64),
    ("gpuRenderEndTimeUs", c_uint64),
]

VkOutOfBandQueueTypeInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queueType", c_int32),
]

VkLatencySubmissionPresentIdNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentID", c_uint64),
]

VkSwapchainLatencyCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("latencyModeEnable", c_uint32),
]

VkLatencySurfaceCapabilitiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentModeCount", c_uint32),
    ("pPresentModes", POINTER(c_int32)),
]

VkPhysicalDeviceCudaKernelLaunchFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cudaKernelLaunchFeatures", c_uint32),
]

VkPhysicalDeviceCudaKernelLaunchPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("computeCapabilityMinor", c_uint32),
    ("computeCapabilityMajor", c_uint32),
]

VkDeviceQueueShaderCoreControlCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderCoreCount", c_uint32),
]

VkPhysicalDeviceSchedulingControlsFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("schedulingControls", c_uint32),
]

VkPhysicalDeviceSchedulingControlsPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("schedulingControlsFlags", c_uint64),
]

VkPhysicalDeviceSchedulingControlsDispatchParametersPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("schedulingControlsMaxWarpsCount", c_uint32),
    ("schedulingControlsMaxQueuedBatchesCount", c_uint32),
    ("schedulingControlsMaxWorkGroupBatchSize", c_uint32),
]

VkDispatchParametersARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("workGroupBatchSize", c_uint32),
    ("maxQueuedWorkGroupBatches", c_uint32),
    ("maxWarpsPerShaderCore", c_uint32),
]

VkPhysicalDeviceRelaxedLineRasterizationFeaturesIMG._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("relaxedLineRasterization", c_uint32),
]

VkPhysicalDeviceRenderPassStripedFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("renderPassStriped", c_uint32),
]

VkPhysicalDeviceRenderPassStripedPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("renderPassStripeGranularity", VkExtent2D),
    ("maxRenderPassStripes", c_uint32),
]

VkRenderPassStripeInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stripeArea", VkRect2D),
]

VkRenderPassStripeBeginInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stripeInfoCount", c_uint32),
    ("pStripeInfos", POINTER(VkRenderPassStripeInfoARM)),
]

VkRenderPassStripeSubmitInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("stripeSemaphoreInfoCount", c_uint32),
    ("pStripeSemaphoreInfos", POINTER(VkSemaphoreSubmitInfo)),
]

VkPhysicalDevicePipelineOpacityMicromapFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineOpacityMicromap", c_uint32),
]

VkPhysicalDeviceShaderMaximalReconvergenceFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderMaximalReconvergence", c_uint32),
]

VkPhysicalDeviceShaderSubgroupRotateFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSubgroupRotate", c_uint32),
    ("shaderSubgroupRotateClustered", c_uint32),
]

VkPhysicalDeviceShaderSubgroupRotateFeaturesKHR._fields_ = [
]

VkPhysicalDeviceShaderExpectAssumeFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderExpectAssume", c_uint32),
]

VkPhysicalDeviceShaderExpectAssumeFeaturesKHR._fields_ = [
]

VkPhysicalDeviceShaderFloatControls2Features._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderFloatControls2", c_uint32),
]

VkPhysicalDeviceShaderFloatControls2FeaturesKHR._fields_ = [
]

VkPhysicalDeviceDynamicRenderingLocalReadFeatures._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dynamicRenderingLocalRead", c_uint32),
]

VkPhysicalDeviceDynamicRenderingLocalReadFeaturesKHR._fields_ = [
]

VkRenderingAttachmentLocationInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentLocations", POINTER(c_uint32)),
]

VkRenderingAttachmentLocationInfoKHR._fields_ = [
]

VkRenderingInputAttachmentIndexInfo._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("colorAttachmentCount", c_uint32),
    ("pColorAttachmentInputIndices", POINTER(c_uint32)),
    ("pDepthInputAttachmentIndex", POINTER(c_uint32)),
    ("pStencilInputAttachmentIndex", POINTER(c_uint32)),
]

VkRenderingInputAttachmentIndexInfoKHR._fields_ = [
]

VkPhysicalDeviceShaderQuadControlFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderQuadControl", c_uint32),
]

VkPhysicalDeviceShaderAtomicFloat16VectorFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderFloat16VectorAtomics", c_uint32),
]

VkPhysicalDeviceMapMemoryPlacedFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryMapPlaced", c_uint32),
    ("memoryMapRangePlaced", c_uint32),
    ("memoryUnmapReserve", c_uint32),
]

VkPhysicalDeviceMapMemoryPlacedPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("minPlacedMemoryMapAlignment", c_uint64),
]

VkMemoryMapPlacedInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pPlacedAddress", c_void_p),
]

VkPhysicalDeviceShaderBfloat16FeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderBFloat16Type", c_uint32),
    ("shaderBFloat16DotProduct", c_uint32),
    ("shaderBFloat16CooperativeMatrix", c_uint32),
]

VkPhysicalDeviceRawAccessChainsFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderRawAccessChains", c_uint32),
]

VkPhysicalDeviceCommandBufferInheritanceFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("commandBufferInheritance", c_uint32),
]

VkPhysicalDeviceImageAlignmentControlFeaturesMESA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("imageAlignmentControl", c_uint32),
]

VkPhysicalDeviceImageAlignmentControlPropertiesMESA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedImageAlignmentMask", c_uint32),
]

VkImageAlignmentControlCreateInfoMESA._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maximumRequestedAlignment", c_uint32),
]

VkPhysicalDeviceShaderReplicatedCompositesFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderReplicatedComposites", c_uint32),
]

VkPhysicalDevicePresentModeFifoLatestReadyFeaturesEXT._fields_ = [
]

VkPhysicalDevicePresentModeFifoLatestReadyFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentModeFifoLatestReady", c_uint32),
]

VkDepthClampRangeEXT._fields_ = [
    ("minDepthClamp", c_float),
    ("maxDepthClamp", c_float),
]

VkPhysicalDeviceCooperativeMatrix2FeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrixWorkgroupScope", c_uint32),
    ("cooperativeMatrixFlexibleDimensions", c_uint32),
    ("cooperativeMatrixReductions", c_uint32),
    ("cooperativeMatrixConversions", c_uint32),
    ("cooperativeMatrixPerElementOperations", c_uint32),
    ("cooperativeMatrixTensorAddressing", c_uint32),
    ("cooperativeMatrixBlockLoads", c_uint32),
]

VkPhysicalDeviceCooperativeMatrix2PropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeMatrixWorkgroupScopeMaxWorkgroupSize", c_uint32),
    ("cooperativeMatrixFlexibleDimensionsMaxDimension", c_uint32),
    ("cooperativeMatrixWorkgroupScopeReservedSharedMemory", c_uint32),
]

VkCooperativeMatrixFlexibleDimensionsPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("MGranularity", c_uint32),
    ("NGranularity", c_uint32),
    ("KGranularity", c_uint32),
    ("AType", c_int32),
    ("BType", c_int32),
    ("CType", c_int32),
    ("ResultType", c_int32),
    ("saturatingAccumulation", c_uint32),
    ("scope", c_int32),
    ("workgroupInvocations", c_uint32),
]

VkPhysicalDeviceHdrVividFeaturesHUAWEI._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("hdrVivid", c_uint32),
]

VkPhysicalDeviceVertexAttributeRobustnessFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("vertexAttributeRobustness", c_uint32),
]

VkPhysicalDeviceDenseGeometryFormatFeaturesAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("denseGeometryFormat", c_uint32),
]

VkAccelerationStructureDenseGeometryFormatTrianglesDataAMDX._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("compressedData", VkDeviceOrHostAddressConstKHR),
    ("dataSize", c_uint64),
    ("numTriangles", c_uint32),
    ("numVertices", c_uint32),
    ("maxPrimitiveIndex", c_uint32),
    ("maxGeometryIndex", c_uint32),
    ("format", c_int32),
]

VkPhysicalDeviceDepthClampZeroOneFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("depthClampZeroOne", c_uint32),
]

VkPhysicalDeviceCooperativeVectorFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeVector", c_uint32),
    ("cooperativeVectorTraining", c_uint32),
]

VkCooperativeVectorPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("inputType", c_int32),
    ("inputInterpretation", c_int32),
    ("matrixInterpretation", c_int32),
    ("biasInterpretation", c_int32),
    ("resultType", c_int32),
    ("transpose", c_uint32),
]

VkPhysicalDeviceCooperativeVectorPropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("cooperativeVectorSupportedStages", c_uint32),
    ("cooperativeVectorTrainingFloat16Accumulation", c_uint32),
    ("cooperativeVectorTrainingFloat32Accumulation", c_uint32),
    ("maxCooperativeVectorComponents", c_uint32),
]

VkConvertCooperativeVectorMatrixInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcSize", c_size_t),
    ("srcData", VkDeviceOrHostAddressConstKHR),
    ("pDstSize", POINTER(c_size_t)),
    ("dstData", VkDeviceOrHostAddressKHR),
    ("srcComponentType", c_int32),
    ("dstComponentType", c_int32),
    ("numRows", c_uint32),
    ("numColumns", c_uint32),
    ("srcLayout", c_int32),
    ("srcStride", c_size_t),
    ("dstLayout", c_int32),
    ("dstStride", c_size_t),
]

VkPhysicalDeviceTileShadingFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tileShading", c_uint32),
    ("tileShadingFragmentStage", c_uint32),
    ("tileShadingColorAttachments", c_uint32),
    ("tileShadingDepthAttachments", c_uint32),
    ("tileShadingStencilAttachments", c_uint32),
    ("tileShadingInputAttachments", c_uint32),
    ("tileShadingSampledAttachments", c_uint32),
    ("tileShadingPerTileDraw", c_uint32),
    ("tileShadingPerTileDispatch", c_uint32),
    ("tileShadingDispatchTile", c_uint32),
    ("tileShadingApron", c_uint32),
    ("tileShadingAnisotropicApron", c_uint32),
    ("tileShadingAtomicOps", c_uint32),
    ("tileShadingImageProcessing", c_uint32),
]

VkPhysicalDeviceTileShadingPropertiesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxApronSize", c_uint32),
    ("preferNonCoherent", c_uint32),
    ("tileGranularity", VkExtent2D),
    ("maxTileShadingRate", VkExtent2D),
]

VkRenderPassTileShadingCreateInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("tileApronSize", VkExtent2D),
]

VkPerTileBeginInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkPerTileEndInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkDispatchTileInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkPhysicalDeviceFragmentDensityMapLayeredPropertiesVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxFragmentDensityMapLayers", c_uint32),
]

VkPhysicalDeviceFragmentDensityMapLayeredFeaturesVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("fragmentDensityMapLayered", c_uint32),
]

VkPipelineFragmentDensityMapLayeredCreateInfoVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxFragmentDensityMapLayers", c_uint32),
]

VkSetPresentConfigNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("numFramesPerBatch", c_uint32),
    ("presentConfigFeedback", c_uint32),
]

VkPhysicalDevicePresentMeteringFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("presentMetering", c_uint32),
]

VkExternalComputeQueueDeviceCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("reservedExternalQueues", c_uint32),
]

VkExternalComputeQueueCreateInfoNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("preferredQueue", c_void_p),
]

VkExternalComputeQueueDataParamsNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceIndex", c_uint32),
]

VkPhysicalDeviceExternalComputeQueuePropertiesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalDataSize", c_uint32),
    ("maxExternalQueues", c_uint32),
]

VkPhysicalDeviceShaderUniformBufferUnsizedArrayFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderUniformBufferUnsizedArray", c_uint32),
]

VkPhysicalDeviceShaderMixedFloatDotProductFeaturesVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderMixedFloatDotProductFloat16AccFloat32", c_uint32),
    ("shaderMixedFloatDotProductFloat16AccFloat16", c_uint32),
    ("shaderMixedFloatDotProductBFloat16Acc", c_uint32),
    ("shaderMixedFloatDotProductFloat8AccFloat32", c_uint32),
]

VkPhysicalDevicePrimitiveRestartIndexFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("primitiveRestartIndex", c_uint32),
]

VkPhysicalDeviceFormatPackFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("formatPack", c_uint32),
]

VkPhysicalDeviceThrottleHintFeaturesSEC._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("throttleHint", c_uint32),
]

VkThrottleHintSubmitInfoSEC._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("throttleHint", c_int32),
]

VkTensorDescriptionARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tiling", c_int32),
    ("format", c_int32),
    ("dimensionCount", c_uint32),
    ("pDimensions", POINTER(c_int64)),
    ("pStrides", POINTER(c_int64)),
    ("usage", c_uint64),
]

VkTensorCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
    ("pDescription", POINTER(VkTensorDescriptionARM)),
    ("sharingMode", c_int32),
    ("queueFamilyIndexCount", c_uint32),
    ("pQueueFamilyIndices", POINTER(c_uint32)),
]

VkTensorViewCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
    ("tensor", c_void_p),
    ("format", c_int32),
]

VkTensorMemoryRequirementsInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensor", c_void_p),
]

VkBindTensorMemoryInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensor", c_void_p),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
]

VkWriteDescriptorSetTensorARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorViewCount", c_uint32),
    ("pTensorViews", POINTER(c_void_p)),
]

VkTensorFormatPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("optimalTilingTensorFeatures", c_uint64),
    ("linearTilingTensorFeatures", c_uint64),
]

VkPhysicalDeviceTensorPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxTensorDimensionCount", c_uint32),
    ("maxTensorElements", c_uint64),
    ("maxPerDimensionTensorElements", c_uint64),
    ("maxTensorStride", c_int64),
    ("maxTensorSize", c_uint64),
    ("maxTensorShaderAccessArrayLength", c_uint32),
    ("maxTensorShaderAccessSize", c_uint32),
    ("maxDescriptorSetStorageTensors", c_uint32),
    ("maxPerStageDescriptorSetStorageTensors", c_uint32),
    ("maxDescriptorSetUpdateAfterBindStorageTensors", c_uint32),
    ("maxPerStageDescriptorUpdateAfterBindStorageTensors", c_uint32),
    ("shaderStorageTensorArrayNonUniformIndexingNative", c_uint32),
    ("shaderTensorSupportedStages", c_uint32),
]

VkTensorMemoryBarrierARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcStageMask", c_uint64),
    ("srcAccessMask", c_uint64),
    ("dstStageMask", c_uint64),
    ("dstAccessMask", c_uint64),
    ("srcQueueFamilyIndex", c_uint32),
    ("dstQueueFamilyIndex", c_uint32),
    ("tensor", c_void_p),
]

VkTensorDependencyInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorMemoryBarrierCount", c_uint32),
    ("pTensorMemoryBarriers", POINTER(VkTensorMemoryBarrierARM)),
]

VkPhysicalDeviceTensorFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorNonPacked", c_uint32),
    ("shaderTensorAccess", c_uint32),
    ("shaderStorageTensorArrayDynamicIndexing", c_uint32),
    ("shaderStorageTensorArrayNonUniformIndexing", c_uint32),
    ("descriptorBindingStorageTensorUpdateAfterBind", c_uint32),
    ("tensors", c_uint32),
]

VkDeviceTensorMemoryRequirementsARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pCreateInfo", POINTER(VkTensorCreateInfoARM)),
]

VkCopyTensorInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcTensor", c_void_p),
    ("dstTensor", c_void_p),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkTensorCopyARM)),
]

VkTensorCopyARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dimensionCount", c_uint32),
    ("pSrcOffset", POINTER(c_uint64)),
    ("pDstOffset", POINTER(c_uint64)),
    ("pExtent", POINTER(c_uint64)),
]

VkMemoryDedicatedAllocateInfoTensorARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensor", c_void_p),
]

VkPhysicalDeviceDescriptorBufferTensorPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorCaptureReplayDescriptorDataSize", c_size_t),
    ("tensorViewCaptureReplayDescriptorDataSize", c_size_t),
    ("tensorDescriptorSize", c_size_t),
]

VkPhysicalDeviceDescriptorBufferTensorFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorBufferTensorDescriptors", c_uint32),
]

VkTensorCaptureDescriptorDataInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensor", c_void_p),
]

VkTensorViewCaptureDescriptorDataInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorView", c_void_p),
]

VkDescriptorGetTensorInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorView", c_void_p),
]

VkFrameBoundaryTensorsARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorCount", c_uint32),
    ("pTensors", POINTER(c_void_p)),
]

VkPhysicalDeviceExternalTensorInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
    ("pDescription", POINTER(VkTensorDescriptionARM)),
    ("handleType", c_int32),
]

VkExternalTensorPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalMemoryProperties", VkExternalMemoryProperties),
]

VkExternalMemoryTensorCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handleTypes", c_uint32),
]

VkPhysicalDeviceShaderFloat8FeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderFloat8", c_uint32),
    ("shaderFloat8CooperativeMatrix", c_uint32),
]

VkSurfaceCreateInfoOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("window", POINTER(c_void_p)),
]

VkPhysicalDeviceDataGraphFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataGraph", c_uint32),
    ("dataGraphUpdateAfterBind", c_uint32),
    ("dataGraphSpecializationConstants", c_uint32),
    ("dataGraphDescriptorBuffer", c_uint32),
    ("dataGraphShaderModule", c_uint32),
]

VkDataGraphPipelineConstantTensorSemiStructuredSparsityInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dimension", c_uint32),
    ("zeroCount", c_uint32),
    ("groupSize", c_uint32),
]

VkDataGraphPipelineConstantARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("id", c_uint32),
    ("pConstantData", c_void_p),
]

VkDataGraphPipelineResourceInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorSet", c_uint32),
    ("binding", c_uint32),
    ("arrayElement", c_uint32),
]

VkDataGraphPipelineResourceInfoImageLayoutARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("layout", c_int32),
]

VkDataGraphPipelineCompilerControlCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pVendorOptions", c_char_p),
]

VkDataGraphPipelineCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
    ("layout", c_void_p),
    ("resourceInfoCount", c_uint32),
    ("pResourceInfos", POINTER(VkDataGraphPipelineResourceInfoARM)),
]

VkDataGraphPipelineShaderModuleCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("module", c_void_p),
    ("pName", c_char_p),
    ("pSpecializationInfo", POINTER(VkSpecializationInfo)),
    ("constantCount", c_uint32),
    ("pConstants", POINTER(VkDataGraphPipelineConstantARM)),
]

VkDataGraphPipelineSessionCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
    ("dataGraphPipeline", c_void_p),
]

VkDataGraphPipelineSessionBindPointRequirementsInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("session", c_void_p),
]

VkDataGraphPipelineSessionBindPointRequirementARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("bindPoint", c_int32),
    ("bindPointType", c_int32),
    ("numObjects", c_uint32),
]

VkDataGraphPipelineSessionMemoryRequirementsInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("session", c_void_p),
    ("bindPoint", c_int32),
    ("objectIndex", c_uint32),
]

VkBindDataGraphPipelineSessionMemoryInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("session", c_void_p),
    ("bindPoint", c_int32),
    ("objectIndex", c_uint32),
    ("memory", c_void_p),
    ("memoryOffset", c_uint64),
]

VkDataGraphPipelineInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataGraphPipeline", c_void_p),
]

VkDataGraphPipelinePropertyQueryResultARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("property", c_int32),
    ("isText", c_uint32),
    ("dataSize", c_size_t),
    ("pData", c_void_p),
]

VkDataGraphPipelineIdentifierCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("identifierSize", c_uint32),
    ("pIdentifier", POINTER(c_uint8)),
]

VkDataGraphPipelineDispatchInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint64),
]

VkPhysicalDeviceDataGraphProcessingEngineARM._fields_ = [
    ("type", c_int32),
    ("isForeign", c_uint32),
]

VkPhysicalDeviceDataGraphOperationSupportARM._fields_ = [
    ("operationType", c_int32),
    ("name", (c_char * VK_MAX_PHYSICAL_DEVICE_DATA_GRAPH_OPERATION_SET_NAME_SIZE_ARM)),
    ("version", c_uint32),
]

VkQueueFamilyDataGraphPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("engine", VkPhysicalDeviceDataGraphProcessingEngineARM),
    ("operation", VkPhysicalDeviceDataGraphOperationSupportARM),
]

VkPhysicalDeviceQueueFamilyDataGraphProcessingEngineInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queueFamilyIndex", c_uint32),
    ("engineType", c_int32),
]

VkQueueFamilyDataGraphProcessingEnginePropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("foreignSemaphoreHandleTypes", c_uint32),
    ("foreignMemoryHandleTypes", c_uint32),
]

VkDataGraphProcessingEngineCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("processingEngineCount", c_uint32),
    ("pProcessingEngines", POINTER(VkPhysicalDeviceDataGraphProcessingEngineARM)),
]

VkPhysicalDevicePipelineCacheIncrementalModeFeaturesSEC._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pipelineCacheIncrementalMode", c_uint32),
]

VkDataGraphPipelineBuiltinModelCreateInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pOperation", POINTER(VkPhysicalDeviceDataGraphOperationSupportARM)),
]

VkPhysicalDeviceDataGraphModelFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataGraphModel", c_uint32),
]

VkPhysicalDeviceShaderUntypedPointersFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderUntypedPointers", c_uint32),
]

VkNativeBufferOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("handle", POINTER(c_void_p)),
]

VkSwapchainImageCreateInfoOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("usage", c_uint32),
]

VkPhysicalDevicePresentationPropertiesOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("sharedImage", c_uint32),
]

VkPhysicalDeviceVideoEncodeRgbConversionFeaturesVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("videoEncodeRgbConversion", c_uint32),
]

VkVideoEncodeRgbConversionCapabilitiesVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rgbModels", c_uint32),
    ("rgbRanges", c_uint32),
    ("xChromaOffsets", c_uint32),
    ("yChromaOffsets", c_uint32),
]

VkVideoEncodeProfileRgbConversionInfoVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("performEncodeRgbConversion", c_uint32),
]

VkVideoEncodeSessionRgbConversionCreateInfoVALVE._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("rgbModel", c_int32),
    ("rgbRange", c_int32),
    ("xChromaOffset", c_int32),
    ("yChromaOffset", c_int32),
]

VkPhysicalDeviceShader64BitIndexingFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shader64BitIndexing", c_uint32),
]

VkNativeBufferUsageOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("OHOSNativeBufferUsage", c_uint64),
]

VkNativeBufferPropertiesOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("allocationSize", c_uint64),
    ("memoryTypeBits", c_uint32),
]

VkNativeBufferFormatPropertiesOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("externalFormat", c_uint64),
    ("formatFeatures", c_uint32),
    ("samplerYcbcrConversionComponents", VkComponentMapping),
    ("suggestedYcbcrModel", c_int32),
    ("suggestedYcbcrRange", c_int32),
    ("suggestedXChromaOffset", c_int32),
    ("suggestedYChromaOffset", c_int32),
]

VkImportNativeBufferInfoOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("buffer", POINTER(c_void_p)),
]

VkMemoryGetNativeBufferInfoOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memory", c_void_p),
]

VkExternalFormatOHOS._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("externalFormat", c_uint64),
]

VkPerfHintInfoQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("scale", c_uint32),
]

VkPhysicalDeviceQueuePerfHintFeaturesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("queuePerfHint", c_uint32),
]

VkPhysicalDeviceQueuePerfHintPropertiesQCOM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedQueues", c_uint32),
]

VkPhysicalDevicePerformanceCountersByRegionFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("performanceCountersByRegion", c_uint32),
]

VkPhysicalDevicePerformanceCountersByRegionPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxPerRegionPerformanceCounters", c_uint32),
    ("performanceCounterRegionSize", VkExtent2D),
    ("rowStrideAlignment", c_uint32),
    ("regionAlignment", c_uint32),
    ("identityTransformOrder", c_uint32),
]

VkPerformanceCounterARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("counterID", c_uint32),
]

VkPerformanceCounterDescriptionARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("name", (c_char * VK_MAX_DESCRIPTION_SIZE)),
]

VkRenderPassPerformanceCountersByRegionBeginInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("counterAddressCount", c_uint32),
    ("pCounterAddresses", POINTER(c_uint64)),
    ("serializeRegions", c_uint32),
    ("counterIndexCount", c_uint32),
    ("pCounterIndices", POINTER(c_uint32)),
]

VkComputeOccupancyPriorityParametersNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("occupancyPriority", c_float),
    ("occupancyThrottling", c_float),
]

VkPhysicalDeviceComputeOccupancyPriorityFeaturesNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("computeOccupancyPriority", c_uint32),
]

VkPhysicalDeviceShaderLongVectorFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("longVector", c_uint32),
]

VkPhysicalDeviceShaderLongVectorPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxVectorComponents", c_uint32),
]

VkPhysicalDeviceTextureCompressionASTC3DFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("textureCompressionASTC_3D", c_uint32),
]

VkPhysicalDeviceShaderSubgroupPartitionedFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderSubgroupPartitioned", c_uint32),
]

VkHostAddressRangeEXT._fields_ = [
    ("address", c_void_p),
    ("size", c_size_t),
]

VkHostAddressRangeConstEXT._fields_ = [
    ("address", c_void_p),
    ("size", c_size_t),
]

VkDeviceAddressRangeEXT._fields_ = [
]

VkTexelBufferDescriptorInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
    ("addressRange", VkDeviceAddressRangeEXT),
]

VkImageDescriptorInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pView", POINTER(VkImageViewCreateInfo)),
    ("layout", c_int32),
]

VkResourceDescriptorDataEXT._fields_ = [
    ("pImage", POINTER(VkImageDescriptorInfoEXT)),
    ("pTexelBuffer", POINTER(VkTexelBufferDescriptorInfoEXT)),
    ("pAddressRange", POINTER(VkDeviceAddressRangeEXT)),
    ("pTensorARM", POINTER(VkTensorViewCreateInfoARM)),
]

VkResourceDescriptorInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("type", c_int32),
    ("data", VkResourceDescriptorDataEXT),
]

VkBindHeapInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("heapRange", VkDeviceAddressRangeEXT),
    ("reservedRangeOffset", c_uint64),
    ("reservedRangeSize", c_uint64),
]

VkPushDataInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("offset", c_uint32),
    ("data", VkHostAddressRangeConstEXT),
]

VkDescriptorMappingSourceConstantOffsetEXT._fields_ = [
    ("heapOffset", c_uint32),
    ("heapArrayStride", c_uint32),
    ("pEmbeddedSampler", POINTER(VkSamplerCreateInfo)),
    ("samplerHeapOffset", c_uint32),
    ("samplerHeapArrayStride", c_uint32),
]

VkDescriptorMappingSourcePushIndexEXT._fields_ = [
    ("heapOffset", c_uint32),
    ("pushOffset", c_uint32),
    ("heapIndexStride", c_uint32),
    ("heapArrayStride", c_uint32),
    ("pEmbeddedSampler", POINTER(VkSamplerCreateInfo)),
    ("useCombinedImageSamplerIndex", c_uint32),
    ("samplerHeapOffset", c_uint32),
    ("samplerPushOffset", c_uint32),
    ("samplerHeapIndexStride", c_uint32),
    ("samplerHeapArrayStride", c_uint32),
]

VkDescriptorMappingSourceIndirectIndexEXT._fields_ = [
    ("heapOffset", c_uint32),
    ("pushOffset", c_uint32),
    ("addressOffset", c_uint32),
    ("heapIndexStride", c_uint32),
    ("heapArrayStride", c_uint32),
    ("pEmbeddedSampler", POINTER(VkSamplerCreateInfo)),
    ("useCombinedImageSamplerIndex", c_uint32),
    ("samplerHeapOffset", c_uint32),
    ("samplerPushOffset", c_uint32),
    ("samplerAddressOffset", c_uint32),
    ("samplerHeapIndexStride", c_uint32),
    ("samplerHeapArrayStride", c_uint32),
]

VkDescriptorMappingSourceIndirectIndexArrayEXT._fields_ = [
    ("heapOffset", c_uint32),
    ("pushOffset", c_uint32),
    ("addressOffset", c_uint32),
    ("heapIndexStride", c_uint32),
    ("pEmbeddedSampler", POINTER(VkSamplerCreateInfo)),
    ("useCombinedImageSamplerIndex", c_uint32),
    ("samplerHeapOffset", c_uint32),
    ("samplerPushOffset", c_uint32),
    ("samplerAddressOffset", c_uint32),
    ("samplerHeapIndexStride", c_uint32),
]

VkDescriptorMappingSourceHeapDataEXT._fields_ = [
    ("heapOffset", c_uint32),
    ("pushOffset", c_uint32),
]

VkDescriptorMappingSourceShaderRecordIndexEXT._fields_ = [
    ("heapOffset", c_uint32),
    ("shaderRecordOffset", c_uint32),
    ("heapIndexStride", c_uint32),
    ("heapArrayStride", c_uint32),
    ("pEmbeddedSampler", POINTER(VkSamplerCreateInfo)),
    ("useCombinedImageSamplerIndex", c_uint32),
    ("samplerHeapOffset", c_uint32),
    ("samplerShaderRecordOffset", c_uint32),
    ("samplerHeapIndexStride", c_uint32),
    ("samplerHeapArrayStride", c_uint32),
]

VkDescriptorMappingSourceIndirectAddressEXT._fields_ = [
    ("pushOffset", c_uint32),
    ("addressOffset", c_uint32),
]

VkDescriptorMappingSourceDataEXT._fields_ = [
    ("constantOffset", VkDescriptorMappingSourceConstantOffsetEXT),
    ("pushIndex", VkDescriptorMappingSourcePushIndexEXT),
    ("indirectIndex", VkDescriptorMappingSourceIndirectIndexEXT),
    ("indirectIndexArray", VkDescriptorMappingSourceIndirectIndexArrayEXT),
    ("heapData", VkDescriptorMappingSourceHeapDataEXT),
    ("pushDataOffset", c_uint32),
    ("pushAddressOffset", c_uint32),
    ("indirectAddress", VkDescriptorMappingSourceIndirectAddressEXT),
    ("shaderRecordIndex", VkDescriptorMappingSourceShaderRecordIndexEXT),
    ("shaderRecordDataOffset", c_uint32),
    ("shaderRecordAddressOffset", c_uint32),
]

VkDescriptorSetAndBindingMappingEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorSet", c_uint32),
    ("firstBinding", c_uint32),
    ("bindingCount", c_uint32),
    ("resourceMask", c_uint32),
    ("source", c_int32),
    ("sourceData", VkDescriptorMappingSourceDataEXT),
]

VkShaderDescriptorSetAndBindingMappingInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("mappingCount", c_uint32),
    ("pMappings", POINTER(VkDescriptorSetAndBindingMappingEXT)),
]

VkSamplerCustomBorderColorIndexCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("index", c_uint32),
]

VkOpaqueCaptureDataCreateInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pData", POINTER(VkHostAddressRangeConstEXT)),
]

VkIndirectCommandsLayoutPushDataTokenNV._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pushDataOffset", c_uint32),
    ("pushDataSize", c_uint32),
]

VkSubsampledImageFormatPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("subsampledImageDescriptorCount", c_uint32),
]

VkPhysicalDeviceDescriptorHeapFeaturesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("descriptorHeap", c_uint32),
    ("descriptorHeapCaptureReplay", c_uint32),
]

VkPhysicalDeviceDescriptorHeapPropertiesEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("samplerHeapAlignment", c_uint64),
    ("resourceHeapAlignment", c_uint64),
    ("maxSamplerHeapSize", c_uint64),
    ("maxResourceHeapSize", c_uint64),
    ("minSamplerHeapReservedRange", c_uint64),
    ("minSamplerHeapReservedRangeWithEmbedded", c_uint64),
    ("minResourceHeapReservedRange", c_uint64),
    ("samplerDescriptorSize", c_uint64),
    ("imageDescriptorSize", c_uint64),
    ("bufferDescriptorSize", c_uint64),
    ("samplerDescriptorAlignment", c_uint64),
    ("imageDescriptorAlignment", c_uint64),
    ("bufferDescriptorAlignment", c_uint64),
    ("maxPushDataSize", c_uint64),
    ("imageCaptureReplayOpaqueDataSize", c_size_t),
    ("maxDescriptorHeapEmbeddedSamplers", c_uint32),
    ("samplerYcbcrConversionCount", c_uint32),
    ("sparseDescriptorHeaps", c_uint32),
    ("protectedDescriptorHeaps", c_uint32),
]

VkCommandBufferInheritanceDescriptorHeapInfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("pSamplerHeapBindInfo", POINTER(VkBindHeapInfoEXT)),
    ("pResourceHeapBindInfo", POINTER(VkBindHeapInfoEXT)),
]

VkPhysicalDeviceDescriptorHeapTensorPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("tensorDescriptorSize", c_uint64),
    ("tensorDescriptorAlignment", c_uint64),
    ("tensorCaptureReplayOpaqueDataSize", c_size_t),
]

VkPhysicalDeviceShaderInstrumentationFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderInstrumentation", c_uint32),
]

VkPhysicalDeviceShaderInstrumentationPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("numMetrics", c_uint32),
    ("perBasicBlockGranularity", c_uint32),
]

VkShaderInstrumentationCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
]

VkShaderInstrumentationMetricDescriptionARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("name", (c_char * VK_MAX_DESCRIPTION_SIZE)),
    ("description", (c_char * VK_MAX_DESCRIPTION_SIZE)),
]

VkShaderInstrumentationMetricDataHeaderARM._fields_ = [
    ("resultIndex", c_uint32),
    ("resultSubIndex", c_uint32),
    ("stages", c_uint32),
    ("basicBlockIndex", c_uint32),
]

VkDeviceAddressRangeKHR._fields_ = [
    ("address", c_uint64),
    ("size", c_uint64),
]

VkDeviceMemoryCopyKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcRange", VkDeviceAddressRangeKHR),
    ("srcFlags", c_uint32),
    ("dstRange", VkDeviceAddressRangeKHR),
    ("dstFlags", c_uint32),
]

VkCopyDeviceMemoryInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkDeviceMemoryCopyKHR)),
]

VkDeviceMemoryImageCopyKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
    ("addressRowLength", c_uint32),
    ("addressImageHeight", c_uint32),
    ("imageSubresource", VkImageSubresourceLayers),
    ("imageLayout", c_int32),
    ("imageOffset", VkOffset3D),
    ("imageExtent", VkExtent3D),
]

VkCopyDeviceMemoryImageInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("image", c_void_p),
    ("regionCount", c_uint32),
    ("pRegions", POINTER(VkDeviceMemoryImageCopyKHR)),
]

VkMemoryRangeBarriersInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("memoryRangeBarrierCount", c_uint32),
    ("pMemoryRangeBarriers", POINTER(VkMemoryRangeBarrierKHR)),
]

VkMemoryRangeBarrierKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("srcStageMask", c_uint64),
    ("srcAccessMask", c_uint64),
    ("dstStageMask", c_uint64),
    ("dstAccessMask", c_uint64),
    ("srcQueueFamilyIndex", c_uint32),
    ("dstQueueFamilyIndex", c_uint32),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
]

VkPhysicalDeviceDeviceAddressCommandsFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("deviceAddressCommands", c_uint32),
]

VkConditionalRenderingBeginInfo2EXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
    ("flags", c_uint32),
]

VkAccelerationStructureCreateInfo2KHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("createFlags", c_uint32),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
    ("type", c_int32),
]

VkBindIndexBuffer3InfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
    ("indexType", c_int32),
]

VkBindVertexBuffer3InfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("setStride", c_uint32),
    ("addressRange", VkStridedDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
]

VkDrawIndirect2InfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkStridedDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
    ("drawCount", c_uint32),
]

VkDrawIndirectCount2InfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkStridedDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
    ("countAddressRange", VkDeviceAddressRangeKHR),
    ("countAddressFlags", c_uint32),
    ("maxDrawCount", c_uint32),
]

VkDispatchIndirect2InfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
]

VkBindTransformFeedbackBuffer2InfoEXT._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("addressRange", VkDeviceAddressRangeKHR),
    ("addressFlags", c_uint32),
]

VkPhysicalDeviceShaderConstantDataFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderConstantData", c_uint32),
]

VkPhysicalDeviceShaderAbortFeaturesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("shaderAbort", c_uint32),
]

VkPhysicalDeviceShaderAbortPropertiesKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("maxShaderAbortMessageSize", c_uint64),
]

VkDeviceFaultShaderAbortMessageInfoKHR._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("messageDataSize", c_uint64),
    ("pMessageData", c_void_p),
]

VkDataGraphTOSANameQualityARM._fields_ = [
    ("name", (c_char * VK_MAX_DATA_GRAPH_TOSA_NAME_SIZE_ARM)),
    ("qualityFlags", c_uint32),
]

VkQueueFamilyDataGraphTOSAPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("profileCount", c_uint32),
    ("pProfiles", POINTER(VkDataGraphTOSANameQualityARM)),
    ("extensionCount", c_uint32),
    ("pExtensions", POINTER(VkDataGraphTOSANameQualityARM)),
    ("level", c_int32),
]

VkDataGraphPipelineSingleNodeConnectionARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("set", c_uint32),
    ("binding", c_uint32),
    ("connection", c_int32),
]

VkPhysicalDeviceDataGraphOpticalFlowFeaturesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("dataGraphOpticalFlow", c_uint32),
]

VkQueueFamilyDataGraphOpticalFlowPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("supportedOutputGridSizes", c_uint32),
    ("supportedHintGridSizes", c_uint32),
    ("hintSupported", c_uint32),
    ("costSupported", c_uint32),
    ("minWidth", c_uint32),
    ("minHeight", c_uint32),
    ("maxWidth", c_uint32),
    ("maxHeight", c_uint32),
]

VkDataGraphOpticalFlowImageFormatInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("usage", c_uint32),
]

VkDataGraphOpticalFlowImageFormatPropertiesARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("format", c_int32),
]

VkDataGraphPipelineSingleNodeCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("nodeType", c_int32),
    ("connectionCount", c_uint32),
    ("pConnections", POINTER(VkDataGraphPipelineSingleNodeConnectionARM)),
]

VkDataGraphPipelineOpticalFlowCreateInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("width", c_uint32),
    ("height", c_uint32),
    ("imageFormat", c_int32),
    ("flowVectorFormat", c_int32),
    ("costFormat", c_int32),
    ("outputGridSize", c_uint32),
    ("hintGridSize", c_uint32),
    ("performanceLevel", c_int32),
    ("flags", c_uint32),
]

VkDataGraphPipelineOpticalFlowDispatchInfoARM._fields_ = [
    ("sType", c_int32),
    ("pNext", c_void_p),
    ("flags", c_uint32),
    ("meanFlowL1NormHint", c_uint32),
]
