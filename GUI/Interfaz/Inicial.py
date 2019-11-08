# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:08:39 2019

@author: John
"""

from flask import Flask

angulo = 0

pruebaX = {"Slider1":0,"Slider2":0,"Slider3":0,"Slider4":0,"Slider5":0,"Slider6":0}

def create_app():
    
    #@app.route("/")
    
    global pruebaX
    
    app = Flask(__name__)
    
    from views import main #, prueba3
    
    app.register_blueprint(main)
    #pruebaX = prueba3
    
    return app

if __name__ == "__main__":
    
    app = create_app()
    
    app.run(debug=True,port=3000, host='0.0.0.0')
    
from views import prueba3

pruebaX = prueba3
print('{}'.format(pruebaX))    