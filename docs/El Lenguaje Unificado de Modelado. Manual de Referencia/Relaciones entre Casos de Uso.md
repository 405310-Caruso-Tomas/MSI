Este tipo de **[Relaciones](../assets/Relaciones.md)** en particular, se utilizan para **factorizar** el comportamiento común entre los **[Caso de Uso](../assets/Caso de Uso.md)** y para factorizar variantes (poniendo ese comportamiento en otros casos de uso que lo extienden).
![Pasted image 20250626105214.png](../assets/Pasted image 20250626105214.png.md)
****
#### **Generalización**
La **generalización** entre **casos de uso** es **como la generalización entre clases.** -
- El caso de uso hijo **hereda** el **comportamiento** del caso de uso **padre**. El hijo puede modificar y/o agregar **comportamiento** al heredado.
- Es utilizada más que nada para simplificar la comprensión del **[Diagrama de Casos de Uso](../assets/Diagrama de Casos de Uso.md)**.
Gráficamente se indica, al igual que la herencia entre clases, con una línea continua con punta de flecha vacía dirigida del caso de uso hijo hacia el padre.
![Pasted image 20250626105648.png](../assets/Pasted image 20250626105648.png.md)
****
#### **Inclusión**
Significa que un caso de uso base **incorpora** **explícitamente** el **comportamiento** de **otro** caso de uso.
- El caso de uso incluido **nunca** es instanciado por un **[Actor](../assets/Actor.md)**, sino que **es instanciado por el/los casos de uso que lo incluyen**. Por ello, **un caso de uso de inclusión es siempre un caso de uso abstracto.**
- La relación se usa para abstraer el comportamiento común entre casos de uso, evitando describir el mismo flujo de eventos repetidas veces. 
- La secuencia de comportamiento y los atributos del caso de uso incluido se encapsulan y no pueden modificarse o accederse, solamente puede utilizarse el resultado (o función) del caso de uso incluido.
- Se representa como una **dependencia** **estereotipada** ([Estereotipo](../assets/Estereotipo.md)) con la palabra `<<include>>`. 
![Pasted image 20250626110558.png](../assets/Pasted image 20250626110558.png.md)
****
#### **Extensión**
Significa que un caso de uso base **incorpora** **implícitamente** el **comportamiento** de **otro** caso de uso. 
- El caso de uso base **puede** **ejecutarse** **aisladamente**, pero bajo ciertas **condiciones** su funcionalidad será extendida por la del caso de uso de **extensión**. De esta forma se separa el comportamiento opcional del obligatorio.
- El caso de uso de extensión puede en algunos casos ser instanciado directamente por un **actor** (en este caso se considera un caso de uso **concreto**).
- Si el caso de uso de extensión nunca es instanciado directamente por un **actor**, entonces es un caso de uso **abstracto**.
- Se representa como una dependencia **estereotipada** ([Estereotipo](../assets/Estereotipo.md)) con la palabra *extend*, dirigida desde el caso de uso de **extensión** hacia el caso de uso **base**.
![Pasted image 20250626111626.png](../assets/Pasted image 20250626111626.png.md)

