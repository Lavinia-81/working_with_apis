# sa salvam niste imagini cu niste caini intr-un pdf
import json
import os
import requests
from json import JSONDecodeError
import time


MENU = """
1. Save Random Image
2. Show all images
3. Save images to pdf
4. Delete all images
"""

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






if __name__ == '__main__':
    config = read_config()

    while True:
        user_pick = input(MENU)

        match user_pick:
            case "1":
                random_image_dict = image_func.get_dog_imag(config['url_dog_images'])
                content = image_funct.download_dog_image(random_image_dict("message"))
                image_func.save_dog_image(content)
            case "2":
                image_func.show
            case "3":
                pass
            case "4":
                pass

    # print(get_dog_image(config['url_dog_image']))
    random_image_dict = get_dog_image(config['url_dog_images'])
    content = download_dog_images(random_image_dict["message"])
    save_dog_image(content)
