# Reporte del Modelo Baseline - Detección de Phishing

## Descripción del Proyecto
Sistema de detección de phishing para protección financiera en Colombia implementando una red neuronal como modelo baseline. El objetivo es clasificar correos electrónicos como legítimos (0) o fraudulentos (1).

## Integrantes del Equipo
- Jesús David Castro Afanador
- Miguel Angel Medina Rangel  
- Federico Negret Cubillos

## Librerías Principales
```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score
```
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

# Variables Utilizadas

## Variables de Entrada (85 características)
- Características de texto procesadas (CountVectorizer)
- Metadatos de correos electrónicos  
- Features de URLs embebidas
- One-Hot Encoding para variables categóricas (`nb_redirection`)

## Variable Objetivo
- Binaria (0: legítimo, 1: phishing)

# Preprocesamiento
1. Codificación One-Hot de variables categóricas
2. Partición de datos:
   - 80% entrenamiento
   - 17% validación
   - 3% prueba
3. Balanceo mediante estratificación

# Optimización
Se utilizó Keras Tuner para encontrar los mejores hiperparámetros:

| Hiperparámetro        | Valor Óptimo |
|-----------------------|--------------|
| Neuronas capa oculta  | 192          |
| Tasa de Dropout       | 0.3          |
| Learning Rate         | 0.0047       |

# Resultados de Evaluación

## Métricas Principales

| Métrica   | Valor    |
|-----------|----------|
| Accuracy  | 0.8342   |
| AUC       | 0.9205   |
| Recall    | 0.8342   |

## Comparación con otros modelos

| Modelo               | Accuracy | AUC    | Recall |
|----------------------|----------|--------|--------|
| Baseline (1 capa ReLU) | 0.8342   | 0.9205 | 0.8342 |
| 2 capas ReLU         | 0.7830   | 0.8713 | 0.7830 |
| 1 capa Sigmoid       | 0.7979   | 0.8856 | 0.7979 |
| 2 capas Sigmoid      | 0.7826   | 0.8662 | 0.7826 |

# Análisis de Resultados

## Fortalezas
- Excelente capacidad discriminativa (AUC 0.92)
- Balance adecuado entre precisión y recall  
- Arquitectura simple pero efectiva

## Limitaciones
- Posible sobreajuste (se implementó dropout para mitigarlo)
- Sensibilidad a patrones no vistos en entrenamiento
- Dependencia de características específicas

# Conclusiones
El modelo baseline demuestra:
1. Capacidad efectiva para detectar phishing (AUC > 0.9)
2. Buen balance entre métricas clave
3. Base sólida para mejoras futuras

# Recomendaciones
1. Implementar aumento de datos sintéticos
2. Probar arquitecturas LSTM/Transformers  
3. Validar con datos más recientes
4. Optimizar umbral de clasificación

# Referencias
- Chollet, F. (2021). *Deep Learning with Python*. Manning Publications.
- Documentación oficial de [TensorFlow](https://www.tensorflow.org/)
- Investigaciones recientes en detección de phishing (IEEE Xplore)
