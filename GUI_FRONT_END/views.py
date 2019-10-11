from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Response
import json,
import imutils.video import VideoStream
import threading
import argparse
import datetime
import imutils
import time
import cv2 as cv


main = Blueprint('main', __name__)

angulo = 0

slider = 0

paquete = {'X':0, 'Y':0}

pruebaJ = {"Slider1":0,"Slider2":0,"Slider3":0,"Slider4":0,"Slider5":0,"Slider6":0}

@main.route('/', methods=['GET','POST'])

outputFrame = None

lock = threading.Lock()

vs = VideoStream(src=0).start()

def index():
    
    global slider
    
    if request.method == 'POST':
    
      slider = request.form["slider"]
      return render_template('home.html')
    
    else:
      
      return render_template('home.html')

def detect_motion():
    
    
    
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
    
    print(pruebaJ)
    return 'A'
    
  else:
    #pruebaJ = request.json
    return jsonify(pruebaJ)  