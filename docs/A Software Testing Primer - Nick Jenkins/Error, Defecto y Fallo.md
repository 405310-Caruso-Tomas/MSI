El testing se enfoca en la identificación de errores, defectos y fallos dentro de un sistema. Para entender bien estos conceptos, es clave diferenciarlos.
****
***(Error)*** **Equivocación humana.** Ocurre cuando una persona comete una equivocación, ya sea al escribir el código o al documentar los requisitos del sistema. 
Surge de un malentendido, o descuido. El error puede introducir un defecto en el software.
- Un programador escribe mal una condición, por ejemplo.
****
***(Defecto)*** **El error se introduce en el sistema.** Consecuencia de un error que ha sido introducido en el código o en un documento. Cuando el programa se ejecuta, el defecto puede generar un comportamiento no deseado. **Es la anomalía en el código o diseño que provoca el incumplimiento de requisitos.**
- Debido al error en la condición lógica, el software no procesa correctamente los casos para dicha condición, y esto constituye un defecto.
El defecto puede categorizarse según la ***SEVERIDAD*** y ***PRIORIDAD*** del mismo. Estas características son mejor detalladas en el apartado [Gestión de Defectos](/carpeta/Gestión de Defectos).
****
***(Fallo)*** **El sistema no se comporta como debería.** Es la manifestación observable de un defecto, es decir, cuando el software no funciona como se espera en un caso de uso real, produciendo resultados incorrectos o un comportamiento inesperado. 
- El usuario ingresa un valor, y gracias al defecto anterior, el programa se detiene o produce un resultado incorrecto, mostrando un mensaje de error inesperado.
****
> *Un sinónimo común de defecto es el término bug. La palabra "bug" (bicho) tiene un origen curioso. En 1947, mientras trabajaban en la supercomputadora Mark II en la Universidad de Harvard, un grupo de científicos descubrió que una polilla se había colado dentro de la máquina, causando un mal funcionamiento. Este incidente fue registrado como el "primer caso real de un bug encontrado", y desde entonces, los defectos en software se conocen como "bugs".*