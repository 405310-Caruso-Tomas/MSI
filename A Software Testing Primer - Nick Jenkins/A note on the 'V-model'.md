%%Este apartado es una especie de agregado (básicamente porque es mencionado en el apunte teórico de la materia y puesto como una nota en el libro)%%
Por lo general el enfoque de pruebas sigue el modelo en **V**, modelo el cual Nick Jenkins denomina "horrible". Este tipo de [[Modelos de PROCESO]] (brevemente mencionado en su respectivo inciso) estructura el desarrollo en niveles.
![[Pasted image 20250526093232.png]]
- Para cada fase de desarrollo en la parte izquierda, se define un nivel de prueba correspondiente en la parte derecha. Por ejemplo:
    - Los requisitos del sistema se validan mediante pruebas de aceptación.
    - El diseño detallado se verifica con pruebas unitarias.
- Las pruebas se planifican en paralelo, pero su ejecución ocurre después de que se completa el desarrollo del código.
****
**Opinión del amigo Jenkins.**
"*No me gusta porque prioriza las tareas de verificación sobre las de validación. Al igual que el modelo en cascada, se basa en la perfección de cada fase y, en última instancia, solo detecta errores al final del ciclo. Los errores se propagan fácilmente de una fase a otra, consumiendo tiempo y esfuerzo*".
"*Sin embargo, el modelo V ilustra la importancia de los diferentes niveles de pruebas en las distintas fases del proyecto.*"