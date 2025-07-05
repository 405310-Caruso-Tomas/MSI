La información de este apartado es sacada del libro “Fundation Level Sillabus”, por parte del International Software Testing Qualifications Board **(ISTQB)**. Organización sin ánimo de lucro creada por empresas, instituciones y profesionales especializados en testing y la industria del software.

![Pasted image 20250524084202.png](/MSI/assets/Pasted image 20250524084202.png)
****
###### 1. ***El testing muestra la presencia de defectos, no su ausencia.*** 
Las pruebas pueden revelar la existencia de errores en el software, pero nunca pueden demostrar que el producto está completamente libre de defectos. Incluso si no se encuentran fallos, no se puede garantizar que no existan.
###### 2. ***El testing exhaustivo es imposible.***
Es imposible probar todas las combinaciones posibles de entradas y escenarios en un software, ya que esto requeriría tiempo y recursos ilimitados. Por lo tanto, se deben priorizar las pruebas en función del riesgo y las áreas más críticas del sistema.

###### 3. ***Testea temprano, y frecuente.*** 
> !!! note "Barry Boehm"
> ***“Un error encontrado en la fase de diseño cuesta diez veces menos que uno en la codificación y cien veces menos que uno encontrado después del lanzamiento.”***

Si quieres encontrar errores, comienza tan pronto como sea posible.
Eso significa pruebas unitarias para los desarrolladores, pruebas de integración durante el ensamblaje y pruebas de sistema, **en ese orden de prioridad**. 

![Pasted image 20250524144335.png](/MSI/assets/Pasted image 20250524144335.png)

Identificar y corregir defectos en etapas tempranas es mucho más económico que hacerlo al final del proyecto.
###### 4. ***Agrupación de defectos.***
A menudo, la mayoría de los defectos se concentran en unos pocos módulos del software. Esto sigue el **principio de Pareto: el 80% de los defectos provienen del 20% de los módulos.** Dirigir más pruebas a estas áreas puede aumentar la efectividad del testing.
###### 5. ***Paradoja del Pesticida.***
Si las mismas pruebas se repiten una y otra vez, eventualmente dejarán de encontrar nuevos errores. Como sucede con los pesticidas que pierden eficacia cuando los insectos desarrollan resistencia, las pruebas también deben actualizarse y mejorarse constantemente para ser efectivas.
###### 6. ***El testing depende del contexto.***
Las pruebas deben adaptarse al tipo de software que se está evaluando. Los riesgos y requisitos de un software médico, por ejemplo, son muy diferentes a los de un sistema comercial.
###### 7. ***Falsedad de la ausencia de errores.***
Encontrar y corregir muchos defectos no garantiza el éxito del software. Aunque un producto puede estar libre de errores técnicos, puede fallar si no satisface las necesidades del usuario o si los requisitos no se definieron adecuadamente.
