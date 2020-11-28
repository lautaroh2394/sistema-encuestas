class Respuesta:
    def __init__(self, id, texto, correcta = False):
        self.id = id
        self.texto = texto
        self.correcta = correcta
    
    def toString(self):
        return {
            "texto" : self.texto,
            "respuesta_id": self.id
        }