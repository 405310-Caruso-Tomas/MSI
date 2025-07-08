En cierto modo, el proceso unificado es un intento por obtener los mejores rasgos y características de los modelos tradicionales del [PROCESO](/MSI/R. Pressman/PROCESO) del software, pero en forma que implemente muchos de los mejores principios de [Agilidad](/MSI/R. Pressman/Agilidad) en el software. 
Desarrollado por *Ivar Jacobson*, *Grady Booch* y *James Rumbaugh* en Rational Software.

![Pasted image 20250625202522.png](/MSI/assets/Pasted image 20250625202522.png)

- Es un **proceso iterativo** e **incremental** que utiliza el **Lenguaje Unificado de Modelado ([UML](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/UML))** como herramienta principal para modelar sistemas.
- **Dirigido por casos de uso.** Utiliza los **[Caso de Uso](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Caso de Uso)** como base para capturar y validar **[Requerimientos](/MSI/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos)** (pruebas).
- **Iterativo e incremental.** El desarrollo se divide en iteraciones cortas, cada una produciendo un incremento funcional del sistema.
- **Centrado en la arquitectura.** Se prioriza la creación de una arquitectura robusta desde el inicio.

El Proceso Unificado se **organiza** en **dos dimensiones principales**:

- **Dimensión horizontal**: Representa el tiempo, dividido en **fases** del ciclo de vida.
- **Dimensión vertical**: Representa las **disciplinas** (o **flujos de trabajo**), que son actividades que se realizan a lo largo del proyecto.
****
#### **Fases**
1. Fase de **inicio**: 
	- Identificar los **casos de uso principales** (**requisitos** iniciales).
	- Definir el **alcance** del sistema y sus **objetivos**.
	- Se puede diseñar una arquitectura del sistema de alto nivel.
	- Se desarrolla una descripción del producto final a partir de una idea y se presenta el análisis de negocio para el producto.
2. Fase de **elaboración**: 
	 - Se especifican en detalle la mayoría de los **casos de uso** y se diseña la **arquitectura del sistema** (con diagramas **UML** y demás elementos). 
	 - Refinar el plan del **proyecto** y el **cronograma**.
3. Fase de **construcción**: 
	- Se crea al producto. Implementar y probar los casos de uso en iteraciones.
	- Realizar **[Pruebas Unitarias](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas Unitarias)**, **[Pruebas de Integración](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas de Integración)** y **[Pruebas de Sistema](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas de Sistema)**.
4. Fase de **transición**: 
	- Se prueba el producto y se informan defectos e deficiencias.
	- Corregir defectos y ajustar el sistema según retroalimentación.
	- Pruebas **beta** o **[Pruebas de Aceptación](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas de Aceptación)**.
	- Desplegar el sistema en el entorno de producción.
****
#### **Flujos de Trabajo**
$$\text{FT}=\text{actividades}\space+\space \text{trabajadores} \space+\space \text{artefactos}$$

Cada **flujo de trabajo** está compuesto por: **Actividades**, que son las tareas que se llevan a cabo en el **flujo de trabajo**; **Trabajadores** que son quiénes ejecutan las actividades y **[Artefacto](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Artefacto)s** que es toda la información generada a partir del trabajo realizado en el **FT**.
Estas actividades se realizan a lo largo de las fases, pero con diferente intensidad en cada una.
###### **Requisitos**
- Capturar y documentar los requisitos funcionales (a través de casos de uso) y no funcionales (rendimiento, seguridad, etc.).
###### **Análisis y Diseño**
- Diseñar la **arquitectura** y los **[Componente](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Componente)s** del sistema, transformando requisitos en modelos técnicos.
###### **Implementación**
- Escribir el código fuente y construir el sistema basado en los modelos de diseño.
###### **Pruebas**
- Verificar que el sistema cumple con los requisitos y está libre de defectos.