# import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
import imutils
import cv2
import random as rng

class SingleMotionDetector:
	def __init__(self, accumWeight=0.5):
		# store the accumulated weight factor
		self.accumWeight = accumWeight

		# initialize the background model
		self.bg = None

	def update(self, image):
		# if the background model is None, initialize it
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return

		# update the background model by accumulating the weighted
		# average
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)

	def detect(self, image, tVal=25):
		# compute the absolute difference between the background model
		# and the image passed in, then threshold the delta image
		delta = cv2.absdiff(self.bg.astype("uint8"), image)
		thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1]

		# perform a series of erosions and dilations to remove small
		# blobs
		thresh = cv2.erode(thresh, None, iterations=2)
		thresh = cv2.dilate(thresh, None, iterations=2)

		# find contours in the thresholded image and initialize the
		# minimum and maximum bounding box regions for motion
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		(minX, minY) = (np.inf, np.inf)
		(maxX, maxY) = (-np.inf, -np.inf)

		# if no contours were found, return None
		if len(cnts) == 0:
			return None

		# otherwise, loop over the contours
		for c in cnts:
			# compute the bounding box of the contour and use it to
			# update the minimum and maximum bounding box regions
			(x, y, w, h) = cv2.boundingRect(c)
			(minX, minY) = (min(minX, x), min(minY, y))
			(maxX, maxY) = (max(maxX, x + w), max(maxY, y + h))

		# otherwise, return a tuple of the thresholded image along
		# with bounding box
		return (thresh, (minX, minY, maxX, maxY))
	def bubbleSort(self,arr):
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
                  
	def bwareafilt(self,image,n):
		n = n + 1
		image = image.astype(np.uint8)
		nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
		sizes = stats[:, -1]

		lista_label = np.zeros(sizes.shape)
		sizes2 = sizes.copy()
		self.bubbleSort(sizes2)

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
	
	def detect2(self, frame, mnh, mxh, mns, mxs, mnv, mxv, tVal=25):
		frame = cv2.normalize(src=frame, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
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
		mask2 = self.bwareafilt(mask,1)
		im = cv2.normalize(src=mask2, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
		(__,contours, hierarchy) = cv2.findContours(image=im, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
		try:
			cnt=contours[0]
		except:
			cnt=None
			return None
		if cnt is not None:
			# otherwise, loop over the contours
			for c in cnt:
				# compute the bounding box of the contour and use it to
				# update the minimum and maximum bounding box regions
				(minX, minY) = (np.inf, np.inf)
				(maxX, maxY) = (-np.inf, -np.inf)
				(x, y, w, h) = cv2.boundingRect(cnt)
				#cv2.imshow('GAA', frame)
				print("{},{},{},{}".format(x,y,w,h))
				(minX, minY) = (x, y)
				(maxX, maxY) = (x+w, y+h)

		# otherwise, return a tuple of the thresholded image along
		# with bounding box
			return (frame, (minX, minY, maxX, maxY))
		else:
			return None

"""
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

		return (thresh, (minX, minY, maxX, maxY))

"""