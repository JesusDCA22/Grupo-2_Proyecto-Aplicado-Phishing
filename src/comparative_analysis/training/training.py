import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# **1. Cargar el archivo Excel y preparar el DataFrame**
# Ruta del archivo de Excel
ruta_excel = r"C:\Users\cdgn2\OneDrive\Escritorio\Maestría\Maestria\Metodologias Agiles\Proyecto\Comparative-analysis-of-products\src\comparative_analysis\database\Adidas_etiquetado.xlsx"

# Crear el DataFrame
df = pd.read_excel(ruta_excel, header=0)

# **2. Preprocesamiento**
# Convertir columnas a numéricas
df['Weight'] = df['Weight'].astype(str).str.extract('(\d+\.?\d*)').astype(float)
df['Drop__heel-to-toe_differential_'] = pd.to_numeric(df['Drop__heel-to-toe_differential_'].astype(str).str.extract('(\d+\.?\d*)'), errors='coerce')

# Limpiar precios y convertir a numéricos
df['regularPrice'] = pd.to_numeric(df['regularPrice'].str.replace(r'[^\d.,]', '', regex=True).str.replace(r'\.', '', regex=True).str.replace(',', '.'), errors='coerce')
df['undiscounted_price'] = pd.to_numeric(df['undiscounted_price'].str.replace(r'[^\d.,]', '', regex=True).str.replace(r'\.', '', regex=True).str.replace(',', '.'), errors='coerce')

# Eliminar columnas no necesarias
cols_to_drop = ['details', 'description', 'category', 'characteristics', 'width', 'Pronation_Type']
df = df.drop(columns=cols_to_drop, errors='ignore')

# Filtrar IDs nulos
id_nan = df[df['id'].isna()]

# **3. Separar datos para clustering**
# Separar columna 'id'
ids = df['id']
X = df.drop(columns=['id'], errors='ignore')

# Manejar valores faltantes y convertir variables categóricas
X = X.fillna(0)
X = pd.get_dummies(X, dummy_na=True)

# Escalar datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# **4. Clustering con KMeans**
k = 8  # Número de clusters
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Crear un DataFrame con los clusters asignados
df_clusters = pd.DataFrame({'id': ids, 'cluster': clusters})

# Evaluar la calidad del clustering
sil_score = silhouette_score(X_scaled, clusters)
db_score = davies_bouldin_score(X_scaled, clusters)

print("Silhouette Score:", sil_score)
print("Davies-Bouldin Score:", db_score)

# **5. Unir clusters con el DataFrame original**
df_final = df.merge(df_clusters, on='id', how='left')

# **6. Análisis por clusters**
def analizar_cluster(cluster_num):
    # Filtrar elementos del cluster específico
    elementos_cluster = df_final[df_final['cluster'] == cluster_num]

    print(f"\nElementos del cluster {cluster_num}:")
    print(elementos_cluster)

    print(f"\nEstadísticas descriptivas del cluster {cluster_num}:")
    print(elementos_cluster.describe())

    # Visualizar características numéricas
    columnas_relevantes = elementos_cluster.select_dtypes(include=['number']).columns
    for col in columnas_relevantes:
        plt.figure(figsize=(8, 5))
        elementos_cluster[col].hist(bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribución de {col} en el cluster {cluster_num}', fontsize=14)
        plt.xlabel(col, fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

# Ejemplo: Analizar el cluster 0
analizar_cluster(0)

# **7. Determinar el número óptimo de clusters**
distortions = []
K = range(2, 11)  # Rango de k a evaluar
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    distortions.append(kmeans.inertia_)

# Graficar la "elbow curve"
plt.figure(figsize=(8, 5))
plt.plot(K, distortions, 'bo-', markersize=8, linewidth=2, color='blue')
plt.title('Elbow Method para determinar el número óptimo de clusters', fontsize=14)
plt.xlabel('Número de clusters', fontsize=12)
plt.ylabel('Distorsión (Inercia)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()