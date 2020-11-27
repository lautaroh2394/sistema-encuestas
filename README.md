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

- Como dueño de producto, me gustaría tener un sistema que me permita realizar encuestas                                            ⛌
- Como dueño de producto, me gustaría que cada pregunta pueda tener una o más respuestas.                                           * listo DM, falta metodo para app flask
- Como dueño de producto, me gustaría que cada pregunta pueda tener como máximo 4 respuestas.                                       * listo DM, falta metodo para app flask
- Como dueño de producto, me gustaría que mi aplicación de encuestas posea un login para usuarios.                                  * listo DM, falta metodo para app flask 
    (mantener sesiones de manera súper básica: 
        al loguear devolver un código al ente que llamó al login. 
        mantener una lista de usuarios logueados junto con el código que se devolvió. 
        cada vez que el usuario haga un post, debe indicar su usuario y este codigo)

- Como dueño de producto, me gustaría que los usuarios de mi aplicación puedan cargar preguntas y sus respectivas respuestas.       * listo DM, falta metodo para app flask
- Como dueño de producto, me gustaría que se puedan responder encuestas sin estar registrado en el sistema.                         
- Como dueño de producto, me gustaría que solo los usuarios registrados puedan cargar encuestas.
- Como dueño de producto, me gustaría poder revisar un historial de preguntas por usuario.
- Como dueño de producto, me gustaría poder agrupar encuestas a través de etiquetas.
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


## 3. Instrucciones de ejecución