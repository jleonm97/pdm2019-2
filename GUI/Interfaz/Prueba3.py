# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:47:24 2019

@author: John
"""

import requests, time

angX = 0
angY = 360

while(1):
    
    var1 = {'X':angX, 'Y':angY}
    r = requests.post('http://10.101.1.142:3000/Prueba', json = var1)
    time.sleep(1)
    if angX>20:
        angX = 0
        if angY<340:
            angY = 360
            
    angX = angX+1
    angY = angY-1
    
#    var2 = {'Q':13, 'N':14}
#    r2 = requests.post('http://10.101.1.142:3000/GA', json = var2)
#    response = requests.get('http://10.101.1.142:3000/GA')
#    payload = response.json()
    print("Angulos son: {}".format(var1))
#    break
    
    