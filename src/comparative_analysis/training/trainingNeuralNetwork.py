import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import keras_tuner as kt
from sklearn.model_selection import StratifiedKFold
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from pandas.api.types import CategoricalDtype
import joblib

directory = 'src/comparative_analysis/models/RedNeuronal'
if not os.path.exists(directory):
    os.makedirs(directory)

directory = r'C:\Users\cdgn2\OneDrive\Escritorio\Maestría\Maestria\Metodologias Agiles\Proyecto\Comparative-analysis-of-products\src\comparative_analysis\models\RedNeuronal'
if not os.path.exists(directory):
    os.makedirs(directory)

# Cargar datos
df = pd.read_excel("src\\comparative_analysis\\models\\RedNeuronal\\productos_con_clusters.xlsx")

# Ajustar nombres de columnas según disponibilidad real en el DataFrame.
numerical_cols = ['Drop__heel-to-toe_differential_', 'Weight', 'regularPrice', 'undiscounted_price', 'percentil_discounted']
categorical_cols = ['Midsole_Material', 'Cushioning_System', 'Outsole', 'Upper_Material', 
                    'Additional_Technologies', 'Gender']

target_col = 'Cluster'
df = df.dropna(subset=[target_col])

X = df[numerical_cols + categorical_cols]
y = df[target_col]

# Convertir a categoría si no lo es ya
if not isinstance(y.dtype, CategoricalDtype):
    y = y.astype('category')

num_classes = len(y.cat.categories)

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

# Función para construir el modelo
def build_model(hp):
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(X_train.shape[1],)))  # Aquí solo tomamos las columnas de X_train, no de X_train_processed


    # Primera capa densa con búsqueda de hiperparámetros
    model.add(keras.layers.Dense(
        units=hp.Int('units_layer1', min_value=32, max_value=128, step=16),
        activation='relu',
        kernel_regularizer=keras.regularizers.l2(hp.Float('l2_layer1', min_value=0.0001, max_value=0.01, sampling='log'))
    ))
    model.add(keras.layers.Dropout(hp.Float('dropout_layer1', min_value=0.2, max_value=0.5, step=0.1)))

    # Segunda capa densa con búsqueda de hiperparámetros
    model.add(keras.layers.Dense(
        units=hp.Int('units_layer2', min_value=16, max_value=64, step=16),
        activation='relu',
        kernel_regularizer=keras.regularizers.l2(hp.Float('l2_layer2', min_value=0.0001, max_value=0.01, sampling='log'))
    ))
    model.add(keras.layers.Dropout(hp.Float('dropout_layer2', min_value=0.2, max_value=0.5, step=0.1)))

    # Capa de salida
    model.add(keras.layers.Dense(num_classes, activation='softmax'))

    # Compilación con optimizador ajustable
    model.compile(
        optimizer=hp.Choice('optimizer', values=['adam', 'rmsprop']),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# Configurar el tuner
tuner = kt.Hyperband(
    build_model,
    objective='val_accuracy',
    max_epochs=50,
    factor=3,
    directory='src/comparative_analysis/models/RedNeuronal/hyperparam_tuning',
    project_name='RedNeuronal'
)

# Realizar búsqueda de hiperparámetros
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

all_reports = []
all_conf_matrices = []

# Realizar la búsqueda de hiperparámetros para cada fold
for fold, (train_index, test_index) in enumerate(skf.split(X, y)):
    X_train, X_val = X.iloc[train_index], X.iloc[test_index]
    y_train, y_val = y.iloc[train_index], y.iloc[test_index]

    X_train_processed = preprocessor.fit_transform(X_train)
    X_val_processed = preprocessor.transform(X_val)
    
    y_train_cat = keras.utils.to_categorical(y_train.cat.codes, num_classes=num_classes)
    y_val_cat = keras.utils.to_categorical(y_val.cat.codes, num_classes=num_classes)

    stop_early = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
    
    tuner.search(
        X_train_processed, y_train_cat,
        validation_data=(X_val_processed, y_val_cat),
        epochs=50,
        callbacks=[stop_early]
    )

    # Obtener los mejores hiperparámetros
    best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

    # Crear y entrenar el modelo con los mejores hiperparámetros
    model = tuner.hypermodel.build(best_hps)
    history = model.fit(
        X_train_processed, y_train_cat,
        validation_data=(X_val_processed, y_val_cat),
        epochs=100,
        batch_size=16,
        callbacks=[stop_early]
    )

    # Evaluar el modelo
    val_loss, val_acc = model.evaluate(X_val_processed, y_val_cat)
    print(f"Fold {fold+1} - Validation Accuracy: {val_acc:.2f}")

    # Predicciones
    y_pred_proba = model.predict(X_val_processed)
    y_pred = np.argmax(y_pred_proba, axis=1)
    y_true = y_val.cat.codes

    report = classification_report(y_true, y_pred)
    conf_mat = confusion_matrix(y_true, y_pred)

    all_reports.append(report)
    all_conf_matrices.append(conf_mat)

# Guardar el mejor modelo y el preprocesador
best_model = tuner.get_best_models(num_models=1)[0]
best_model.save("src/comparative_analysis/models/RedNeuronal/modelo_optimizacion_hiperparametros.keras")
joblib.dump(preprocessor, "src/comparative_analysis/models/RedNeuronal/preprocessor.pkl")