###### Procesos en ingeniería de software: Perspectiva general
En la ingeniería de software, los flujos de proceso se definen como la serie coordinada de actividades, acciones y tareas para desarrollar un sistema de software.
Los flujos de proceso se representan a través de [[Modelos de PROCESO]], cada uno con características específicas. Este inciso aprovecha hacer referencia a otros enfoques y plasmar las diferencias de estos enfoques.
****
#### Importancia y flexibilidad
En términos de lo que sería ideal para el desarrollo, se suele enfatizar por distintas fuentes que los flujos de proceso deben ser **flexibles** y **adaptables**, especialmente en entornos donde los requisitos cambian. Y usando estrategias como el prototipado para anticipar necesidades o desarrollo incremental para reducir costos de modificación. La mejora continua, como el modelo CMMI, ayuda a optimizar procesos. 
****
#### Estrategias para manejar el cambio
Los flujos de proceso deben ser capaces de adaptarse a cambios, ya que los requisitos del software a menudo evolucionan. Sommerville sugiere dos estrategias:
- **Evitar el cambio**: Usar técnicas como el prototipado para anticipar y validar requisitos antes de que se produzcan cambios costosos.
- **Tolerar el cambio**: Diseñar procesos para cambios de bajo costo, como el desarrollo incremental, que permite ajustes en cada iteración.

![[Pasted image 20250319202808.png]]
****
###### **Controversias**
Son muchas las controversias que surgen de la utilización de un enfoque u otro, esto se refleja en discusiones en foros académicos y profesionales. De esto ha surgido el concepto de **"code hacked"**, que no es un término técnico oficial, pero se puede interpretar como una referencia a una práctica o situación en la que el código se desarrolla de manera rápida, desordenada o sin seguir las mejores prácticas, a menudo como resultado de una mala aplicación de los principios ágiles. 

Karl Wiegers, un ingeniero de software con un enfoque tradicional pero pragmático, en su artículo _License to Hack_ (AgileConnection, 2001), describe cómo algunos desarrolladores, al adoptar metodologías ágiles como XP (que ganaron popularidad tras la publicación del _Manifesto for Agile Software Development_) fueron interpretadas erróneamente: se confunde la falta de documentación extensa como una invitación a abandonar buenas prácticas de ingeniería de software, sin planificación ni diseño.
****
#### Enfoques adicionales
Si bien estos no son modelos de proceso, son **paradigmas de desarrollo** que pueden integrarse en diferentes modelos de proceso:
- **Ingeniería de componentes**: Pressman describe este enfoque como un flujo de proceso centrado en integrar componentes loosely-coupled (débilmente acoplados, que tienen mínimas dependencias entre si) y reutilizables, reduciendo tiempo y mejorando calidad.
- **Métodos formales**: Sommerville menciona que los métodos formales usan notación matemática para especificar y verificar software, comunes en sistemas críticos. Son técnicas matemáticamente rigurosas utilizadas para especificar, desarrollar y verificar sistemas de software y hardware. Su objetivo es garantizar la corrección y confiabilidad. Incluyen lenguajes como Z, VDM o TLA+, y herramientas como SPIN o Coq, que facilitan la verificación formal. Requieren un alto nivel de expertise en matemáticas y lógica, lo que puede ser una barrera de entrada.
- **Programación orientada a aspectos**: Ambos autores coinciden en que es un paradigma que ayuda a manejar preocupaciones transversales, como seguridad o logging, y separarlas del código principal para que no se entrelazen con la lógica de negocio. 