import pytesseract
from pathlib import Path
from PIL import Image,ImageFilter

def ocr():
    text = []
    imgs = Path('D:/ML/Langchain_app/imgs').glob('*')
    for i in imgs:
        img = Image.open(i)
        img = img.convert('L')
        img = img.filter(ImageFilter.UnsharpMask(1.5,200,2))
        text.append(pytesseract.image_to_string(img))
        #img.show()
    return text
