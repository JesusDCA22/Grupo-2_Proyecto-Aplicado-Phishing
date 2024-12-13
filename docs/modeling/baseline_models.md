# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

### bert-large-uncased-whole-word-masking-finetuned-squad

Este modelo es una versión grande de BERT (Bidirectional Encoder Representations from Transformers) preentrenado en texto en inglés en minúsculas utilizando la técnica de Whole Word Masking y afinado en el conjunto de datos SQuAD (Stanford Question Answering Dataset).

Características:	
Capas: 24
Dimensión oculta: 1024
Cabezas de atención: 16
Parámetros: 336 millones
Objetivo de preentrenamiento: Modelado de lenguaje enmascarado (MLM) y predicción de la siguiente oración (NSP)
Uso principal: Respuesta a preguntas en inglés2.
Pertenece a: Google
Referencia en Hugging Face


## Variables de entrada

La variable de entrada del modelo es el corpus de los archivos PDF, en este caso 1 archivo para que el modelo no fuera demasiado pesado.
Este es un modelo de Preguntas y Respuestas que utiliza un modelo de generación de texto, afinado con el conjunto de datos SQuAD 2.0. 

## Variable objetivo

Por ser un proyecto de análisis no supervisado no tiene variable objetivo.

## Evaluación del modelo

### Métricas de evaluación

Se utilizaron las siguientes métricas de evaluación:

- Validation Loss (Pérdida de Validación):  Mide cuán bien el modelo se ajusta a los datos de validación. Ayuda a evaluar si el modelo está aprendiendo correctamente y no está sobreajustando los datos de entrenamiento. Utilizada en modelos de aprendizaje supervisado, especialmente en redes neuronales y modelos de aprendizaje profundo.

- Exact Match (EM): Mide el porcentaje de respuestas que coinciden exactamente con la respuesta correcta. Evalúa la precisión de un modelo de Preguntas y Respuestas. Comúnmente utilizada en modelos de Preguntas y Respuestas extractivas.

- F1 Score: Combina la precisión y la exhaustividad en una sola puntuación. Proporciona una medida equilibrada del rendimiento del modelo, especialmente útil cuando hay un desequilibrio entre clases. Utilizada en clasificación binaria y multiclase, 
así como en modelos de Preguntas y Respuestas.

- Precision (Precisión): Mide el porcentaje de respuestas correctas entre todas las respuestas proporcionadas por el modelo. Evalúa la exactitud de las predicciones del modelo. Utilizada en clasificación binaria y multiclase, así como en modelos de Preguntas y Respuestas.

- Recall (Exhaustividad): Mide el porcentaje de respuestas correctas entre todas las respuestas posibles. Evalúa la capacidad del modelo para encontrar todas las respuestas correctas. Utilizada en clasificación binaria y multiclase, así como en modelos de Preguntas y Respuestas.

### Resultados de evaluación

![image](./Baseline_metrics.png)

## Análisis de los resultados

El Validation Loss se mantiene constante en 6.051758 durante las tres épocas. Esto indica que el modelo no mejora su rendimiento en el conjunto de validación, lo que puede deberse a varias razones:
Problemas en los hiperparámetros (p. ej., tasa de aprendizaje).
Insuficiencia en la cantidad de datos de entrenamiento.
El modelo no está aprendiendo adecuadamente de los datos.

Exact Match, F1 Score, Precision y Recall:
Todas estas métricas están en 0.0000 para las tres épocas. Esto significa que el modelo no está realizando predicciones correctas, ni siquiera parcialmente.
Estas métricas sugieren que el modelo no está captando relaciones útiles entre las características y las etiquetas.

## Conclusiones

- El modelo no está aprendiendo de los datos proporcionados, como lo demuestran el Validation Loss constante y las métricas de rendimiento (Exact Match, F1, Precision, Recall) en 0.
- Es necesario revisar los datos de entrada, las etiquetas, los hiperparámetros y la configuración del entrenamiento para identificar y corregir las posibles causas del bajo rendimiento.
- Considerar registrar el Training Loss para monitorear el aprendizaje durante el entrenamiento.


