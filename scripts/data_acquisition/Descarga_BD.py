#Requisitos
!pip install kaggle gdown

# Descargar kaggle.json desde Drive
!gdown --id 1ZpnQ6PeUaFOepK6OIA6ryaw-cJ_qHfFA -O kaggle.json

# Configurar credenciales de Kaggle
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Descargar y descomprimir dataset
!kaggle datasets download -d shashwatwork/web-page-phishing-detection-dataset
!unzip -o web-page-phishing-detection-dataset.zip -d phishing_data

#Lectura de datos
import pandas as pd
data = pd.read_csv("phishing_data/dataset_phishing.csv")
data.head()
