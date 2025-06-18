import pytesseract 
from pathlib import Path
from PIL import Image, ImageFilter


imgs = Path('D:/ML/tesseract_code/Imgs/Task-2').glob('*')
count = 0
for i in imgs:
    count+=1
    img = Image.open(i)
    img = img.convert('L')
    img = img.filter(ImageFilter.UnsharpMask(1.5,100,5))
    new_size = (img.size[0] * 2, img.size[1] * 2)
    img = img.resize(new_size)
    custom = None 
    if count == 1 or count == 2:
        custom = '--psm 6'
    if count==3:
        custom='--psm 1'
    print(pytesseract.image_to_string(img,config=custom)) 
    print('\n---------------\n')
