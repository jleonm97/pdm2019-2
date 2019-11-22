# Libreria para matrices
import numpy as np
import matplotlib.pyplot as plt
#Libreria para procesamiento de imagenes
import cv2
# Libreria para cargar y guardar archivos
import json, time
import random as rng

def nothing(x):
    pass
# Funcion para ordenar un arreglo de menor a mayor
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
# Funcion de filtro de tamaño, toma como parametro el numero de elementos deseados
def bwareafilt(image,n):
    n = n + 1
    # Convertimos la imagen en una matriz
    image = image.astype(np.uint8)
    # Equivalente a region props
    # nb_components: Numero de componentes
    # output: Equivalente a bwlabel, devuelve una imagen donde cada blob tiene un numero diferente
    # Stats: Vector con: vertice más proximo, Ancho, largo y área
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
    # Extraemos el area, usamos -1 ya que el area es el ultimo elemento del vector
    sizes = stats[:, -1]
    # Creamos una lista del mismo numero de elementos que los blobs
    lista_label = np.zeros(sizes.shape)
    # Creamos una copia de los tamaños
    sizes2 = sizes.copy()
    # Ordenamos esta copia
    bubbleSort(sizes2)
    # Invertimos el orden, ahora esta de mayor a menor
    sizes2 = sizes2[::-1]
    # Obtenemos los indices ordenados por tamaño de blobs
    for i in range(0, sizes.size - 1):
        for j in range(0, sizes.size - 1):
            if sizes2[i] == sizes[j]:
                lista_label[i] = j

    # Obtenemos el numero de blobs a filtrar, comparamos lo que necesitamos con lo que tenemos
    m = 0
    if n > sizes.size:
        m = sizes.size
    else:
        m = n
    # Creamos una imagen del mismo tamaño de la imagen actual
    img2 = np.zeros(output.shape)

    # Iteramos para resaltar los blobs deseados
    for i in range(1, m):
        img2[output == lista_label[i]] = 255

    return img2


def createTrackbar(datos):

    mnh = int(datos['minHue'])
    mxh = int(datos['maxHue'])
    mns = int(datos['minSat'])
    mxs = int(datos['maxSat'])
    mnv = int(datos['minVal'])
    mxv = int(datos['maxVal'])

    cv2.createTrackbar('min_h', "Clase01_color", mnh, 180, nothing)
    cv2.createTrackbar('max_h', "Clase01_color", mxh, 180, nothing)
    cv2.createTrackbar('min_s', "Clase01_color", mns, 255, nothing)
    cv2.createTrackbar('max_s', "Clase01_color", mxs, 255, nothing)
    cv2.createTrackbar('min_v', "Clase01_color", mnv, 255, nothing)
    cv2.createTrackbar('max_v', "Clase01_color", mxv, 255, nothing)

# Funcion para filtrar el ruido con morfologia
def morfologia(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

    mascara_rojo_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    mascara_rojo_close = cv2.morphologyEx(mascara_rojo_open, cv2.MORPH_CLOSE, kernel)

    return mascara_rojo_close

# Funcion que nos permite hallar bounding boxes de los objetos deseados y unirla en una
# mask2 es la imagen
# n es el numero de blobs a reconocer
# M y N son las dimensiones de la imagen
# Frame es la imagen obtenida de la camara


def boundingboxcolectivo(mask2,n,M,N,frame):

    #Convertimos la imagen a 8UC1 para que funcione el codigo
    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    # Obtenemos los contornos para sacar los bounding boxes
    (contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    # Verificamos que se pueden obtener bounding boxes
    try:
        cnt = contours[0]
    except:
        cnt = None

    if cnt is not None:
        # Creamos listas
        # Lista x,y tienen un vertice de los bounding boxes
        # Lista x1 y1 tienen el vertice opuesto
        # Listaw, listah tienen ancho y largo de cada bounding box
        listax = []
        listay = []
        listax1 = []
        listay1 = []
        listaw = []
        listah = []
        # Iteramos para cada blob mostrar
        for i in range(0, n):
            try:
                cnt = contours[i]
            except:
                break
            # Obtenemos los parametros del boundingbox
            x, y, w, h = cv2.boundingRect(cnt)
            x1 = x + w
            y1 = y + h
            # Guardamos los valores en la lista
            listax.append(x)
            listay.append(y)
            listax1.append(x1)
            listay1.append(y1)
            listaw.append(w)
            listah.append(h)
            color = (255, 0, 0)
        # Ordenamos las listas
        bubbleSort(listax)
        bubbleSort(listay)
        bubbleSort(listax1)
        bubbleSort(listay1)
        # Obtenemos las coordenadas del bounding box general asi como su area
        Xc = (listax[0] + listax1[-1] )/ 2 - N/2
        Yc =  (listay[0]+ listay1[-1]) / 2 - M/2
        Area =  (listay1[-1] - listay[0]) * (listax1[-1] - listax[0])

        # Obtenemos los parametros para crear dicho bounding box
        mp = int(Xc + N/2 - 3)
        np = int(Yc + M/2 - 3)
        #NUEVO: MODIFICACION
        cv2.rectangle(frame, (int(N / 2) - 3, int(M / 2) - 3), (int(N / 2) + 3, int(M / 2) + 3), color, 3)
        if Area<0.9*M*N:
            # Creamos los bounding boxes en la imagen obtenida por la camara
            cv2.rectangle(frame, (listax[0], listay[0]), (listax1[-1], listay1[-1]), color, 2)
            cv2.rectangle(frame, (mp,np), (mp+6,np+6), color, 3)
        #FIN
            # Devolvemos las coordenadas, su area y la imagen con bounding boxes
        return (Xc,Yc,Area,frame)

    else:

        salida = np.zeros((M, N * 2, 3), dtype='uint8')
        salida[0:M, 0:N] = frame
        salida[0:M, N:N * 2, 0] = mask2

        return salida


def boundingboxunitario(mask2,n,M,N,frame):

    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

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
        return salida

# Funcion principal: Obtiene las coordenadas de una imagen, necesita el cap de la videocaptura y el numero de objetos a detectar
def coorBoundingBoxes(cap,n,mnh,mxh,mns,mxs,mnv,mxv):


    cv2.namedWindow("Clase01_color",cv2.WINDOW_NORMAL)
    ret,frame = cap.read()


    # Obtenemos las dimensiones de la imagen
    M,N = frame.shape[:2]
    with open('initialValues.json') as json_file:
        datos = json.load(json_file)
    # Obtenemos los parametros del filtro HSV


    # Convertimos la imagen a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # Filtramos la imagen con los parametros obtenidos
    rojo_bajos = np.array([mnh, mns, mnv], dtype=np.uint8)
    rojo_altos = np.array([mxh, mxs, mxv], dtype=np.uint8)
    #Obtenemos la imagen filtrada
    mascara_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos)

    # Quitamos el ruido
    mask = morfologia(mascara_rojo)
    # Filtro de tamaño
    mask2 = bwareafilt(mask,n)
    # Normalizamos la imagen
    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    # Verificamos la existencia de bounding boxes
    try:
        cnt = contours[0]
    except:
        cnt = None

    if cnt is not None:

        # Obtenemos coordenadas del bounding box
        (Xc, Yc, Area, im) = boundingboxcolectivo(mask2, n, M, N, frame)
        print(Xc)
        print(Yc)
        print(Area)
        return(Xc,Yc,Area,im)


    else:

        salida = boundingboxunitario(mask2,n,M,N,frame)
        cv2.imshow("Clase01_color", salida)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            DefVal = {'maxHue': mxh,
                      'minHue': mnh,
                      'maxSat': mxs,
                      'minSat': mns,
                      'maxVal': mxv,
                      'minVal': mnv}
            with open('initialValues.json', 'w') as outfile:
                 json.dump(DefVal, outfile)
                    #break

    DefVal = {'maxHue' : mxh,
              'minHue' : mnh,
              'maxSat' : mxs,
              'minSat' : mns,
              'maxVal' : mxv,
              'minVal' : mnv}
    with open('initialValues.json', 'w') as outfile:
        json.dump(DefVal, outfile)




#NUEVO
def falla(cap):
    Xc = 0
    Yc = 0
    Area = 0
    ret, im = cap.read()
    M, N = im.shape[:2]
    color = (255, 0, 0)
    cv2.rectangle(im, (int(N / 2) - 3, int(M / 2) - 3), (int(N / 2) + 3, int(M / 2) + 3), color, 3)
    return(Xc,Yc,Area,im)

def coorBoundingBoxes2(cap,n,mnh,mxh,mns,mxs,mnv,mxv,mnh2,mxh2,mns2,mxs2,mnv2,mxv2):


    cv2.namedWindow("Clase01_color",cv2.WINDOW_NORMAL)
    ret,frame = cap.read()


    # Obtenemos las dimensiones de la imagen
    M,N = frame.shape[:2]
    with open('initialValues.json') as json_file:
        datos = json.load(json_file)
    # Obtenemos los parametros del filtro HSV


    # Convertimos la imagen a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # Filtramos la imagen con los parametros obtenidos
    color1_bajos = np.array([mnh, mns, mnv], dtype=np.uint8)
    color1_altos = np.array([mxh, mxs, mxv], dtype=np.uint8)
    #Obtenemos la imagen filtrada
    mascara_color1 = cv2.inRange(hsv, color1_bajos, color1_altos)

    # Filtramos la imagen con los parametros obtenidos
    color2_bajos = np.array([mnh2, mns2, mnv2], dtype=np.uint8)
    color2_altos = np.array([mxh2, mxs2, mxv2], dtype=np.uint8)
    # Obtenemos la imagen filtrada
    mascara_color2 = cv2.inRange(hsv, color2_bajos, color2_altos)
    mascaraTotal = cv2.add(mascara_color1,mascara_color2)
    # Quitamos el ruido
    mask = morfologia(mascaraTotal)
    # Filtro de tamaño
    mask2 = bwareafilt(mask,n)
    # Normalizamos la imagen
    im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    (contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    # Verificamos la existencia de bounding boxes
    try:
        cnt = contours[0]
    except:
        cnt = None

    if cnt is not None:

        # Obtenemos coordenadas del bounding box
        (Xc, Yc, Area, im) = boundingboxcolectivo(mask2, n, M, N, frame)
        print(Xc)
        print(Yc)
        print(Area)
        return(Xc,Yc,Area,im)


    else:

        salida = boundingboxunitario(mask2,n,M,N,frame)
        cv2.imshow("Clase01_color", salida)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            DefVal = {'maxHue': mxh,
                      'minHue': mnh,
                      'maxSat': mxs,
                      'minSat': mns,
                      'maxVal': mxv,
                      'minVal': mnv}
            with open('initialValues.json', 'w') as outfile:
                 json.dump(DefVal, outfile)
                    #break

    DefVal = {'maxHue' : mxh,
              'minHue' : mnh,
              'maxSat' : mxs,
              'minSat' : mns,
              'maxVal' : mxv,
              'minVal' : mnv}
    with open('initialValues.json', 'w') as outfile:
        json.dump(DefVal, outfile)