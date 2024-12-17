# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:04:17 2024

@author: azacipac
"""

# Importar librerias
import pandas as pd
import re
import sklearn
import matplotlib
#mport matplotlib.pyplot as plt
import numpy as np
import clusteval
import df2onehot
import sys

#from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler
from utilities.utilities import Utilities
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
print('Matplotlib', matplotlib.__version__)
print('Clusteval', clusteval.__version__)
print('Scikit-Learn', sklearn.__version__)
print('DF2Onehot', df2onehot.__version__)

# ** Carga y limpieza de datos **
ruta_excel = r"..\\database\\Adidas_etiquetado_new.xlsx"

# Crear el DataFrame
df_adidas = pd.read_excel(ruta_excel, header=0)
df_adidas.info()

# validacion de nulos/ceros en el dataframe
Utilities.null_or_zero_values(df = df_adidas)

# rellenar valores nulos y eliminar columnas no relevantes
cols_to_drop = ['Width', 'characteristics', 'Pronation_Type', 'Available_Sizes', 'undiscounted_price']
df_adidas = df_adidas.drop(columns=cols_to_drop, errors='ignore')

# limpieza de texto
# Aplicamos limpieza de texto
df_adidas = df_adidas.fillna("0")
reg_numbers = re.compile(r'[^0-9.,]+')
df_adidas['Drop__heel-to-toe_differential_'] = df_adidas['Drop__heel-to-toe_differential_'].apply(lambda doc: Utilities.preprocess(doc, [reg_numbers]))
df_adidas['Weight'] = df_adidas['Weight'].apply(lambda doc: Utilities.preprocess(doc, [reg_numbers]))

# Procesar valores numericos
price_cols = ['regularPrice', 'Drop__heel-to-toe_differential_', 'Weight']
for col in price_cols:
    df_adidas[col] = df_adidas[col].astype(str).str.replace(r'[^0-9.,]', '', regex=True)
    df_adidas[col] = df_adidas[col].str.replace(r'\\.', '', regex=True).str.replace(',', '.')
    df_adidas[col] = pd.to_numeric(df_adidas[col], errors='coerce')

# rellenar variables numericas vacias con 0
df1 = df_adidas.fillna(0)

# normalizar genero
df_adidas['Gender'] = df_adidas['Gender'].apply(lambda x: "Mujer" if x == 'Woman' else x)
df_adidas['Gender'] = df_adidas['Gender'].apply(lambda x: "Hombre" if x == 'Men' else x)
df_adidas['Gender'] = df_adidas['Gender'].apply(lambda x: "0" if x == '5' else x)

# analizar columnas
Utilities.analyze_columns(df = df_adidas, cols = ['Cushioning_System', 'Midsole_Material'])
Utilities.analyze_columns(df = df_adidas, cols = ['Drop__heel-to-toe_differential_','Weight'])
Utilities.analyze_columns(df = df_adidas, cols = ['Gender', 'Additional_Technologies'])
Utilities.analyze_columns(df = df_adidas, cols = ['Usage_Type', 'regularPrice'])
Utilities.analyze_columns(df = df_adidas, cols = ['category'])

# conservar el ID que identifica cada muestra
# ** Clustering y evaluación **
ids = df_adidas['id']

# Eliminar columnas innecesarias
cols_to_drop = ['details', 'description', 'characteristics', 'Pronation_Type', 'id']
df_adidas = df_adidas.drop(columns=cols_to_drop, errors='ignore')

# Realizar codificacion de variables categoricas
dfhot_adidas = df2onehot.df2onehot(df_adidas, excl_background=['0.0', 'None', '?', 'False'], y_min=30
                  , perc_min_num=0.8, remove_mutual_exclusive=True, verbose=4)['onehot']

dfhot_adidas.info()
dfhot_adidas

# Analisis de clusters
# Se realiza comparacion de 4 modelos de clustering
# * kmeans
# * agglomerative
# * dbscan
# * hdbscan
#
def cluster_eval(X, cluster, evaluate, metric = "euclidean", normalize = False, verbose = 40, savefig = False):
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
    
    Ejemplo:
    
        >>> results_kmeans = cluster_eval(X = X_scaled, cluster = "kmeans", evaluate = "silhouette", savefig=True)
            
            Silhouette Score: 0.25816924466629976
            Davies-Bouldin Score: 0.5575649799417841
            [Grafica plot]
            ...
    """
    # Initialize
    ce = clusteval.clusteval(cluster = cluster, evaluate=evaluate, metric = metric, verbose = verbose
                            ,normalize = normalize)
    # Fit
    results = ce.fit(X)
    #
    # metrics
    if(evaluate == "silhouette"):
        sil_score = silhouette_score(X, results["labx"])
        db_score  = davies_bouldin_score(X, results["labx"])
        print(f"Silhouette Score: {sil_score}")
        print(f"Davies-Bouldin Score: {db_score}")
    # Plot
    title = f"Clustering method {cluster} with evaluation {evaluate}"
    if(savefig == True):
        plot_name     = Utilities.image_path + cluster + ".png"
        plot_sil_name = Utilities.image_path + cluster + "_silhouette.png"
        ce.plot(title = title, verbose = verbose, savefig = {"fname" : plot_name, "format" : "png"})
        ce.plot_silhouette(savefig = {"fname" : plot_sil_name})
    else:
        ce.plot(title = title, verbose = verbose)
        ce.plot_silhouette()        
    return results

# analisis con kmeans
results_kmeans = cluster_eval(X = dfhot_adidas, cluster = "kmeans"
                              , evaluate = "silhouette", savefig=True)

# analisis con cluster aglomerativo
results_aggl = cluster_eval(X = dfhot_adidas, cluster = "agglomerative"
                            , evaluate = "silhouette", savefig=True)

# analisis con dbscan
results_dbscan = cluster_eval(X = dfhot_adidas, cluster = "dbscan"
                              , evaluate = "silhouette", savefig=True)

# analisis con hdbscan
results_hdbscan = cluster_eval(X = dfhot_adidas, cluster = "hdbscan"
                               , evaluate = "silhouette", savefig=True)

# Ensamblar en dataframes el resultado de los cluster generados por cada modelo
dfhot_adidas['cluster_kmeans'] = results_kmeans["labx"]
dfhot_adidas['cluster_aggl'] = results_aggl["labx"]
dfhot_adidas['cluster_dbscan'] = results_dbscan["labx"]
dfhot_adidas['cluster_hdbscan'] = results_hdbscan["labx"]

# agrupar la cantidad de elementos de cada cluster
serie1 = dfhot_adidas.groupby(['cluster_kmeans'])['cluster_kmeans'].agg('count')
serie2 = dfhot_adidas.groupby(['cluster_aggl'])['cluster_aggl'].agg('count')
serie3 = dfhot_adidas.groupby(['cluster_dbscan'])['cluster_dbscan'].agg('count')
serie4 = dfhot_adidas.groupby(['cluster_hdbscan'])['cluster_hdbscan'].agg('count')

# generar dataframe con la cantidad y porcentaje de elementos en cada cluster para cada modelo
df1 = pd.DataFrame({'cluster':serie1.index, 'cantidad':serie1.values})
df2 = pd.DataFrame({'cluster':serie2.index, 'cantidad':serie2.values})
df3 = pd.DataFrame({'cluster':serie3.index, 'cantidad':serie3.values})
df4 = pd.DataFrame({'cluster':serie4.index, 'cantidad':serie4.values})
df1["%cluster_kmeans"] = df1['cantidad'] / df1['cantidad'].sum() * 100
df2["%cluster_aggl"] = df2['cantidad'] / df2['cantidad'].sum() * 100
df3["%cluster_dbscan"] = df3['cantidad'] / df3['cantidad'].sum() * 100
df4["%cluster_hdbscan"] = df4['cantidad'] / df4['cantidad'].sum() * 100

# mostrar los datos de cada cluster
print("\nComposicion de clusters por modelo")
print("\nCluster KMeans",df1)
print("\nCluster Agglomerative",df2)
print("\nCluster DBScan",df3)
print("\nCluster HDBScan",df4)