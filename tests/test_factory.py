import json
from flaskr import create_app
from flaskr.DataManager import DataManager
from flaskr.SessionManager import SessionManager

DMI = DataManager.get_instance()
SM = SessionManager.get_instance()
testing_values = {}
headers = {"Content-Type":"application/json"}

def test_config():
    assert not create_app().testing

def test_signup(client):
    res = client.post("/signup", json={
        "usuario" : "usuario11",
        "password" : "1234"
    }, headers=headers)    
    res_json = res.json
    assert "exito" in res_json and res_json["exito"]
    assert DMI.usuarios[0].id == "usuario11"

def test_login_incorrecto(client):
    res = client.post("/login", json={
        "usuario" : "usuario11",
        "password" : "0"
    }, headers=headers)
    res_json = res.json
    assert "exito" in res_json and not res_json["exito"]
    assert "session_key" not in res_json

def test_login_correcto(client):
    res = client.post("/login", json={
        "usuario" : "usuario11",
        "password" : "1234"
    }, headers=headers)
    res_json = res.json
    assert "exito" in res_json and res_json["exito"]
    assert "session_key" in res_json
    testing_values["session_key"] = res_json["session_key"]

def test_encuesta(client):
    payload = {
        'usuario': 'usuario11',
        'session_key': '0',
        'preguntas': [
            {
                "pregunta" : "ejemplo",
                "respuestas": [
                    { "texto" : "rta 1", "correcta" : True },
                    { "texto" : "rta 2" },
                    { "texto" : "rta 3"}
                ]
            }
        ],
        'etiquetas': "etiqueta1"
    }
    #session_key incorrecta
    res = client.post("/encuesta", json=payload, headers=headers)
    res_json = res.json
    assert "exito" in res_json and not res_json["exito"] and "id_encuesta" not in res_json

    #reenvío con session key correcta
    payload["session_key"] = testing_values["session_key"]
    res = client.post("/encuesta", json=payload, headers=headers)
    res_json = res.json
    assert "exito" in res_json and res_json["exito"]
    assert "id_encuesta" in res_json
    testing_values["id_encuesta"] = res_json["id_encuesta"]

def test_get_encuesta(client):
    #borro manualmente la entrada del usuario en SessionManager para demostrar la consulta pública de las encuestas
    SM.usuarios_logueados = []
    
    res = client.get(f'/encuesta/{testing_values["id_encuesta"]}')
    res_json = res.json
    assert "encuesta" in res_json
    assert "etiquetas" in res_json["encuesta"]
    assert "etiqueta1" in res_json["encuesta"]["etiquetas"]
    assert "preguntas" in res_json["encuesta"]
    assert res_json["encuesta"]["preguntas"][0]["respuestas"] == [
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
    res = client.get(f'/verificar/encuesta_id={testing_values["id_encuesta"]}&respuestas=[%7B"pregunta_id": 0, "respuesta_indicada_id" : 0%7D]')
    res_json = res.json
    assert "exito" in res_json and res_json["exito"]
    assert "preguntas_correctas" in res_json
    assert res_json["preguntas_correctas"] == 1

def test_verificar_encuesta_incorrecta(client):
    #rta incorrecta
    res = client.get(f'/verificar/encuesta_id={testing_values["id_encuesta"]}&respuestas=[%7B"pregunta_id": 0, "respuesta_indicada_id" : 1%7D]')
    res_json = res.json
    assert "exito" in res_json and res_json["exito"]
    assert "preguntas_correctas" in res_json
    assert res_json["preguntas_correctas"] == 0