from flaskr.Respuesta import Respuesta
class Pregunta:
    MAX_RESPUESTAS = 4
    MAX_CORRECTAS = 1

    def __init__(self, id_pregunta, pregunta, respuestas=[]):
        self.pregunta = pregunta
        self.respuestas = []
        self.total_correctas = 0
        for res in respuestas:
            self.agregar_respuesta(res)
        self.id = id_pregunta
        self.id_correctas = [respuesta.id for respuesta in self.respuestas if respuesta.correcta]
    
    def agregar_respuesta(self, respuesta):
        if not isinstance(respuesta, Respuesta):
            raise Exception("El parámetro debe ser tipo Respuesta")

        if len(self.respuestas) == Pregunta.MAX_RESPUESTAS:
            print(f"No se pueden agregar más de {Pregunta.MAX_RESPUESTAS} respuestas")
            return False

        if (self.total_correctas == Pregunta.MAX_CORRECTAS) and (respuesta.correcta):
            print(f"No se pueden agregar más de {Pregunta.MAX_CORRECTAS} respuestas correctas")
            return False
        
        if respuesta.correcta:
            self.total_correctas += 1
        
        if len(self.respuestas) == (Pregunta.MAX_RESPUESTAS - 1):
            #Si no hay una respuesta correcta, por defecto será la última agregada
            correctas = [respuesta for respuesta in self.respuestas if respuesta.correcta]
            if not correctas:
                respuesta.correcta = True
        
        self.respuestas.append(respuesta)
        return True
    
    def to_string(self, incluir_correcta=False):
        return {
            "pregunta_id" : self.id,
            "pregunta" : self.pregunta,
            "respuestas": [respuesta.to_string(incluir_correcta) for respuesta in self.respuestas]
        }
    
    def validar_respuesta_id(self, id_respuesta):
        return id_respuesta in self.id_correctas
