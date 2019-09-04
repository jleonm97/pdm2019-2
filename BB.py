from __future__ import print_function
import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random as rng
cap = cv2.VideoCapture(0)
while(True):
    ret, src = cap.read()
    # Convert image to gray and blur it
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    src_gray=((src_gray>5)&(src_gray<200))*255
    src_gray=np.uint8(src_gray)
    kernel1 = np.ones((100,100),np.uint8)
    src_gray =  cv2.morphologyEx(src_gray, cv2.MORPH_OPEN, kernel1)
    #kernel2 = np.ones((50,50),np.uint8)
    #src_gray =  cv2.morphologyEx(src_gray, cv2.MORPH_CLOSE, kernel2)
    canny_output = cv2.Canny(src_gray, 50, 150) 
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
    
    
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
    
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.drawContours(drawing, contours_poly, i, color)
        cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
       # cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
    #cv2.namedWindow(source_window)
    neg=drawing==0
    img=src*neg+drawing
    cv2.imshow('contours',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()