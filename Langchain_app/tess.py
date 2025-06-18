import pytesseract
from pathlib import Path
from PIL import Image
import pdf2image

def ocr():
    text = []
    imgs = Path('D:/ML/Task-2/imgs').glob('*')
    for img in imgs:
        image = Image.open(img)
        text.append(pytesseract.image_to_string(image))
    return text