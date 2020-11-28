#TODO: En lo posible reemplazar por session de Flask
from flaskr.DataManager import DataManager
import os
from random import random
import math

class SessionManager:
    instance = None
    @staticmethod
    def getInstance():
        if SessionManager.instance is None:
            SessionManager.instance = SessionManager()
        return SessionManager.instance
    
    def __init__(self):
        self.usuarios_logueados = []

    def usuarioLogueado(self, id_usuario, session_key):
        ids_logueados = [user.id for user in self.usuarios_logueados]
        if id_usuario in ids_logueados:
            usuario_logueado = list(filter(lambda user: user.id == id_usuario, self.usuarios_logueados))[0]
            return usuario_logueado.session_key == session_key
        return False

    def loginUsuario(self, id, pw):
        usuarios = list(filter(lambda x: x.id == id, DataManager.getInstance().usuarios))
        if len(usuarios) == 0:
            return False

        usuario = usuarios[0]
        if usuario.password == pw:
            usuario.session_key = self.getRandomKey()
            self.usuarios_logueados.append(usuario)
            return usuario.session_key
        return False

    def getRandomKey(self):
        return str(math.trunc(random()*10000000000))