import torch
from diffusers import StableDiffusionPipeline



def hello(a):
    
    if torch.cuda.is_available():
        model_id = "CompVis/stable-diffusion-v1-4"
        device = "cuda"


        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
        pipe = pipe.to(device)

        prompt = a
        image = pipe(prompt, guidance_scale=8.5).images[0]  
    
        image.save("image.png")

    else:
        torch.cuda.empty_cache()
        hello(a)
    d=1


def ok():
    print("tis ")