import torch
from diffusers import ZImagePipeline

# 1. Load the pipeline
# Use bfloat16 for optimal performance on supported GPUs
print("Step 1")
pipe = ZImagePipeline.from_pretrained(
    "Tongyi-MAI/Z-Image-Turbo",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=False,
)

print("Step 2")
##pipe.to("cuda")
pipe.to("cpu")

print("Step 3")
# [Optional] Attention Backend
# Diffusers uses SDPA by default. Switch to Flash Attention for better efficiency if supported:
# pipe.transformer.set_attention_backend("flash")    # Enable Flash-Attention-2
# pipe.transformer.set_attention_backend("_flash_3") # Enable Flash-Attention-3

#pipe.transformer.set_attention_backend("flash")    # Enable Flash-Attention-2
#pipe.transformer.set_attention_backend("_flash_3") # Enable Flash-Attention-3

# [Optional] Model Compilation
# Compiling the DiT model accelerates inference, but the first run will take longer to compile.
# pipe.transformer.compile()

# [Optional] CPU Offloading
# Enable CPU offloading for memory-constrained devices.
# pipe.enable_model_cpu_offload()

#pipe.enable_model_cpu_offload()
print("Step 3.5")

prompt = "man holding a football"

# 2. Generate Image
# image = pipe(
#     prompt=prompt,
#     height=1024,
#     width=1024,
#     num_inference_steps=9,  # This actually results in 8 DiT forwards
#     guidance_scale=0.0,     # Guidance should be 0 for the Turbo models
#     generator=torch.Generator("cuda").manual_seed(42),
# ).images[0]
print("Step 4")

image = pipe(
    prompt=prompt,
    height=512,
    width=512,
    num_inference_steps=6,  # This actually results in 8 DiT forwards
    guidance_scale=0.0,     # Guidance should be 0 for the Turbo models
    generator=torch.Generator("cpu").manual_seed(42),
).images[0]

print("Step 5")

image.save("example1.png")

print("Completed")