# sistema-encuestas

1. Enunciado
1. Descripción de la solución
1. Instrucciones de ejecución

## 1. Enunciado

Para conocer más sobre tus skills te vamos a plantear un ejercicio práctico cuyo objetivo principal es conocer cómo es tu proceso de resolución de problemas. Sabemos que es probable que no termines el ejercicio en el tiempo indicado (NO TE PREOCUPES POR ESO!), lo que más nos importa es ver cómo encarás la solución y para eso te pedimos que los commits que hagas sean pequeños y descriptivos.

Puntos obligatorios:

 - El código debe estar alojado en un repositorio público del servidor de tu preferencia (github, bitbucket, gitlab, etc, etc)
 - Los commits y push realizados en el código deben ser pequeños y con titulo descriptivo.
 - Debe haber un archivo readme en donde indique como debe ser ejecutado.
 - Dentro del archivo readme debe haber un segmento en el que nos cuentes qué fue lo más desafiante del desarrollo realizado.
 - El código del backend de la aplicación debe ser python.
 - En caso de querer usar un framework, el único permitido es “Flask”
 - Debe estar dockerizado.

Puntos optativos:

 - En caso de hacerle también un frontend, el lenguaje debe ser React
 - Debe tener tests.
 - Si el código requiere de bibliotecas que no sean del tipo standard, es obligatorio tener un archivo requirements con el listado de las mismas.



Requerimientos:
(⛌ = Hecho)
- Como dueño de producto, me gustaría tener un sistema que me permita realizar encuestas                                            ⛌
- Como dueño de producto, me gustaría que cada pregunta pueda tener una o más respuestas.                                           ⛌
- Como dueño de producto, me gustaría que cada pregunta pueda tener como máximo 4 respuestas.                                       ⛌
- Como dueño de producto, me gustaría que mi aplicación de encuestas posea un login para usuarios.                                  ⛌
- Como dueño de producto, me gustaría que los usuarios de mi aplicación puedan cargar preguntas y sus respectivas respuestas.       ⛌
- Como dueño de producto, me gustaría que se puedan responder encuestas sin estar registrado en el sistema.                         ⛌
- Como dueño de producto, me gustaría que solo los usuarios registrados puedan cargar encuestas.                                    ⛌
- Como dueño de producto, me gustaría poder revisar un historial de preguntas por usuario.
- Como dueño de producto, me gustaría poder agrupar encuestas a través de etiquetas.                                                ⛌
- Como dueño de producto, me gustaría poder acceder a un listado de todas las encuestas del sistema.                                ⛌
- Como dueño de producto, me gustaría que las encuestas tengan vencimiento.

## 2. Descripción de la solución

### Impresiones iniciales

Luego de leer los requerimientos, comento lo que planeo hacer: 
- Backend en Python con Flask, definiendo métodos que permitan lo que el dueño de producto plantea.
- No implementaré persistencia porque el dueño de producto no lo mencionó (jeje), pero principalmente porque no creo llegar con los tiempos.
- Por la misma razón no implementaré frontend y porque no soy conocedor de React. Si llego a estar más disponible de lo que supongo, me gustaría intentar armar algo sencillo con dicha tecnología
- Tests
- Docker

Por desconocimiento, probablemente dejaré los tests y la dockerizacion para lo último, aunque los tests me gustaría escribirlos a medida que voy sumando métodos.

### Comentarios durante el desarrollo

- Para lo referido al guardado de datos decidí armar un singleton para que maneje todo en memoria. Mi idea es que esto sería de alguna manera escalable para poder a futuro modificarlo y realmente interactuar con una bd. Para eso también pensé en varias entidades (clases Encuesta, Respuesta, Pregunta, Usuario) que a mi entender resultarían fáciles de mapear a una base relacional. Hablo de base relacional porque entiendo que para python también hay un módulo para un sqlite autocontenido
- Para tema login de usuarios se que Flask tiene un módulo 'session' que facilita mucho esto, pero nunca lo usé y no quise 'perder' el poco tiempo investigando. Armé una entidad que maneja de manera muy muy básica las sesiones, pero siempre pensando que dentro de lo posible lo mejor será aprenderlo y usarlo.
- Siguiendo con el tema de sesiones, mi idea es que el usuario al loguearse reciba una key, y en futuras consultas deba indicar su usuario y esta key.

### Comentarios finales

Bueno, tal como supuse no alcancé a implementar varias cosas que me gustaría haber hecho.

#### Que armé?
Una app con Flask que responde a 8 métodos:
- signup (POST): Para registrar un usuario
- login (POST): Para loguear un usuario. Devuelve una session key requerida en métodos no públicos
- encuesta (POST): Para crear una nueva encuesta. Se le envía en el form_data varios datos, entre ellos un string parseable a json que describe las preguntas, respuestas, respuestas correctas. También puede recibir etiquetas que no son más que strings para poder identificar/buscar la encuesta
- encuesta/{id} (GET): Para recibir un json que describe la encuesta indicada por el id. El json no indica las respuestas correctas.
- listar?etiquetas?{lista de etiquetas} (POST): Devuelve todas las encuestas cuyas etiquetas contengan todas las indicadas por parámetro. Es post porque se necesita pasar datos de usuario ya que no es un método accesible por cualquiera.
- listar (POST): Lista todas las encuestas existentes en json.
- verificar/encuesta={id}&respuestas={lista de respuestas} (GET): Método abierto para cualquiera, recibe por parámetros el id de la encuesta y una lista de diccionarios con clave para el id de la pregunta y el id de la respuesta dada por el usuario. Devuelve un json que indica el total de preguntas y el total de preguntas correctas
- listar_dm (GET): Método que armé para chequear en cualquier momento el estado del sistema.

En general no tuve muchas dificultades, las cosas que me complicaron principalmente fueron temas que desconocía. Un primer pequeño traspié fue al inicio, los requerimientos no parecían complicados y por eso no los revisé mucho, al rato andaba con dudas y revisando una y otra vez así que volví para atrás y me puse a pensar como corresponde el diseño sin subestimar el enunciado.\
Para cuando llegó el momento de 'deployear' ahí si tuve inconvenientes, no conocía formas de hacerlo para una aplicación Flask. Por esto estuve gran parte del sábado leyendo sobre docker, gunicorn, tutoriales, etc. Anécdota graciosa: Luego de tres horas no entendía por qué seguía sin levantar docker. Resulta que windows necesitaba actualizarse nomás... *(Ahora resulta graciosa)* \
Para el tema tests tuve complicaciones similares, conflictos de paquetes, no me quedaba claro de donde tomaba algunas cosas, pero bien, pude armar algunos pocos tests para cada método. Lo ideal habría sido ir armándolos a medida que implementaba cada método, lo cual me habría ayudado bastante, pero al desconocer la herramienta pytest no sabía cuanto me tomaría en aprender lo básico para usarlo.\
Como comentaba al inicio de esta sección, no llegué a implementar varias cosas. A continuación dejo una lista que me gustaría haber podido completar:
- Implementar sqlite. No lo usé nunca, pero es un módulo incluido en python que no requiere una instalación aparte.
- sessions de flask. Flask tiene un módulo para manejar sesiones que es mucho más poderoso que el que armé y maneja por sí solo muchas cuestiones que facilita mucho el desarrollo de un sistema de logueo.
- Mejorar algunos métodos. No todos los métodos tienen estructuras similares en cuanto a endpoint o json de respuesta. Me gustaría unificar un poco los estilos que usan. Las respuestas en json deberían mejorarse, por ejemplo no tiene mucho sentido el campo 'exito' en algunas respuestas y además a veces no se devuelve.
- A nivel diseño hay algunas clases que creo que podrían mejorar

## 3. Instrucciones de ejecución

- Clonar el repo
```
git clone https://github.com/lautaroh2394/sistema-encuestas.git
```

- Posicionado en la carpeta del repositorio ejecutar:
```
.../sistema-encuestas> docker build -t sistema-encuestas .
.../sistema-encuestas> docker run -dp 5000:5000 sistema-encuestas
```
(Tema nuevo para mi docker, no se si me estoy salteando algún prerequisito, pude iniciar el container y al hacer requests recibo respuestas de forma correcta)

- Para ejecutar localmente en modo debug (windows):
```
.../sistema-encuestas> venv/Scripts/activate
.../sistema-encuestas> pip install -e .
.../sistema-encuestas> $env:FLASK_APP = "flaskr"
.../sistema-encuestas> $env:FLASK_ENV = "development"
.../sistema-encuestas> flask run
```

Se puede importar la colección de Postman en la carpeta 'postman' para enviar requests prearmados al servidor. \
Recordar que luego de crear un usuario (request "signup") se debe loguear a través del request "login". Este devuelve una 'session_key' la cual debe usarse en las siguientes peticiones:
- encuesta consulta (GET /encuesta/{id_encuesta})
- verificar (GET /verificar/encuesta_id={id_encuesta}&respuestas={lista de mapas con id de pregunta y id de repuesta dada})

Para correr los tests (windows):
```
.../sistema-encuestas> venv/Scripts/activate
.../sistema-encuestas> pytest
```