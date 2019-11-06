import cv2 as cv2
import numpy as np

def bwareafilt(image):
    image = image.astype(np.uint8)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
    sizes = stats[:, -1]

    max_label = 1
    max_label2 = 1

    max_size = sizes[1]
    max_size2 = 0

    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]
            max_size2 = max_size

        if sizes[i] > max_size2:
            max_label2 = sizes[i]
            max_size2 = sizes[i]

    img2 = np.zeros(output.shape)
    img2[output == max_label] = 255
    img2[output == max_label2] = 255

    return img2


frame = cv2.imread('rojito.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

rojo_bajos = np.array([170,100,100], dtype=np.uint8)
rojo_altos = np.array([179,255,255], dtype=np.uint8)
mascara_rojo1 = cv2.inRange(hsv, rojo_bajos, rojo_altos)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))

mascara_rojo1 = cv2.morphologyEx(mascara_rojo1, cv2.MORPH_OPEN, kernel)
mascara_rojo1 = cv2.morphologyEx(mascara_rojo1, cv2.MORPH_CLOSE, kernel)

mask = mascara_rojo1

#imagen = bwareafilt(mask)
cv2.imshow('imagen',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

