import json
from flaskr import create_app
from flaskr.DataManager import DataManager
from flaskr.SessionManager import SessionManager

DMI = DataManager.get_instance()
SM = SessionManager.get_instance()
testing_values = {}

def test_config():
    assert not create_app().testing

def test_signup(client):
    response_b = client.post("/signup", data={
        "usuario" : "usuario11",
        "password" : "1234"
    })    
    response = json.loads(response_b.data.decode())
    assert "exito" in response and response["exito"]
    assert DMI.usuarios[0].id == "usuario11"

def test_login(client):
    #pw incorrecta
    response_b = client.post("/login", data={
        "usuario" : "usuario11",
        "password" : "0"
    })
    response = json.loads(response_b.data.decode())
    assert "exito" in response and not response["exito"]
    assert "session_key" not in response

    #reenvío con pw correcta
    response_b = client.post("/login", data={
        "usuario" : "usuario11",
        "password" : "1234"
    })
    response = json.loads(response_b.data.decode())
    assert "exito" in response and response["exito"]
    assert "session_key" in response
    testing_values["session_key"] = response["session_key"]

def test_encuesta(client):
    payload = {
        'usuario': 'usuario11',
        'session_key': '0',
        'preguntas': '''[
            {
                "pregunta" : "ejemplo",
                "respuestas": [
                    { "texto" : "rta 1", "correcta" : true },
                    { "texto" : "rta 2" },
                    { "texto" : "rta 3"}
                ]
            }
        ]''',
        'etiquetas': '["etiqueta1"]'
    }
    #session_key incorrecta
    response_b = client.post("/encuesta", data=payload)
    response = json.loads(response_b.data.decode())
    assert "exito" in response and not response["exito"] and "id_encuesta" not in response

    #reenvío con session key correcta
    payload["session_key"] = testing_values["session_key"]
    response_b = client.post("/encuesta", data=payload)
    response = json.loads(response_b.data.decode())
    assert "exito" in response and response["exito"]
    assert "id_encuesta" in response
    testing_values["id_encuesta"] = response["id_encuesta"]

def test_get_encuesta(client):
    #borro manualmente la entrada del usuario en SessionManager para demostrar la consulta pública de las encuestas
    SM.usuarios_logueados = []
    response_b = client.get(f'/encuesta/{testing_values["id_encuesta"]}')
    response = json.loads(response_b.data.decode())
    assert "encuesta" in response
    assert "etiquetas" in response["encuesta"]
    assert "etiqueta1" in response["encuesta"]["etiquetas"]
    assert "preguntas" in response["encuesta"]
    assert response["encuesta"]["preguntas"][0]["respuestas"] == [
                    {
                        "respuesta_id": 0,
                        "texto": "rta 1"
                    },
                    {
                        "respuesta_id": 1,
                        "texto": "rta 2"
                    },
                    {
                        "respuesta_id": 2,
                        "texto": "rta 3"
                    }
                ]

def test_verificar_encuesta_correcta(client):
    #rta correcta
    response_b = client.get(f'/verificar/encuesta_id={testing_values["id_encuesta"]}&respuestas=[%7B"pregunta_id": 0, "respuesta_indicada_id" : 0%7D]')
    response = json.loads(response_b.data.decode())
    assert "exito" in response and response["exito"]
    assert "preguntas_correctas" in response
    assert response["preguntas_correctas"] == 1

def test_verificar_encuesta_incorrecta(client):
    #rta incorrecta
    response_b = client.get(f'/verificar/encuesta_id={testing_values["id_encuesta"]}&respuestas=[%7B"pregunta_id": 0, "respuesta_indicada_id" : 1%7D]')
    response = json.loads(response_b.data.decode())
    assert "exito" in response and response["exito"]
    assert "preguntas_correctas" in response
    assert response["preguntas_correctas"] == 0