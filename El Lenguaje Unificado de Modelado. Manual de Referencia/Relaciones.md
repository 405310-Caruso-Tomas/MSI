Las **relaciones** entre **[[Clasificador]]es** son **asociación**, **generalización** y varios tipos de **dependencia**, entre los que se incluyen la **realización** y el **uso**.
Describen cómo se conectan y colaboran los diferentes **[[Componente]]s** de un sistema, como **[[Clases]]**, **objetos**, **[[Caso de Uso]]**, entre otros.
También suelen mostrar información adicional como **multiplicidad** (número de instancias de una clase que pueden estar relacionadas con la clase asociada) y **nombres de roles** (identificación del extremo de una asociación).
![[Pasted image 20250625150939.png]]
****
#### **Asociación**
La relación de asociación describe conexiones semánticas entre objetos individuales (instancias) de clases dadas. Indicando que los **objetos** de **una clase** pueden estar relacionados con **los objetos de otra.**
Las relaciones restantes relacionan las descripciones de los propios **clasificadores**, no de sus instancias.
No implica una dependencia fuerte, sino que **simplemente existe una conexión entre las clases.** Ambas pueden existir por separado.
- **Notación**: Una línea sólida entre dos clases, a menudo con un nombre que describe la relación. Puede incluir **multiplicidad** (e.g., 1, `0..`, `1..`).
- `Estudiante ---- Curso`
- **Ejemplo**: Una clase `Estudiante` está asociada con una clase `Curso`. Un estudiante puede estar inscrito en varios cursos (multiplicidad `0..*`).
****
#### **Agregación**
Es un **tipo especial** de **asociación** que representa una relación "todo-parte" donde **las partes pueden existir independientemente del todo**. Es una relación más débil que la composición. 
Quiere decir que si el objeto "*todo*" se destruye, el objeto "*parte*" sigue existiendo.
- **Notación**: Una línea con un diamante hueco en el lado del "*todo*". `Universidad ◇---- Departamento`
- **Ejemplo**: Una clase `Universidad` tiene una agregación con la clase `Departamento`. Los departamentos forman parte de la universidad, pero un departamento puede existir sin una universidad específica.
****
#### **Composición**
Es una forma más fuerte de **agregación**, donde **las partes no pueden existir sin el todo**. Si el todo se destruye, las partes también. 
El compuesto es el responsable único de gestionar sus partes.
- **Notación**: Una línea con un diamante lleno en el lado del "todo".
- **Ejemplo**: Una clase `Casa` tiene una composición con la clase `Habitación`. Si la casa se destruye, las habitaciones también dejan de existir.
- `Casa ◆---- Habitación`
****
#### **Dependencia**
Indica que una **clase** **depende** de otra para realizar alguna función, pero **la relación es más débil y no implica una conexión estructural** permanente.
Un cambio en la clase de la que depende puede afectar a la otra clase.
- Según esta definición, las relaciones de **asociación**, de **generalización** y **realización** son dependencias, pero éstas tienen semánticas específicas con consecuencias importantes. Por lo tanto, ellas tienen sus propios nombres y su semántica detallada.
- **Notación**: Una línea discontinua con una flecha apuntando a la clase de la que se depende.
- **Ejemplo**: Una clase Informe depende de una clase Impresora para imprimir un documento.
- `Informe ----> Impresora`
****
#### **Generalización (Herencia)**
La descripción más específica es completamente consistente con la más general. Representa una relación "*es-un*" entre una **clase padre (superclase)** y una **clase hija (subclase)**. La subclase hereda atributos y métodos de la superclase.
- **Notación**: Una línea con una flecha triangular hueca apuntando a la superclase.
- **Ejemplo**: Una clase `Vehículo` es la superclase de `Coche` y `Bicicleta`. Ambos heredan propiedades de **vehículo**.
- `Coche ----|> Vehículo`
- La generalización permite **operaciones polimórficas**, es decir, cuya **implementación (método)** se determina por la clase de objeto a la que se aplican, en lugar de ser explícitamente indicadas en la subclase.
- Además permite lo que se denomina **herencia**, que permite que las partes compartidas de la descripción se declaren una vez y sean compartidas por muchas clases, en lugar de repetirlas en cada clase que las utiliza.
- Se puede dar el caso de **herencia múltiple**, donde una clase hereda los atributos y operaciones de sus dos padres.
****
#### **Realización**
Es una relación entre una **interfaz** y una **clase** concreta que la implementa.
La **clase** se compromete a implementar **todos los métodos definidos en la interfaz**, pero no la estructura.
El cliente debe tener (por **herencia** o por **declaración directa**) al menos todas las operaciones que tiene el proveedor.
- **Notación**: Similar a la herencia, pero **con una línea discontinua** y una flecha triangular hueca.
- **Ejemplo**: Una clase `Coche` implementa una interfaz `VehículoConducible`.
- `Coche ----|> VehículoConducible`
- Notar que para **interfaz**, así como para otros elementos UML, hay más de una notación común, pero que son más convenientes unas u otras notaciones dependiendo el diagrama o vista UML. Se adjunta otro ejemplo, este tipo de notación es más común en un **[[Diagrama de Componentes]]** (apartado donde además se aprovecha para explicar la **interfaz obligatoria** y **proporcionada**)
	- ![[Pasted image 20250625150253.png]]

