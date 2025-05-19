#### **1. Pruebas de Caja Blanca (White Box Testing)**
Se enfoca en validar la lógica interna del código y su estructura. El tester necesita acceso completo al código fuente para analizar su comportamiento y asegurar que cada línea funcione como se espera.
- Significan analizar el código en sí mismo
- Por lo general, están más al alcance de ser realizadas por los mismos desarrolladores.
- Pueden ser hechas en cualquier etapa del ciclo de vida de un software, pero tienden a encontrarse durante pruebas unitarias.
- Abarcan técnicas como 
	-La **Cobertura de Sentencias** (cada línea de código es ejecutada al menos una vez).
	-La **Cobertura de Desiciones** (todos los resultados if/switch son probados).
	-La **Cobertura de Caminos** (Recorre todos los caminos posibles en el código).
****
#### **2. Pruebas de Caja Negra (Black Box Testing)**
Probar la funcionalidad sin conocer la implementación interna del sistema. No requiere acceso al código fuente.
- Se basan en los requisitos del usuario y las especificaciones del sistema.
- Se enfocan en verificar un resultado específico con determinados valores de entrada.
- Las [[Pruebas de Aceptación]] del usuario es un ejemplo de los tests de caja negra.
- Abarcan técnicas como
	-**Partición de equivalencia** (se agrupan datos similares, y se los toma como el mismo caso de prueba para reducir los mismos).
	-**Pruebas de caso de uso** (valida que los flujos de usuario funcionen correctamente).


