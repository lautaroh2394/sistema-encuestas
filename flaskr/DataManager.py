from flaskr.Usuario import Usuario
from flaskr.Pregunta import Pregunta
from flaskr.Respuesta import Respuesta
from flaskr.Encuesta import Encuesta

class DataManager:
    instance = None

    @staticmethod
    def getInstance():
        if DataManager.instance is not None:
            return DataManager.instance
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
        if id in [user.id for user in self.usuarios]:
            return False
        self.usuarios.append(Usuario(id,pw))
        return True

    def nuevaRespuesta(self, respuesta_map):
        texto = respuesta_map["texto"]
        correcta = False
        if "correcta" in respuesta_map:
            correcta = respuesta_map["correcta"]
        
        nueva_respuesta = Respuesta(self.total_respuestas, texto, correcta)
        self.respuestas.append(nueva_respuesta)
        self.total_respuestas += 1
        return nueva_respuesta.id
    
    def nuevaPregunta(self, pregunta, ids_respuestas):
        respuestas = filter(lambda resp: resp.id in ids_respuestas, self.respuestas)
        print(f"respuestas:{respuestas}")
        nueva_pregunta = Pregunta(self.total_preguntas, pregunta, respuestas)
        self.preguntas.append(nueva_pregunta)
        self.total_preguntas += 1
        return nueva_pregunta.id

    def nuevaEncuesta(self, id_preguntas, etiquetas = []):
        nueva_encuesta = Encuesta(self.total_encuestas, id_preguntas, etiquetas)
        self.encuestas.append(nueva_encuesta)
        self.total_encuestas += 1
        return nueva_encuesta.id

    def encuesta(self,id):
        encuestas = list(filter(lambda e: e.id == int(id), self.encuestas))
        if len(encuestas) == 0:
            return {}

        encuesta = encuestas[0]
        preguntas = filter(lambda pregunta: pregunta.id in encuesta.id_preguntas, DataManager.getInstance().preguntas)
        return {
            "encuesta_id" : encuesta.id,
            "etiquetas" : encuesta.etiquetas,
            "preguntas" : [pregunta.toString() for pregunta in preguntas]
        }

    def verificarEncuesta(self):
        #TODO