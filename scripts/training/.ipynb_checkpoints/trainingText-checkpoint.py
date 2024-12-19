import pandas as pd
import re
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler

# ** Carga y limpieza de datos **
ruta_excel = r"C:\\Users\\cdgn2\\OneDrive\\Escritorio\\Maestría\\Maestria\\Metodologias Agiles\\Proyecto\\Comparative-analysis-of-products\\src\\comparative_analysis\\database\\Adidas_etiquetado.xlsx"

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
    df[col] = df[col].str.replace(r'\\.', '', regex=True).str.replace(',', '.')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Eliminar columnas innecesarias
cols_to_drop = ['details', 'description', 'category', 'characteristics', 'width', 'Pronation_Type']
df = df.drop(columns=cols_to_drop, errors='ignore')

# ** Clustering y evaluación **
ids = df['id']
X = df.drop(columns=['id'], errors='ignore').fillna(0)

# Codificar variables categóricas
df_dummies = pd.get_dummies(X, dummy_na=True).fillna(0)

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_dummies)

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
    print(f"\n=== Análisis del cluster {cluster_num} ===")
    print(f"Total de elementos: {len(elementos_cluster)}")

    print(f"\nEstadísticas descriptivas principales:")
    print(elementos_cluster.describe().loc[['mean', 'std', 'min', 'max']])

    print(f"\nValores más frecuentes por columna categórica:")
    cols_categoricas = elementos_cluster.select_dtypes(include=['object', 'category']).columns
    for col in cols_categoricas:
        print(f"  - {col}: {elementos_cluster[col].mode().values[0]}")

# Analizar los clusters 2 y 3
analizar_cluster(df, cluster_num=2)
analizar_cluster(df, cluster_num=3)