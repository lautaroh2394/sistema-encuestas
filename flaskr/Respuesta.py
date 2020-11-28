class Respuesta:
    def __init__(self, id, texto, correcta = False):
        self.id = id
        self.texto = texto
        self.correcta = correcta
    
    def toString(self, incluirCorrecta = False):
        rta =  {
            "texto" : self.texto,
            "respuesta_id": self.id
        }

        if incluirCorrecta:
            rta["correcta"] = self.correcta

        return rta