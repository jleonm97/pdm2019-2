import numpy as np
import matplotlib.pyplot as plt
import cv2 
import random as rng

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
    image1 = image.astype(np.uint8)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image1, connectivity=4)

    try:
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
    except:

        return image



cap = cv2.VideoCapture('C:/Users/Valverde/Desktop/codigos_pdm/hsv/videopelota.mp4')
cv2.namedWindow("Clase01_color",cv2.WINDOW_NORMAL)
ret,frame = cap.read()

#frame = cv2.imread('bola1.jpg')

M,N = frame.shape[:2]


cv2.createTrackbar('min_h',"Clase01_color",50,180,nothing)
cv2.createTrackbar('max_h',"Clase01_color",86,180,nothing)
cv2.createTrackbar('min_s',"Clase01_color",56,255,nothing)
cv2.createTrackbar('max_s',"Clase01_color",255,255,nothing)
cv2.createTrackbar('min_v',"Clase01_color",107,255,nothing)
cv2.createTrackbar('max_v',"Clase01_color",218,255,nothing)

#while (True):
    #ret,frame = cap.read()

while(cap.isOpened()):                    # play the video by reading frame by frame
    ret, frame = cap.read()

    mnh = cv2.getTrackbarPos("min_h","Clase01_color")
    mxh = cv2.getTrackbarPos("max_h","Clase01_color")
    mns = cv2.getTrackbarPos("min_s","Clase01_color")
    mxs = cv2.getTrackbarPos("max_s","Clase01_color")
    mnv = cv2.getTrackbarPos("min_v","Clase01_color")
    mxv = cv2.getTrackbarPos("max_v","Clase01_color")

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # Rango de colores detectados:

    # Rojo Bajo:
    rojo_bajos = np.array([mnh, mns, mnv], dtype=np.uint8)
    rojo_altos = np.array([mxh, mxs, mxv], dtype=np.uint8)
    mascara_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

    mascara_rojo_open = cv2.morphologyEx(mascara_rojo, cv2.MORPH_OPEN, kernel)
    mascara_rojo_close = cv2.morphologyEx(mascara_rojo, cv2.MORPH_CLOSE, kernel)
    #mascara_rojo1 = cv2.morphologyEx(mascara_rojo1, cv2.MORPH_ERODE, kernel)

    # Unir las dos masCARAS
    mask = mascara_rojo_close
    mask2 = bwareafilt(mask,1)
    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    color = (255, 0, 0)
    cv2.rectangle(mask2, (x, y), (x + w, y + h), color, 2)

    Xc = x + w / 2
    Yc = y + h / 2

    text1 = "Xc : {}".format(Xc)
    text2 = "Yc : {}".format(Yc)

    cv2.putText(frame, text1, (50, 60), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 255))
    cv2.putText(frame, text2, (50, 120), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 255))

    salida = np.zeros((M , N * 2, 3), dtype='uint8')
    salida[0:M, 0:N] = frame
    salida[0:M, N:N * 2,0] = mask2
    
    cv2.imshow("Clase01_color", salida)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()