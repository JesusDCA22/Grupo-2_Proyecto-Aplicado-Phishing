from flask import Flask, jsonify, request
from apiRest.get import test, get_product_by_id
from apiRest.post import get_products_by_parameters, predictKMeansV1
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import pandas as pd
import keras

# Crear la instancia de Flask
app = Flask(__name__)

# Registrar las rutas GET
app.add_url_rule('/api/test', view_func=test, methods=['GET'])
app.add_url_rule('/api/product', view_func=get_product_by_id, methods=['GET'])

# Registrar las rutas POST
app.add_url_rule('/api/products', view_func=get_products_by_parameters, methods=['POST'])
app.add_url_rule('/predict/KMeansV1', view_func=predictKMeansV1, methods=['POST'])

model = keras.saving.load_model(".\src\comparative_analysis\models\RedNeuronal\modelo_entrenado.keras")

# Ajusta las columnas según tu caso real:
numerical_cols = ['Drop__heel-to-toe_differential_', 'Weight', 'regularPrice','undiscounted_price','percentil_discounted']
categorical_cols = ['Midsole_Material', 'Cushioning_System', 'Outsole', 'Upper_Material', 
                    'Additional_Technologies', 'Gender']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)


categories = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

@app.route('/classify', methods=['POST'])
def classify():
    # Se espera un JSON con las llaves que coincidan con las columnas esperadas
    data = request.get_json()
    # Crear DataFrame con el nuevo elemento
    # Asumimos que 'data' es un dict con las columnas correctas
    nuevo_elemento = pd.DataFrame([data])  # Convierte el dict a DF con una fila
    
    # Preprocesar
    #preprocessor.fit_transform(nuevo_elemento)
    X_new_processed = preprocessor.fit_transform(nuevo_elemento)
    
    
    # Predecir
    y_pred_proba = model.predict(X_new_processed)
    y_pred_class = np.argmax(y_pred_proba, axis=1)
    predicted_cluster = categories[y_pred_class[0]]

    # Retornar la predicción en formato JSON
    return jsonify({'prediction': predicted_cluster})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=2626)