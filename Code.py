
import os
from PIL import Image
import cv2
from pdf2image import convert_from_path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(threshold)
    
    return text

def extract_text_from_pdf(path):
     print(path)
     doc = convert_from_path(path,poppler_path=r' C:\Users\dell\Downloads\poppler-0.68.0\bin')
     path, fileName = os.path.split(filePath)
     fileBaseName, fileExtension = os.path.splitext(fileName)

     for page_number, page_data in enumerate(doc):
       txt = pytesseract.image_to_string(Image.fromarray(page_data)).encode("utf-8")
       print("Page # {} - {}".format(str(page_number),txt))
    
     return txt



