**Gherkin** es un lenguaje de patrones en inglés simple que se usa para especificar **ejemplos** de **escenarios** que ilustran las reglas o **[Criterios de Aceptación](/carpeta/Criterios de Aceptación)** detrás de un **requisito**.
La estructura es un escenario con la forma: 
- **Dado** (un conjunto de condiciones previas o contexto)
- **Cuando** (se inicia una acción o un disparador) 
- **Entonces** (el programa produce un resultado o un resultado)

> [!Jenkins] 
> *"Cuando Gherkin está vinculado al desarrollo metodologías como BDD, esto proporciona un virtuoso bucle de retroalimentación donde la especificación valida directamente el comportamiento de la aplicación a través de [Pruebas Automatizadas](/carpeta/Pruebas Automatizadas). Esto minimiza los problemas de mantenimiento con pruebas, proporciona un conjunto de pruebas que son directamente rastreables a los requisitos y ofrece a los desarrolladores una forma de refactorizar constructivamente su código.”*

****
##### **Given (Dado)**
Establece el **contexto inicial** o las condiciones previas de un escenario. Describe el estado del sistema antes de que ocurra la acción principal.
Se utiliza para definir las precondiciones necesarias para que el escenario tenga sentido. Por ejemplo, datos iniciales, configuraciones o estados del sistema.
****
##### **When (Cuando)**
Describe la acción o el evento que desencadena un cambio en el sistema. Es el paso donde se realiza la interacción principal que se está probando.
Representa lo que el usuario o el sistema hace para provocar una respuesta.
****
##### **Then (Entonces)**
Especifica el **resultado esperado** tras la acción realizada en el "When". Define cómo debería comportarse el sistema o qué debería observarse.
Se usa para verificar los resultados de la acción, comprobando si el sistema cumple con el comportamiento esperado.
****
###### **Ejemplo. Estructura Completa de un Escenario en Gherkin**
```gherkin
Feature: Inicio de sesión de usuario
  Scenario: Inicio de sesión exitoso
    Given que un usuario está registrado en el sistema
    And el usuario tiene credenciales válidas
    When el usuario inicia sesión con credenciales válidas
    Then el usuario es redirigido al panel principal
    And se muestra un mensaje de bienvenida
```
Un escenario típico en Gherkin combina estos tres elementos para describir un comportamiento específico. Además, puede incluir otros elementos como And (Y) o But (Pero) para añadir más condiciones o resultados.
En otros ejemplos, la parte de "Escenario (Scenario)" suele ser más larga, pero al fin y al cabo se busca simplemente dar una descripción de la funcionalidad y el resultado esperado. 
Por otra parte, el agregado de "Funcionalidad (Feature)" hace referencia a esto mismo, solamente la funcionalidad que se está trabajando en el criterio de aceptación. Puede funcionar como identificador para el escenario.
****
Los escenarios en Gherkin sirven como un puente entre la descripción de alto nivel de las [Historias de Usuario](/carpeta/Historias de Usuario) ("Criterios de Aceptación") y las [Pruebas Automatizadas](/carpeta/Pruebas Automatizadas), ya que cada paso (Given, When, Then) puede ser mapeado a código ejecutable.