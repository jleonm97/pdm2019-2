# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import cv2 as cv

cap = cv.VideoCapture(0)

leido, frame = cap.read()

if leido == True:
    cv.imwrite("foto.png", frame)
    print ("C logró")
    cv.imshow('foto',frame)
    cv.waitKey(0)
    
else:
    print ("Nel")
    
cap.release()
