import argparse
import os
import requests
import dotenv
from text2image import Illusion_diffusion
from plant_identifier import Plant_identifier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', help='prompt to generate image', required=True, type=str)
    parser.add_argument('--imgName', help='Name of image', required=False, type=str, default='generated_image')
    args = parser.parse_args()
    
    dotenv = dotenv.load_dotenv()
    Fal_API_KEY = os.getenv("Fal_API_KEY")
    PlantNet_API_KEY = os.getenv("PlantNet_API_KEY")

    try:
        text2img_obj = Illusion_diffusion(Fal_API_KEY=Fal_API_KEY, prompt=args.prompt)
        if text2img_obj.get_responseCode != 200:
            raise Exception(f"There is a problem in generating image.")
        
        res = requests.get(text2img_obj.get_imgLink(), allow_redirects=True)
        open(f'{args.imgName}.png', 'wb').write(res.content)

        plant_identifier_obj = Plant_identifier(PlantNet_API_KEY=PlantNet_API_KEY, imgPath=f'{args.imgName}.png')
        if plant_identifier_obj.get_responseCode != 200:
            raise Exception(f"There is a problem in Identifying plant.")
    except Exception as e:
        print(e)
    else:
        print(plant_identifier_obj.get_plantName())


if __name__ == "__main__":
    main()