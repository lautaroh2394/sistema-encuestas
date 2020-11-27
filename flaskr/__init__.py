import os
from flask import Flask, redirect, url_for, request
from flaskr.DataManager import DataManager
from flaskr.SessionManager import SessionManager

#Inicializo usuarios de prueba
#DataManager.get_instance().nuevoUsuario("usuario11","1234")

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/login', methods=["POST"])
    def login():
        logged = SessionManager.getInstance().loginUsuario(request.form["usuario"], request.form["password"])
        if logged == False:
            return str({
                "mensaje": "Combinación de usuario y contraseña incorrectas",
                "exito": False
            })
        
        return str({
            "exito" : True,
            "session_key": logged
        })
    
    @app.route('/signup',methods=['POST'])
    def signup():
        rdo = DataManager.getInstance().nuevoUsuario(request.form["usuario"],request.form["password"])
        return str({
            "exito": rdo
        })

    return app