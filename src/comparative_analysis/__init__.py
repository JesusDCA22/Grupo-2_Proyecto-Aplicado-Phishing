from flask import Flask
from apiRest.get import test, get_product_by_id
from apiRest.post import get_products_by_parameters, classify_new_element_KMeansV1

# Crear la instancia de Flask
app = Flask(__name__)

# Registrar las rutas GET
app.add_url_rule('/api/test', view_func=test, methods=['GET'])
app.add_url_rule('/api/product', view_func=get_product_by_id, methods=['GET'])

# Registrar las rutas POST
app.add_url_rule('/api/products', view_func=get_products_by_parameters, methods=['POST'])
app.add_url_rule('/api/classify/KMeansV1', view_func=classify_new_element_KMeansV1, methods=['POST'])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=2626)