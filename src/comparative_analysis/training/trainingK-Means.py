import pandas as pd
import re
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ** Carga y limpieza de datos **
# Ruta del archivo de Excel
ruta_excel = r"C:\Users\cdgn2\OneDrive\Escritorio\Maestría\Maestria\Metodologias Agiles\Proyecto\Comparative-analysis-of-products\src\comparative_analysis\database\Adidas_etiquetado.xlsx"

# Crear el DataFrame
df = pd.read_excel(ruta_excel, header=0)

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
    df[col] = df[col].str.replace(r'\.', '', regex=True).str.replace(',', '.')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Eliminar columnas innecesarias
cols_to_drop = ['details', 'description', 'category', 'characteristics', 'width', 'Pronation_Type']
df = df.drop(columns=cols_to_drop, errors='ignore')

# ** Clustering y evaluación **
# Separar la columna ID
ids = df['id']
X = df.drop(columns=['id'], errors='ignore').fillna(0)

# Codificar variables categóricas
df_dummies = pd.get_dummies(X, dummy_na=True).fillna(0)

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_dummies)

# Determinar el número óptimo de clusters usando el método del codo
def metodo_del_codo(X, k_range):
    distortions = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)
    
    plt.figure(figsize=(8, 5))
    plt.plot(k_range, distortions, 'bx-')
    plt.xlabel('Número de clusters k')
    plt.ylabel('Distorsión (Inercia)')
    plt.title('Método del Codo para determinar k')
    plt.show()

# Mostrar el método del codo
metodo_del_codo(X_scaled, range(2, 11))

# Clustering con un número específico de clusters
k = 8
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Agregar el cluster al DataFrame original
df['cluster'] = clusters

# Evaluar calidad del clustering
sil_score = silhouette_score(X_scaled, clusters)
db_score = davies_bouldin_score(X_scaled, clusters)
print(f"Silhouette Score: {sil_score}")
print(f"Davies-Bouldin Score: {db_score}")

# ** Análisis de clusters **
def analizar_cluster(df, cluster_num):
    elementos_cluster = df[df['cluster'] == cluster_num]
    print(f"Elementos del cluster {cluster_num}:")
    print(elementos_cluster.head())

    print(f"\nEstadísticas descriptivas del cluster {cluster_num}:")
    print(elementos_cluster.describe())

    # Visualización de histogramas
    columnas_relevantes = elementos_cluster.select_dtypes(include=['number']).columns
    for col in columnas_relevantes:
        elementos_cluster[col].plot(kind='hist', title=f"Distribución de {col} en cluster {cluster_num}")
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()

# Ejemplo de análisis para un cluster específico
analizar_cluster(df, cluster_num=2)