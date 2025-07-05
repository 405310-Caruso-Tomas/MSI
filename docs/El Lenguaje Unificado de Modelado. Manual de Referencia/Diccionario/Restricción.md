> **Condición** **semántica** representada como texto en lenguaje natural o en un lenguaje formal especificado.

Se puede adjuntar a **cualquier** **elemento** del modelo o **lista de elementos** del modelo, por lo que pueden aplicarse en casi **cualquier** diagrama UML.
Una restricción es una **aserción**, **no** un mecanismo ejecutable. 

- Se utilizan para especificar requisitos adicionales, e indica una restricción que debe ser impuesta por el correcto diseño del sistema.
****
#### **Notación**
**Símbolo**: Las restricciones se representan encerradas entre llaves {} y suelen colocarse cerca del elemento al que afectan. La descripción dentro de las llaves puede ser:

- **Texto informal**: Una frase en lenguaje natural (por ejemplo, `{edad debe ser mayor a 18}`).
- **Expresión formal**: Usando un lenguaje como *OCL* (*Object Constraint Language*, es un lenguaje formal de **UML**) o pseudocódigo (por ejemplo, `{self.edad > 18}`).
###### **Tipos de restricciones**
1. **Restricciones de atributos**:
    
	- Limitan los valores de un atributo.
    - Ejemplo: `{edad >= 18}` en un atributo edad de una **clase** **`Usuario`**.
2. **Restricciones de asociaciones**:
    
	- Definen reglas sobre las relaciones entre clases.
    - Ejemplo: En una asociación entre `Estudiante` y `Curso`, `{un estudiante puede inscribirse en un máximo de 5 cursos}`.
3. **Restricciones de operaciones**:
    
	- Especifican condiciones para ejecutar una operación.
    - Ejemplo: `{pre: usuario autenticado}` para una operación `realizarPago()`.
4. **Restricciones de estados o transiciones** (en diagramas de estados):
    
	- Definen condiciones para cambiar de un estado a otro.
    - Ejemplo: `{transición solo si pago confirmado}` en una **[Máquina de Estados](/El Lenguaje Unificado de Modelado. Manual de Referencia/Máquina de Estados)**.
5. **Restricciones globales**:
    
	- Aplican a todo un modelo o diagrama.
    - Ejemplo: `{todas las transacciones deben completarse en menos de 5 segundos}`.

![Pasted image 20250624231215.png](/assets/Pasted image 20250624231215.png)