import os
from flask import Flask, redirect, url_for, request
from flaskr.DataManager import DataManager
from flaskr.SessionManager import SessionManager
import json

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

    @app.route("/encuesta", methods=['POST'])
    def encuesta():
        '''
        logueado = SessionManager.getInstance().usuarioLogueado(request.form["usuario"],request.form["session_key"])
        if not logueado:
            return str({
                "exito": False,
                "mensaje": "Usuario no logueado"
            })
        '''
            
        preguntas = json.loads(request.form["preguntas"])
        preguntas_id = []
        for pregunta in preguntas:
            respuestas_id = [ DataManager.getInstance().nuevaRespuesta(respuesta) for respuesta in pregunta["respuestas"] ]
            pregunta_id = DataManager.getInstance().nuevaPregunta(pregunta["pregunta"], respuestas_id)
            preguntas_id.append(pregunta_id)

        etiquetas = []
        if "etiquetas" in request.form:
            etiquetas = json.loads(request.form["etiquetas"])

        id_encuesta = DataManager.getInstance().nuevaEncuesta(preguntas_id, etiquetas)
        return str({
                "exito": True,
                "id_encuesta": id_encuesta
            })


    @app.route("/encuesta/<encuesta_id>", methods=['GET'])
    def get_encuesta(encuesta_id = None):
        if encuesta_id is None:
            return str({
                "exito" : False,
                "mensaje" : "Debe indicar un id de encuesta"
            })
        
        return str({
            "exito" : True,
            "encuesta" : DataManager.getInstance().encuesta(encuesta_id)
            })
    
    @app.route('/listar/<etiquetas>', methods=['POST'])
    def listar_etiquetas(etiquetas):
        #etiquetas tendrá la estructura: "tag1&tag2&..."
        '''
        logueado = SessionManager.getInstance().usuarioLogueado(request.form["usuario"],request.form["session_key"])
        if not logueado:
            return str({
                "exito": False,
                "mensaje": "Usuario no logueado"
            })
        '''
        return str(DataManager.getInstance().encuestasSegunEtiquetas(etiquetas.split("&")))
    
    @app.route('/listar', methods=['POST'])
    def listar():
        '''
        logueado = SessionManager.getInstance().usuarioLogueado(request.form["usuario"],request.form["session_key"])
        if not logueado:
            return str({
                "exito": False,
                "mensaje": "Usuario no logueado"
            })
        '''
        return str(DataManager.getInstance().encuestasSegunEtiquetas([]))

    @app.route('/listar_dm')
    def listarDM():
        #Debugging purposes only
        usuarios = [{"usuario_id": u.id} for u in DataManager.getInstance().usuarios]
        logueados = [{"usuario_id": u.id, "s_k": u.session_key } for u in SessionManager.getInstance().usuarios_logueados]
        encuestas = [DataManager.getInstance().encuesta(e.id) for e in DataManager.getInstance().encuestas]
        return str({
            "usuarios" : usuarios,
            "logueados": logueados,
            "encuestas" : encuestas
        })

    return app