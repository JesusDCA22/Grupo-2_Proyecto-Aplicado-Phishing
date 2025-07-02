# Proyecto Sistema de Detección de Phishing para Protección Financiera en Colombia

Este repositorio contiene el código en Python y las instrucciones necesarias para cargar el dataset desde Kaggle, con el objetivo de construir un sistema de detección de sitios web de phishing que pueda aplicarse en contextos financieros en Colombia.

## Requisitos

```python
!pip install kaggle gdown
```
## Descarga de Dataset
El dataset se encuentra en Kaggle:
🔗 [Web Page Phishing Detection Dataset](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)

```python
# Descargar kaggle.json desde Drive
!gdown --id 1ZpnQ6PeUaFOepK6OIA6ryaw-cJ_qHfFA -O kaggle.json

# Configurar credenciales de Kaggle
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Descargar y descomprimir dataset
!kaggle datasets download -d shashwatwork/web-page-phishing-detection-dataset
!unzip -o web-page-phishing-detection-dataset.zip -d phishing_data
```

## Lectura de Dataset (Python)

```python
import pandas as pd
data = pd.read_csv("phishing_data/dataset_phishing.csv")
data.head()
```
