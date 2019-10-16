from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Response
import json,
import imutils.video import VideoStream
import threading
import argparse
import datetime
import imutils
import time
import cv2 as cv

#Definicion del blueprint que se utilizará en Inicial.py
main = Blueprint('main', __name__)
#Inicialización de variables globales
angulo = 0
slider = 0
paquete = {'X':0, 'Y':0}
pruebaJ = {"Slider1":0,"Slider2":0,"Slider3":0,"Slider4":0,"Slider5":0,"Slider6":0}
#Página principal, donde se mostrará la plantilla home.html
#Esta página solo utilizará el método GET
@main.route('/', methods=['GET'])
outputFrame = None

def index():
    
    return render_template('home.html')
#Página de prueba donde se muestra la plantilla video.html que muestra un video
@main.route('/video')
def index_post():
   
    return render_template('video.html')
#Página de prueba donde se recibe un dato en formato JSON.
#Cuando un programa envía un request de método POST, esta página recibe el dato y lo guarda en una variable global
#Cuando un programa envía un request de método GET, esta página envía la variable global guardada, cambiando su tipo a JSON
#Esta sirve para comunicar programas en python con programas en javascript: python--->javascript
#Esta se utilizará para enviar los ángulos medidos y así mover la figura 3D
@main.route('/Prueba', methods = ['POST', 'GET'])
def pruebaR():
  
  global paquete
  
  if request.method == 'POST':
  
    paquete = request.json
    return 'Bien'
    
  else:
  
    return jsonify(paquete)
#Página de prueba donde se recibe un dato de un programa en javascript
#Cuando un programa envía un request de método POST, esta página recibe el dato y lo guarda en una variable global
#Cuando un programa envía un request de método GET, esta página envía la variable global guardada, cambiando su tipo a JSON
#Esta sirve para comunicar programas en javascript con programas en python: javascript--->python
#Esta se utilizará para enviar los datos de los scrollbars de la interfaz al programa de calibración
@main.route('/Prueba2', methods = ['POST', 'GET'])
def Prueba2():

  global pruebaJ
  
  if request.method == 'POST':
  
    pruebaJ = request.values
    
    print(pruebaJ)
    return 'A'
    
  else:
    
    return jsonify(pruebaJ)  
