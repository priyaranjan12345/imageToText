import cv2 as cv
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print('_'*60)

def img_to_text():
    t = pytesseract.image_to_string(Image.open('img.png'))
    return t

print(img_to_text())

print('_'*60)
