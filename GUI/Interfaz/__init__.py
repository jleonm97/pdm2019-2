# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:08:39 2019

@author: John
"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .views import main
    app.register_blueprint(main)
    
    return app