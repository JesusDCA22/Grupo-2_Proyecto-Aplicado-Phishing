# Proyecto Sistema de Detección de Phishing para Protección Financiera en Colombia

## 📌 Descripción
El siguiente repositorio contiene toda la documentación y scripts desarrollados para el modelo de detección de phishing. Usando un modelo de redes neuronales con Keras, se entreno un modelo de capas densas con alto grado de acertitud para la detección de URL sospechosas de phishing. Este proyecto esta orientado para la prevención de fraude financiero en Colombia.

## 🎯 Objetivo
Desarrollar y desplegar un modelo ML que permita identificar evaluar la propención de riesgo de phishing de las URL usadas por cualquier cliente financiero en Colombia
## 🧠 Tegnología y Tecnicas
- Python 3.2.1
- Colab (Notebook)
- Keras
## 📄 Contenido del Repositorio
### 📚 Docs
- Acceptance
- Business_understanding
- Data
- Deployment
- Modeling
### 💻 Scripts
- Data_acquisition
- Deployment
- Eda
- Evaluation
- preprocessing
- training
### src
### 📊 Datos
Los datos fueron obtenidos de la pagina kaggle.com , en el enlace https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset?resource=download. 
Allí se puede obtener una base de datos equilibrada con más de 11 mil URLs diferentes y más de 87 variables que describen tanto la sintaxis de la URL como el contenido de la pagina a la que lleva dicho enlace.
### 🤖 Modelo
Se uso un algoritmo de redes neuronales de capa densa (deep learning) con la librería Keras. Este modelo fue entrenado en Colab y usando un pipeline basado en RandomSearch para obtener los hiperparametros más optimos. Con una partición 70% entrenamiento, 10% validación y 20% de evaluación. 

la arquitectura del modelo es :
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
### 📈 Resultados

Durante el entrenamiento se entrenaron varios algoritmos con el objetivo de escoger el mejor. Para ello, se tomo un modelo base que permite obtener comparativas de las metricas mas importantes.

| Métrica       | Modelo Base (RF) | Modelo Final (NN) | Mejora |
|---------------|------------------|-------------------|--------|
| Accuracy      | 79.2%            | 83.4%             | +4.2pp |
| AUC           | 0.85             | 0.92              | +8.2%  |
| Recall        | 81.0%            | 83.4%             | +2.4pp |
| Tiempo inferencia | 12ms         | 8ms               | -33%   |


El modelo definitivo obtuvo las siguiente metricas y la siguiente matriz de confusión:

#### Reporte de clasificación
| Clase       | Precision | Recall | F1-score | Support |
|-------------|-----------|--------|----------|---------|
| Legitimate  | 0.78      | 0.90   | 0.83     | 1143    |
| Phishing    | 0.88      | 0.74   | 0.80     | 1143    |
| **Accuracy**      |           |        | 0.82     | 2286    |
| **Macro avg**     | 0.83      | 0.82   | 0.82     | 2286    |
| **Weighted avg**  | 0.83      | 0.82   | 0.82     | 2286    |

#### Matriz de confusión
<img width="658" height="547" alt="image" src="https://github.com/user-attachments/assets/81449acc-ec29-48f8-84e2-1ae0b9cd3516" />

#### Métricas Finales
- Accuracy: 0.8198
- AUC: 0.9003
- Recall: 0.8196


#### Curva ROC

<img width="702" height="548" alt="image" src="https://github.com/user-attachments/assets/818c73ee-2f15-40e6-959a-fc214f037343" />

El área bajo la curva (AUC) es de 0.90, lo que significa que el modelo logra un desempeño sólido, muy por encima del azar. Lo que significa que hay un 90% de probabilidad de que el modelo asigne una puntuación más alta a un correo phishing que a uno legítimo al comparar un par aleatorio de correos.

### ✅ Conclusiones
El modelo demuestra:  
1. Capacidad efectiva para detectar intentos de phishing con base en URLs (AUC > 0.9)  
2. Un desempeño balanceado entre precisión y recall, reduciendo falsos positivos y falsos negativos  
3. Solidez como punto de partida para sistemas de detección más avanzados  
4. Aplicabilidad a múltiples contextos (correos, navegación web) sin depender del idioma  

## 👥 Autories
- Miguel Ángel Medina
- Jesus Castro
- Federico Negret

