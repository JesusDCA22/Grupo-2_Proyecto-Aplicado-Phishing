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


# Ruta GET para obtener productos por número de cluster
def get_products_by_cluster():
    cluster_number = request.args.get('cluster')  # Obtener el número de cluster desde los parámetros

    if not cluster_number:
        return jsonify({"error": "Se requiere un número de cluster"}), 400

    try:
        file_path = 'src/comparative_analysis/models/RedNeuronal/productos_con_clusters.xlsx'
        df = pd.read_excel(file_path)

        # Verificar que la columna "Cluster" exista en el archivo
        if 'Cluster' not in df.columns:
            return jsonify({"error": "El archivo no contiene la columna 'Cluster'"}), 500

        # Filtrar los productos por el número de cluster
        filtered_products = df[df['Cluster'] == int(cluster_number)]

        if filtered_products.empty:
            return jsonify({"error": f"No se encontraron productos para el cluster {cluster_number}"}), 404

        # Convertir los datos filtrados a un diccionario
        products_dict = filtered_products.to_dict(orient='records')

        return jsonify({"cluster": cluster_number, "products": products_dict}), 200

    except ValueError:
        return jsonify({"error": "El número de cluster debe ser un valor entero"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
