El **riesgo** de un proyecto es un evento o condición incierta que, de producirse, tiene un efecto positivo o negativo en uno o más de los objetivos del [Proyecto](../assets/Proyecto.md), tales como el **alcance**, el **cronograma**, el **costo** y la [Calidad](../assets/Calidad.md). (**[Triple Restricción](../assets/Triple Restricción.md)**)
****
Los riesgos del proyecto tienen su origen en la incertidumbre que está presente en todos los proyectos.
##### **Tipos de riesgos según el PMBOK**
- **Riesgos conocidos**: Aquellos que se identifican y analizan durante la planificación, permitiendo desarrollar respuestas específicas.
- A los riesgos conocidos que no se pueden gestionar de manera proactiva se les debe asignar una reserva para contingencias.

- **Riesgos desconocidos**: Eventos imprevistos que no se identificaron previamente, manejados mediante reservas de contingencia o respuestas reactivas.
- Los riesgos **desconocidos** no se pueden gestionar de manera proactiva y por lo tanto se les puede asignar una reserva de gestión. 

- **Riesgos individuales**: Afectan actividades específicas del proyecto.

- **Riesgos generales**: Afectan al proyecto en su conjunto (por ejemplo, cambios en regulaciones o desastres naturales).

Un riesgo negativo del proyecto que se ha materializado se considera un problema, en cambio un riesgo positivo suele ser visto como una oportunidad.
****
###### **¿Cómo una organización o interesados abordan la incertidumbre en un proyecto?**
1. **Apetito al riesgo**: Es el nivel general de riesgo que una organización está dispuesta a aceptar en busca de sus objetivos estratégicos o del proyecto. **Refleja la disposición de la organización a asumir riesgos para lograr beneficios**, equilibrando oportunidades y amenazas.
- Ejemplo: Una empresa de desarrollo de software puede aceptar riesgos relacionados con la adopción de tecnologías nuevas para ganar ventaja competitiva (alto apetito), pero no tolerar riesgos que comprometan la seguridad de datos.

1. **Umbral de riesgo:** Es el nivel específico de riesgo (probabilidad o impacto) que la organización o los interesados han determinado para cuándo un riesgo requiere acción.
- Ejemplo: En un proyecto de construcción, el umbral de riesgo podría establecerse como "no se aceptará un retraso superior al 10% del cronograma planificado". Si un riesgo amenaza con exceder este umbral, se implementa una respuesta.

1. **Tolerancia al riesgo**: Es el grado de variación o desviación que la organización o los interesados están dispuestos a soportar si un riesgo en relación con un objetivo específico del proyecto (costo, cronograma o calidad) ocurre.
- Ejemplo: En un proyecto de desarrollo de software, la tolerancia al riesgo podría ser "aceptar un aumento de costos del 5% del presupuesto original" o "tolerar defectos menores en la interfaz de usuario, pero no en la funcionalidad crítica".
****
##### **Otra definición desde una perspectiva del [Testing](../assets/Testing.md)**
El **riesgo** mide la probabilidad de que algo salga mal y el impacto que tendría ese fallo en el sistema. En base al riesgo, podemos priorizar qué partes del software necesitan más pruebas y cuáles pueden ser probadas con menos intensidad.
El riesgo se basa en dos factores: la probabilidad de que el problema ocurra y su impacto cuando ocurre:
- Un módulo de código **complejo** tiene una mayor probabilidad de contener errores debido a su dificultad intrínseca.
- Un módulo de código **crítico** para el funcionamiento del producto tiene un alto impacto, ya que su fallo podría impedir que el producto cumpla con su propósito.
Ambas áreas (alta probabilidad o alto impacto) deben recibir más atención y pruebas que las áreas de menor riesgo. Esto se alinea con el enfoque de pruebas basadas en riesgos del **PMBOK**, donde los recursos de **testing** se priorizan según la probabilidad e impacto de los riesgos.

