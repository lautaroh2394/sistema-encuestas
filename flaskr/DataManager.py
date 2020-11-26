from Usuario import Usuario

class DataManager:
    instance = None

    @staticmethod
    def get_instance():
        if DataManager.instance is not None:
            return instance
        else:
            DataManager.instance = DataManager()
            return DataManager.instance

    def __init__(self):
        self.usuarios = []
        self.encuestas = []
        self.preguntas = []

    def nuevoUsuario(self, id, pw):
        self.usuarios.append(Usuario(id,pw))
    
    def loginUsuario(self, id, pw):
        usuarios = list(filter(lambda x: x.id == id,self.usuarios))
        if len(usuarios) == 0:
            return False

        usuario = usuarios[0]
        if usuario.password == pw:
            return True

        return False