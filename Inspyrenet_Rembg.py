from PIL import Image
import torch
import numpy as np
from .Remover import Remover
from tqdm import tqdm
import folder_paths


# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# Convert PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

model_path = 'InSPyReNet'

class InspyrenetRembg:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "threshold": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "torchscript_jit": (["default", "on"],),
                "ckpt_name": (folder_paths.get_filename_list(model_path), ),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "remove_background"
    CATEGORY = "rembg"

    def remove_background(self, image, torchscript_jit, ckpt_name, threshold):
        ckpt_path = folder_paths.get_full_path(model_path, ckpt_name)
        if (torchscript_jit == "default"):
            remover = Remover(ckpt=ckpt_path)
        else:
            remover = Remover(jit=True, ckpt=ckpt_path)
        img_list = []
        for img in tqdm(image, "Inspyrenet Rembg"):
            mid = remover.process(tensor2pil(img), type='rgba', threshold=threshold)
            out =  pil2tensor(mid)
            img_list.append(out)
        img_stack = torch.cat(img_list, dim=0)
        mask = img_stack[:, :, :, 3]
        return (img_stack, mask)