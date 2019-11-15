import numpy as np
#import matplotlib.pyplot as plt
import cv2
import json, time
import random as rng

def nothing(x):
    pass

def bubbleSort(arr):
    
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bwareafilt(image,n):
    n = n + 1
    image = image.astype(np.uint8)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
    sizes = stats[:, -1]

    lista_label = np.zeros(sizes.shape)
    sizes2 = sizes.copy()
    bubbleSort(sizes2)

    sizes2 = sizes2[::-1]

    for i in range(0, sizes.size - 1):
        for j in range(0, sizes.size - 1):
            if sizes2[i] == sizes[j]:
                lista_label[i] = j


    m = 0
    if n > sizes.size:
        m = sizes.size
    else:
        m = n

    img2 = np.zeros(output.shape)


    for i in range(1, m):
        img2[output == lista_label[i]] = 255

    return img2


def morfologia(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

    mascara_rojo_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    mascara_rojo_close = cv2.morphologyEx(mascara_rojo_open, cv2.MORPH_CLOSE, kernel)

    return mascara_rojo_close


def boundingboxcolectivo(mask2,n,M,N,frame):
    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (_,contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    try:
        cnt = contours[0]
    except:
        cnt = None

    if cnt is not None:

        listax = []
        listay = []
        listax1 = []
        listay1 = []
        listaw = []
        listah = []
        for i in range(0, n):
            try:
                cnt = contours[i]
            except:
                break
            x, y, w, h = cv2.boundingRect(cnt)
            x1 = x + w
            y1 = y + h
            listax.append(x)
            listay.append(y)
            listax1.append(x1)
            listay1.append(y1)
            listaw.append(w)
            listah.append(h)
            color = (255, 0, 0)

        bubbleSort(listax)
        bubbleSort(listay)
        bubbleSort(listax1)
        bubbleSort(listay1)

        Xc = (listax[0] + listax1[-1] )/ 2 - N/2
        Yc =  (listay[0]+ listay1[-1]) / 2 - M/2
        Area =  (listay1[-1] - listay[0]) * (listax1[-1] - listax[0])
        
        mp = int(Xc + N/2 - 3)
        np = int(Yc + M/2 - 3)
        cv2.rectangle(frame, (listax[0], listay[0]), (listax1[-1], listay1[-1]), color, 2)
        cv2.rectangle(frame, (mp,np), (mp+6,np+6), color, 3)
        cv2.rectangle(frame,(int(N/2) - 3, int(M/2) - 3),(int(N/2) + 3, int(M/2) + 3), color, 3)
        return (Xc,Yc,Area,frame)
        salida = np.zeros((M, N * 2, 3), dtype='uint8')
        salida[0:M, 0:N] = frame
        salida[0:M, N:N * 2, 0] = mask2

    else:

        salida = np.zeros((M, N * 2, 3), dtype='uint8')
        salida[0:M, 0:N] = frame
        salida[0:M, N:N * 2, 0] = mask2

        return (0,0,0,frame)


def boundingboxunitario(mask2,n,M,N,frame):

    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (_,contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    try:
        cnt = contours[0]
    except:
        cnt = None

    if cnt is not None:

        listax = []
        listay = []
        listax1 = []
        listay1 = []
        listaXc = []
        listaYc = []
        listaArea = []

        for i in range(0, n):

            try:
                cnt = contours[i]
            except:
                break

            x, y, w, h = cv2.boundingRect(cnt)
            x1 = x + w
            y1 = y + h
            Area = w * h
            Xc = x + (w / 2) - N / 2
            Yc = y + (h / 2) - M / 2
            listax.append(x)
            listay.append(y)
            listax1.append(x1)
            listay1.append(y1)
            listaXc.append(Xc)
            listaYc.append(Yc)
            listaArea.append(Area)
            color = (255, 0, 0)
            cv2.rectangle(mask2, (listax[i], listay[i]), (listax1[i], listay1[i]), color, 2)

        salida = np.zeros((M, N * 2, 3), dtype='uint8')
        salida[0:M, 0:N] = frame
        salida[0:M, N:N * 2, 0] = mask2
        #cv2.imshow("Clase01_color", mask2)
        return(listaXc,listaYc,listaArea,mask2)


    else:

        salida = np.zeros((M, N * 2, 3), dtype='uint8')
        salida[0:M, 0:N] = frame
        salida[0:M, N:N * 2, 0] = mask2
        #cv2.imshow("Clase01_color", mask2)
        return (0,0,0,frame)


def coorBoundingBoxes(frame,n,mnh, mxh, mns, mxs, mnv, mxv):

    
    print("mnh{},mxh{},mns{},mxs{},mnv{},mxv{}".format(mnh, mxh, mns, mxs, mnv, mxv))
    M,N = frame.shape[:2]


    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    rojo_bajos = np.array([mnh, mns, mnv], dtype=np.uint8)
    rojo_altos = np.array([mxh, mxs, mxv], dtype=np.uint8)
    mascara_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos) 

    mask = morfologia(mascara_rojo)

    mask2 = bwareafilt(mask,n)

    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (_,contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    try:
        cnt = contours[0]
    except:
        cnt = None

    if cnt is not None:

            
        (Xc, Yc, Area, im) = boundingboxcolectivo(im, n, M, N, frame)
        print(Xc)
        print(Yc)
        print(Area)
        
        return(Xc,Yc,Area,im)
        
    else:

        salida = boundingboxunitario(mask2,n,M,N,frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            DefVal = {'maxHue': mxh,
                      'minHue': mnh,
                      'maxSat': mxs,
                      'minSat': mns,
                      'maxVal': mxv,
                      'minVal': mnv}
            with open('initialValues.json', 'w') as outfile:
                 json.dump(DefVal, outfile)
                    
        return(0,0,0,frame)

    DefVal = {'maxHue' : mxh,
              'minHue' : mnh,
              'maxSat' : mxs,
              'minSat' : mns,
              'maxVal' : mxv,
              'minVal' : mnv}
    with open('initialValues.json', 'w') as outfile:
        json.dump(DefVal, outfile)
