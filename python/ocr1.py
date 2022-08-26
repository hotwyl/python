#Como transformar imagem em texto usando OCR em Python com OpenCV , Tesseract reconhecendo caracteres
#https://www.youtube.com/watch?v=GMqFZ7f0dy4

import cv2
import pytesseract

img = cv2.imread("anexos/img/texto.png")

resultado = pytesseract.image_to_string(img)

print(resultado)