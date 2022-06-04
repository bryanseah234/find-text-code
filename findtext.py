import pytesseract
import os
import sys


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


directory =input('Where to find text from?\n')
    
for file in os.listdir(directory):
  filename = os.fsdecode(file)
  
  if filename.endswith(".jpg") or filename.endswith(".JPEG") or filename.endswith(".JPG") or filename.endswith(".jpeg"):
    imagepath = os.path.join(directory, filename)
    text = pytesseract.image_to_string(imagepath)
    
    if text == '':
      pass
    
    else:
      os.remove(imagepath)
      print(f'Removed {filename} from {directory}')
      
  else:
    continue


