import json
import requests


class Illusion_diffusion:
    def __init__(self, Fal_API_KEY, prompt):
        self.url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
        self.payload = {
            "image_url": "https://github.com/BenyaminZojaji/PyDeploy-Course/blob/main/Assignment02/pattern.png?raw=true",
            "prompt": f"(masterpiece:1.4), (best quality), (detailed), {prompt}",
            "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
        }
        self.headers = {
            "Authorization": Fal_API_KEY,
            "Content-Type": "application/json"
        }
        self.response = requests.post(self.url, json=self.payload, headers=self.headers)
    
    def get_responseCode(self):
        return self.response.status_code

    def get_imgLink(self):
        return self.response.json()['image']['url']
    