from flaskr.Usuario import Usuario
from flaskr.Pregunta import Pregunta
from flaskr.Respuesta import Respuesta
from flaskr.Encuesta import Encuesta

class DataManager:
    instance = None

    @staticmethod
    def get_instance():
        if DataManager.instance is not None:
            return DataManager.instance
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

    def nuevo_usuario(self, user_id, password):
        if user_id in [user.id for user in self.usuarios]:
            return False
        self.usuarios.append(Usuario(user_id, password))
        return True

    def nueva_respuesta(self, respuesta_map):
        texto = respuesta_map["texto"]
        correcta = False
        if "correcta" in respuesta_map:
            correcta = respuesta_map["correcta"]
        
        nueva_respuesta = Respuesta(self.total_respuestas, texto, correcta)
        self.respuestas.append(nueva_respuesta)
        self.total_respuestas += 1
        return nueva_respuesta.id
    
    def nueva_pregunta(self, pregunta, ids_respuestas):
        respuestas = [respuesta for respuesta in self.respuestas if respuesta.id in ids_respuestas]
        nueva_pregunta = Pregunta(self.total_preguntas, pregunta, respuestas)
        self.preguntas.append(nueva_pregunta)
        self.total_preguntas += 1
        return nueva_pregunta.id

    def nueva_encuesta(self, id_preguntas, etiquetas=[]):
        nueva_encuesta = Encuesta(self.total_encuestas, id_preguntas, etiquetas)
        self.encuestas.append(nueva_encuesta)
        self.total_encuestas += 1
        return nueva_encuesta.id

    def encuesta(self, encuesta_id, incluir_correcta=False):
        encuestas = [encuesta for encuesta in self.encuestas if encuesta.id == int(encuesta_id)]
        if not encuestas:
            return {}

        encuesta = encuestas[0]
        preguntas = [pregunta for pregunta in self.preguntas if pregunta.id in encuesta.id_preguntas]
        return {
            "encuesta_id" : encuesta.id,
            "etiquetas" : encuesta.etiquetas,
            "preguntas" : [pregunta.to_string(incluir_correcta) for pregunta in preguntas]
        }

    def verificar_encuesta(self, encuesta_id, respuestas_dadas):
        #respuestas: lista de maps con estructura:
        '''
        {
            pregunta_id: n,
            respuesta_indicada_id : m
        }
        '''
        encuesta = self.encuesta(encuesta_id, incluir_correcta=True)
        correctas = 0
        for pregunta in encuesta["preguntas"]:
            pregunta_id = pregunta["pregunta_id"]
            respuestas_indicada = [respuesta for respuesta in respuestas_dadas if respuesta["pregunta_id"] == pregunta_id]
            if respuestas_indicada:
                respuesta_indicada = respuestas_indicada[0]
                correcta = self.validar_pregunta(
                    pregunta_id,
                    respuesta_indicada["respuesta_indicada_id"]
                    )
                if correcta: 
                    correctas += 1

        return {
            "total_preguntas" : len(encuesta["preguntas"]),
            "preguntas_correctas" : correctas
        }
    
    def validar_pregunta(self, pregunta_id, respuesta_dada_id):
        pregunta = [pregunta for pregunta in self.preguntas if pregunta.id == pregunta_id][0]
        return pregunta.validar_respuesta_id(respuesta_dada_id)

    def encuestas_segun_etiquetas(self, etiquetas):
        encuestas = [encuesta for encuesta in self.encuestas if encuesta.contiene_todas(etiquetas)]

        encontradas = []
        for encuesta in encuestas:
            preguntas = [pregunta for pregunta in self.preguntas if pregunta.id in encuesta.id_preguntas]
            encontradas.append({
                "encuesta_id" : encuesta.id,
                "etiquetas" : encuesta.etiquetas,
                "preguntas" : [pregunta.to_string() for pregunta in preguntas]
            })
        
        return encontradas
