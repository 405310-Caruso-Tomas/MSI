##### **Modelos de Proceso Prescriptivos**
Propuestos originalmente para poner orden en el caos del desarrollo de software. Definen un conjunto prescrito de elementos del proceso y un flujo **predecible** para el trabajo del proceso.
- **Modelo en Cascada**:
    - Fases secuenciales (**Requisitos** → **Diseño** → **Implementación** → **Pruebas** → **Mantenimiento**). Toma las [Actividades Fundamentales para la Ingeniería de Software](../assets/Actividades Fundamentales para la Ingeniería de Software.md) y, luego, las representa como fases separadas del proceso.
    - No permite volver atrás fácilmente. No permite flexibilidad en los cambios. Presupone que el producto está perfectamente definido antes de iniciar el desarrollo.
    - Útil cuando los requisitos son bien conocidos desde el inicio.
    - Paradigma más antiguo de la ingeniería del software.
    - Con frecuencia, la naturaleza lineal del ciclo de vida clásico llega a "estados de bloqueo". Por lo que miembros del equipo deben esperar a otros para terminar tareas dependientes.
    - **Útil en situaciones en las que los requerimientos son fijos y el trabajo avanza en forma lineal hacia el final.**
    ![Pasted image 20250315185115.png](../assets/Pasted image 20250315185115.png.md)
- **Modelo V**:
    - Variante del modelo en cascada donde cada fase de desarrollo tiene su fase de prueba correspondiente.
    - Refuerza la validación y verificación en cada etapa. 
    - ![Pasted image 20250526093104.png](../assets/Pasted image 20250526093104.png.md)
    - (Imagen del libro de testing y mencionado en [A note on the 'V-model'](../assets/A note on the 'V-model'.md))
****
##### **Modelos de Proceso Evolutivo**
Es frecuente que los requerimientos del negocio y del producto cambien conforme avanza el desarrollo, lo que hace que no sea realista trazar una trayectoria rectilínea hacia el producto final.
**Los modelos evolutivos son iterativos**. Se caracterizan por la manera en la que permiten desarrollar versiones cada vez más completas del software:

- **Modelo Incremental**:
    - Desarrollo en módulos o **versiones** **sucesivas**.
    - Cada incremento agrega **funcionalidad**.
    - Combina elementos de los flujos de proceso lineal y paralelo
    - Permite recibir retroalimentación temprana.
    - Es común que el primer incremento sea el producto fundamental. El cliente usa el producto y como resultado de su evaluación, se desarrolla un plan para el incremento que sigue, el cual puede incluir modificaciones al producto.
    - El proceso se repite hasta terminar el producto final.
    - ![Pasted image 20250315185538.png](../assets/Pasted image 20250315185538.png.md)
- **Paradigma de Prototipos** / Modelo Prototipado Evolutivo:
	- Es frecuente que un cliente defina un conjunto de objetivos generales para el software, pero que no identifique los requerimientos detallados para las funciones y características. 
	- El diseño rápido lleva a la construcción de un prototipo. Este se entrega y es evaluado por los participantes, que dan **retroalimentación** para **mejorar** los requerimientos. 
	- Es posible hacer prototipos como un modelo de proceso aislado, pero es más común usarlo como una técnica que puede implementarse en el contexto de cualquiera de los modelos de proceso
		-![Pasted image 20250315191624.png](../assets/Pasted image 20250315191624.png.md)
	 -***Aunque algunos prototipos se construyen para ser “desechables”, otros son evolutivos; es decir, poco a poco se transforman en el sistema real. 
	 -Aunque puede haber problemas, hacer prototipos es un paradigma eficaz para la ingeniería de software. La clave es definir desde el principio las reglas del juego; es decir, todos los participantes deben estar de acuerdo en que el prototipo sirva como el mecanismo para definir los requerimientos. 
- **Modelo en Espiral**:
    - Basado en **iteraciones** haciendo énfasis en la **reducción** **del** **riesgo** con cada una.
    - Se acopla el hacer **prototipos** con aspectos controlados del modelo de cascada. Se repiten las actividades predefinidas.
    - Se realizan ciclos de **planificación**, análisis de **[Riesgos](../assets/Riesgos.md)**, desarrollo y **evaluación**.
    - En cada paso evolutivo se marcan **puntos de referencia**: una combinación de productos del trabajo con las condiciones en las que se encuentra dicho incremento. Cada vuelta representa una fase del proyecto con análisis de riesgos integrado.
    - ![Pasted image 20250315192711.png](../assets/Pasted image 20250315192711.png.md)
    - El costo y programación de actividades se ajustan en base a la **retroalimentación** del cliente después de la entrega.
    - El gerente del proyecto puede ajustar el número planeado de iteraciones que se requieren para terminar el software. Incluso el modelo puede adaptarse para ser aplicado a lo largo de toda la vida del software.
    - Es difícil convencer a los clientes de que este enfoque es controlable. Demanda mucha experiencia en la evaluación del riesgo y se basa en ella para llegar al éxito.
    - A diferencia del modelo incremental (que tiene como objetivo la entrega rápida de incrementos), el modelo en espiral se enfoca en la identificación y minimización previa de **[Riesgos](../assets/Riesgos.md)** en cada ciclo. En el modelo incremental, por otro lado, la gestión del **riesgo** se hace de forma reactiva, y no suele ser tan costoso como el espiral, el cual requiere un prototipado constante.

| Característica     | Modelo Incremental 🚀                                   | Modelo de Prototipos 🎭                               |
| ------------------ | ------------------------------------------------------- | ----------------------------------------------------- |
| **Objetivo**       | Construcción por partes funcionales del producto final. | Crear un modelo funcional para validar requisitos.    |
| **Foco principal** | Agregar funcionalidades gradualmente.                   | Probar ideas y conceptos antes del desarrollo final.  |
| **Producto final** | Se obtiene tras varias versiones incrementales.         | Puede ser descartado o refinado en una nueva versión. |
| **Utilidad**       | Ideal cuando se conocen bien los requisitos.            | Útil cuando los requisitos no están bien definidos.   |
##### **Modelos Ágiles**
Priorizan la flexibilidad, la colaboración y entregas frecuentes, adaptándose a cambios constantes mediante iteraciones cortas.
[Modelos Ágiles](../assets/Modelos Ágiles.md)
****
##### **Métodos Tradicionales Vs. Ágiles**
Los modelos prescriptivos y evolutivos podrían ser agrupados en lo que se llamarían **[Metodología](../assets/Metodología.md)s** **Tradicionales**, mientras que los **[Modelos Ágiles](../assets/Modelos Ágiles.md)** se autoreferencian por sí solos. Se enuncian algunas diferencias:
![Pasted image 20250702194739.png](../assets/Pasted image 20250702194739.png.md)
********************************************
##### ***Al Borde del Caos***
La historia indica que estos modelos tradicionales han dado cierta estructura útil al trabajo de ingeniería de software. Sin embargo, el trabajo de ingeniería de software y el producto que genera siguen *“al borde del caos”*.

> [!Nogueira y sus colegas!]
> **Borde del Caos** “el estado natural, inestable y parcialmente estructurado entre el orden y el caos.” Es inestable debido a que se ve atraído constantemente hacia el caos o hacia el orden absoluto.

Si los modelos de proceso prescriptivo buscan generar estructura y orden, **¿Son inapropiados para el mundo del software, que se basa en el cambio?**. Pero si rechazamos los modelos de proceso tradicional (y el orden que implican) y los reemplazamos con algo menos estructurado, **¿Hacemos imposible la coordinación y coherencia en el trabajo de software?.**
Es difícil responder, pero existen alternativas disponibles...
 [Modelo Concurrente](../assets/Modelo Concurrente.md), podría ser un ejemplo simple.
