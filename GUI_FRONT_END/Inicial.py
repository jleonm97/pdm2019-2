# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:08:39 2019

@author: John
"""

from flask import Flask

angulo = 0

def create_app():
    
    #@app.route("/")
    
    app = Flask(__name__)
    
    from views import main
    
    app.register_blueprint(main)
    
    return app

if __name__ == "__main__":
    
    app = create_app()
    
    app.run(debug=True,port=3000, host='0.0.0.0')
    
    