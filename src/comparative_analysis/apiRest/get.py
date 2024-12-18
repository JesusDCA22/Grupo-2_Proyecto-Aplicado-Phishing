from flask import jsonify, request
import pandas as pd

# Ruta GET de prueba
def test():
    response = {
        "message": "¡Hola! Esta es una respuesta GET de prueba.",
        "status": "success"
    }
    return jsonify(response)

# Ruta GET para obtener el producto por ID
def get_product_by_id():
    product_id = request.args.get('id')  # Cambié de `request.json` a `request.args`

    if not product_id:
        return jsonify({"error": "Se requiere un ID de producto"}), 400

    try:
        file_path = 'src/comparative_analysis/database/Adidas_etiquetado.xlsx'
        df = pd.read_excel(file_path)
        product_data = df[df['id'] == product_id]

        if product_data.empty:
            return jsonify({"error": "Producto no encontrado"}), 404

        product_info = product_data.to_dict(orient='records')[0]
        return jsonify(product_info)

    except Exception as e:
        return jsonify({"error": str(e)}), 500