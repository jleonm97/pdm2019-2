# USAGE
# python webstreaming.py --ip 0.0.0.0 --port 8000

# import the necessary packages
from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2
import json
import requests

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing tthe stream)
outputFrame = None
lock = threading.Lock()

# initialize a flask object
app = Flask(__name__)

# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)

url = 'http://10.100.186.188:3000/Prueba3'
url2 = 'http://10.100.186.188:3000/John'

#DefVal = {'Slider1':mxh,
#          'Slider2':mnh,
#          'Slider3':mxs,
#          'Slider4':mns,
#          'Slider5':mxv,
#          'Slider6':mnv}
#
#r = requests.post(url, json = DefVal)

@app.route("/")
def index():

	global url
  
	# return the rendered template
	with open('initialValues.json') as json_file:
		datos = json.load(json_file)
	mnh = int(datos['minHue'])
	mxh = int(datos['maxHue'])
	mns = int(datos['minSat'])
	mxs = int(datos['maxSat'])
	mnv = int(datos['minVal'])
	mxv = int(datos['maxVal'])
	DefVal = {'Slider1':mxh,
          'Slider2':mnh,
          'Slider3':mxs,
          'Slider4':mns,
          'Slider5':mxv,
          'Slider6':mnv}

	r = requests.post(url, json = DefVal)
	return render_template("index.html")

def detect_motion(frameCount):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock, mnh, mxh, mns, mxs, mnv, mxv, url2

	# initialize the motion detector and the total number of frames
	# read thus far
	md = SingleMotionDetector(accumWeight=0.1)
	total = 0

	# loop over frames from the video stream
	while True:
		try:
			var2 = requests.get(url2)
			var3 = json.loads(var2.text)
		except:
			break
      
		mnh = int(var3['Slider2'])
		mxh = int(var3['Slider1'])
		mns = int(var3['Slider4'])
		mxs = int(var3['Slider3'])
		mnv = int(var3['Slider6'])
		mxv = int(var3['Slider5'])
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
#		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#		gray = cv2.GaussianBlur(gray, (7, 7), 0)

		# grab the current timestamp and draw it on the frame
		#timestamp = datetime.datetime.now()
		#cv2.putText(frame, timestamp.strftime(
		#	"%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
		#	cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

		# if the total number of frames has reached a sufficient
		# number to construct a reasonable background model, then
		# continue to process the frame
		#if total > frameCount:
			# detect motion in the image
			#ingresar variables del scrollbar
		motion = md.detect2(frame, mnh, mxh, mns, mxs, mnv, mxv, 25)
      #detect2(self, image, tVal=25, mnh, mxh, mns, mxs, mnv, mxv):
			# cehck to see if motion was found in the frame
		if motion is not None:
				# unpack the tuple and draw the box surrounding the
				# "motion area" on the output frame
			(thresh, (minX, minY, maxX, maxY)) = motion
			cv2.rectangle(thresh, (minX, minY), (maxX, maxY),(0, 0, 255), 2)
		
		# update the background model and increment the total number
		# of frames read thus far
		#md.update(gray)
		total += 1

		# acquire the lock, set the output frame, and release the
		# lock
		with lock:
			#outputFrame = frame.copy()
			outputFrame = thresh.copy()
		
def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())

	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(
		args["frame_count"],))
	t.daemon = True
	t.start()

	# start the flask app
	app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
   
DefVal = {'maxHue':mxh,
          'minHue':mnh,
          'maxSat':mxs,
          'minSat':mns,
          'maxVal':mxv,
          'minVal':mnv}
with open('initialValues.json', 'w') as outfile:
		json.dump(DefVal, outfile)
# release the video stream pointer
vs.stop()