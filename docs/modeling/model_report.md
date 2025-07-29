# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final implementado para la detección de correos phishing es una red neuronal con una capa oculta y función de activación ReLU. Fue entrenado con 85 variables, incluyendo texto procesado, metadatos y características de URL.

En la etapa de evaluación sobre el conjunto de prueba, el modelo alcanzó los siguientes resultados:

-  Accuracy: 83.4%

-  AUC: 0.9205

-  Recall: 83.4%

Estos resultados indican que el modelo tiene una buena capacidad para distinguir entre correos legítimos y fraudulentos, con un buen equilibrio entre falsos positivos y falsos negativos. El valor alto de AUC refleja una discriminación efectiva, y el recall demuestra que el modelo logra detectar la mayoría de los casos de phishing.


## Descripción del Problema

Este proyecto tiene como objetivo desarrollar un modelo de clasificación para la detección de URLs de tipo phishing. En esta sección se presenta el análisis exploratorio de datos (EDA), el cual incluye una evaluación de la calidad de los datos, una revisión de la variable objetivo, un vistazo inicial a las variables explicativas y sus principales características. Asimismo, se describen las estrategias implementadas para la preparación y limpieza de la base de datos, en función de las falencias y patrones identificados durante el análisis.

## Descripción del Modelo

El modelo final fue una red neuronal secuencial con una capa oculta de 192 neuronas y activación ReLU y una capa de salida softmax. Usamos Adam como optimizador con un learning rate de 0.0047, y la pérdida fue categorical crossentropy. Probamos cuatro modelos distintos (combinando activaciones ReLU/Sigmoid y 1 o 2 capas ocultas), y cada uno pasó por una búsqueda aleatoria de hiperparámetros con Keras Tuner, ajustando el número de neuronas (32–512), el dropout (0.1–0.5) y el learning rate (0.0001–0.01). El mejor modelo alcanzó un AUC de 0.9205, recall de 83.4% y accuracy de 83.3%.

## Arquitectura del Modelo
```
model = Sequential([
    Dense(64, activation='relu', input_shape=(85,)),
    Dropout(0.4),
    Dense(2, activation='softmax')
])
model.compile(
    optimizer=Adam(learning_rate=0.0047),
    loss='categorical_crossentropy',
    metrics=['accuracy', 'AUC', 'Recall']
)
```


## Evaluación del Modelo

### Matriz de confusión
En esta sección se presentará una evaluación detallada del modelo final. Se deben incluir las métricas de evaluación que se utilizaron y una interpretación detallada de los resultados.

| Clase       | Precision | Recall | F1-score | Support |
|-------------|-----------|--------|----------|---------|
| Legitimate  | 0.78      | 0.90   | 0.83     | 1143    |
| Phishing    | 0.88      | 0.74   | 0.80     | 1143    |
| **Accuracy**      |           |        | 0.82     | 2286    |
| **Macro avg**     | 0.83      | 0.82   | 0.82     | 2286    |
| **Weighted avg**  | 0.83      | 0.82   | 0.82     | 2286    |

<img width="658" height="547" alt="image" src="https://github.com/user-attachments/assets/81449acc-ec29-48f8-84e2-1ae0b9cd3516" />

Métricas Finales:
- Accuracy: 0.8198
- AUC: 0.9003
- Recall: 0.8196


### Curva ROC

<img width="702" height="548" alt="image" src="https://github.com/user-attachments/assets/818c73ee-2f15-40e6-959a-fc214f037343" />

El área bajo la curva (AUC) es de 0.90, lo que significa que el modelo logra un desempeño sólido, muy por encima del azar. Lo que significa que hay un 90% de probabilidad de que el modelo asigne una puntuación más alta a un correo phishing que a uno legítimo al comparar un par aleatorio de correos.

## Conclusiones y Recomendaciones

## Fortalezas  
- Excelente capacidad discriminativa (AUC 0.90)  
- Precisión razonablemente alta (Accuracy 82%)  
- Arquitectura del modelo simple y eficiente.
- Independencia del idioma o contenido textual (solo requiere la URL)  


## Limitaciones  
- Posible pérdida de desempeño con URLs en alfabetos no latinos o codificaciones poco comunes  
- Potencial sensibilidad a patrones de phishing no presentes en los datos de entrenamiento  
- Foco exclusivo en URLs: no incorpora señales adicionales como contenido del correo, IPs o metadatos  
- Aunque robusto, podrían existir modelos con métricas levemente superiores  

## Conclusiones  
El modelo demuestra:  
1. Capacidad efectiva para detectar intentos de phishing con base en URLs (AUC > 0.9)  
2. Un desempeño balanceado entre precisión y recall, reduciendo falsos positivos y falsos negativos  
3. Solidez como punto de partida para sistemas de detección más avanzados  
4. Aplicabilidad a múltiples contextos (correos, navegación web) sin depender del idioma  

## Recomendaciones  
1. Evaluar desempeño con URLs en otros alfabetos o estructuras regionales  
2. Explorar el uso de modelos con mayor capacidad (como LSTM, Transformers) para capturar secuencias complejas  
3. Complementar el modelo con otras fuentes de información (contenido del mensaje, metadatos, patrones de envío)  
4. Reentrenar periódicamente el modelo con datos más recientes para adaptarse a nuevas tácticas de phishing  
5. Ajustar y monitorear el umbral de clasificación para balance


# Referencias
- Chollet, F. (2021). *Deep Learning with Python*. Manning Publications.
- Documentación oficial de [TensorFlow](https://www.tensorflow.org/)
- Investigaciones recientes en detección de phishing (IEEE Xplore)
