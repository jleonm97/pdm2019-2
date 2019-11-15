from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Response
import json
from imutils.video import VideoStream #
import threading #
import argparse #
import datetime #
import imutils #
import time #
import cv2 as cv


main = Blueprint('main', __name__)

angulo = 0

slider = 0

paquete = {'X':0, 'Y':0}

centro = {"X":0, "Y":0, "Area":0}

with open('initialValues.json') as json_file:
		datos = json.load(json_file)
   
mnh = int(datos['minHue'])
mxh = int(datos['maxHue'])
mns = int(datos['minSat'])
mxs = int(datos['maxSat'])
mnv = int(datos['minVal'])
mxv = int(datos['maxVal'])

pruebaJ = {"Slider1":mxh,"Slider2":mnh,"Slider3":mxs,"Slider4":mns,"Slider5":mxv,"Slider6":mnv}

prueba3 = {"Slider1":mxh,"Slider2":mnh,"Slider3":mxs,"Slider4":mns,"Slider5":mxv,"Slider6":mnv}

controlM = {"m":0,"f":0,"t":0,"h":0,"g":0}

outputFrame = None
#
lock = threading.Lock()
#
#vs = VideoStream(src=0).start()
time.sleep(2.0)
#vs.stop()
def guardar():
    global prueba3
    return prueba3

@main.route('/', methods=['GET','POST'])

def index():
    
    global slider
    
    if request.method == 'POST':
    
      slider = request.form["slider"]
      return render_template('home.html')
    
    else:
      
      return render_template('home.html')

def generate():
    global outputFrame, lock
    
    cap = cv.VideoCapture(0)
    
    while True:
      ret,frame = cap.read()
      encodedImage = cv.imencode(".jpg",frame)
      yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
    
#def detect_motion():
@main.route("/video_feed")
def video_feed():
    return Response(generate(),	mimetype = "multipart/x-mixed-replace; boundary=frame")    

    
@main.route('/am')

def index_post():
   
    return render_template('video.html')

@main.route('/recibir', methods = ['GET', 'POST'])

def recibir():
  
  global angulo
  
  angulo = request.args.get('angulo')
  
  if angulo != None:
    
    return '''{}'''.format(angulo) 
    
  else:
  
    return ' '
  #return 'El angulo es {}'.format(angulo)

@main.route('/env', methods = ['GET'])  

def enviar():
  
  global angulo
  global paquete
  
  return '''<meta http-equiv="refresh" content="1"/>El angulo es {} y el slider {}'''.format(angulo,paquete)

@main.route('/pb1', methods = ['GET'])

def pb1():
  meen = '?pb=1'
  
  return redirect(url_for('main.pb2',name = meen))
  
#@main.route('/GA', methods = ['POST','GET'])
#def ga():
#  
#  if request.method == 'POST':
#    global prueba
#    prueba = request.json
#    return 'GA'
#  else:
#    return jsonify(prueba)
  
@main.route('/Prueba', methods = ['POST', 'GET'])
def pruebaR():
  
  global paquete
  
  if request.method == 'POST':
  
    paquete = request.json
    return 'Bien'
    
  else:
    return jsonify(paquete)

@main.route('/pb2/<name>', methods = ['GET'])

def pb2():
  
  pbb = request.args.get('pb')
  
  return '''{}'''.format(pbb)
  
@main.route('/John', methods = ['POST', 'GET'])

def John():

  global pruebaJ
  
  if request.method == 'POST':
  
    pruebaJ = request.values
    
    #print(pruebaJ)
    return 'A'
    
  else:
    #pruebaJ = request.json
    return jsonify(pruebaJ)  

@main.route('/Prueba3', methods = ['POST', 'GET'])

def Prueba3():

  global prueba3
  
  if request.method == 'POST':
  
    prueba3 = request.json
    
    print(prueba3)
    return 'A'
    
  else:
    #prueba3 = request.json
    return jsonify(prueba3)
    
@main.route('/Control', methods = ['POST', 'GET'])

def Control():

  global controlM
  
  if request.method == 'POST':
  
    controlM = request.values
    
    print(controlM)
    return 'A'
    
  else:
    #prueba3 = request.json
    return jsonify(controlM)
    
#AltoenGA
@main.route('/AltoenGA', methods = ['POST', 'GET'])

def AltoenGA():

  global centro
  
  if request.method == 'POST':
  
    centro = request.json
    
    #print(centro)
    return 'A'
    
  else:
    #prueba3 = request.json
    return jsonify(centro)
@main.route('/am')

def index_post():
   
    return render_template('video.html')

@main.route('/recibir', methods = ['GET', 'POST'])

def recibir():
  
  global angulo
  
  angulo = request.args.get('angulo')
  
  if angulo != None:
    
    return '''{}'''.format(angulo) 
    
  else:
  
    return ' '
  #return 'El angulo es {}'.format(angulo)

@main.route('/env', methods = ['GET'])  

def enviar():
  
  global angulo
  global paquete
  
  return '''<meta http-equiv="refresh" content="1"/>El angulo es {} y el slider {}'''.format(angulo,paquete)

@main.route('/pb1', methods = ['GET'])

def pb1():
  meen = '?pb=1'
  
  return redirect(url_for('main.pb2',name = meen))
  
#@main.route('/GA', methods = ['POST','GET'])
#def ga():
#  
#  if request.method == 'POST':
#    global prueba
#    prueba = request.json
#    return 'GA'
#  else:
#    return jsonify(prueba)
  
@main.route('/Prueba', methods = ['POST', 'GET'])
def pruebaR():
  
  global paquete
  
  if request.method == 'POST':
  
    paquete = request.json
    return 'Bien'
    
  else:
    return jsonify(paquete)

@main.route('/pb2/<name>', methods = ['GET'])

def pb2():
  
  pbb = request.args.get('pb')
  
  return '''{}'''.format(pbb)
  
@main.route('/John', methods = ['POST', 'GET'])

def John():

  global pruebaJ
  
  if request.method == 'POST':
  
    pruebaJ = request.values
    
    #print(pruebaJ)
    return 'A'
    
  else:
    #pruebaJ = request.json
    return jsonify(pruebaJ)  

@main.route('/Prueba3', methods = ['POST', 'GET'])

def Prueba3():

  global prueba3
  
  if request.method == 'POST':
  
    prueba3 = request.json
    
    print(prueba3)
    return 'A'
    
  else:
    #prueba3 = request.json
    return jsonify(prueba3)
    
@main.route('/Control', methods = ['POST', 'GET'])

def Control():

  global controlM
  
  if request.method == 'POST':
  
    controlM = request.values
    
    print(controlM)
    return 'A'
    
  else:
    #prueba3 = request.json
    return jsonify(controlM)
