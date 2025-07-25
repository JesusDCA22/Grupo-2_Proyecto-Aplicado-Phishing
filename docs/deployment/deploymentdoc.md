# Despliegue de modelos

## Infraestructura

* **Nombre del modelo:** Proyecto Sistema de Detección de Phishing para Protección Financiera en Colombia
* **Plataforma de despliegue:** Servidor local con una API REST.
    * **Framework de la API:** Flask / FastAPI
    * **Servidor WSGI:** Gunicorn (para entornos tipo Linux) o Waitress (para entornos Windows).
    * **Sistema Operativo del Servidor:** Ubuntu Server 22.04 LTS / Windows Server 2022.
* **Requisitos técnicos:**
    * **Software:**
        * Python 3.8+
        * TensorFlow 2.x
        * Pandas
        * Scikit-learn
        * Flask o FastAPI
        * Gunicorn o Waitress
        * MySQL Connector for Python
    * **Hardware (mínimo recomendado):**
        * **CPU:** 4 núcleos
        * **RAM:** 8 GB
        * **Almacenamiento:** 50 GB de espacio en disco para el entorno, logs y la base de datos.

* **Requisitos de Seguridad:**
    * **Autenticación:** El acceso a la API del modelo debe estar protegido mediante una **API Key** que las aplicaciones cliente deberán incluir en las cabeceras de sus peticiones.
    * **Encriptación de datos:**
        * **En tránsito:** Si la API se expone a través de una red, se debe configurar un proxy inverso (como Nginx) para habilitar **TLS/SSL** y asegurar la comunicación vía HTTPS.
        * **En reposo:** Las credenciales de acceso a la base de datos MySQL deben almacenarse de forma segura (e.g., variables de entorno) y no directamente en el código.
    * **Validación de entradas:** La API debe validar y sanear todas las URLs de entrada para prevenir ataques de inyección o el procesamiento de datos malformados.
    * **Control de acceso a la red:** Configurar un **firewall** en el servidor para permitir únicamente el tráfico entrante en el puerto de la API (e.g., 80/443) desde direcciones IP autorizadas.
    * **Logging y Monitoreo:** Registrar todas las peticiones y predicciones en la base de datos MySQL para auditoría y para detectar patrones de uso anómalos.

* **Arquitectura del Modelo:**
El modelo se define en Keras de la siguiente manera

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

model = Sequential([
    Dense(64, activation='relu', input_shape=(85,)),
    Dropout(0.4),
    Dense(2, activation='softmax')
])

model.compile(
    optimizer=Adam(learning_rate=0.0047),
    loss='categorical_crossentropy',
    metrics=['accuracy', 'AUC', 'Recall']
)
```
* **Diagrama de Arquitectura:**
A continuación se presenta un diagrama textual que ilustra el flujo de una solicitud de predicción de phishing en la infraestructura local.

```text
                +-----------------------------+
                |   Cliente / Aplicación      |
                +-----------------------------+
                              |
          1. Petición HTTPS   |   8. Respuesta
              con URL         v
+-------------------------------------------------------------+
|                     SERVIDOR LOCAL                          |
|                                                             |
|           +---------------------------------+               |
|           |   Proxy Inverso (e.g., Nginx)   |               |
|           +---------------------------------+               |
|                        |                                    |
|       2. Petición      |      7. Respuesta                  |
|          interna       v                                    |
|                                                             |
| +---------------------------------------------------------+ |
| |                    API DE PREDICCIÓN                    | |
| |             (Servidor Flask / Gunicorn)                 | |
| |                                                         | |
| |   +----------------------+   +-----------------------+  | |
| |   | Módulo de            |   | Modelo TF/Keras       |  | |
| |   | Preprocesamiento     |-->| (Cargado en memoria)  |  | |
| |   | (Extrae features)    |<--| (Realiza predicción)  |  | |
| |   +----------------------+   +-----------------------+  | |
| |              |                                          | |
| |              | 6. Registrar petición y resultado        | |
| |              v                                          | |
| |   +----------------------+                              | |
| |   | Base de Datos        |                              | |
| |   | (MySQL)              |                              | |
| |   +----------------------+                              | |
| |                                                         | |
| +---------------------------------------------------------+ |
+-------------------------------------------------------------+
```
## Código de despliegue

* **Archivo principal:** Despliegue_MLFlow_Phishing.py
* **Rutas de acceso a los archivos:** 
    * **Despliegue_MLFlow_Phishing.py:** script donde se ejecuta el código que configura la URI de MLflow
    * **models:/airline_delay/1** Como MLflow accede al modelo desde Model Registry (Se debe actualizar si el nombre del modelo o la vrsion cambian)
* **Variable de entorno:**
     * **URI para MLflow:** URL del servidor de MLflow que se está usando para registrar y servir modelos.
 ```bash
  export MLFLOW_TRACKING_URI=http://localhost:5000
```

## Documentación del despliegue

* **Instrucciones de instalación:** 
     *  Clonar el repositorio del proyecto en la máquina donde se realizará el despliegue, asegurándose de tener Python y MLflow instalados:
  ```bash
      git clone <URL_DEL_REPOSITORIO>
      cd <NOMBRE_DEL_PROYECTO>
      pip install -r requirements.txt
   ``` 
  Esto garantiza que tengas todos los archivos del proyecto y las dependencias necesarias para ejecutar el modelo.
  
* **Instrucciones de configuración:**
   * Definir las variables de entorno necesarias antes de iniciar el servidor:
  
     ```bash
         export MLFLOW_TRACKING_URI=http://localhost:5000
      ```
     
  Con lo que se configura la dirección del servidor de MLflow donde se encuentra el modelo registrado. (En este caso el servidor MLflow está corriendo localmente en el puerto 5000, pero se puede cambiar con una IP o dominio si es un servidor remoto)

* **Instrucciones de uso:** 
   * Lanzar el servidor REST del modelo con el siguiente comando:
   ```bash
         mlflow models serve -m 'models:/airline_delay/1' -p 8001 --env-manager 'local' &
   ``` 
Esto inicia un servicio en el puerto 8001, sirviendo la versión 1 del modelo airline_delay desde el Model Registry de MLflow.
El parámetro --env-manager 'local' permite usar el entorno de Python actual sin necesidad de contenedores o entornos adicionales.
   * Para enviar datos de prueba al modelo y obtener una predicción desde un cliente, puedes usar Python:
  ```python
      import requests

data_request = features_test[:2].tolist()
r = requests.post("http://localhost:8001/invocations", json={"inputs": data_request})
print(r.text)

   ```
Esto envía los datos como JSON al servidor y retorna la respuesta del modelo.

* **Instrucciones de mantenimiento:**
     * Para verificar si el modelo sigue corriendo correctamente:
       ```bash
       ps aux | grep mlflow
        ``` 
       
     * Para detener el servicio si es necesario:
        ```bash
        pkill -f "mlflow models serve"
         ```
       
     * Para actualizar el modelo a una nueva versión (por ejemplo, versión 2):   
         ```bash
            pkill -f "mlflow models serve"
            mlflow models serve -m 'models:/airline_delay/2' -p 8001 --env-manager 'local' &
         ```

   *  Para revisar posibles errores durante la ejecución:
      ```bash
         tail -f mlflow.log
      ```  
