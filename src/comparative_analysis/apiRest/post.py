from flask import jsonify, request
import pandas as pd
import re
from joblib import load

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
    
# Ruta POST para clasificar un nuevo elemento
def classify_new_element_KMeansV1():
    """
    Endpoint POST para clasificar un nuevo elemento y devolver productos similares en el mismo cluster.

    Request JSON:
    {
        "nuevo_elemento": { ... },  # Diccionario con las características del nuevo producto
    }

    Response JSON:
    {
        "cluster": int,
        "productos_similares": [ ... ]  # Lista de productos similares en el mismo cluster
    }
    """
    try:
        # Obtener el nuevo elemento del cuerpo de la solicitud
        nuevo_elemento = request.json.get('nuevo_elemento')

        if not nuevo_elemento:
            return jsonify({"error": "Se requiere el nuevo elemento en el cuerpo de la solicitud"}), 400

        # Cargar el archivo del dataset
        file_path = 'src/comparative_analysis/database/Adidas_etiquetado.xlsx'
        df = pd.read_excel(file_path)

        # Verificar si el DataFrame tiene la columna 'cluster'
        if 'cluster' not in df.columns:
            return jsonify({"error": "El dataset no contiene la columna 'cluster'. Verifica si el modelo fue entrenado correctamente."}), 500

        # Cargar el modelo y el escalador
        modelo_path = 'src/comparative_analysis/models/K-MeansV1/kmeans_model.joblib'
        scaler_path = 'src/comparative_analysis/models/K-MeansV1/scaler.joblib'
        kmeans = load(modelo_path)
        scaler = load(scaler_path)

        # Obtener las columnas utilizadas en el entrenamiento
        columnas_entrenamiento = [col for col in df.columns if col not in ['id', 'cluster']]

        # Preprocesar el nuevo elemento
        nuevo_df = pd.DataFrame([nuevo_elemento], columns=columnas_entrenamiento).fillna(0)

        # Convertir variables categóricas en dummies para que coincidan con el entrenamiento
        nuevo_df = pd.get_dummies(nuevo_df)
        df_dummies = pd.get_dummies(df[columnas_entrenamiento])

        # Asegurar que las columnas del nuevo elemento coincidan con las del dataset original
        nuevo_df = nuevo_df.reindex(columns=df_dummies.columns, fill_value=0)

        # Escalar las características del nuevo elemento
        nuevo_elemento_escalado = scaler.transform(nuevo_df)

        # Predecir el cluster del nuevo elemento
        cluster_predicho = kmeans.predict(nuevo_elemento_escalado)[0]

        # Filtrar productos en el mismo cluster
        productos_similares = df[df['cluster'] == cluster_predicho].to_dict(orient='records')

        # Devolver el cluster y los productos similares
        return jsonify({
            "cluster": int(cluster_predicho),
            "productos_similares": productos_similares
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500