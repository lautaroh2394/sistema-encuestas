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
        usuarios = []
        encuestas = []
        preguntas = []

    