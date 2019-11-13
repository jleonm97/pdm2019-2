import time
import libmaestro
import numpy as np
import matplotlib.pyplot as plt
#import cv2
import random as rng
import requests
import json

url = "http://192.168.10.28:3000/AltoenGA"
obj=libmaestro.Maestro()
k=1500 #Duty cycle para mantener motores estticos
#Se conecta cada motor a un pin del minimaestro
m1=1
m2=2
m3=3
m4=4
m5=5
m6=6
m7=7
m8=8
for i in range (1,9):
 obj.setMS(i,k)
print("probando")

def duty(k):
    k=float(k)
    if (k>=0):
      t=0.0299*k+0.005
      p=12.379*t**5-99.227*t**4+291.93*t**3-396.86*t**2+339.84*t+1500.8
      print(p,t)
      time.sleep(1)
    elif k<0:
      t=-0.0235*k-0.0017
      p=12.379*t**5-99.227*t**4+291.93*t**3-396.86*t**2+339.84*t+1500.8
    return p
      
def nothing(x):
    pass


#def bubbleSort(arr):
#    n = len(arr)
#
#    # Traverse through all array elements
#    for i in range(n):
#
#        # Last i elements are already in place
#        for j in range(0, n - i - 1):
#
#            # traverse the array from 0 to n-i-1
#            # Swap if the element found is greater
#            # than the next element
#            if arr[j] > arr[j + 1]:
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
#def bwareafilt(image, n):
#    n = n + 1
#    image = image.astype(np.uint8)
#    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
#    sizes = stats[:, -1]
#
#    lista_label = np.zeros(sizes.shape)
#    sizes2 = sizes.copy()
#    bubbleSort(sizes2)
#
#    sizes2 = sizes2[::-1]
#
#    for i in range(0, sizes.size - 1):
#        for j in range(0, sizes.size - 1):
#            if sizes2[i] == sizes[j]:
#                lista_label[i] = j
#
#    m = 0
#    if n > sizes.size:
#        m = sizes.size
#    else:
#        m = n
#
#    img2 = np.zeros(output.shape)
#
#    for i in range(1, m):
#        img2[output == lista_label[i]] = 255
#
#    return img2
#
#def obtenerN1N2():
#    cap = cv2.VideoCapture(0)
#    cv2.namedWindow("Clase01_color", cv2.WINDOW_NORMAL)
#    ret, frame = cap.read()
#
#    # frame = cv2.imread('bola1.jpg')
#
#    M, N = frame.shape[:2]
#
#    cv2.createTrackbar('min_h', "Clase01_color", 18, 255, nothing)
#    cv2.createTrackbar('max_h', "Clase01_color", 42, 255, nothing)
#    cv2.createTrackbar('min_s', "Clase01_color", 101, 255, nothing)
#    cv2.createTrackbar('max_s', "Clase01_color", 220, 255, nothing)
#    cv2.createTrackbar('min_v', "Clase01_color", 104, 255, nothing)
#    cv2.createTrackbar('max_v', "Clase01_color", 181, 255, nothing)
#    #86
#    # while (True):
#    # ret,frame = cap.read()
#
#    while (cap.isOpened()):  # play the video by reading frame by frame
#        ret, frame = cap.read()
#
#        mnh = cv2.getTrackbarPos("min_h", "Clase01_color")
#        mxh = cv2.getTrackbarPos("max_h", "Clase01_color")
#        mns = cv2.getTrackbarPos("min_s", "Clase01_color")
#        mxs = cv2.getTrackbarPos("max_s", "Clase01_color")
#        mnv = cv2.getTrackbarPos("min_v", "Clase01_color")
#        mxv = cv2.getTrackbarPos("max_v", "Clase01_color")
#
#        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
#
#        # Rango de colores detectados:
#
#        # Rojo Bajo:
#        rojo_bajos = np.array([mnh, mns, mnv], dtype=np.uint8)
#        rojo_altos = np.array([mxh, mxs, mxv], dtype=np.uint8)
#        mascara_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos)
#
#        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
#
#        mascara_rojo_open = cv2.morphologyEx(mascara_rojo, cv2.MORPH_OPEN, kernel)
#        mascara_rojo_close = cv2.morphologyEx(mascara_rojo, cv2.MORPH_CLOSE, kernel)
#        # mascara_rojo1 = cv2.morphologyEx(mascara_rojo1, cv2.MORPH_ERODE, kernel)
#
#        # Unir las dos masCARAS
#        mask = mascara_rojo_close
#        mask2 = bwareafilt(mask, 1)
#        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
#        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
#        im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
#        (_,contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
#
#        try:
#            cnt = contours[0]
#
#        except:
#            cnt = None
#
#        if cnt is not None:
#
#            cnt = contours[0]
#            x, y, w, h = cv2.boundingRect(cnt)
#            color = (255, 0, 0)
#            cv2.rectangle(mask2, (x, y), (x + w, y + h), color, 2)
#
#            Xc = x + (w / 2) - N/2
#            Yc = y + (h / 2) - M/2
#
#            text1 = "Xc : {}".format(Xc)
#            text2 = "Yc : {}".format(Yc)
#
#            cv2.putText(frame, text1, (50, 60), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 255))
#            cv2.putText(frame, text2, (50, 120), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 255))
#
#            salida = np.zeros((M, N * 2, 3), dtype='uint8')
#            salida[0:M, 0:N] = frame
#            salida[0:M, N:N * 2, 0] = mask2
#            if (w*h < 0.9*M*N) & (w*h > 0.01*M*N):
#                Area = w*h
#                li = []
#                li.append(Xc)
#                li.append(Yc)
#                li.append(Area)
#
#                print(Xc)
#                print(Yc)
#                print(Area)
#                cap.release()
#                cv2.destroyAllWindows()
#                return li
#                break
#
#        else:
#
#            salida = np.zeros((M, N * 2, 3), dtype='uint8')
#            salida[0:M, 0:N] = frame
#            salida[0:M, N:N * 2, 0] = mask2
#
#        cv2.imshow("Clase01_color", salida)
#
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break
#
#    cap.release()
#    cv2.destroyAllWindows()


print("probando deteccion, avance y luego giro")
try:
  while True:
     try:
       li0 = requests.get(url)
       print(li0)
       li1 = json.loads(li0.text)
       print(li1)
       li = []
#                li.append(Xc)
#                li.append(Yc)
#                li.append(Area)
       li.append(li1["X"]) 
       li.append(li1["Y"]) 
       li.append(li1["Area"])
     except:
       print("Error mio")
       break
     #li = obtenerN1N2() #FUNCION SHAVO
     
     N2 = li[1]
     kdown = int(duty(21))
     kdown1 = 1500 - (kdown-1500)
     obj.setMS(m1,kdown1)
     obj.setMS(m3,kdown)
     obj.setMS(m5,kdown1)
     obj.setMS(m6,kdown)
     obj.setMS(m4,k)
     obj.setMS(m7,k)
     obj.setMS(m2,k)
     obj.setMS(m8,k)
     time.sleep(3)   
     while True:
         AreaSup1 = li[2]
         if AreaSup1 > 0.3*1280*720 :
           N1 = li[0]
           print(N1)
           K = 0.02*N1  #Indicador de potencia a turbinas K = [0;100]
           k2 = int(duty(int(K)))  
           # k2= 1620
           k1=1500-(k2-1500)
           obj.setMS(m4,k2)
           obj.setMS(m7,k2)
           obj.setMS(m2,k1)
           obj.setMS(m8,k2)
           #print("girando xd")
           N1vef = li[0]
         if N1vef < 55:
           break
     print("vamo pa adelante")
     obj.setMS(m4,1500)
     obj.setMS(m7,1500)
     obj.setMS(m2,1500)
     obj.setMS(m8,1500)
     time.sleep(1)
     k22 = 1620
     k11 = 1500 - (k22-1500)    
     obj.setMS(m4,k22)
     obj.setMS(m7,k11)
     obj.setMS(m2,k22)
     obj.setMS(m8,k22)     
     while True:
         liArea = li[2]
         AreaSup = li[2]
         if AreaSup > 1280*720*0.1:
           break
     obj.setMS(m4,1500)
     obj.setMS(m7,1500)
     obj.setMS(m2,1500)
     obj.setMS(m8,1500)                              
     time.sleep(10)
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")
  obj.setMS(m3,1500)
  obj.setMS(m1,1500)
  obj.setMS(m5,1500)
  obj.setMS(m6,1500)
  obj.setMS(m2,1500)
  obj.setMS(m4,1500)
  obj.setMS(m7,1500)
  obj.setMS(m8,1500)
  for j in range (1,9):
    obj.setMS(j,k)
  # -*- coding: utf-8 -*-
