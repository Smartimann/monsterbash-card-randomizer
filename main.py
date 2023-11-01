import os 
from pathlib import Path
import PIL
from PIL import Image, ImageOps
import config

def main(): 
    originals_path = Path("originals")
    rotated_path = Path("rotated")
    padded_path = Path("padded")

    rotate_image_if_necessary(originals_path, rotated_path)
    resize_image_with_padding(rotated_path, padded_path)

def rotate_image_if_necessary(input_path, output_path): 
    print("> Rotating vertical images")
    all_images = os.listdir(input_path)

    for img in all_images: 
        image = Image.open(Path.joinpath(input_path, img))

        if image.width < image.height:
            new_image = Image.new("RGB",(image.height, image.width))
            image = image.rotate(90, expand=True)

        image.save(Path.joinpath(output_path, "rot-"+img),"PNG")
        

def resize_image_with_padding(input_path, output_path):
    print("> Padding images")
    all_images = os.listdir(input_path)
    wanted_aspect_ration = config.card_width / config.card_height

    for img in all_images:
        if ".DS_Store" not in img:
            image = Image.open(Path.joinpath(input_path, img))
            current_aspect_ratio = image.width / image.height

            if current_aspect_ratio is not wanted_aspect_ration:            
                border_color = image.getpixel((image.width - 1, image.height / 2))

                image = ImageOps.pad(image, (config.card_width, config.card_height), color=border_color)
            
            image.save(Path.joinpath(output_path, "pad-"+img),"PNG")

if __name__ == "__main__": 
    main()