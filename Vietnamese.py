import cv2
from PIL import Image, ImageFilter
import numpy as np
import enchant
from enchant.checker import SpellChecker
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import Segmentation as sg

import os

def convertToString(segments):
    os.environ['KMP_DUPLICATE_LIB_OK']='True'

    config = Cfg.load_config_from_file('venv/Include/Models/config.yaml')

    # config['weights'] = 'venv/Include/Models/model.pth'
    # config['device'] = 'cpu' # device để huấn luyện mô hình, để sử dụng cpu huấn luyện thì thay bằng 'cpu'

    detector = Predictor(config)

    # segments = sg.line_segmentation(img)
    result = ""

    for segment in segments:
        segment_pil = Image.fromarray(cv2.cvtColor(segment, cv2.COLOR_BGR2RGB))
        segment_pil_gray = segment_pil.convert('L')
        text = detector.predict(segment_pil_gray)
        result = result + " " + text + "\n"
        
    vi_dict = enchant.Dict("vi_VN")
    chkr = SpellChecker(vi_dict)
    # Set the text to be checked
    chkr.set_text(result)

    # Iterate over misspelled words and suggest replacements
    for err in chkr:
        sug = err.suggest()
        if sug:
            err.replace(sug[0])
            result = chkr.get_text()
                
    return result

def NonTextSeparate(img_path):
    results = []
    results = osg.notText(img_path)       
    return results

if __name__ == "__main__":
    image_path = "Images/sample7.jpg"
    result = convertToString(image_path)
    print(f"result: {result}")
