import cv2 as cv
import numpy as np

clasi = cv.imread('/home/pi/Interfaz/static/asets/backround.jpg')
clasi = cv.cvtColor(clasi, cv.COLOR_BGR2RGB)

#ret,tsk1 = cv.threshold(,thresh,255,0)