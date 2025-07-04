El [PROCESO](/carpeta/PROCESO) de pruebas de software incluye una serie de actividades esenciales que aseguran la [Calidad](/carpeta/Calidad) del producto.
![Pasted image 20250529112546.png](/carpeta/Pasted image 20250529112546.png)
****
##### **Planificación de las Pruebas.**
Esta etapa implica definir el enfoque, los objetivos, el alcance y los recursos necesarios para las pruebas. Se establece un **plan de pruebas** que detalla qué se probará, cómo se probará y quién lo hará.
El **PLAN DE PRUEBAS** es el documento que incluye la asignación de recursos, la gestión de riesgos y los criterios de cobertura de las pruebas, lo que facilita la toma de decisiones durante todo el proceso.
Por lo general, un plan de prueba cuenta con los siguientes elementos:
- **Introducción.** Propósito y alcance del plan.
- **Características a probar.** Lista de aspectos/requisitos a probar.
- **Características que no deben ser probadas.** 
- **Supuestos.** Suposiciones que se tienen respecto a cierta funcionalidad o módulo del sistema en particular.
- **Aproximación.** Estrategia general (manuales, automatizadas).
- **Criterios de Aceptación.** 
- **Entregables de las pruebas.** Cómo serán documentados los resultados de las pruebas. (Los [Casos de Prueba](/carpeta/Casos de Prueba), por ejemplo, sirven como base para esta documentación.)
- **Tareas de prueba.** Actividades específicas que se realizarán en las pruebas. (Crear los [Casos de Prueba](/carpeta/Casos de Prueba), por ejemplo)
- **Ambiente.** Descripción del entorno de pruebas (hardware, software, configuraciones) necesario para la ejecución de los casos de prueba.

El punto de partida más común para la planificación de pruebas es una descomposición funcional del producto basada en una especificación técnica, esto nos permite abordar distintas características deseables a testear. Este es un excelente punto de partida, pero no debe ser el único aspecto que se aborde; de lo contrario, las pruebas se limitarán a la 'verificación' pero no a la 'validación'. A continuación una lista de aspectos comunes a verificar: ![Pasted image 20250529114432.png](/carpeta/Pasted image 20250529114432.png)

Diversas fuentes sugieren en esta etapa identificar objetivos a testear (funcionalidad o rendimiento), y definir métricas de éxito, en cierto período de tiempo. Otra sugerencia suele ser que los criterios de aceptación de las historias de usuario sirvan como base para las pruebas.
****
##### **Especificación de las Pruebas.**
Esta fase consiste en la definición detallada de los [Casos de Prueba](/carpeta/Casos de Prueba), considerando principalmente el ambiente de prueba.
**Actividades clave**:
- **Analizar los requisitos o historias de usuario para identificar casos de prueba.**
- **Diseñar casos de prueba con entradas, pasos y resultados esperados.**
- **Preparar datos de prueba (reales o simulados).**
- **Priorizar casos de prueba según riesgos o criticidad.**
Es crucial en esta etapa asegurarse de que los requerimientos sean testeables, es decir, que puedan ser verificados de manera adecuada mediante pruebas.
****
##### **Ejecución de las Pruebas.**
Se ejecutan los casos de prueba en el entorno preparado, registrando los resultados y detectando defectos. El sistema pasa por todos los niveles de prueba detallados en otros incisos.
**Actividades clave**:
- **Configurar el entorno de pruebas.**
- **Ejecutar los casos de prueba (manual o automáticamente).**
- **Registrar los resultados (aprobado/fallido) y los defectos encontrados.**
- **Reproducir y documentar errores para el equipo de desarrollo.**
La correcta instalación de la versión del software previo a la ejecución de las pruebas (pero perteneciente a la etapa) se le denomina *build*. 
****
##### **Análisis de las Pruebas.**
El análisis, es **principalmente una fase en la que el probador de software aplica sus habilidades para interpretar los resultados obtenidos.** Estas habilidades se desarrollan a lo largo del tiempo, ya que el tester adquiere experiencia y conocimiento mientras participa en el proceso de pruebas.
Es en esta etapa, donde el probador compara los resultados reales con los esperados, se hace la clasificación de defectos
###### **Características clave de la etapa de análisis**
1. **Interpretación de resultados**:
    - El probador compara los **resultados reales** de la etapa de ejecución con los **resultados esperados** definidos en los casos de prueba.
2. **Clasificación de defectos**:
    - Los defectos encontrados se clasifican según su **severidad** y **prioridad**, como vimos en el apartado de [Gestión de Defectos](/carpeta/Gestión de Defectos).
3. **Toma de decisiones**:
    - Basado en el análisis, el probador recomienda acciones, como aprobar el software para su liberación, requerir correcciones y repetir pruebas (pruebas de regresión).
    - Se subraya la importancia de comunicar estas decisiones a los interesados (desarrolladores, gerentes, clientes) mediante reportes claros.
****
##### **Evaluación de las Pruebas.**
Se comparan los resultados obtenidos con los planes y criterios de aceptación previamente establecidos.
Se verifica que los entregables sean correctos, que los defectos hayan sido corregidos. 
Al finalizar, se elabora un resumen/reporte de los resultados. 
La imagen es un ejemplo de un reporte de una prueba de humo en forma manual.
![Pasted image 20250602221732.png](/carpeta/Pasted image 20250602221732.png)
La evaluación sobre si el software cumple con los criterios de salida definidos en el plan de pruebas, suele tener en cuenta aspectos como:
- Porcentaje mínimo de casos de prueba aprobados.
- Ausencia de defectos críticos o de alta severidad.
- Cobertura de requisitos alcanzada.

No está de más decir que el reporte de esta etapa puede ser completamente automatizado, en herramientas como Qase (plataforma de gestión de pruebas).
