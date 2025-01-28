import requests
import json
import os
import time
import cv2


def read_config(path: str = "config.json") -> dict:
    try:
         with open(path, "r") as f:
             data = f.read()
             conf_dict = json.loads(data)
    except FileNotFoundError as e:
        print(f"The config file is missing..{e}")
    except JSONDecodeError as e:
        print("Watch you JSON...")
    except Exception as e:
        print(f"Unknow exception: {e}")

    return conf_dict

def get_dog_image(url: str) -> dict:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
            data = json.loads(response.text)
            return data
        else:
            raise Exception("Status code is not 200, therefore the api didin't work")
    except Exception as e:
        print(f"Something went wrong with api. {e}")
        f"{response.status_code}"
        f"{response.text}"


def download_dog_images(url: str):

    try:
        response = requests.get(url)
        return response.content
    except Exception as e:
        print(e)

def save_dog_image(conten, path: str = "images"):
    os.makedirs(path, exit_ok=True)
    timestamp = int(time.time())

    with open(f"/{path}/dog_image_{timestamp}.png", "wb") as f:
        f.write(content)


def show_all_images(path: str = "images"):
    images_list = os.listdir(path)

    for image in images_list:
        image_content = cv2.imread(f"/{path}/{image}")
        cv2.imshow(image, image_content)
        cv2.waitkey(0)
        # cv2.destroyAllWindows()



