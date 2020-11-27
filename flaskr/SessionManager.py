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
        self.usuarios_loggueados = []

    def usuarioLogueado(self, id_usuario, session_key):
        ids_logueados = [user.id for user in self.usuarios_loggueados]
        if id_usuario not in ids_logueados:
            return False
        usuario_logueado = list(filter(lambda user: user.id == id_usuario))[0]
        return usuario_logueado.session_key == session_key

    def loginUsuario(self, id, pw):
        usuarios = list(filter(lambda x: x.id == id, DataManager.getInstance().usuarios))
        if len(usuarios) == 0:
            return False

        usuario = usuarios[0]
        if usuario.password == pw:
            usuario.session_key = self.getRandomKey()
            self.usuarios_loggueados.append(usuario)
            return usuario.session_key
        return False

    def getRandomKey(self):
        return math.trunc(random()*10000000000)