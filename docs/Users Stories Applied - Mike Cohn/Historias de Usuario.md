> *Extensive upfront requirements gathering and documentation can kill a project in many ways. One of the most common is when the requirements document itself becomes a goal. A requirements document should be written only when it helps achieve the real goal of delivering some software.*
****

Los **requerimientos** del software son un problema de comunicación: aquellos que quieren el software deben comunicarse con aquellos que lo desarrollan.

- Una ***Historia de Usuario*** describe funcionalidad valiosa para un usuario o comprador del **[Sistema](../assets/Sistema.md)**. Representa específicamente [Requerimientos](../assets/Requerimientos.md) del usuario, **más** que la **documentación** de los mismos. 
- Son **descripciones** breves y simples de una **funcionalidad** que un usuario desea. 
- Son utilizadas principalmente en [Modelos Ágiles](../assets/Modelos Ágiles.md).
- Deben ser escritas ***sin*** el uso de lenguaje técnico.
****
#### **Ejemplo**
Para ejemplificar, usaremos el ejemplo de ***BigMoneyJobs.com*** (*sitio web de búsqueda de empleo que operaba como una plataforma para conectar a profesionales con oportunidades laborales*). Historias de usuario de este software serían:
	- El usuario puede buscar trabajos.
	- Una compañía puede publicar ofertas de trabajo.
	- Un usuario puede limitar las visualizaciones a su perfil.
Las siguientes ****NO**** serían ejemplos de historias de usuario:
	- El software será escrito en **C++**.
	- El programa se conectará a la base de datos mediante (herramienta o patrón cualquiera).
Los malos ejemplos para una historia de usuario se deben a que en principio al usuario no le importan los detalles técnicos sobre la implementación o diseño del sistema. **Las historias son escritas de forma que sean valiosas para un cliente**.

**Detalles.*** Si bien en los ejemplos nos referimos a las primeras tres proposiciones como historias de usuario, vemos que son muy abarcativas y no son la mejor guía para comenzar a desarrollar y testear, por lo que se propone una estructura mejor definida.
****
#### ***Notas*** 
Las **notas en las historias de usuario** son información adicional que proporciona contexto o detalles específicos para ayudar a los desarrolladores y otros miembros del equipo a entender mejor los requisitos. Aunque no son siempre necesarias, pueden ser muy útiles para aclarar aspectos técnicos, restricciones o reglas de negocio.
****
###### **[Criterios de Aceptación](../assets/Criterios de Aceptación.md)**
****
##### ****El Proceso con Historias de Usuario****
Un proyecto que hace uso de **H.U** no se parecerá en nada a un modelo de proceso estilo cascada, en el que la participación del usuario se verá limitada a la etapa de recabación de requerimientos y retroalimentación del producto terminado. 
Un proyecto que hace uso de **H.U** ([Modelos Ágiles](../assets/Modelos Ágiles.md)) necesita la participación frecuente del equipo cliente, ya que las **H.U** pueden ser escritas en cualquier etapa del proyecto, y ***la parte más importante de una historia de usuario es la conversación previa a escribirla***. 
El formato de las **H.U** permite una flexibilidad y adaptación clave para este tipo de metodologías. Más razones para el uso de historias de usuario son detalladas en el apartado de [Por qué usar Historias de Usuario](../assets/Por qué usar Historias de Usuario.md)
