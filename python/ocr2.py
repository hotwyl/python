#Como Ler Textos Dentro de Imagens com Python [Introdução ao OpenCV e Tesseract]
#https://www.youtube.com/watch?v=Wx3SyNwZtsA
#https://drive.google.com/drive/folders/1hkddnn-XeQlc1gXeI1KfJc39SSiS2LH_

import pytesseract
import cv2

# passo 1: ler a imagem
imagem = cv2.imread("anexos/img/email.JPG")

# passo 2: pedir pro tesseract extrair o texto da imagem
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)
