from Usuario import Usuario
from Pregunta import Pregunta
from Respuesta import Respuesta
from Encuesta import Encuesta

class DataManager:
    instance = None

    @staticmethod
    def get_instance():
        if DataManager.instance is not None:
            return instance
        else:
            DataManager.instance = DataManager()
            return DataManager.instance

    def __init__(self):
        self.usuarios = []
        self.encuestas = []
        self.preguntas = []
        self.respuestas = []
        self.total_preguntas = 0
        self.total_respuestas = 0
        self.total_encuestas = 0

    def nuevoUsuario(self, id, pw):
        self.usuarios.append(Usuario(id,pw))
    
    def loginUsuario(self, id, pw):
        usuarios = list(filter(lambda x: x.id == id,self.usuarios))
        if len(usuarios) == 0:
            return False

        usuario = usuarios[0]
        if usuario.password == pw:
            return True

        return False

    def nuevaRespuesta(self, texto, correcta = False):
        nueva_respuesta = Respuesta(self.total_respuestas, texto, correcta)
        self.respuestas.append(nueva_respuesta)
        self.total_respuestas += 1
        return nueva_respuesta.id
    
    def nuevaPregunta(self, pregunta, ids_respuestas):
        respuestas = filter(labmda r: ids_respuestas.contains(r), self.respuestas)
        nueva_pregunta = Pregunta(self.total_preguntas, respuestas)
        self.preguntas.append(nueva_pregunta)
        self.total_preguntas += 1
        return nueva_pregunta.id

    def nuevaEncuesta(self, id_preguntas, etiquetas = []):
        nueva_encuesta = Encuesta(self.total_encuestas, id_preguntas, etiquetas)
        self.encuestas.append(nueva_encuesta)
        self.total_encuestas += 1
        return nueva_encuesta.id

    