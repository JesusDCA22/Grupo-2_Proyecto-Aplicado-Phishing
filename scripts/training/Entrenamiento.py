#### librerias ####
from tensorflow import keras
from keras.callbacks import ModelCheckpoint, EarlyStopping
import keras_tuner as kt
import pandas as pd

#### Datos ####
# Definición de Matriz de variables explicativas X y variable respuesta y
X = data.drop(['url','status'], axis=1)
y = data['status']

# Partición del conjunto de datos Entrenamiento, Validación y Evaluación
X_train, X_test, y_train, y_test = train_test_split(X_Dummies, y, test_size=0.2, stratify=y, random_state=42)
X_train_final, X_val, y_train_final, y_val = train_test_split( X_train, y_train, test_size=0.15,stratify=y_train, random_state=42)

# Seleccionamos las semillas para efectos de reproducibilidad
np.random.seed(0)
keras.utils.set_random_seed(0)
# Convertir las etiquetas de string a enteros
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train_final)#vuelve los legitimates == 0 y los phishing ==1
y_test_encoded = le.transform(y_test)
y_val_encoded = le.transform(y_val)

# FUNCIÓN CALIFICADA one_hot_labels
def one_hot_labels(y_train_final, y_test,y_val):
    # Ingrese su código aquí
    y_train_ohe = keras.utils.to_categorical(y_train_final, num_classes=2)
    y_test_ohe = keras.utils.to_categorical(y_test, num_classes=2)
    y_val_ohe = keras.utils.to_categorical(y_val, num_classes=2)
    return y_train_ohe, y_test_ohe, y_val_ohe

y_tr_ohe, y_te_ohe,y_val_ohe = one_hot_labels(y_train_encoded, y_test_encoded, y_val_encoded )

# Metricas que vamos a monitorear en todos los modelos
# Callbacks para accuracy
checkpoint_acc = ModelCheckpoint(
    "mejor_modelo_acc.keras", monitor="val_accuracy", mode="max",
    save_best_only=True, verbose=1)
early_stop_acc = EarlyStopping(
    monitor="val_accuracy", mode="max", patience=50, verbose=1)
# Callbacks para recall
checkpoint_recall = ModelCheckpoint(
    "mejor_modelo_recall.keras", monitor="val_recall", mode="max",
    save_best_only=True, verbose=1)
early_stop_recall = EarlyStopping(
    monitor="val_recall", mode="max", patience=50, verbose=1)
# Callbacks para AUC
checkpoint_auc = ModelCheckpoint(
    "mejor_modelo_auc.keras", monitor="val_auc", mode="max",
    save_best_only=True, verbose=1)
early_stop_auc = EarlyStopping(
    monitor="val_auc", mode="max", patience=50, verbose=1)
# Guardar los Callbacks
callbacks = [
    checkpoint_acc, early_stop_acc,
    checkpoint_recall, early_stop_recall,
    checkpoint_auc, early_stop_auc]

#Modelo 1
#Especificación del modelo anterior entrega

model_seq1 = keras.models.Sequential()
model_seq1.add(keras.layers.Dense(units=64, input_shape=(X_train.shape[1],), activation="relu"))
model_seq1.add(keras.layers.Dropout(0.4))
model_seq1.add(keras.layers.Dense(units=2, activation="softmax"))
model_seq1.summary()

model_seq1.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss='categorical_crossentropy',
    metrics=[
        keras.metrics.CategoricalAccuracy(name="accuracy"),
        keras.metrics.AUC(name="auc"),
        keras.metrics.Recall(name="recall")])

# Definimos una función para crear el modelo con los hiperparámetros para optimizar
def build_model(hp):
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(units=hp.Int('units', min_value=32, max_value=512, step=32),
                                 input_shape=(X_train.shape[1],),
                                 activation="relu"))
    model.add(keras.layers.Dropout(rate=hp.Float('dropout', min_value=0.1, max_value=0.5, step=0.1)))
    model.add(keras.layers.Dense(units=2, activation="softmax"))

    # Podemos también optimizar la tasa de aprendizaje
    learning_rate = hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='log')

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='categorical_crossentropy',
        metrics=[
            keras.metrics.CategoricalAccuracy(name="accuracy"),
            keras.metrics.AUC(name="auc"),
            keras.metrics.Recall(name="recall")
        ]
    )
    return model

# Creamos el Keras Tuner
tuner = kt.RandomSearch(
    build_model,
    objective=kt.Objective("val_auc", direction="max"),
    max_trials=1,  # Puedes cambiar esto según la cantidad de pruebas que quieras realizar
    executions_per_trial=2,
    directory='keras_tuner_dir',
    project_name='phishing_detection')

# Iniciamos la búsqueda de hiperparámetros
tuner.search(X_train_final, y_tr_ohe, epochs=5, validation_data=(X_val, y_val_ohe), callbacks=callbacks)

# Guardamos el mejor modelo 
best_model = tuner.get_best_models(num_models=1)[0]

# Salida de optimizacion primer modelo
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
print(best_hps.values)

## Codigo consolidado para los 4 modelos ##
# --------------------------------------------------
# 1. Modelo Seq1 (1 capa oculta con ReLU)
# --------------------------------------------------
def build_model_seq1(hp):
    model = keras.Sequential()
    model.add(layers.Dense(
        units=hp.Int('units', min_value=32, max_value=512, step=32),
        input_shape=(X_train_final.shape[1],),
        activation='relu'
    ))
    model.add(layers.Dropout(
        rate=hp.Float('dropout', min_value=0.1, max_value=0.5, step=0.1)
    ))
    model.add(layers.Dense(2, activation='softmax'))

    lr = hp.Float('lr', min_value=1e-4, max_value=1e-2, sampling='log')

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc'), keras.metrics.Recall(name='recall')]
    )
    return model

# --------------------------------------------------
# 2. Modelo Seq2 (2 capas ocultas con ReLU)
# --------------------------------------------------
def build_model_seq2(hp):
    model = keras.Sequential()
    model.add(layers.Dense(
        units=hp.Int('units_layer1', min_value=32, max_value=512, step=32),
        input_shape=(X_train_final.shape[1],),
        activation='relu'
    ))
    model.add(layers.Dropout(
        rate=hp.Float('dropout1', min_value=0.1, max_value=0.5, step=0.1)
    ))
    model.add(layers.Dense(
        units=hp.Int('units_layer2', min_value=16, max_value=256, step=16),
        activation='relu'
    ))
    model.add(layers.Dropout(
        rate=hp.Float('dropout2', min_value=0.1, max_value=0.4, step=0.1)
    ))
    model.add(layers.Dense(2, activation='softmax'))

    lr = hp.Float('lr', min_value=1e-4, max_value=1e-2, sampling='log')

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc'), keras.metrics.Recall(name='recall')]
    )
    return model

# --------------------------------------------------
# 3. Modelo Seq3 (1 capa oculta con Sigmoid)
# --------------------------------------------------
def build_model_seq3(hp):
    model = keras.Sequential()
    model.add(layers.Dense(
        units=hp.Int('units', min_value=32, max_value=512, step=32),
        input_shape=(X_train_final.shape[1],),
        activation='sigmoid'
    ))
    model.add(layers.Dropout(
        rate=hp.Float('dropout', min_value=0.1, max_value=0.5, step=0.1)
    ))
    model.add(layers.Dense(2, activation='softmax'))

    lr = hp.Float('lr', min_value=1e-4, max_value=1e-2, sampling='log')

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc'), keras.metrics.Recall(name='recall')]
    )
    return model

# --------------------------------------------------
# 4. Modelo Seq4 (2 capas ocultas con Sigmoid)
# --------------------------------------------------
def build_model_seq4(hp):
    model = keras.Sequential()
    model.add(layers.Dense(
        units=hp.Int('units_layer1', min_value=32, max_value=512, step=32),
        input_shape=(X_train_final.shape[1],),
        activation='sigmoid'
    ))
    model.add(layers.Dropout(
        rate=hp.Float('dropout1', min_value=0.1, max_value=0.5, step=0.1)
    ))
    model.add(layers.Dense(
        units=hp.Int('units_layer2', min_value=16, max_value=256, step=16),
        activation='sigmoid'
    ))
    model.add(layers.Dropout(
        rate=hp.Float('dropout2', min_value=0.1, max_value=0.4, step=0.1)
    ))
    model.add(layers.Dense(2, activation='softmax'))

    lr = hp.Float('lr', min_value=1e-4, max_value=1e-2, sampling='log')

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc'), keras.metrics.Recall(name='recall')]
    )
    return model

# --------------------------------------------------
# Configuración común para todos los tuners
# --------------------------------------------------
tuner_config = {
    'objective': kt.Objective("val_auc", direction="max"),
    'max_trials': 10, # 30
    'executions_per_trial': 2,
    'directory': 'keras_tuner_dir',
    'overwrite': True
}

# --------------------------------------------------
# Búsqueda de hiperparámetros para cada modelo
# --------------------------------------------------
def run_tuning(build_fn, project_name):
    tuner = kt.RandomSearch(
        build_fn,
        project_name=project_name,
        **tuner_config
    )

    tuner.search(
        X_train_final,
        #y_train_final_ohe,
        y_tr_ohe,
        epochs=10, # 100
        validation_data=(X_val, y_val_ohe),
        callbacks=[
            keras.callbacks.EarlyStopping(
                monitor='val_auc',
                patience=15,
                mode='max',
                restore_best_weights=True
            )
        ]
    )

    return tuner.get_best_models(num_models=1)[0]

# --------------------------------------------------
# Ejecutar la optimización para los 4 modelos
# --------------------------------------------------
models = {
    'model_seq1': (build_model_seq1, 'phishing_seq1'),
    'model_seq2': (build_model_seq2, 'phishing_seq2'),
    'model_seq3': (build_model_seq3, 'phishing_seq3'),
    'model_seq4': (build_model_seq4, 'phishing_seq4')
}

best_models = {}
for name, (build_fn, project) in models.items():
    print(f"\n⚡ Optimizando {name}...")
    best_models[name] = run_tuning(build_fn, project)
    print(f"✅ {name} optimizado!")

