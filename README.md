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
- Como dueño de producto, me gustaría que se puedan responder encuestas sin estar registrado en el sistema.                         * se pueden pedir encuestas anónimamente, aún no se pueden evaluar encuestas anónimamente
- Como dueño de producto, me gustaría que solo los usuarios registrados puedan cargar encuestas.                                    ⛌
- Como dueño de producto, me gustaría poder revisar un historial de preguntas por usuario.
- Como dueño de producto, me gustaría poder agrupar encuestas a través de etiquetas.                                                * falta método en DM para filtrar por etiquetas
- Como dueño de producto, me gustaría poder acceder a un listado de todas las encuestas del sistema.
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
- Para tema login de usuarios se que Flask tiene un módulo 'session' que facilita mucho esto, pero nunca lo usé y no quise 'perder' el tiempo. Armé una entidad que maneja de manera muy muy básica las sesiones, pero siempre pensando que dentro de lo posible lo mejor será aprenderlo y usarlo.
- Siguiendo con el tema de sesiones, mi idea es que el usuario al loguearse reciba una key, y en futuras consultas deba indicar su usuario y esta key.


## 3. Instrucciones de ejecución