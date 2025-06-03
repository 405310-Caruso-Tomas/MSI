#### **1. Pruebas de Caja Blanca (White Box Testing)**
Conocidas también como *pruebas **estructurales***.
Se enfoca en validar la lógica interna del código y su estructura. 
El tester necesita acceso completo al código fuente para analizar el flujo del programa y asegurar que cada línea funcione como se espera.
- Significan analizar el código en sí mismo, y tener un entendimiento profundo de este.
- Se busca que ***el software se comporte correctamente en todas las situaciones posibles.***
- Por lo general, están más al alcance de ser realizadas por los mismos desarrolladores.
- Pueden ser hechas en cualquier etapa del ciclo de vida de un software, pero tienden a encontrarse durante pruebas unitarias.
- Abarcan técnicas como 
	-La **Cobertura de Sentencias** (cada sentencia ejecutable en el código es ejecutada al menos una vez durante la prueba: mientras se ejecute, está cubierta, sin importar condicionales o ciclos).
	-La **Cobertura de Decisiones** (todos los resultados if/switch son probados).
	-La **Cobertura de Caminos** (Recorre todos los caminos posibles en el código).
	-[[Pruebas Unitarias]].
****
#### **2. Pruebas de Caja Negra (Black Box Testing)**
Probar la funcionalidad sin conocer la implementación interna del sistema. No requiere acceso al código fuente.
- Se basan en los requisitos del usuario y las especificaciones del sistema.
- Se enfocan en verificar un resultado específico con determinados valores de entrada.
- Las [[Pruebas de Aceptación]] del usuario es un ejemplo de los tests de caja negra.
- Abarcan técnicas como
	-**Partición de equivalencia** (se agrupan datos similares, y se los toma como el mismo caso de prueba para reducir los mismos).
	-**Pruebas de caso de uso** (valida que los flujos de usuario funcionen correctamente).
	-**Análisis de valores límite** (verificar comportamiento con valores extremos de entrada)
	-**Tablas de decisión** (utilizar tablas para representar condiciones de entrada y sus salidas correspondientes)
- **Ejemplo.** Pruebas de login, ingresar combinaciones de usuario y contraseña (correctas, incorrectas, vacías) para comprobar que el sistema responde de manera adecuada.

****

[Pruebas de usabilidad](https://chatgpt.com/c/683eea96-2ef8-8001-81eb-9918e84a67c6) resumir esto