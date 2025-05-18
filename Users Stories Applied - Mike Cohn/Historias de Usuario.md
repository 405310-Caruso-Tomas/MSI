> *Extensive upfront requirements gathering and documentation can kill a project in many ways. One of the most common is when the requirements document itself becomes a goal. A requirements document should be written only when it helps achieve the real goal of delivering some software.*
****

Los requerimientos del software son un problema de comunicación: aquellos que quieren el software deben comunicarse con aquellos que lo desarrollan. 
Una ***Historia de Usuario*** describe funcionalidad valiosa para un usuario o comprador del sistema. Representa específicamente [[Requerimientos]] del usuario, más que la documentación de los mismos. Son **descripciones** breves y simples de una funcionalidad que un usuario desea. Son utilizadas principalmente en [[Modelos Ágiles]].
Deben ser escritas ***sin*** el uso de lenguaje técnico.
****
Para ejemplificar, usaremos el ejemplo de ***BigMoneyJobs.com*** (*sitio web de búsqueda de empleo que operaba como una plataforma para conectar a profesionales con oportunidades laborales*). Historias de usuario de este software serían:
	- El usuario puede buscar trabajos.
	- Una compañía puede publicar ofertas de trabajo.
	- Un usuario puede limitar las visualizaciones a su perfil.
Las siguientes ****NO**** serían ejemplos de historias de usuario:
	- El software será escrito en **C++**.
	- El programa se conectará a la base de datos mediante (herramienta o patrón cualquiera).
Los malos ejemplos para una historia de usuario se deben a que en principio al usuario no le importan los detalles técnicos sobre la implementación o diseño del sistema. **Las historias son escritas de forma que sean valiosas para un cliente**.
****
****Detalles.**** Si bien en los ejemplos nos referimos a las primeras tres proposiciones como historias de usuario, vemos que son muy abarcativas y no son la mejor guía para comenzar a desarrollar y testear. 
****
###### **Épicas**
Cuando una historia es muy larga, o de este estilo, suelen ser denominadas ***Épicas***. Las épicas pueden ser divididas en dos o más historias de usuario más chicas y específicas. "Un usuario puede buscar trabajo según localización, salario, puesto, compañía." es una historia que surge de la primera épica ejemplo, "El usuario puede ver información acerca de cada trabajo según la búsqueda." es otra. 
La mejor forma de encarar el escribir una historia de usuario es que el equipo de desarrollo y el cliente se pongan de acuerdo acerca de estos detalles, y de hasta qué punto vale la pena mencionarlos en las historias. 
****
###### ****Notas***. 
Las **notas en las historias de usuario** son información adicional que proporciona contexto o detalles específicos para ayudar a los desarrolladores y otros miembros del equipo a entender mejor los requisitos. Aunque no son siempre necesarias, pueden ser muy útiles para aclarar aspectos técnicos, restricciones o reglas de negocio.
****
###### **Criterios de Aceptación.**
Es importante saber las expectativas de los clientes. Estas expectativas son mejor capturadas en forma de ***Criterios de Aceptación.*** En el desarrollo de software, cumplir con las expectativas quiere decir que el sistema cumpla con lo que se espera de este por parte del cliente. **De esta forma, los criterios de aceptación funcionan como el aviso para el desarrollador sobre cuándo han completado de producir la funcionalidad esperada.** 
**Características principales:**
	- ***Formato flexible***: No hay un formato estricto, pero suelen escribirse en forma de lista de condiciones o escenarios. Más formatos son detallados en [[Testing en Ambientes Ágiles]]
	- ***Definen el "qué" y no el "cómo":*** Centrados en el resultado esperado y no en la implementación técnica.
	- ***Verificables:*** Deben ser claros, objetivos y medibles.
	- ***Escritos desde la perspectiva del usuario:*** Reflejan el comportamiento esperado del sistema desde lo que ve el usuario.
Además, estos criterios no son estáticos, estos suelen refinarse con el tiempo durante el desarrollo, o incluso pueden ser descubiertos nuevos criterios durante discusiones (por ejemplo, una historia sobre "iniciar sesión" podría no mencionar inicialmente la autenticación multifactor, pero esto podría surgir en la conversación.).
****
###### **Equipo Cliente***. 
En un proyecto ideal, se tendría a un cliente único que prioriza el trabajo para los desarrolladores, responde sus preguntas, usa y comprueba el software finalizado, y escribe todas las historias de usuario. Este escenario es demasiado exigente, y por ello es que se suele establecer un equipo cliente, un equipo que se asegurará que el sistema cumpla con las necesidades del usuario final, y que escribirá las historias de usuario.
Este equipo puede incluir ***testers***, un ***product owner***, **usuarios finales**, o representaciones de estos. 
Con estos integrantes, es claro que el equipo cliente están mejor parados para describir el comportamiento del producto a través de historias.
Otros de los propósitos de este equipo son:
	. Proporcionar claridad sobre los requisitos.
	. Tomar decisiones sobre qué funcionalidades se desarrollan y en qué orden.
	. Definir y priorizar las historias de usuario.
****
##### ****El Proceso con Historias de Usuario****
Un proyecto que hace uso de **H.U** no se parecerá en nada a un modelo de proceso estilo cascada, en el que la participación del usuario se verá limitada a la etapa de recabación de requerimientos y retroalimentación del producto terminado. 
Un proyecto que hace uso de **H.U** ([[Modelos Ágiles]]) necesita la participación frecuente del equipo cliente, ya que las **H.U** pueden ser escritas en cualquier etapa del proyecto, y ***la parte más importante de una historia de usuario es la conversación previa a escribirla***. 
El formato de las **H.U** permite una flexibilidad y adaptación clave para este tipo de metodologías. Más razones para el uso de historias de usuario son detalladas en el apartado de [[Por qué usar Historias de Usuario]]