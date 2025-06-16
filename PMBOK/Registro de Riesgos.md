Documento clave en la Gestión de los [[Riesgos]] del Proyecto que sirve como repositorio central para identificar, documentar, analizar, planificar respuestas y monitorear todos los riesgos asociados con un proyecto.
Se utiliza a lo largo de todo el ciclo de vida del proyecto y se crea durante el proceso **Identificar los riesgos**, siendo actualizado y refinado en los procesos posteriores de la gestión de riesgos.
****
El registro de riesgos es un documento dinámico que recopila toda la información relevante sobre los riesgos del proyecto, desde su identificación hasta su cierre o materialización.
El registro de riesgos suele presentarse como una tabla o matriz, aunque puede adaptarse según las necesidades del proyecto.
###### **Registro de Riesgos - Proyecto de Desarrollo de Aplicación Bancaria Móvil**

| ID  | Descripción del Riesgo                                                          | Categoría  | Probabilidad | Impacto                        | Prioridad | Estrategia de Respuesta                                     | Responsable         | Estado | Acciones                                                      |
| --- | ------------------------------------------------------------------------------- | ---------- | ------------ | ------------------------------ | --------- | ----------------------------------------------------------- | ------------------- | ------ | ------------------------------------------------------------- |
| R1  | Defectos no detectados en el módulo de pagos debido a baja cobertura de pruebas | Técnico    | Alta (70%)   | Muy Alto (fallo en producción) | Muy Alta  | Mitigar: Aumentar pruebas automatizadas y de estrés         | Equipo de Testing   | Activo | Diseño de casos de prueba completado; automatización en curso |
| R2  | Retraso en pruebas por falta de dispositivos para pruebas de compatibilidad     | Técnico    | Media (50%)  | Medio (retraso de 4 días)      | Media     | Mitigar: Usar emuladores en la nube                         | Equipo de QA        | Activo | Contrato con proveedor de emuladores firmado                  |
| R3  | Cambios frecuentes en requisitos de UI invalidan casos de prueba                | Requisitos | Alta (80%)   | Bajo (retraso de 2 días)       | Media     | Aceptar: Tolerar retraso menor; monitorear cambios          | Analista de Negocio | Activo | Reuniones semanales con el cliente para revisar requisitos    |
| R4  | Oportunidad: Automatización de pruebas reduce tiempo de ejecución               | Técnico    | Baja (30%)   | Medio (reducción de 5 días)    | Baja      | Mejorar: Capacitar equipo en herramientas de automatización | Líder de Proyecto   | Activo | Curso de automatización programado para la próxima semana     |

##### Notas:
- **Probabilidad**: Escala cualitativa (Baja: <30%, Media: 30-60%, Alta: >60%).
- **Impacto**: Evaluado en función de cronograma, costo y calidad.
- **Prioridad**: Calculada como Probabilidad × Impacto (Matriz de Riesgos).
- **Estado**: Activo (en monitoreo), Cerrado (resuelto), Materializado (ocurrió).
- **Categoría:** Esta característica es utilizada como agrupación general de las causas potenciales del riesgo. Abajo se las detalla.
****
##### **Categorías de Riesgo según el PMBOK**
Proporcionan un medio para agrupar las causas potenciales de riesgo. Se pueden utilizar diversos enfoques, por ejemplo, una estructura jerárquica de riesgos potenciales ordenados por categorías (se lo suele conocer como **Risk Breakdown Structure RBS** y es muy similar en formato a una [[EDT o WBS]]) .
Diferentes estructuras RBS resultarán adecuadas para diferentes tipos de proyectos. La imagen adjunta es un ejemplo, y no la categorización estándar.
![[Pasted image 20250616173644.png]]