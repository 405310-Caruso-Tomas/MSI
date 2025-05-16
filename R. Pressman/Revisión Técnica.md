%%cap 15 r pressman%%
Las revisiones del software son un “filtro” para el proceso del software. Es decir, se aplican en varios puntos durante la ingeniería de software y sirven para descubrir errores y defectos a fin de poder eliminarlos. Lo ideal sería el descubrimiento temprano de los errores, de modo que no se propaguen a la siguiente etapa.

En el contexto del proceso de software, los términos _defecto_ y _falla_ son sinónimos: implican un problema de [[Calidad]] descubierto ***después*** de haberse liberado el software a los usuarios finales .

Como parte de la ingeniería de software, pueden realizarse muchos diferentes tipos de revisiones. Una reunión informal alrededor de la máquina del café es una forma de revisión si se analizan problemas técnicos, por ejemplo.
****
###### **Revisión Técnica en Requerimientos**
Se pueden definir muchas métricas para las revisiones técnicas, este conjunto relativamente pequeño da una perspectiva útil. Aunque pueden ser aplicables no solamente a la revisión de requerimientos, el ejemplo será para la revisión de un modelo de requerimientos. Las métricas son:
- ***Esfuerzo de Preparación. $E_p$***: esfuerzo (en horas-hombre) requerido para revisar un producto del trabajo.
- ***Esfuerzo de Evaluación. $E_a$***: esfuerzo requerido (en horas-hombre) que se dedica a la revisión real.
- ***Esfuerzo de la Repetición. $E_r$***: esfuerzo (en horas-hombre) que se dedica a la corrección de los errores descubiertos durante la revisión.
- ***Tamaño del producto del trabajo, $\text{TPT}$***. medición del tamaño del producto del trabajo que se ha revisado (por ejemplo, número de modelos UML o número de páginas de documento o de líneas de código).
- ***Errores menores detectados. $Err_{menores}$***: número de errores detectados que requieren menos de algún esfuerzo especificado para corregirse.
- ***Errores mayores detectados. $Err_{mayores}$***: número de errores detectados que requieren más que algún esfuerzo especificado para corregirse.
Luego, el esfuerzo total de revisión y el número total de errores descubiertos es$$ E_{revisión} = E_p + E_a + E_r 
\space $$
$$Err_{tot} = Err_{menores} + Err_{mayores}$$
Lo que se hace con estas métricas es básicamente calcular la densidad del error, que está dada por: $$\text{Densidad del error} = \frac{Err_{tot}}{TPT}$$Una vez recabados los datos para muchas revisiones efectuadas en muchos proyectos, los valores promedio de la densidad del error permiten estimar el número de errores por hallar en un nuevo documento (aún no revisado). Si la densidad promedio de error para un modelo de requerimientos es de $0.6$ errores por página, y un nuevo modelo de requerimientos tiene una longitud de $32$ páginas, una estimación gruesa sugiere que el equipo de software encontrará alrededor de $19$ o $20$ errores durante la revisión del documento.
****
##### **Revisiones Informales**
Las revisiones informales incluyen una simple verificación de escritorio de un trabajo de ingeniería de software, hecha con algún colega, o una reunión casual con objeto de revisar un producto o aspectos orientados a la revisión de programación por pares. La eficacia de tales revisiones es mucho menor que la de los enfoques más formales. Pero una verificación de escritorio sencilla descubre errores que de otro modo se propagarían en el proceso del software.
****
##### **Revisiones Técnicas Formales**
**Actividad del control de calidad del software realizada por ingenieros de software. Se busca descubrir errores en funcionamiento, lógica o implementación, verificar que el software cumpla los requerimientos, garantizar que el software está representado de acuerdo con estándares predefinidos y hacer proyectos más manejables.**

Sin importar cuál formato de **RTF** se elija, cualquiera de ellos debe cumplir las restricciones siguientes: 
• En la revisión deben involucrarse de tres a cinco personas (normalmente). 
• Debe haber preparación previa, pero no debe exigir más de dos horas de trabajo de cada persona. 
• La duración de la reunión de revisión debe ser de al menos dos horas.

Se centra en una parte específica (y pequeña) del software general. El desarrollador del producto informa al ***líder del proyecto*** que ha terminado y que se requiere hacer una revisión. El líder del proyecto contacta al ***líder de la revisión***, este genera copias del producto y las distribuye a dos o tres **revisores** para la preparación previa. Se espera que cada revisor dedique de una a dos horas a la inspección del producto, tome notas y se familiarice con el trabajo. Al mismo tiempo, el líder del proyecto también revisa el producto y establece una agenda para la **reunión de revisión**. A la reunión de revisión acuden el líder de ésta, todos los revisores y el desarrollador. En esta reunión se "recorre" el producto del trabajo, mientras los revisores hacen sus comentarios. Se toma nota de los errores descubiertos. 
Al terminar, todos deciden si aceptan el producto, lo rechazan debido a errores graves (y una vez corregido se vuelve a hacer otra revisión) o aceptan el producto de forma provisional (se encontraron errores menores que deben corregirse, pero no es necesaria otra revisión). 
Una vez tomada la decisión, los asistentes firman el acta que indica su participación y su acuerdo con los descubrimientos del equipo de revisión.