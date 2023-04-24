import cv2
import enchant
import pytesseract
import numpy as np

from enchant.checker import SpellChecker

pytesseract.pytesseract.tesseract_cmd = r'venv\Lib\Tesseract-OCR\tesseract.exe'

# Hàm chuyển đổi hình ảnh sang PDF

def convertToString(image_location):
    image_path = image_location

    # Đọc hình ảnh sử dụng OpenCV
    img = cv2.imread(image_path)

    # Chuyển đổi hình ảnh sang định dạng xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Nhận dạng văn bản sử dụng pytesseract
    text = pytesseract.image_to_string(gray, lang='eng')
    
    vi_dict = enchant.Dict("en_US")
    chkr = SpellChecker(vi_dict)
    # Set the text to be checked
    chkr.set_text(text)

    # Iterate over misspelled words and suggest replacements
    for err in chkr:
        sug = err.suggest()
        if sug:
            err.replace(sug[0])
            text = chkr.get_text()

    return text
