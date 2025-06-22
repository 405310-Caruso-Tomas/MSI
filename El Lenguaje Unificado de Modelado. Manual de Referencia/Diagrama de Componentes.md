Un **diagrama de componentes** muestra los componentes de un sistema, es decir, las unidades software con las que se construye la aplicación, así como las dependencias entre componentes,

Un componente es un tipo de clasificador estructurado, por lo que es recomendable definir su estructura interna en un [[Diagrama de Estructura Interna]], el cual adjuntaremos más abajo.
![[Pasted image 20250622184840.png]]
Un pequeño círculo vinculado a un componente o a una clase es una **interfaz proporcionada** (el componente **implementa** una funcionalidad para otros).
Un pequeño semicírculo vinculado a un componente o a una clase es una **interfaz obligatoria** (el componente **espera** que otro le proporcione esa funcionalidad).
Anidando una interfaz proporcionada con una interfaz obligatoria se indica que un componente llamará a otro para obtener los servicios que necesita

Las líneas discontinuas de dependencia muestran interfaces proporcionadas y obligatorias compatibles entre sí, pero cuando las interfaces tienen los mismos nombres las líneas de dependencia son redundantes.
****
###### **[[Diagrama de Estructura Interna]] de uno de los Componentes**
![[Pasted image 20250622185427.png]]
