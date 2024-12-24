import pandas as pd
import re
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# ** Carga y limpieza de datos **
ruta_excel = r"C:\\Users\\cdgn2\\OneDrive\\Escritorio\\Maestría\\Maestria\\Metodologias Agiles\\Proyecto\\Comparative-analysis-of-products\\src\\comparative_analysis\\database\\Adidas_etiquetado.xlsx"

# Crear el DataFrame
df = pd.read_excel(ruta_excel, header=0, engine='openpyxl')

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
ids = df['id']
X = df.drop(columns=['id'], errors='ignore').fillna(0)

# Codificar variables categóricas
df_dummies = pd.get_dummies(X, dummy_na=True).fillna(0)

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_dummies)

print("Media X_scaled:", X_scaled.mean(axis=0))
print("Desviación estándar X_scaled:", X_scaled.std(axis=0))

# Función para explorar parámetros de DBSCAN
def explorar_parametros_dbscan(X, eps_values, min_samples_values):
    resultados = []
    for eps in eps_values:
        for min_samples in min_samples_values:
            dbscan = DBSCAN(eps=eps, min_samples=min_samples)
            clusters = dbscan.fit_predict(X)
            num_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
            
            if num_clusters > 1:  # Evaluar solo si hay más de 1 cluster válido
                sil_score = silhouette_score(X, clusters)
                db_score = davies_bouldin_score(X, clusters)
                resultados.append((eps, min_samples, num_clusters, sil_score, db_score))
    return resultados

# Rango de parámetros a explorar
eps_values = np.arange(0.1, 3.0, 0.1)
min_samples_values = range(2, 20)

# Explorar los parámetros
resultados = explorar_parametros_dbscan(X_scaled, eps_values, min_samples_values)

# Mostrar los mejores parámetros según Silhouette Score
resultados_sorted = sorted(resultados, key=lambda x: x[3], reverse=True)
mejores_parametros = resultados_sorted[0]
print("\n** Mejores parámetros para DBSCAN **")
print(f"EPS: {mejores_parametros[0]}")
print(f"Min Samples: {mejores_parametros[1]}")
print(f"Número de Clusters: {mejores_parametros[2]}")
print(f"Silhouette Score: {mejores_parametros[3]}")
print(f"Davies-Bouldin Score: {mejores_parametros[4]}")

# Aplicar DBSCAN con los mejores parámetros
dbscan = DBSCAN(eps=mejores_parametros[0], min_samples=mejores_parametros[1])
clusters = dbscan.fit_predict(X_scaled)

# Agregar los clusters al DataFrame
df['cluster'] = clusters


# ** Análisis de clusters para DBSCAN **
def analizar_cluster_dbscan(df, cluster_num):
    elementos_cluster = df[df['cluster'] == cluster_num]
    print(f"\n=== Análisis del cluster {cluster_num} ===")
    print(f"Total de elementos: {len(elementos_cluster)}")

    if len(elementos_cluster) == 0:
        print("El cluster está vacío.")
        return

    print(f"\nEstadísticas descriptivas principales:")
    print(elementos_cluster.describe().loc[['mean', 'std', 'min', 'max']])

    print(f"\nValores más frecuentes por columna categórica:")
    cols_categoricas = elementos_cluster.select_dtypes(include=['object', 'category']).columns
    for col in cols_categoricas:
        if not elementos_cluster[col].dropna().empty:
            modo = elementos_cluster[col].mode()
            valor_modo = modo.values[0] if not modo.empty else "Sin valores frecuentes"
            print(f"  - {col}: {valor_modo}")
        else:
            print(f"  - {col}: Sin datos disponibles")


# Analizar clusters generados
clusters_unicos = set(clusters)
clusters_unicos.discard(-1)  # Ignorar ruido (-1)
print("\n** Análisis de Clusters **")
for cluster_num in clusters_unicos:
    analizar_cluster_dbscan(df, cluster_num)

# Visualización de distribución de clusters
def graficar_distribucion_clusters_dbscan(df):
    plt.figure(figsize=(8, 5))
    df['cluster'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('Cluster')
    plt.ylabel('Número de elementos')
    plt.title('Distribución de elementos por cluster (DBSCAN)')
    plt.xticks(rotation=0)
    plt.show()

print("\n** Distribución de Clusters **")
graficar_distribucion_clusters_dbscan(df)

ruido = sum(clusters == -1)
total = len(clusters)
print(f"Puntos clasificados como ruido: {ruido}/{total} ({ruido/total:.2%})")

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], s=10, c=clusters, cmap='viridis', alpha=0.7)
plt.title('Proyección 2D de los datos escalados')
plt.xlabel('Componente principal 1')
plt.ylabel('Componente principal 2')
plt.colorbar(label='Cluster')
plt.show()

if resultados:
    resultados_sorted = sorted(resultados, key=lambda x: x[3], reverse=True)
    mejores_parametros = resultados_sorted[0]
    print("\n** Mejores parámetros para DBSCAN **")
    print(f"EPS: {mejores_parametros[0]}")
    print(f"Min Samples: {mejores_parametros[1]}")
    print(f"Número de Clusters: {mejores_parametros[2]}")
    print(f"Silhouette Score: {mejores_parametros[3]}")
    print(f"Davies-Bouldin Score: {mejores_parametros[4]}")

    # Aplicar DBSCAN con los mejores parámetros
    dbscan = DBSCAN(eps=mejores_parametros[0], min_samples=mejores_parametros[1])
    clusters = dbscan.fit_predict(X_scaled)
else:
    print("No se encontraron parámetros válidos.")