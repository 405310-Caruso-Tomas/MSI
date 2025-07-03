En el desarrollo ágil, los [[Casos de Prueba]] son dados como criterios de aceptación.
****
Para las metodologías tradicionales, el [[Testing]] es una etapa que se realiza al final del proceso de desarrollo, mientras que para las metodologías ágiles, el [[Testing]] es una actividad continua que se realiza de forma iterativa y forma parte del ciclo de vida del producto.
![[Pasted image 20250605080532.png]]
Todo el equipo es responsable de la calidad del producto en las metodologías de este último tipo (testers y especialistas QA deben participar en eventos clave de Scrum como reuniones diarias, refinamiento, y demás). 
Esta adaptación del testing ágil trae como ventajas la detección temprana de errores, reducción de costos y mayor valor entregado al cliente. Existen prácticas que podríamos referir al "Testing Ágil" que se adecuan a estos ciclos de retroalimentación cortos fundamentales para [[Modelos Ágiles]], entre ellas se encuentran las enunciadas abajo.
****
#### **Test Driven Development (TDD)**

> Técnica de diseño e implementación de software que forma parte de la metodología XP (Extreme Programming), desarrollada por Kent Beck (más información en el apartado de [[Agilidad]]) alrededor del 2003. 

Para esta práctica los desarrolladores escriben pruebas unitarias antes de escribir el código fuente (pruebas que por supuesto van a fallar por obvias razones), luego se escribe el código mínimo para que cada prueba pase, y finalmente se optimiza el código en conjunto sin alterar su funcionalidad. Este proceso se conoce como ***"Red-Green-Refactor"***.
Esto garantiza que solo se agregue el código suficiente para que la prueba pase, proporcionando la solución más simple a un problema de software.
El **TDD** crea ciclos de retroalimentación cortos mediante la regresión a nivel de unidad y significa que el código se autodocumenta eficazmente a través de sus pruebas integradas, por lo que se integra de manera natural con [[Modelos Ágiles]].
![[Pasted image 20250605085036.png]]
El desarrollador no solo puede ver qué hace el código, sino que también comprende por qué.
**Ejemplo.** (La primera función es la escrita con anterioridad)
```python
def test_calcular_cuadrado():
    assert calcular_cuadrado(3) == 9, "El cuadrado de 3 debe ser 9"
    assert calcular_cuadrado(0) == 0, "El cuadrado de 0 debe ser 0"
    assert calcular_cuadrado(-2) == 4, "El cuadrado de -2 debe ser 4"

def calcular_cuadrado(numero):
    return numero * numero
```

*Se dice hay hasta beneficios psicológicos para el uso de esta práctica, reduciendo el estrés y aumentando la satisfacción laboral al minimizar errores inesperados, lo cual es comprensible cuando cada funcionalidad tiene una prueba asociada, asegurando cobertura completa.*
****
#### **Behavior Driven Development (BDD)**
Los conceptos básicos del TDD se han ampliado para incluir pruebas de nivel superior y definir el comportamiento esperado del software desde la perspectiva del usuario, y del negocio. Esto se conoce como "***Especificación por ejemplo***".

> Es un enfoque de desarrollo de software que utiliza un lenguaje natural para describir el comportamiento esperado del sistema, asegurando que cumpla con las expectativas del usuario. Se basa en escribir escenarios en formato **"[[Given-When-Then (Dado-Cuando-Entonces)]]**" que sirven como pruebas ejecutables y documentación.

***Este enfoque asegura que las pruebas sean comprensibles, ejecutables***, proporcionando un marco para definir y validar el comportamiento del sistema de manera colaborativa.
BDD puede considerarse una evolución de TDD, ya que combina las técnicas de TDD con un enfoque más orientado al negocio, haciendo que las pruebas sean más accesibles y comprensibles para las partes interesadas no técnicas.
![[Pasted image 20250605092843.png]]
En BDD, el ciclo de desarrollo no necesariamente implica hacer TDD primero, sino que comienza con la definición de criterios de aceptación en forma de escenarios de comportamiento. El flujo típico que se repite sigue de la forma:
1. **Definir criterios de aceptación**: Se escriben escenarios en [[Given-When-Then (Dado-Cuando-Entonces)]] colaborativamente.
2. **Automatizar pruebas de comportamiento**: Convertir escenarios en pruebas ejecutables. Se suelen utilizar herramientas como Cucumber, Behave o SpecFlow.
3. **Usar TDD (si aplica)**: Escribir pruebas unitarias (TDD) para desarrollar el código que cumpla con las pruebas de comportamiento.
4. **Implementar y refactorizar**: Escribir el código funcional, ejecutando pruebas de comportamiento y unitarias para validar.

De momento, la información de este inciso la considero suficiente para entender a grandes rasgos ambas metodologías. Sin embargo, en el apartado de [[Implementación del BDD]] se hace un ejemplo más práctico del uso del BDD con herramientas reales.
****
#### **Acceptance Test Driven Development (ATDD)**
Como pasa con las prácticas mencionadas arriba, la siguiente también agrega un nivel más a lo que sería la definición de la funcionalidad del sistema. **ATDD** opera a un nivel más alto, enfocándose en funcionalidad completa desde la perspectiva del usuario, por lo que una de las diferencias con BDD es que **las pruebas escritas durante ATDD son pensadas para que sean leídas por clientes.**

> Metodología de desarrollo de software ágil que fomenta la colaboración entre **clientes**, **desarrolladores** y **testers** para definir criterios de aceptación antes de iniciar la codificación.

ATDD comparte principios con otras metodologías como **Test-Driven Development (TDD)**, **Behavior-Driven Development (BDD)**, pero se distingue por la colaboración de las tres partes (a menudo referida como los "three amigos": **cliente, desarrollador y tester**). El enfoque está 
El ciclo de desarrollo se ve de la siguiente forma:
1. **Discutir**: Los "tres amigos" (cliente, desarrollador, tester) colaboran en un taller de especificación para definir los requisitos a través de historias de usuario y criterios de aceptación. Este paso busca alinear expectativas. **Ejemplo**: Para una funcionalidad de "pago con tarjeta de crédito", los tres amigos discuten **cómo** el sistema debe manejar transacciones válidas e inválidas.
2. **Destilar**: Los requisitos se convierten en pruebas de aceptación claras y concisas, a menudo utilizando el formato [[Given-When-Then (Dado-Cuando-Entonces)]].
3. **Desarrollar**: Los desarrolladores escriben el código necesario para que las pruebas de aceptación pasen.
4. **Demostrar**: Se presenta un prototipo funcional a los interesados para obtener retroalimentación. Esto permite iterar sobre el producto y ajustar los requisitos si es necesario.
En general, ATDD no incluye TDD, pero ambas metodologías pueden complementarse en un proyecto de desarrollo ágil.
****
Para evitar mareos, se enuncia de forma más breve cada metodología nuevamente:
• **TDD (Test Driven Development):** El ciclo comienza con la escritura de una prueba que falla, luego se escribe el código mínimo necesario para pasar la prueba, y finalmente se refactoriza el código para mejorarlo.

• **BDD (Behavior Driven Development):** Se enfoca en el comportamiento del sistema a través de escenarios, permitiendo definir los requisitos de manera que todos los miembros del equipo los comprendan. 

**• ATDD (Acceptance Test Driven Development):** Implica discusiones entre el equipo para definir los criterios de aceptación antes de escribir el código, seguido de la demostración y el desarrollo.