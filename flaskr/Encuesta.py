class Encuesta:
    def __init__(self, id, id_preguntas, etiquetas = []):
        self.id = id
        self.id_preguntas = id_preguntas
        self.etiquetas = etiquetas
    
    def contieneTodas(self,etiquetas = []):
        return all([ etiqueta in self.etiquetas for etiqueta in etiquetas])