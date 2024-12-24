from flask import jsonify, request
import pandas as pd
import re


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