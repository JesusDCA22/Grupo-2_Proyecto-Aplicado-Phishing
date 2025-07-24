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

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
