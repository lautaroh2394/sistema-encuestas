class Respuesta:
    def __init__(self, id_respuesta, texto, correcta=False):
        self.id = id_respuesta
        self.texto = texto
        self.correcta = correcta
    
    def to_string(self, incluir_correcta=False):
        rta =  {
            "texto" : self.texto,
            "respuesta_id": self.id
        }

        if incluir_correcta:
            rta["correcta"] = self.correcta

        return rta