from .Inspyrenet_Rembg import InspyrenetRembg

NODE_CLASS_MAPPINGS = {
    "InspyrenetRembg" : InspyrenetRembg,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InspyrenetRembg": "InSPyReNet Rembg",
}
__all__ = ['NODE_CLASS_MAPPINGS', "NODE_DISPLAY_NAME_MAPPINGS"]
