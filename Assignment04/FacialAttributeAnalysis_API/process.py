from deepface import DeepFace

def main_process(input_img):
        data = DeepFace.analyze(img_path = input_img, actions = ['age', 'gender', 'race', 'emotion'])
        return data
