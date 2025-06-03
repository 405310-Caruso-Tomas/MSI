El desarrollo de software implica ambigüedad, suposiciones y comunicación humana defectuosa. Cada cambio realizado a una pieza de software, introduce el riesgo de error, testing reduce ese riesgo.
Se suelen utilizar diferentes enfoques y [[Enfoques de Testing]] para lograr reducir el riesgo.
****
***Concepto.*** Serie de actividades orientadas a recopilar información sobre el funcionamiento y comportamiento de una aplicación, con el fin de determinar si está lista para su uso público o generalizado.
**Otra definición.** IEEE (1990): *“El proceso de operar un sistema o componente bajo condiciones específicas, observando o registrando los resultados, y evaluando algún aspecto del sistema o componente.”*
****
- Podemos usar procesos de [[QA (Quality Assurance o Aseguramiento de la Calidad)]] para intentar prevenir defectos en el software, pero lo único que podemos hacer para reducir la cantidad de errores ya presente es testear.
- El testing también nos ayuda a cuantificar los [[Riesgos]] en un software no probado. Sobre todo cuando usamos un ciclo de testing.
- **Mindset.** Un tester profesional encara esta actividad suponiendo que el producto está roto, y ya tiene defectos por descubrir. Siempre se hace la pregunta **¿por qué?**, y buscan la certeza donde no la hay. Desarrolladores y diseñadores pueden adoptar esta mentalidad también, lo cual beneficia enormemente al proyecto. Más sobre esto, en el inciso de [[Roles en el Testing]].
****
Idealmente las pruebas deberían llevarse a cabo a lo largo del ciclo de vida del desarrollo, ya que a medida que retrasamos la evaluación del producto durante el desarrollo, también aumenta la complejidad de resolver los problemas.
##### **Trazabilidad**
Otra función del testing es (de manera extraña) confirmar lo que se ha entregado. "Que sea rastreable".
Dado un proyecto complejo con miles de requisitos de posibles clientes, ***¿cómo sabemos que se cumplen las expectativas?*** ¿Cómo demostramos que se ha cumplido un requerimiento en particular?. 

*(Una posible solución es el uso de herramientas disponibles en el mercado que utilizan bases de datos para rastrear requisitos, y están vinculadas a otras herramientas de especificación de pruebas.)*.
****
***Retesteo. (Volver a testear)***. Es el acto de repetir una prueba para verificar que el defecto encontrado fue correctamente arreglado.
****
###### ****¿Cuánto testing es suficiente?****
Los errores humanos son impredecibles, por lo tanto no es posible probar todas las combinaciones posibles de errores o defectos. Esto hace que el testing exhaustivo sea imposible, ya que no podemos cubrir cada posible situación en la que el software podría fallar. 
Pero en un proyecto, determinar cuánto testing es necesario y suficiente para garantizar calidad, es por supuesto algo que nos interesa. Para resolver esta cuestión, se utilizan dos variables clave: [[Riesgos]] y [[Costos]].

