from Respuesta import Respuesta
class Pregunta:
    MAX_RESPUESTAS =  4

    def __init__(self, id, respuestas = []):
        self.respuestas = []
        for res in respuestas:
            self.agregarRespuesta(res)
        self.id = id
    
    def agregarRespuesta(self, respuesta):
        if type(respuesta) != Respuesta:
            raise Exception("El parámetro debe ser tipo Respuesta")

        if len(self.respuestas) == Pregunta.MAX_RESPUESTAS:
            print(f"No se pueden agregar más de {Pregunta.MAX_RESPUESTAS} respuestas")
            return False
        
        if len(self.respuestas) == (Pregunta.MAX_RESPUESTAS - 1):
            #Si no hay una respuesta correcta, por defecto será la última agregada
            correctas = list(filter(lambda r: r.correcta, self.respuestas))
            if len(correctas) == 0:
                respuesta.correcta = True
        
        self.respuestas.append(respuesta)
        return True