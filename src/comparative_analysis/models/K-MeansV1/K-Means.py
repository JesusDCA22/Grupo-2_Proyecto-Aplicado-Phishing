import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
import pickle

# Cargar los datos desde el archivo Excel
df = pd.read_excel(r"C:\\Users\\cdgn2\\OneDrive\\Escritorio\\Maestría\\Maestria\\Metodologias Agiles\\Proyecto\\Comparative-analysis-of-products\\src\\comparative_analysis\\database\\Adidas_etiquetado.xlsx")

# Eliminar columnas no relevantes
cols_to_drop = ['details', 'description', 'category', 'characteristics', 'Width', 'Pronation_Type']
df = df.drop(columns=cols_to_drop, errors='ignore')

id_column = df['id']  # Guardar la columna 'id'
df = df.drop(columns=['id'], errors='ignore')  # Eliminar temporalmente la columna 'id'

# Crear el OneHotEncoder
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Convertir las columnas categóricas en variables dummy
categorical_columns = df.columns  # Todas las columnas son categóricas
df_dummies = pd.get_dummies(df, columns=categorical_columns, dummy_na=True)

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_dummies)

# Entrenar el modelo KMeans con el número óptimo de clusters (5)
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# Obtener los clusters asignados
df['cluster'] = kmeans.labels_

# Volver a añadir la columna 'id' con los clusters asignados
df['id'] = id_column

# Guardar el encoder, scaler y modelo KMeans
pickle.dump(encoder, open('src\\comparative_analysis\\models\\K-MeansV1\\encoder.pkl', 'wb'))
pickle.dump(scaler, open('src\\comparative_analysis\\models\\K-MeansV1\\scaler.pkl', 'wb'))
pickle.dump(kmeans, open('src\\comparative_analysis\\models\\K-MeansV1\\kmeans_model.pkl', 'wb'))

# Si deseas guardar el dataframe con los clusters y el id:
df.to_excel('src\\comparative_analysis\\models\\K-MeansV1\\productos_con_clusters.xlsx', index=False)