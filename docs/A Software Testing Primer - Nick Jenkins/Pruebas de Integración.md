*Las unidades más pequeñas se integran en unidades más grandes, y estas, a su vez, en el sistema general.* 

Estas pruebas difieren de las pruebas unitarias en que las unidades **ya no se prueban de forma independiente, sino en grupos**, y el enfoque se desplaza de las unidades individuales a **la interacción entre ellas**.
****
El objetivo principal de las pruebas de integración es **GARANTIZAR funcionalidad conjunta**, identificar fallos que puedan surgir en las interfaces entre los módulos, como errores en la transmisión de datos, problemas de sincronización o dependencias mal gestionadas.
****
###### **¿Qué se hace en las pruebas de integración?.** 
Se crean casos de prueba específicos para examinar las interacciones entre módulos. Algunos ejemplos de lo que se podría probar incluyen:

- La comunicación entre dos servicios web.
- La integración de un frontend con un backend.

Se pueden utilizar distintos enfoques para llevar a cabo estas pruebas, como la **integración progresiva** (agregar módulos uno por uno) o la **integración a gran escala**, donde se prueba todo el sistema de una vez.
****
###### **¿Quién realiza las pruebas de integración?**
Las pruebas de integración suelen ser realizadas tanto por los desarrolladores como por los equipos de [QA (Quality Assurance o Aseguramiento de la Calidad)](/A Software Testing Primer - Nick Jenkins/QA (Quality Assurance o Aseguramiento de la Calidad)).

Los desarrolladores realizan pruebas básicas de integración mientras construyen el software, pero el equipo de QA normalmente lleva a cabo pruebas más exhaustivas en un entorno que simula mejor la interacción real entre los módulos.
****
###### **Tipos de Pruebas de Integración**
Las pruebas de integración pueden ser utilizadas para verificar diferentes características del código, y suelen responder a las preguntas:

- ***Enfoque Big-Bang.*** Todos los módulos se integran de una sola vez y se prueban como un sistema completo. Este enfoque puede dificultar la localización de errores si los fallos son numerosos. Los módulos deben estar implementados y conectados entre sí.
- ***De Integración Incremental.*** Los módulos se integran y prueban de manera gradual, uno a uno. Se pueden realizar en dos subtipos: 
	- **Top-Down** (de arriba hacia abajo) - Los módulos de alto nivel se prueban primero y se van integrando gradualmente los módulos de nivel inferior.
	- Ejemplo: En una aplicación web, primero se integraría el frontend con el controlador, luego el controlador con el backend, y finalmente el backend con la base de datos.
	- **Bottom-Up** (de abajo hacia arriba) - Se comienza integrando los módulos de bajo nivel y se va ascendiendo a los de alto nivel.
- ***Pruebas de Integración Continua.*** Común en [Modelos Ágiles](/R. Pressman/Modelos Ágiles) y DevOps, las pruebas de integración se realizan de forma continua a medida que se desarrollan nuevos componentes. Con cada cambio en el código se ejecuta una prueba de integración. Suelen ser automáticas.
	- Ejemplo: Cada vez que un desarrollador sube cambios al repositorio de código, se ejecutan automáticamente las pruebas de integración para asegurar que esos cambios no rompan la funcionalidad de otros módulos.
- ***Pruebas de Interfaz.*** Refieren a la **COMUNICACIÓN**. Verifican que las interfaces (por ejemplo, APIs REST, gRPC) manejen correctamente las solicitudes y respuestas, y que los módulos se comuniquen correctamente (que se envíen y reciban los datos correctamente). 
****
A su vez, podemos sumar otros tipos de pruebas a la lista, las **Pruebas de Integración de Extremo a Extremo**, se tratan de probar un proceso completo que ofrece el sistema, pasando por todos los módulos que harían posible el proceso. Un ejemplo de este último podría ser probar un proceso completo de compra en un sitio web, desde el frontend hasta el backend y la base de datos.

Por otro lado, **es muy común que el cambio en el código realizado para arreglar un error introduzca errores adicionales en otras partes o componentes del software**, y por ello existen las llamadas:
***Pruebas de Regresión.***  Es el acto de repetir otras pruebas en áreas 'paralelas', o que comparten una misma implementación, para asegurarse de que un cambio de código no haya introducido otros errores o comportamientos inesperados, en otros módulos del sistema.
Se centra en validar que cambios recientes no hayan roto funcionalidades anteriores.
