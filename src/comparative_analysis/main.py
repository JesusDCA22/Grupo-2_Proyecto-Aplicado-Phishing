from flask import Flask, jsonify, request
from apiRest.get import test, get_product_by_id, get_products_by_cluster
from apiRest.post import get_products_by_parameters
import pandas as pd
import keras
import joblib

# Crear la instancia de Flask
app = Flask(__name__)

# Registrar las rutas GET
app.add_url_rule('/api/test', view_func=test, methods=['GET'])
app.add_url_rule('/api/product', view_func=get_product_by_id, methods=['GET'])
app.add_url_rule('/api/similarProducts', view_func=get_products_by_cluster, methods=['GET'])

# Registrar las rutas POST
app.add_url_rule('/api/products', view_func=get_products_by_parameters, methods=['POST'])

model = keras.saving.load_model(".\src\comparative_analysis\models\RedNeuronal\modelo_entrenado.keras")
# Cargar el preprocessor
preprocessor = joblib.load(".\src\comparative_analysis\models\RedNeuronal\preprocessor.pkl")  

numerical_cols = ['Drop__heel-to-toe_differential_', 'Weight', 'regularPrice','undiscounted_price','percentil_discounted']
categorical_cols = ['Midsole_Material', 'Cushioning_System', 'Outsole', 'Upper_Material', 
                    'Additional_Technologies', 'Gender']


@app.route('/predict', methods=['POST'])
def predict():
    # Recibir datos en formato JSON
    data = request.get_json()
    df_new = pd.DataFrame([data])
    
    # Procesar los datos usando el preprocessor cargado
    X_new_processed = preprocessor.transform(df_new)
    
    # Hacer predicción con el modelo
    predictions_proba = model.predict(X_new_processed)
    predictions = predictions_proba.argmax(axis=1)  # Obtener la clase con mayor probabilidad
    
    return jsonify({'prediction': int(predictions[0])})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=2626)