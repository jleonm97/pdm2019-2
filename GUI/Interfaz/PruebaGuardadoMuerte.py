# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:34:29 2019

@author: John
"""
import cv2
import json, requests, time

with open('initialValues.json') as json_file:
    datos = json.load(json_file)
    
mnh = int(datos['minHue'])
mxh = int(datos['maxHue'])
mns = int(datos['minSat'])
mxs = int(datos['maxSat'])
mnv = int(datos['minVal'])
mxv = int(datos['maxVal'])

url = 'http://10.100.186.125:3000/Prueba3'
url2 = 'http://10.100.186.125:3000/John'

DefVal = {'Slider1':mxh,
          'Slider2':mnh,
          'Slider3':mxs,
          'Slider4':mns,
          'Slider5':mxv,
          'Slider6':mnv}

r = requests.post(url, json = DefVal)
#r2 = requests.post(url2, json = DefVal)
cap = cv2.VideoCapture(0)
if cap is None:
  print("No se pudo")
else:
  print("Se pudo")
while True:
    try:
        var2 = requests.get(url2)
        var3 = json.loads(var2.text)
    except:
        break
    
    ret,frame = cap.read()
    
    mnh = int(var3['Slider2'])
    mxh = int(var3['Slider1'])
    mns = int(var3['Slider4'])
    mxs = int(var3['Slider3'])
    mnv = int(var3['Slider6'])
    mxv = int(var3['Slider5'])
    
    cv2.imwrite("imagenPrueba.jpg",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        DefVal = {'maxHue':mxh,
                  'minHue':mnh,
                  'maxSat':mxs,
                  'minSat':mns,
                  'maxVal':mxv,
                  'minVal':mnv}
        with open('initialValues.json', 'w') as outfile:
            json.dump(DefVal, outfile)
        break
    
DefVal = {'maxHue':mxh,
          'minHue':mnh,
          'maxSat':mxs,
          'minSat':mns,
          'maxVal':mxv,
          'minVal':mnv}
with open('initialValues.json', 'w') as outfile:
    json.dump(DefVal, outfile)
cap.release()