# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Chatbot pregunta-respuesta en español

## Objetivo del Proyecto

El objetivo es brindar una solución a los intermediarios de seguros, de tal forma que obtengan información rápida y precisa sobre los procedimientos que deben seguir para lograr una mejor atención a los clientes.
Para lograrlo inicialmente vamos a entrenar un modelo de preguntas y respuestas (QA) utilizando datos específicos.

## Descripción breve del objetivo del proyecto y por qué es importante

El dominio en el que se encuentra el proyecto son las compañías de seguros y el principal cliente o beneficiario son los intermediarios de seguros.
Un seguro es un producto intangible de protección financiera, creado para brindar la continuidad y estabilidad patrimonial a las empresas y/o ciudadanos de un país. Su beneficio es minimizar una pérdida económica derivada de los daños ocasionados por riesgos no controlables, evitando tener que volver a empezar, cada vez que esos factores externos afecten su patrimonio. En los seguros hay varios actores, entre otros: el Cliente que desea proteger su vida o patrimonio, la Aseguradora que dispone productos de seguros y los comercializadores de seguros, tradicionalmente denominados intermediarios de seguros.
Los intermediarios brindan asesoría a sus clientes ayudándoles a entender las características, alcance, costos y diferencias de un producto de seguros frente a otros que existan en el mercado, también brindan atención al cliente en la post-venta en la administración de sus pólizas, rol muy importante especialmente en el momento de presentarse un siniestro.
Por lo anterior es importante desarrollar una herramienta de fácil acceso con la cual los intermediarios obtengan información real, clara y rápida.


## Alcance del Proyecto

La solución que se pretende implementar es un Chatbot para atender a los intermediarios de seguros utilizando las herramientas aprendidas en el curso de Machine Learning.
La herramienta a desarrollar debe dar las instrucciones precisas para los siguientes procesos de seguros para el ramo de automóviles: Cotización, emisión, modificación, anulación, SARLAFT Y documentos necesarios y requerimientos para lo anterior.

Para lograr el objetivo vamos a entrenar un modelo de preguntas y respuestas (QA) utilizando datos específicos. Por el momento contamos con 18 documentos en formato pdf los cuales se encuentran subidos en Google drive. La información ha sido revisada para validar que aporten a los temas planteados en el proyecto, es actualizada y real.

Los ramos diferentes a automóviles están por fuera del alcance del proyecto.

## Metodología

1.	Transformar los datos del formato PDF a texto plano. 
Registro en GitHub: Subir el archivo de texto plano inicial.
2.	Normalización: Limpia y estandariza el texto para consistencia. 
Registro en GitHub: Subir el script de normalización y el archivo de texto normalizado.
3.	Organización: Crear un diccionario con claves para contextos, preguntas y respuestas. Registro en GitHub: Subir el diccionario creado y el script correspondiente.
4.	Preparación del Dataset: Utiliza la biblioteca datasets de Hugging Face para gestionar los datos. 
Registro en GitHub: Subir los archivos del dataset en el formato de Hugging Face y los scripts utilizados.
5.	División de Datos: Separa el dataset en conjuntos de entrenamiento y evaluación. Registro en GitHub: Subir los conjuntos de datos de entrenamiento y evaluación, y el script de división.
6.	Modelo Inicial: Comienza con un modelo BERT preentrenado.
Registro en GitHub: Documentar la configuración del modelo inicial en GitHub.
7.	Preprocesamiento: Tokeniza y prepara los datos para el modelo. 
Registro en GitHub: Subir los datos tokenizados y el script de preprocesamiento.
8.	Ajuste de Hiperparámetros: Define la tasa de aprendizaje, tamaño del lote y número de épocas. 
Registro en GitHub: Documentar los hiperparámetros en GitHub y subir el script de configuración.
9.	Evaluación Inicial: Monitorea la pérdida de entrenamiento y validación. 
Registro en GitHub: Subir los resultados de la evaluación inicial y el script de monitoreo.
10.	Transfer Learning: Cambia a un modelo más robusto y ajusta hiperparámetros adicionales. 
Registro en GitHub: Documentar los cambios realizados y subir el nuevo modelo y los scripts ajustados.
11.	Análisis de Resultados: Evalúa la precisión y ajusta según sea necesario. 
Registro en GitHub: Subir el análisis de resultados y cualquier ajuste final.
12.	Ajustes Finales: Realiza los ajustes finales y prepara la entrega. Registro en GitHub**: Subir toda la documentación final y los scripts finales.


## Cronograma

![image](./gantt_chart.png)

## Equipo del Proyecto

1.	Laura Mercedes 

2.	William Marín J


## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
