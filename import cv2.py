import cv2
import numpy as np

# Carregar uma imagem
print("O caminho da imagem é fornecido no código.")
print("Caso informe erro, verifique se o caminho está correto.")

imagem = cv2.imread('C:/Users/SEU USER/Documents/.../Computer Vision/Imagem.jpg')

if imagem is None:
    print("Carregue uma imagem válida ou verifique o caminho fornecido.")
    
else:
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagem em Escala de Cinza', imagem_cinza)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
