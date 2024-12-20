# Librerías estándar
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocesamiento
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Modelado
from sklearn.cluster import KMeans

# Embeddings
from sentence_transformers import SentenceTransformer

# Reducción de dimensionalidad
from sklearn.decomposition import PCA

# Evaluación
from sklearn.metrics import silhouette_score

# Visualización de datos
from sklearn.manifold import TSNE

# Transformadores personalizados
from sklearn.base import BaseEstimator, TransformerMixin


df = pd.read_excel(r"C:\\Users\\cdgn2\\OneDrive\\Escritorio\\Maestría\\Maestria\\Metodologias Agiles\\Proyecto\\Comparative-analysis-of-products\\src\\comparative_analysis\\database\\Adidas_etiquetado.xlsx")


def preprocess_outsole(text):
    if pd.isna(text):
        return "Desconocido"
    # Reemplazar porcentajes o valores numericos por una etiqueta genérica
    text = re.sub(r'\d+(\.\d+)?\%?', 'X%', text)
    # Unificar materiales
    text = text.replace("Acetato de etileno y vinilo", "EVA")
    text = text.replace("Caucho sintético", "CauchoSintetico")
    # Quitar espacios extra
    text = re.sub(r'\s+', ' ', text).strip()
    return text


#Remplaza los caracteres no numéricos
df['Weight'] = df['Weight'].apply(lambda x: re.sub(r'[^\d.]', '', str(x)))
df['Drop__heel-to-toe_differential_'] = df['Drop__heel-to-toe_differential_'].apply(lambda x: re.sub(r'[^\d.]', '', str(x)))
df['regularPrice'] = df['regularPrice'].apply(lambda x: re.sub(r'\D', '', str(x)))
df['undiscounted_price'] = df['undiscounted_price'].apply(lambda x: re.sub(r'\D', '', str(x)))


df['Weight'] = df['Weight'].replace('', np.nan)
df['Drop__heel-to-toe_differential_'] = df['Drop__heel-to-toe_differential_'].replace('', np.nan)
df['regularPrice'] = df['regularPrice'].replace('', np.nan)
df['undiscounted_price'] = df['undiscounted_price'].replace('', np.nan)


df['Weight'] = df['Weight'].astype(float)
df['Drop__heel-to-toe_differential_'] = df['Drop__heel-to-toe_differential_'].astype(float)
df['regularPrice'] = df['regularPrice'].astype(float)
df['undiscounted_price'] = df['undiscounted_price'].astype(float)


df['percentil_discounted'] = 1-(df['undiscounted_price']/df['regularPrice'])


df_reduced = df[['Weight','Upper_Material','Midsole_Material','Outsole','Cushioning_System','Drop__heel-to-toe_differential_','regularPrice','undiscounted_price','percentil_discounted', 'Gender','Additional_Technologies']]


df_reduced['Outsole'] = df_reduced['Outsole'].apply(preprocess_outsole)


 
 # Identificar columnas numéricas y categóricas
numerical_cols = ['Drop__heel-to-toe_differential_','Weight', 'regularPrice','undiscounted_price','percentil_discounted']
categorical_cols = ['Midsole_Material', 'Cushioning_System', 'Outsole', 'Upper_Material', 
                    'Additional_Technologies', 'Gender']
 
# Definir qué columnas numéricas se imputarán con mediana y escalado
numeric_impute_cols = ['regularPrice']

# Definir columnas numéricas "especiales" que no se deben imputar con mediana
special_numeric_cols = ['Drop__heel-to-toe_differential_', 'percentil_discounted','Weight', 'undiscounted_price']

###################################
# Transformador personalizado
###################################
class SpecialNumericToCategory(BaseEstimator, TransformerMixin):
 
    """
    Este transformador convierte las columnas numéricas "especiales" en categorías.
    Por ejemplo:
    - Si el valor es NaN, lo marca como "NoValue".
    - Si tiene valor, lo convierte a una categoría del tipo "Value:X".
    """
    def __init__(self, cols):
        self.cols = cols
        
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for col in self.cols:
            X[col] = X[col].apply(lambda val: 'NoValue' if pd.isna(val) else f'Value:{val}')
        return X[self.cols]

###################################
# Pipelines
###################################

# Pipeline para columnas numéricas "normales"
numeric_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),  # Imputar con mediana
    ('scaler', StandardScaler())                    # Escalar a media=0, std=1
])

# Pipeline para columnas numéricas "especiales", convertidas a categóricas
special_numeric_pipeline = Pipeline(steps=[
    ('to_category', SpecialNumericToCategory(special_numeric_cols)),
    ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')), 
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Pipeline para columnas categóricas normales
categorical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinar todos los pipelines con ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_pipeline, numeric_impute_cols),
    ('special_num', special_numeric_pipeline, special_numeric_cols),
    ('cat', categorical_pipeline, categorical_cols)
])
X_transformed = preprocessor.fit_transform(df_reduced)
feature_names = (preprocessor.named_transformers_['num'][-1].get_feature_names_out(numeric_impute_cols).tolist() 
                 + preprocessor.named_transformers_['special_num'][-1].get_feature_names_out(special_numeric_cols).tolist()
                 + preprocessor.named_transformers_['cat'][-1].get_feature_names_out(categorical_cols).tolist())



model = SentenceTransformer('all-MiniLM-L6-v2')

# Preprocesar columnas numéricas
print("Preprocesando columnas numéricas...")
scaler = StandardScaler()
numerical_scaled = scaler.fit_transform(df_reduced[numerical_cols].fillna(0))

# Generar embeddings para columnas categóricas
print("Generando embeddings para columnas categóricas...")
categorical_embeddings = []
for col in categorical_cols:
    embeddings = model.encode(df_reduced[col].fillna('Unknown').astype(str).tolist())
    categorical_embeddings.append(embeddings)

# Asignar importancia a las columnas categóricas según el orden dado
# Asumiendo el orden de categorical_cols:
# ['Midsole_Material', 'Cushioning_System', 'Additional_Technologies', 'Outsole', ...]
Midsole_Material_embeddings = categorical_embeddings[0] * 5.0      # 1ra prioridad
Cushioning_System_embeddings = categorical_embeddings[1] * 5.0      # 1ra prioridad
Additional_Technologies_embeddings = categorical_embeddings[2] * 2.0 # info adicional
Outsole_embeddings = categorical_embeddings[3] * 3.0                # 3ra prioridad

# Otras columnas categóricas (si las hay)
if len(categorical_embeddings) > 4:
    other_cat_embeddings = np.hstack(categorical_embeddings[4:])
else:
    other_cat_embeddings = np.empty((len(df_reduced), 0))

# Ajustar importancia en las variables numéricas:
# numerical_cols = ['Drop__heel-to-toe_differential_','Weight','regularPrice','undiscounted_price','percentil_discounted']
drop_idx = numerical_cols.index('Drop__heel-to-toe_differential_')
weight_idx = numerical_cols.index('Weight')
regular_price_idx = numerical_cols.index('regularPrice')

# Aplicar factores
numerical_scaled[:, drop_idx] *= 4.0     # 2da prioridad
numerical_scaled[:, weight_idx] *= 2.0   # 5ta prioridad
numerical_scaled[:, regular_price_idx] *= 1.5 # 6ta prioridad

# Combinar embeddings categóricos con sus factores
combined_categorical_embeddings = np.hstack([
    Midsole_Material_embeddings,
    Cushioning_System_embeddings,
    Additional_Technologies_embeddings,
    Outsole_embeddings,
    other_cat_embeddings
])

# Combinar características numéricas y categóricas sin volver a escalar,
# para no perder la ponderación manual
print("Concatenando características numéricas y categóricas...")
combined_features = np.hstack([numerical_scaled, combined_categorical_embeddings])

# Ahora aplicamos PCA, k-means, etc., sobre combined_features
print("Aplicando PCA para reducir dimensiones...")
pca = PCA(n_components=400, random_state=42)  # Ajusta n_components según necesidad
reduced_features = pca.fit_transform(combined_features)

print("Calculando el Método del Codo para determinar el número óptimo de clusters...")
wcss = []
k_values = range(10, 21)  # Rango de k para explorar

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(reduced_features)
    wcss.append(kmeans.inertia_)

# Visualizar el Método del Codo
plt.figure(figsize=(10, 6))
plt.plot(k_values, wcss, marker='o')
plt.title('Método del Codo para Determinar el Número Óptimo de Clusters')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('WCSS (Inercia)')
plt.xticks(k_values)
plt.grid(True)
plt.show()

print("Calculando el Silhouette Score para diferentes valores de k...")
silhouette_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(reduced_features)
    score = silhouette_score(reduced_features, clusters)
    silhouette_scores.append(score)

# Visualizar el Silhouette Score
plt.figure(figsize=(10, 6))
plt.plot(k_values, silhouette_scores, marker='o', color='orange')
plt.title('Silhouette Score para Diferentes Valores de k')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Silhouette Score')
plt.xticks(k_values)
plt.grid(True)
plt.show()

best_k = k_values[np.argmax(silhouette_scores)]
print(f"El número óptimo de clusters según el Silhouette Score es: {best_k}")

print(f"Aplicando K-Means con k={best_k}...")
kmeans_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
clusters_final = kmeans_final.fit_predict(reduced_features)

# Añadir etiquetas de cluster al DataFrame original
df['Cluster'] = clusters_final

n_clusters_final = len(set(clusters_final))
print(f'\nNúmero de clusters encontrados: {n_clusters_final}')

print("Reduciendo dimensiones para visualización con t-SNE...")
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
tsne_results = tsne.fit_transform(reduced_features)

df['tsne-2d-one'] = tsne_results[:, 0]
df['tsne-2d-two'] = tsne_results[:, 1]

plt.figure(figsize=(12, 8))
palette = sns.color_palette("hsv", n_clusters_final)
sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    hue="Cluster",
    palette=palette,
    data=df,
    legend="full",
    alpha=0.7
)
plt.title('Visualización de Clusters con t-SNE')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

print("\nResumen de Clusters:")
print(df['Cluster'].value_counts())


df.to_excel('src\\comparative_analysis\\models\\K-MeansV2\\productos_con_clusters.xlsx', index=False)