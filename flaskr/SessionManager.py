#TODO: En lo posible reemplazar por session de Flask
from random import random
import math
from flaskr.DataManager import DataManager

class SessionManager:
    instance = None
    USUARIO_NO_LOGUEADO = {
        "exito": False,
        "mensaje": "Usuario no logueado"
        }
    LOGIN_ERROR = {
                "mensaje": "Combinación de usuario y contraseña incorrectas",
                "exito": False
                }
    
    @staticmethod
    def get_instance():
        if SessionManager.instance is None:
            SessionManager.instance = SessionManager()
        return SessionManager.instance
    
    def __init__(self):
        self.usuarios_logueados = []

    def usuario_logueado(self, id_usuario, session_key):       
        ids_logueados = [user.id for user in self.usuarios_logueados]
        if id_usuario in ids_logueados:
            usuario_logueado = [user for user in self.usuarios_logueados if user.id == id_usuario][0]
            return usuario_logueado.session_key == session_key
        return False

    def login_usuario(self, id_usuario, pw):
        usuarios = [usuario for usuario in DataManager.get_instance().usuarios if usuario.id == id_usuario]
        if not usuarios:
            return False

        usuario = usuarios[0]
        if usuario.password == pw:
            usuario.session_key = self.get_random_key()
            self.usuarios_logueados.append(usuario)
            return usuario.session_key
        return False

    def get_random_key(self):
        return str(math.trunc(random()*10000000000))
