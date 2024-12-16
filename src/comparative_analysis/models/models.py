# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:04:17 2024

@author: azacipac
"""

# Importar librerias
import pandas as pd
#import re
import sklearn
#import matplotlib
#mport matplotlib.pyplot as plt
import numpy as np
#import time
import clusteval
import sys

#from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler
#from sklearn.cluster import DBSCAN, HDBSCAN
#from sklearn import metrics
#from sklearn.preprocessing import StandardScaler

# Version de las librerias
"""
Este codigo ha sido verificado con las siguientes versiones:

Python 3.12.4
Pandas 2.2.3
Numpy 2.1.3
Matplotlib 3.9.3
Clusteval 2.2.2
Scikit-Learn 1.6.0
"""
print(sys.version)
print('Pandas', pd.__version__)
print('Numpy', np.__version__)
#print('Matplotlib', matplotlib.__version__)
print('Clusteval', clusteval.__version__)
print('Scikit-Learn', sklearn.__version__)

# ** Carga y limpieza de datos **
ruta_excel = r"..\\database\\Adidas_etiquetado_new.xlsx"

# Crear el DataFrame
df = pd.read_excel(ruta_excel, header=0)
df.info()

# Procesamiento de columnas numéricas
num_cols = {
    'Weight': '(\d+\.?\d*)',
    'Drop__heel-to-toe_differential_': '(\d+\.?\d*)'
}
for col, pattern in num_cols.items():
    df[col] = df[col].astype(str).str.extract(pattern).astype(float, errors='ignore')
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
# Procesar precios
price_cols = ['regularPrice', 'undiscounted_price']
for col in price_cols:
    df[col] = df[col].astype(str).str.replace(r'[^0-9.,]', '', regex=True)
    df[col] = df[col].str.replace(r'\\.', '', regex=True).str.replace(',', '.')
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
# Eliminar columnas innecesarias
cols_to_drop = ['details', 'description', 'category', 'characteristics', 'width', 'Pronation_Type']
df = df.drop(columns=cols_to_drop, errors='ignore')

# Generar array de caracteristicas
ids = df['id']
X = df.drop(columns=['id'], errors='ignore').fillna(0)

# Codificar variables categóricas
df_dummies = pd.get_dummies(X, dummy_na=True).fillna(0)

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_dummies)
df_dummies.info()

# Analisis de clusters
# Se realiza comparacion de 4 modelos de clustering
# * kmeans
# * agglomerative
# * dbscan
# * hdbscan
#
def cluster_eval(X, cluster, evaluate, verbose = 40, savefig = False):
    """"
    Función cluster_eval: Realiza evaluacion de clustering sobre el conjunto de datos que se indica. Genera grafica de el score que se indica vs numero de clusters
                          y grafico de los coeficientes silhouette para los diferentes clusters
    
    Parámetros:
        X   (Numpy-array): Arreglo de muestras y caracteristicas
        cluster     (str): Tipo de clustering: agglomerative, kmeans, dbscan, hdbscan
        evaluate    (str): Metodo de evaluacion: silhouette, dbindex, derivative
        verbose     (int): Nivel de detalle para mensajes de salida
        savefig (boolean): Indica si se almacena la imagen en archivo png
    
    Return:
        results: Diccionario con diferentes llaves que dependen del metodo de evaluacion utilizado
        sil_score (float): Silhouette Score
        db_score  (float): Davies-Bouldin Score
    
    Ejemplo:
    
        >>> results_kmeans = cluster_eval(X = X_scaled, cluster = "kmeans", evaluate = "silhouette", savefig=True)
            
            Silhouette Score: 0.25816924466629976
            Davies-Bouldin Score: 0.5575649799417841
            [Grafica plot]
            ...
    """
    # Initialize
    ce = clusteval.clusteval(cluster = cluster, evaluate=evaluate, verbose = verbose)
    # Fit
    results = ce.fit(X)
    #
    # metrics
    sil_score = silhouette_score(X, results["labx"])
    db_score  = davies_bouldin_score(X, results["labx"])
    print(f"Silhouette Score: {sil_score}")
    print(f"Davies-Bouldin Score: {db_score}")
    # Plot
    title = f"Clustering method {cluster} with evaluation {evaluate}"
    if(savefig == True):
        plot_path     = r"..\\visualization\\"
        plot_name     = plot_path + cluster + ".png"
        plot_sil_name = plot_path + cluster + "_silhouette.png"
        ce.plot(title = title, verbose = verbose, savefig = {"fname" : plot_name, "format" : "png"})
        ce.plot_silhouette(savefig = {"fname" : plot_sil_name})
    else:
        ce.plot(title = title, verbose = verbose)
        ce.plot_silhouette()        
    return results, sil_score, db_score

# analisis con kmeans
results_kmeans,sil_kmeans_score,db_kmeans_score = cluster_eval(X = X_scaled
                                                              ,cluster = "kmeans"
                                                              ,evaluate = "silhouette"
                                                              ,savefig=True)

# analisis con cluster aglomerativo
results_aggl,sil_aggl_score,db_aggl_score = cluster_eval(X = X_scaled
                                                         ,cluster = "agglomerative"
                                                         ,evaluate = "silhouette"
                                                         ,savefig=True)

# analisis con dbscan
results_dbscan,sil_dbscan_score,db_dbscan_score = cluster_eval(X = X_scaled
                                                               ,cluster = "dbscan"
                                                               ,evaluate = "silhouette"
                                                               ,savefig=True)

# analisis con hdbscan
results_hdbscan,sil_hdbscan_score,db_hdbscan_score = cluster_eval(X = X_scaled
                                                                  ,cluster = "hdbscan"
                                                                  ,evaluate = "silhouette"
                                                                  ,savefig=True)

# Comparacion del score de los modelos
# Silhouette Score
print(f"\nKMeans Silhouette Score: {sil_kmeans_score}")
print(f"Agglomerative Silhouette Score: {sil_aggl_score}")
print(f"DBScan Silhouette Score: {sil_dbscan_score}")
print(f"HDBScan Silhouette Score: {sil_hdbscan_score}")

# Davies-Bouldin
print(f"\nKMeans Davies-Bouldin Score: {db_kmeans_score}")
print(f"Agglomerative Davies-Bouldin Score: {db_aggl_score}")
print(f"DBScan Davies-Bouldin Score: {db_dbscan_score}")
print(f"HDBScan Davies-Bouldin Score: {db_hdbscan_score}")