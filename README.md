# AI Text-Image Generator 

An Application that genrates realistic-photo images with text input. The application was developed using PyQT5 with PyTorch-Cuda version. Model used in this project is   Stable diffusion.  

Stable Diffusion is a latent text-to-image diffusion model capable of generating High Resolution photo-realistic images given any text input.


## **Results**


<img src="https://user-images.githubusercontent.com/114252357/204707155-d8bdbc61-5922-4661-bbea-afb52876eff0.jpg" width="300" height="300"><img src="https://user-images.githubusercontent.com/114252357/204707166-2ed1fb0d-1dfc-4850-9840-ef44c6071516.jpg" width="300" height="300"><img src="https://user-images.githubusercontent.com/114252357/204707182-1be3b37f-b528-441d-9298-1a4c08cffcef.jpg" width="300" height="300">

the above images were geneareted by inputs "Bear on Mars", "a photo of an astronaut riding a horse on mars", "A fantasy landscape, trending on artstation"

## **User Interface** 


<img src="https://user-images.githubusercontent.com/114252357/204708294-0ddecdba-ba3e-4be1-9b0e-e80827bcb530.png" width="700" height="700">


## **Commands**

1. pip install --upgrade diffusers transformers scipy
2. huggingface-cli login
3. pip install requirements.txt
4. python app.py


Note - Authentication token has to be generated from: https://huggingface.co/docs/hub/security-tokens
