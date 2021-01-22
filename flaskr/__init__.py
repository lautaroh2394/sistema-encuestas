import os
import json
from flask import Flask, request, jsonify, make_response
from flaskr.DataManager import DataManager
from flaskr.SessionManager import SessionManager

#Inicializo usuarios de prueba
#DataManager.get_instance().nuevo_usuario("usuario11","1234")

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    DMI = DataManager.get_instance()
    SM = SessionManager.get_instance()

    def logueado(request):
        return SM.usuario_logueado(
            request.json["usuario"],
            request.json["session_key"]
            )

    @app.route('/login', methods=["POST"])
    def login():
        if "usuario" not in request.json or "password" not in request.json:
            return jsonify(SM.LOGIN_ERROR)

        logged = SM.login_usuario(
            request.json["usuario"],
            request.json["password"]
            )
        if logged == False:
            return jsonify(SessionManager.LOGIN_ERROR)
        
        return jsonify({
            "exito" : True,
            "session_key": logged
        })
    
    @app.route('/signup', methods=['POST'])
    def signup():
        if "usuario" not in request.json or "password" not in request.json:
            return jsonify(SM.LOGIN_ERROR)

        rdo = DMI.nuevo_usuario(
            request.json["usuario"],
            request.json["password"]
            )
        return jsonify({
            "exito": rdo
        })

    @app.route("/encuesta", methods=['POST'])
    def encuesta():
        if not logueado(request): 
            return jsonify(SessionManager.USUARIO_NO_LOGUEADO)
        
        preguntas = request.json["preguntas"]
        preguntas_id = []
        for pregunta in preguntas:
            respuestas_id = [DMI.nueva_respuesta(respuesta) for respuesta in pregunta["respuestas"]]
            pregunta_id = DMI.nueva_pregunta(pregunta["pregunta"], respuestas_id)
            preguntas_id.append(pregunta_id)

        etiquetas = []
        if "etiquetas" in request.json:
            etiquetas = request.json["etiquetas"]

        id_encuesta = DMI.nueva_encuesta(preguntas_id, etiquetas)
        return jsonify({
                "exito": True,
                "id_encuesta": id_encuesta
            })

    @app.route("/encuesta/<encuesta_id>", methods=['GET'])
    def get_encuesta(encuesta_id=None):
        if encuesta_id is None:
            return jsonify({
                "exito" : False,
                "mensaje" : "Debe indicar un id de encuesta"
            })
        
        return jsonify({
            "exito" : True,
            "encuesta" : DMI.encuesta(encuesta_id)
            })
    
    @app.route('/listar?etiquetas=<etiquetas>', methods=['POST'])
    def listar_etiquetas(etiquetas=[]):
        if not logueado(request): return jsonify(SessionManager.USUARIO_NO_LOGUEADO)
        
        #return jsonify(DMI.encuestas_segun_etiquetas(json.loads(etiquetas)))
        return jsonify(DMI.encuestas_segun_etiquetas(etiquetas))
    
    @app.route('/listar', methods=['POST'])
    def listar():
        if not logueado(request):
            return jsonify(SessionManager.USUARIO_NO_LOGUEADO)
        return jsonify(DMI.encuestas_segun_etiquetas([]))
    
    @app.route('/verificar/encuesta_id=<encuesta_id>&respuestas=<respuestas_dadas>', methods=['GET'])
    def verificar_encuesta(encuesta_id=None, respuestas_dadas=[]):
        if encuesta_id is None or respuestas_dadas is None:
            return jsonify({
                "exito" : False,
                "mensaje" : "Debe indicar tanto el id de la encuesta como las respuestas"
            })
        
        #respuestas_dadas = json.loads(respuestas_dadas)
        respuestas_dadas = respuestas_dadas
        resultados = DMI.verificar_encuesta(encuesta_id, respuestas_dadas)
        resultados["exito"] = True
        return jsonify(resultados)

    @app.route('/listar_dm')
    def listarDM():
        #Debugging purposes only
        usuarios = [{"usuario_id": u.id, "usuario_pw": u.password} for u in DMI.usuarios]
        logueados = [{"usuario_id": u.id, "s_k": u.session_key} for u in SM.usuarios_logueados]
        encuestas = [DMI.encuesta(e.id, incluir_correcta=True) for e in DMI.encuestas]
        return jsonify({
            "usuarios" : usuarios,
            "logueados": logueados,
            "encuestas" : encuestas
        })

    return app
