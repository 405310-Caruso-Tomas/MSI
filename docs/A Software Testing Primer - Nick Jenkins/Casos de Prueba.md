> Un caso de prueba es un elemento fundamental en el proceso de pruebas de software, que nos asegura la cobertura adecuada de los [Requerimientos](/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos) del sistema.
****
- Su propósito principal es verificar que una funcionalidad específica de un producto de **[Software](/carpeta/Software)** opere según lo esperado.

*Definición Norma ISO 29119 (2007)*. Conjunto de precondiciones, entradas y resultados esperados, diseñados para guiar la ejecución de una prueba con el fin de alcanzar los objetivos del proceso de prueba.
Puede describirse también como un conjunto de condiciones que el analista de [QA (Quality Assurance o Aseguramiento de la Calidad)](/carpeta/QA (Quality Assurance o Aseguramiento de la Calidad)) debe validar.
En lineas generales, son una herramienta que traza el comportamiento del sistema, y de la misma forma, pueden documentarse estos mismos con herramientas como hojas de cálculo (Excel) o automatizadas de gestión de pruebas (Qase, por ejemplo).
****
##### ****Elementos de un Caso de prueba****
Por lo general se compone de los siguientes elementos:
1. **Objetivo**: Qué funcionalidad o comportamiento del sistema se va a validar. 
2. **Datos de entrada y ambiente**: Valores de entrada necesarios y las condiciones del entorno (hardware, software, configuración) bajo las cuales se ejecutará la prueba. 
3. **Comportamiento esperado y actual**: Cuál es el resultado que se espera obtener y el comportamiento real observado durante la ejecución.
Los más recomendados, y utilizados en el curso son los de la imagen.
![Pasted image 20250529101712.png](/carpeta/Pasted image 20250529101712.png)
La estructura cuenta con las siguientes columnas:
- **Nro. Caso de Prueba.** ID para facilitar trazabilidad.
- **Prioridad (Alta, Media, Baja).** Importancia del caso de prueba.
- **Precondiciones.** Estado inicial o condiciones previas que deben cumplirse antes de la ejecución.
- **Pasos.** Acciones que el usuario o el sistema deben seguir durante la prueba. Secuencia lógica.
- **Resultado Esperado.** Lo que el sistema debe mostrar o hacer si todo se ejecuta correctamente.
- **Estado (Pasa/Falla)**. ¿El caso de prueba ha fallado o pasado?. En caso de fallo, se debe especificar el punto exacto del error y su descripción.
****
**Características.** Un caso de prueba debe ser **PRECISO** (Sin ambigüedades, evitando información innecesaria), **RASTREABLE** (Vinculado a algún requisito), **REPETIBLE** (Puede ejecutarse varias veces en diferentes entornos), **REUTILIZABLE** (Genérico.) 
****
Es importante destacar que la relación entre los requisitos y los casos de prueba no siempre es uno a uno. En muchos casos, un solo requisito puede necesitar varios casos de prueba para ser completamente validado. Existen metodologías, como **RUP** (Proceso Unificado de Rational), que especifican debería haber dos casos de prueba por requerimiento: uno negativo y otro positivo.
##### ****Casos de prueba POSITIVOS y NEGATIVOS.****
Un caso de prueba positivo está destinado a demostrar que la función se comporta como se requiere con una entrada correcta y un caso de prueba negativo está destinado a demostrar que la función no provoca un error con una entrada incorrecta (o responde de manera adecuada a ese error).
****
###### ****Ejemplos****
Supongamos los siguientes casos de prueba para un sistema GPS. El primero es un ejemplo de un caso de prueba positivo, a diferencia del tercero, que se trata de uno negativo.
![Pasted image 20250529102932.png](/carpeta/Pasted image 20250529102932.png)
![Pasted image 20250529103010.png](/carpeta/Pasted image 20250529103010.png)
Ahora recordemos, como vimos más arriba, que en caso de un error en un caso de prueba, es decir, que el sistema no se comporte como lo esperado, se debe documentar el mismo de cierta forma, especificando el estado del mismo. El siguiente es un ejemplo de esto.
![Pasted image 20250529103513.png](/carpeta/Pasted image 20250529103513.png)