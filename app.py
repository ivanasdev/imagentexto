from PIL import Image


import pytesseract

#print(pytesseract.get_languages())

imagen = Image.open('img/acta.gif')

ocr_result = pytesseract.image_to_string(imagen, lang='spa')
#Se guarda el texto en un txt
text_file=open("texto12.txt","w")
text_file.write(ocr_result)

print(ocr_result)
