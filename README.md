# ComfyUI-Inspyrenet-Rembg
[ComfyUI](https://github.com/comfyanonymous/ComfyUI) node for background removal, implementing [InSPyReNet](https://github.com/plemeri/InSPyReNet)
</br></br>

I've tested a lot of different AI rembg methods (BRIA - U2Net - IsNet - SAM - OPEN RMBG, ...) but in all of my tests InSPyReNet was always ON A WHOLE DIFFERENT LEVEL!

The cherry on top is that [InSPyReNet](https://github.com/plemeri/InSPyReNet) has MIT License which allows for Commercial use (for example BRIA does not allow Commercial use to my knowledge)

Check the Licenses for yourself I will not be held accountable :)

## Updates

Added an advanced node that supports threshold

## Features

Superior rembg quality compared to other methods (just give it a try!)

Can take batch of images as input

Optimized for image batch to be the fastest rembg node (perfect for video frames)

Outputs both the image and the corresponding mask

Shows the progress in terminal


## Installation 

Set InSPyReNet in `extra_model_paths.yaml` for specifying the model path.

## Available Models

base:
  url: "https://github.com/plemeri/transparent-background/releases/download/1.2.12/ckpt_base.pth"
  md5: "d692e3dd5fa1b9658949d452bebf1cda"
  ckpt_name: "ckpt_base.pth"
  http_proxy: NULL
  base_size: [1024, 1024]


fast:
  url: "https://github.com/plemeri/transparent-background/releases/download/1.2.12/ckpt_fast.pth"
  md5: "9efdbfbcc49b79ef0f7891c83d2fd52f"
  ckpt_name: "ckpt_fast.pth"
  http_proxy: NULL
  base_size: [384, 384]

base-nightly:
  url: "https://github.com/plemeri/transparent-background/releases/download/1.2.12/ckpt_base_nightly.pth"
  md5: NULL
  ckpt_name: "ckpt_base_nightly.pth"
  http_proxy: NULL
  base_size: [1024, 1024]

