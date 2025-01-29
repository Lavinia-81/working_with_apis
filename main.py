# sa salvam imagini cu niste caini intr-un pdf

import json
import os
import requests
from json import JSONDecodeError
import time
import image_functions as image_func
import pdf_functions as pdf

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
        print(f"The config file is missing...{e}")
    except JSONDecodeError as e:
        print("Watch you JSON...")
    except Exception as e:
        print(f"Unknow exception: {e}")

    return conf_dict


if __name__ == '__main__':
    config = read_config()

    while True:
        user_pick = input(MENU)

        match user_pick:
            case "1":
                random_image_dict = image_func.get_dog_image(config["url_dog_images"])
                content = image_func.download_dog_images(random_image_dict["message"])
                # image_func.save_dog_image(content)
            case "2":
                image_func.show_all_images()
            case "3":
                pdf.create_pdf("test.pdf")
            case "4":
                pass

