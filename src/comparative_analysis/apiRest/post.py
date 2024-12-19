from flask import jsonify, request
import pandas as pd
import re
import pickle

# Cargar el encoder, scaler y modelo KMeans guardados
encoder = pickle.load(open('src\comparative_analysis\models\K-MeansV1\encoder.pkl', 'rb'))
scaler = pickle.load(open('src\comparative_analysis\models\K-MeansV1\scaler.pkl', 'rb'))
kmeans = pickle.load(open('src\comparative_analysis\models\K-MeansV1\kmeans_model.pkl', 'rb'))

# Ruta POST para buscar productos por diferentes parámetros
def get_products_by_parameters():
    params = request.json

    if not params:
        return jsonify({"message": "No se proporcionaron parámetros de búsqueda"}), 400

    try:
        file_path = 'src/comparative_analysis/database/Adidas_etiquetado.xlsx'
        df = pd.read_excel(file_path)
        filtered_df = df

        for key, value in params.items():
            if key in df.columns:
                filtered_df = filtered_df[filtered_df[key].astype(str).apply(
                    lambda x: bool(re.search(r'\b' + re.escape(str(value)) + r'\b', str(x), flags=re.IGNORECASE)))]

        if filtered_df.empty:
            return jsonify({"message": "No se encontraron productos que coincidan con los parámetros proporcionados"}), 404

        products_info = filtered_df.to_dict(orient='records')
        return jsonify(products_info)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def preprocess_data(new_data):
    # Cargar el dataset original para obtener las columnas dummy
    df_original = pd.read_excel('src/comparative_analysis/database/Adidas_etiquetado.xlsx')
    df_dummies_original = pd.get_dummies(df_original, dummy_na=True)

    # Convertir los datos nuevos en un DataFrame
    df_new = pd.DataFrame([new_data])

    # Convertir las columnas categóricas del nuevo producto en variables dummy
    df_dummies_new = pd.get_dummies(df_new, dummy_na=True)

    # Alinear las columnas del nuevo producto con las del dataset original
    df_dummies_new = df_dummies_new.reindex(columns=df_dummies_original.columns, fill_value=0)

    # Escalar los nuevos datos con el scaler previamente entrenado
    X_scaled_new = scaler.transform(df_dummies_new)

    return X_scaled_new


def predictKMeansV1():
    try:
        new_data = request.json  # Obtener datos del producto del cuerpo de la solicitud
        if not new_data:
            return jsonify({"error": "No se enviaron datos para predecir el cluster"}), 400

        # Preprocesar los datos del nuevo producto
        X_scaled_new = preprocess_data(new_data)

        # Asignar el producto a un cluster
        cluster_label = kmeans.predict(X_scaled_new)[0]

        # Obtener los productos originales
        df_original = pd.read_excel('src/comparative_analysis/database/Adidas_etiquetado.xlsx')

        # Agregar los clusters asignados a cada producto
        df_original['cluster'] = kmeans.predict(scaler.transform(pd.get_dummies(df_original, dummy_na=True)))

        # Filtrar los productos que pertenecen al mismo cluster
        products_in_cluster = df_original[df_original['cluster'] == cluster_label]

        # Convertir a JSON y devolver los productos
        products_info = products_in_cluster.to_dict(orient='records')
        return jsonify(products_info)

    except Exception as e:
        return jsonify({"error": str(e)}), 500