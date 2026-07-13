import torch
from diffusers import  StableDiffusionPipeline

large_model = "sd-legacy/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(large_model, torch_dtype=torch.bfloat16)
pipe.enable_attention_slicing()
#pipe = pipe.to("cuda")
pipe = pipe.to("cpu")

#prompt = "Young boy playing football"
prompt = "boy holding football"

results = pipe(
    prompt,
    num_inference_steps=6,
    guidance_scale=3.5,
    height=512,
    width=512
)

images = results.images

# Save or display the images
for i, img in enumerate(images):
    img.save(f"image-{prompt}.png")  # Save each image
