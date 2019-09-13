#Importar librerías
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import random as rng
rng.seed(12345)
#Función para filtrar imágenes por tamaño
def bwareafilt ( image ):
    image = image.astype(np.uint8)
    nb_components, output, stats, centroids = cv.connectedComponentsWithStats(image, connectivity=4)
    sizes = stats[:, -1]

    max_label = 1
    max_size = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]

    img2 = np.zeros(output.shape)
    img2[output == max_label] = 255

    return img2
#Leer imagen y cambiarla de BGR a RGB
clasi = cv.imread('puerta.jpg')
clasi = cv.cvtColor(clasi, cv.COLOR_BGR2RGB)
color = ('r','g','b')
#Histogramas en cada capa de color, así determinamos el valor umbral de 100 en
#la capa azul
for i,col in enumerate(color):
  histr = cv.calcHist([clasi],[i],None,[256],[0,256])
  plt.plot(histr,color = col)
  plt.xlim([0,256])
  plt.show()
blue = clasi[:,:,2]
#Umbralización
ret, tsk2 = cv.threshold(blue, 100, 255, 1)
#Se filtra para segmentar el objeto de mayor área
imagenBW=bwareafilt(tsk2)
#Se normaliza el tipo de la variable imagenBW a CV_8UC1
im = cv.normalize(src=imagenBW, dst=None, alpha=0, beta=255,
                  norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
#Se hallan los contornos
(_, contours, hierarchy) = cv.findContours(image = im, 
    mode = cv.RETR_EXTERNAL,
    method = cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
#Se hallan y dibujan rectángulos alrededor del objeto hallado anteriormente(arco)
x,y,w,h = cv.boundingRect(cnt)
color = (255, 0, 0)
cv.rectangle(clasi,(x,y),(x+w,y+h),color,2)
clasi = cv.cvtColor(clasi, cv.COLOR_RGB2BGR)
cv.imwrite('puertaBB.jpg', clasi)
cv.imshow('Contours',clasi)
cv.waitKey()
#Se corta la imagen para poder analizar la parte inferior y poder detectar el ángulo
#de inclinación
centroidX = x + w/2
centroidY = x + h/2
a = int(centroidY - h/5)
b = int(centroidY + h/5)
c = int(centroidX-w/2)
d = int(centroidX+w/2)
Iprueba = im[c:d , a:b]
#Se genera un kernel horizontal para erosionar los segmentos verticales de la imagen
kernel_h = np.ones((1,10),np.uint8)
#Se genera un kernel de 5x5 para utilizar la operación morfológica de cerrado
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(Iprueba, kernel_h, iterations = 1)
erosion=bwareafilt(erosion)
erosion = cv.normalize(src=erosion, dst=None, alpha=0, beta=255,
                       norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
close = cv.morphologyEx(erosion, cv.MORPH_CLOSE, kernel)
#Se hallan los contornos de la imagen para poder hallar el boundingRectangle
im2,contours2,hierarchy2 = cv.findContours(close, 1, 2)
cnt2 = contours2[0]
rect2 = cv.minAreaRect(cnt2)
box = cv.boxPoints(rect2)
box = np.int0(box)
cv.drawContours(im2,[box],0,color,2)
cv.imshow('Prueba5',close)
cv.waitKey()
#Se obtienen las coordenadas de los vértices de del boundingRectangle para luego
#hallar la pendiente de una recta entre vértices continuos y así hallar el ángulo
x1 = box[0,0]
x2 = box[1,0]

y1 = box[0,1]
y2 = box[1,1]

angulo = np.arctan((y1-y2)/(x1-x2))
angulo = angulo * 180/np.pi
print ("Este es el angulo ")
print (angulo)