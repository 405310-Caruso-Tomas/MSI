Las pruebas de sistema consisten en evaluar el software como un todo, una vez que sus componentes individuales (unidades) y sus interacciones (integración) han sido probados.

Este tipo de prueba se realiza en un entorno que simula lo más fielmente posible el entorno de producción, y garantizar su funcionamiento en dicho ambiente según lo esperado es el propósito de dichas pruebas.

En este tipo de pruebas se busca validar la funcionalidad completa y garantizar la [Calidad](/R. Pressman/Calidad) del producto, además de identificar errores que no fueron detectados en los otros tipos de pruebas.

Estas pruebas tienen en cuenta el sistema en conjunto, incluyendo **funcionalidades** como aspectos **no funcionales.** Se incluye el rendimiento del sistema bajo cargas de trabajo intensas y capacidad de recuperación ante fallos (hasta de hardware). Es a menudo la etapa más formal de las pruebas y más estructurada.
****
###### **¿Cómo suelen ser?**
Las pruebas de sistema son **típicamente pruebas de caja negra**, lo que significa que los evaluadores no necesitan conocer el código interno, solo el comportamiento esperado según los requisitos. Sin embargo, en algunos casos, se combinan con enfoques de caja blanca para pruebas más técnicas, como las de rendimiento o seguridad. 

Uno de los aspectos más importantes es que suelen detectar problemas en entornos reales, errores que lógicamente no pueden saltar en etapas anteriores.
****
###### **¿Quién las realiza?**
Suelen ser realizadas por el equipo de [QA (Quality Assurance o Aseguramiento de la Calidad)](/A Software Testing Primer - Nick Jenkins/QA (Quality Assurance o Aseguramiento de la Calidad)) o un equipo especializado en pruebas de software. Este equipo también evalúa la experiencia del usuario final. En algunos casos, también pueden participar probadores externos o usuarios reales en entornos de prueba beta.
****
###### **Tipos de Pruebas de Sistema**
- ***Pruebas Funcionales***. Se prueban las entradas y salidas, asegurándose de que los resultados sean los esperados, según las especificaciones del cliente. Poco más detalladas en [Enfoques de Testing](/A Software Testing Primer - Nick Jenkins/Enfoques de Testing).
	- **Ejemplo.** Probar una aplicación de comercio electrónico para verificar que los usuarios puedan agregar productos al carrito, procesar pagos y recibir confirmaciones de compra correctamente.
- ***Pruebas No Funcionales.*** Se fijan en aspectos no relacionados a funcionalidad del sistema, sino más bien a rendimiento esperado, seguridad, usabilidad y fiabilidad.
	- **Ejemplo.** Medir el tiempo de respuesta del sistema bajo cierta demanda de usuarios (asegurarse que cumple con los tiempos de respuesta esperados).
- ***Pruebas de Carga.*** Se evalúa el rendimiento del sistema bajo diferentes niveles de carga.
	- **Ejemplo.** Probar una aplicación de banca en línea para ver cómo se comporta cuando 10,000 usuarios realizan transferencias simultáneamente.
- ***Pruebas de Estrés.*** Buscan determinar los límites del sistema sometiéndolo a condiciones extremas, como un volumen de usuarios superior al esperado o recursos del sistema limitados.
- ***Pruebas de Seguridad.*** ¿El sistema resiste ataques de seguridad?. ¿Hay brechas en el manejo de datos sensibles?.
	- **Ejemplo.** Se evalúa la exposición del sistema a ataques de inyección SQL. Ejemplo en código más adelante de cómo podría darse este tipo de ataques.
- ***Pruebas de Backup.*** Se evalúa la capacidad del sistema para realizar copias de seguridad de datos de manera efectiva y restaurarlos de manera efectiva.
	- **Ejemplo.** Probar que un sistema de gestión de datos pueda realizar copias de seguridad automáticas, y que los datos puedan restaurarse luego de una interrupción.
- ***Pruebas de Humo.*** Pruebas rápidas para verificar si las funcionalidades principales del sistema funcionan correctamente después de una nueva construcción o actualización. O simplemente para verificar que un elemento particular del sistema está presente y en funcionamiento.
	- **Ejemplo.** Ejemplo en código más adelante.
- ***Pruebas de Usabilidad.*** Evalúan lo fácil y amigable que es el sistema para los usuarios finales. Navegabilidad, diseño y facilidad para realizar tareas. Más adelante más información sobre este tipo de pruebas.
- ***Pruebas de Compatibilidad.*** ¿El sistema funciona correctamente en otras plataformas?. 
- ***Pruebas de Recuperación.*** Evalúan la capacidad del sistema para recuperarse de fallos, como caídas del sistema o pérdida de conexión.
- ***Pruebas de Extremo a Extremo (Endo-to-End).*** Validan el flujo completo de la aplicación, que todos los módulos del sistema trabajen en conjunto correctamente.
	- **Ejemplo.** Probar un proceso completo de compra en línea, verificando que el cliente pueda navegar por el sitio, agregar productos al carrito, realizar el pago y recibir la confirmación de compra sin problemas a lo largo de todo el flujo.
****
###### ***Ejemplo Smoke Testing***
Supongamos tenemos una API REST para gestión de usuarios. La siguiente es una prueba básica para verificar que la aplicación arranca y que el endpoint principal responde como debería.
**Controlador**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping
    public ResponseEntity<String> getAllUsers() {
        return ResponseEntity.ok("Lista de usuarios");
    }
}
```
**Smoke Test con JUnit 5 y Spring Boot:**
```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
public class SmokeTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void testUserEndpoint() throws Exception {
        mockMvc.perform(get("/api/users"))
               .andExpect(status().isOk())
               .andExpect(content().string(containsString("Lista de usuarios")));
    }

    @Test
    public void contextLoads() {
        // Verifica que el contexto de Spring Boot se cargue correctamente
    }
}```
****
###### **Ejemplo de Ataque de Inyección SQL***
**¿Cómo podría ocurrir un ataque de inyección SQL?**. El siguiente es un escenario de una aplicación vulnerable (**PHP + MySQL**).
```php
<?php
$username = $_GET['username'];
$password = $_GET['password'];

$sql = "SELECT * FROM usuarios WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    echo "Acceso concedido";
} else {
    echo "Acceso denegado";
}
?>
```
La inyección SQL posible puede darse de forma que un atacante coloque como usuario `' OR '1'='1 `. Así, la consulta SQL quedaría así:
```sql
SELECT * FROM usuarios WHERE username = '' OR '1'='1' AND password = ''
```
 ****
##### ****Algo más sobre las Pruebas de Usabilidad****
En este tipo de pruebas, el probador debe observar las reacciones de los usuarios a un producto de software. Se elige en particular a un usuario final para que pruebe el producto, aunque este no tenga un conocimiento técnico para tomar decisiones (solo serán emisores de opinión).
**Guía práctica para hacer una prueba de usabilidad.*

- Se presenta un modelo básico o prototipo del producto a usuarios finales típicos.
- Se establece una serie de tareas estándar que deben completar con el producto.
- Se registra cualquier dificultad que se encuentre durante la prueba.
- Se realizan los correspondientes cambios de diseño.
- Se repite el proceso con el nuevo diseño.

No se necesitan más de cuatro o cinco usuarios finales para evaluar en una sesión.

