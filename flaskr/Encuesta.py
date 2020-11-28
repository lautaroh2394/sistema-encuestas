class Encuesta:
    def __init__(self, id_encuesta, id_preguntas, etiquetas=[]):
        self.id = id_encuesta
        self.id_preguntas = id_preguntas
        self.etiquetas = etiquetas
    
    def contiene_todas(self, etiquetas=[]):
        return all([etiqueta in self.etiquetas for etiqueta in etiquetas])