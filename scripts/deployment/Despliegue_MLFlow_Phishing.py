#### INSTALACIÓN DE LIBRERIAS ####
%%capture
!pip install mlflow
!pip install pyngrok

#### LIBRERIAS ####
import mlflow
import os
import pandas as pd
from IPython.display import display
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.preprocessing import LabelEncoder


#### AJUSTES DE MLFLOW ####

# Servidor de MLFlow #
command = """
mlflow server \
        --backend-store-uri sqlite:///tracking.db \
        --default-artifact-root file:mlruns \
        -p 5000 &
"""
get_ipython().system_raw(command)

# Token de ngrok #
token = "2zL7vEJwMZsnXDweLrLi5trGlDp_3Vw8zyeVBETQGuR98aRA"
os.environ["NGROK_TOKEN"] = token

# Auntenticación de ngrok #
!ngrok authtoken $NGROK_TOKEN

# Conexión con ngrok # 
from pyngrok import ngrok
ngrok.connect(5000, "http")

# Especificamos el servidor
mlflow.set_tracking_uri("http://localhost:5000")

# Definir experimento #
exp_id = mlflow.create_experiment(name="Phishing_Model", artifact_location="mlruns/")

#### CARGAR DE DATOS ####

# Lectura de datos #
data = pd.read_csv("/content/dataset_phising_prepoces.csv")
data.head()

# Especificar Matriz X & Y #
X = data.drop(['url','status'], axis=1)
y = data['status']

# One Hot Encoder #
columnas_categoricas = ['nb_redirection']
X[columnas_categoricas] = X[columnas_categoricas].astype('category')
dummies = pd.get_dummies(X[columnas_categoricas], drop_first=False)
X_Dummies = X.drop(columnas_categoricas, axis=1).join(dummies)

#### MODELAMIENTO ####

# Cargar modelo #
model = tf.keras.models.load_model("/content/mejor_modelo_recall.keras")

#### DESPLIEGUE EN API ####

mlflow.set_experiment("nombre_del_experimento")

with mlflow.start_run(run_name="keras_model_run"):
    mlflow.keras.log_model(model, artifact_path="model")

import os
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"


command = """
mlflow models serve -m 'models:/Phishing_Model/1' -p 8001 --env-manager 'local' &
"""
get_ipython().system_raw(command)

import requests

data_request = X_Dummies.iloc[0:2].values.tolist()
display(data_request)

r = requests.post("http://localhost:8001/invocations", json={"inputs": data_request})
print(r.text)




