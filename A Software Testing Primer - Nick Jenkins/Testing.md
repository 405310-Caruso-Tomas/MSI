El desarrollo de software implica ambigüedad, suposiciones y comunicación humana defectuosa. Cada cambio realizado a una pieza de software, introduce el riesgo de error, testing reduce ese riesgo.
Se suelen utilizar diferentes enfoques y [[Enfoques de Testing]] para lograr reducir el riesgo.
****
***Concepto.*** %%LEETE EL TEORICO%%
****
- Podemos usar procesos de [[QA (Quality Assurance o Aseguramiento de la Calidad)]] para intentar prevenir defectos en el software, pero lo único que podemos hacer para reducir la cantidad de errores ya presente es testear.
- El testing también nos ayuda a cuantificar los [[Riesgos]] en un software no probado. Sobre todo cuando usamos un ciclo de testing.
- **Mindset.** Un tester profesional encara esta actividad suponiendo que el producto está roto, y ya tiene defectos por descubrir. Siempre se hace la pregunta **¿por qué?**, y buscan la certeza donde no la hay. Desarrolladores y diseñadores pueden adoptar esta mentalidad también, lo cual beneficia enormemente al proyecto.
****
Idealmente las pruebas deberían llevarse a cabo a lo largo del ciclo de vida del desarrollo, ya que a medida que retrasamos la evaluación del producto durante el desarrollo, también aumenta la complejidad de resolver los problemas.
##### **Trazabilidad**
Otra función del testing es (de manera extraña) confirmar lo que se ha entregado. 
Dado un proyecto complejo con miles de requisitos de posibles clientes, ***¿cómo sabemos que se cumplen las expectativas?*** ¿Cómo demostramos que se ha cumplido un requerimiento en particular?. 

*(Una posible solución es el uso de herramientas disponibles en el mercado que utilizan bases de datos para rastrear requisitos, y están vinculadas a otras herramientas de especificación de pruebas.)*.
****
##### **Testea Temprano y Frecuente**

> [!Barry_Boehm]
> ***“Un error encontrado en la fase de diseño cuesta diez veces menos que uno en la codificación y cien veces menos que uno encontrado después del lanzamiento.”*** 

Si quieres encontrar errores, comienza tan pronto como sea posible.
Eso significa pruebas unitarias para los desarrolladores, pruebas de integración durante el ensamblaje y pruebas de sistema, **en ese orden de prioridad**.
****
***Pruebas de Regresión.***  Es el acto de repetir otras pruebas en áreas 'paralelas', o que comparten una misma implementación, para asegurarse de que un cambio de código no haya introducido otros errores o comportamientos inesperados, en otros módulos del sistema.
Se centra en validar que cambios recientes no hayan roto funcionalidades anteriores.
**(Es muy común que el cambio en el código realizado para arreglar un error introduzca errores adicionales en otras partes o componentes del software.)**

***Retesteo. (Volver a testear)***. Es el acto de repetir una prueba para verificar que el defecto encontrado fue correctamente arreglado.
****
