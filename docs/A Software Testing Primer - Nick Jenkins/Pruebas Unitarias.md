Se verifica el funcionamiento de partes pequeñas y aisladas de una aplicación (**funciones o métodos individuales dentro de una clase u objeto en un lenguaje de programación**)

**Propósito.** El propósito principal de las pruebas unitarias es asegurarse de que cada unidad de código funcione correctamente de manera independiente, sin depender de otras partes del sistema, para luego ser integrada con otros componentes del software.
****
##### **Arneses de Prueba***
Las unidades se prueban generalmente mediante el uso de "arneses de prueba" que simulan el contexto en el que se integrará la unidad. 
El arnés de prueba proporciona una serie de entradas conocidas y mide las salidas de la unidad bajo prueba, que luego se comparan con los valores esperados para determinar si existen problemas. 
Es decir, se crea un conjunto de [Casos de Prueba](/A Software Testing Primer - Nick Jenkins/Casos de Prueba) específicos que cubren escenarios para la unidad de código bajo prueba.
****
###### **¿Qué mejor que un ejemplo real en código de lo que es una prueba unitaria?**
Supongamos tenemos la siguiente función que calcula el cuadrado de un número.
```python
def square(num):
    return num * num
    ```
Una prueba unitaria para esta función usando ```pytest```(framework para testing) podría ser:
```python
import pytest
def test_square():
    assert square(3) == 9  # Prueba con un número positivo
    assert square(-2) == 4  # Prueba con un número negativo
    assert square(0) == 0  # Prueba con cero
```
****
###### ¿Quién realiza las pruebas unitarias?
Normalmente realizadas por los desarrolladores del software, quienes escriben estas pruebas en paralelo al desarrollo del código.
****
###### **Tipos de Pruebas Unitarias**
Las pruebas unitarias pueden ser utilizadas para verificar diferentes características del código, y suelen responder a las preguntas:

- ***Pruebas positivas.*** ¿Cada unidad de código se comporta cómo es esperado en condiciones normales o válidas?.
- ***Pruebas negativas.*** ¿El código maneja adecuadamente entradas no válidas?.
- ***Pruebas de Frontera.*** ¿El código se comporta adecuadamente dentro y fuera de los límites de sus valores permitidos?.
- ***Pruebas de excepción.*** ¿Cómo se comporta el código frente a un error?, ¿Es informada la excepción?.
