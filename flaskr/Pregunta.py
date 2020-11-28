from flaskr.Respuesta import Respuesta
class Pregunta:
    MAX_RESPUESTAS =  4
    MAX_CORRECTAS = 1

    def __init__(self, id, pregunta, respuestas = []):
        self.pregunta = pregunta
        self.respuestas = []
        self.total_correctas = 0
        for res in respuestas:
            self.agregarRespuesta(res)
        self.id = id
        self.id_correctas = [respuesta.id for respuesta in filter(lambda r : r.correcta, self.respuestas)]
    
    def agregarRespuesta(self, respuesta):
        if type(respuesta) != Respuesta:
            raise Exception("El parámetro debe ser tipo Respuesta")

        if len(self.respuestas) == Pregunta.MAX_RESPUESTAS:
            print(f"No se pueden agregar más de {Pregunta.MAX_RESPUESTAS} respuestas")
            return False

        if (self.total_correctas == Pregunta.MAX_CORRECTAS) and (respuesta.correcta):
            print(f"No se pueden agregar más de {Pregunta.MAX_CORRECTAS} respuestas correctas")
            return False
        
        if respuesta.correcta:
            self.total_correctas +=1
        
        if len(self.respuestas) == (Pregunta.MAX_RESPUESTAS - 1):
            #Si no hay una respuesta correcta, por defecto será la última agregada
            correctas = list(filter(lambda r: r.correcta, self.respuestas))
            if len(correctas) == 0:
                respuesta.correcta = True
        
        self.respuestas.append(respuesta)
        return True
    
    def toString(self, incluirCorrecta = False):
        return {
            "pregunta_id" : self.id,
            "pregunta" : self.pregunta,
            "respuestas": [ respuesta.toString(incluirCorrecta) for respuesta in self.respuestas]
        }
    
    def validarRespuestaId(self, id):
        return id in self.id_correctas