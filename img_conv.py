from PIL import Image
import io, cv2, base64
import numpy as np

def convert_to_webp():
    image = Image.open("image1.jpg")
    data_buffer = io.BytesIO()
    image.save(data_buffer, format='webp')
    image.close()

    data = data_buffer.getvalue()
    data_buffer.close()
    return data

def convert_webp(filename ='image1.jpg'):
    newFilePath = filename[0: filename.rfind(".")] + ".webp"
    image = Image.open(filename)  # Open image
    image.save(newFilePath, format="webp")


def scale_img(filename ='image44.jpeg'):
    with open(filename, 'rb') as imagefile:
        img_file = imagefile.read()
    image=Image.open(io.BytesIO(img_file))
    image = image.resize((896, 300), Image.LANCZOS)
    print(image.size)
    image.save("newsdf.webp", quality=95, format='webp')

iamg = cv2.imread("image1.png", cv2.IMREAD_COLOR)