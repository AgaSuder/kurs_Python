#!/usr/bin/python3
from PIL import Image

with Image.open("sample.jpg") as img:
    print("Image mode is: " + img.mode)
    print("Image format is: " + img.format)
    print("Image size is: ")
    print( img.size)
    img.thumbnail((128, 128))
    print("Saving image as thumbnail to sample_thmubnail.jpg")
    img.save('sample_thmubnail.jpg', "JPEG")

input()