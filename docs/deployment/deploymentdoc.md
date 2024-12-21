# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Clasificador de productos
- **Plataforma de despliegue:** AWS
- **Requisitos técnicos:** 
Librerías: torch, fairscale, fire, blobfile, pandas, requests, openpyxl, httpx, boto3, scikit-learn, matplotlib, flask (requirements.txt)
LLMs: AWS Bedrock o Llama 3.1, modelo de 70B de parámetros
Databricks: Ambiente conectado a Glue Storage

- **Requisitos de seguridad:** En este momento la base de datos en firebase no requiere autenticación, pero se implementará en un futuro cercano.
- **Diagrama de arquitectura:**
  
![arquitectura (1)](https://github.com/user-attachments/assets/4565491e-0dc2-4345-948c-c88167d42f16)

Arquitectura

## Código de despliegue

- **Archivo principal:** src/main.py
- **Rutas de acceso a los archivos:** https://scraping-firestore-178159629911.us-central1.run.app//v1/scraping/
- **Variables de entorno:**

En el despliegue en databricks se solicita:
ACCESS_TOKEN: Token de acceso generado por databricks
USERNAME: Usuario corporativo


## Documentación del despliegue

**Flujo de datos**
![dataflow](https://github.com/user-attachments/assets/2f14053b-4d55-4ca5-8afd-05d1321add3a)

Flujo de datos

### **Instrucciones de instalación**
Para iniciar un ambiente virtual e instalar las dependencias necesarias para la aplicación, sigue los siguientes pasos:

1. Asegúrate de tener Python 3.7 o superior instalado.
2. Crea un ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el ambiente virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias listadas en el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### **Instrucciones de configuración**
Para configurar el modelo en la plataforma de despliegue:

1. Asegúrate de que los modelos entrenados estén ubicados en:
   - `src\comparative_analysis\models\K-MeansV1\`

2. Verifica que el archivo Excel requerido para la base de datos se encuentre en:
   - `src/comparative_analysis/database/Adidas_etiquetado.xlsx`

3. Configura el puerto de ejecución predeterminado (2626) si es necesario modificarlo, ajustando el archivo `main.py`.

### **Instrucciones de uso**

#### **Manual Técnico: Endpoints de la API REST**

**Aplicación desarrollada en Flask.**

1. **Endpoints disponibles:**

   - **GET /api/test**
     - Descripción: Este endpoint es una prueba básica para verificar el funcionamiento del servidor.
     - Respuesta esperada (200):
       ```
       {
           "message": "¡Hola! Esta es una respuesta GET de prueba.",
           "status": "success"
       }
       ```

   - **GET /api/product**
     - Descripción: Permite obtener la información de un producto a partir de su ID.
     - Parámetros:
       - `id` (obligatorio): ID del producto a buscar.
     - Ejemplo de solicitud:
       ```
       GET http://127.0.0.1:2626/api/product?id=08sjncACSjSvg2t9DS73
       ```
     - Respuesta esperada (200):
       ```
       {
           "Additional_Technologies": "ENERGYRODS 2.0, Waterproofing, Recyclable material",
           "Available_Sizes": NaN,
           "Cushioning_System": "Lightstrike Pro",
           "Drop__heel-to-toe_differential_": "6 mm",
           "Gender": "Woman",
           "Midsole_Material": NaN,
           "Outsole": "Textile rubber",
           "Pronation_Type": NaN,
           "Upper_Material": "Synthetic",
           "Usage_Type": "Racing",
           "Weight": "183 g",
           "Width": NaN,
           "category": "Mujer • Running",
           "characteristics": NaN,
           "description": "Los Adizero Adios Pro 3 son la máxima expresión de los productos Adidas...",
           "id": "08sjncACSjSvg2t9DS73",
           ...
       }
       ```
     - Errores posibles:
       - 400: Si no se proporciona el ID del producto.
       - 404: Si el producto no se encuentra.

   - **POST /api/products**
     - Descripción: Busca productos que coincidan con los parámetros proporcionados.
     - Cuerpo de la solicitud:
       ```
       {
           "key1": "value1",
           "key2": "value2",
           ...
       }
       ```
     - Ejemplo de solicitud:
       ```
       POST http://127.0.0.1:2626/api/products
       {
           "category": "Mujer • Running",
           "Cushioning_System": "Lightstrike Pro"
       }
       ```
     - Respuesta esperada (200):
       ```
       [
           {
               "id": "08sjncACSjSvg2t9DS73",
               "category": "Mujer • Running",
               ...
           },
           ...
       ]
       ```
     - Errores posibles:
       - 400: Si no se proporcionan parámetros.
       - 404: Si no se encuentran productos que coincidan con los parámetros.

   - **POST /predict/KMeansV1**
     - Descripción: Realiza una predicción utilizando un modelo K-Means para asignar un producto a un cluster y devuelve productos similares en el mismo cluster.
     - Cuerpo de la solicitud:
       ```
       {
           "key1": "value1",
           "key2": "value2",
           ...
       }
       ```
     - Ejemplo de solicitud:
       ```
       POST http://127.0.0.1:2626/predict/KMeansV1
       {
           "category": "Mujer • Running",
           "Cushioning_System": "Lightstrike Pro",
           ...
       }
       ```
     - Respuesta esperada (200):
       ```
       [
           {
               "id": "08sjncACSjSvg2t9DS73",
               "category": "Mujer • Running",
               ...
           },
           ...
       ]
       ```
     - Errores posibles:
       - 400: Si no se envían datos para la predicción.
       - 500: Si ocurre un error interno.
   - **GET /api/similarProducts**
     - Descripción: Permite obtener un diccionario de productos pertenecientes a un mismo Cluster.
     - Parámetros:
       - `Cluster` (obligatorio): Cluster del producto para el cual se buscarán productos similares.
     - Ejemplo de solicitud:
       ```
       GET http://127.0.0.1:2626/api/similarProducts?cluster=9
       ```
     - Respuesta esperada (200):
       ```json
        {
            "id": "09skdjf20sldkj32sd",
            "category": "Mujer • Running",
            "description": "Producto similar al Adizero Adios Pro 3...",
        },
        {
            "id": "09adsfkdjfasdfdkasdfassd",
            "category": "Hombre • Running",
            "description": "Producto similar al Adizero Adios Pro 3..."
        }
       ```
     - Errores posibles:
       - 400: Si no se proporciona el Cluster del producto.
       - 404: Si no se encuentran productos.

   - **POST /predict**
     - Descripción: Realiza una predicción basada en características proporcionadas y asigna un numero de cluster al nuevo producto.
     - Cuerpo de la solicitud:
       ```json
       {
           "key1": "value1",
           "key2": "value2",
           ...
       }
       ```
     - Ejemplo de solicitud:
       ```
       POST http://127.0.0.1:2626/predict
       {
           "category": "Mujer • Running",
           "Cushioning_System": "Lightstrike Pro",
           ...
       }
       ```
     - Respuesta esperada (200):
        ```json
        {
          "prediction": 9
        }
        ```
     - Errores posibles:
       - 400: Si no se proporcionan datos para la predicción.
       - 500: Si ocurre un error interno.


2. **Notas técnicas:**
   - La API utiliza pandas para manipular datos en formato Excel y pickle para cargar los modelos entrenados.
   - Todos los modelos (encoder, scaler y KMeans) deben estar en la ruta `src\comparative_analysis\models\K-MeansV1\`.
   - El archivo Excel utilizado debe estar en `src/comparative_analysis/database/Adidas_etiquetado.xlsx`.
   - El puerto de ejecución por defecto es el 2626.

3. **Requerimientos:**
   - Python 3.7 o superior.
   - Flask.
   - Pandas.
   - Re.
   - Pickle.

4. **Cómo iniciar la aplicación:**
   Ejecuta el archivo `main.py`:
   ```
   python main.py
   ```

### **Instrucciones de mantenimiento**
1. **Actualización del modelo:**
   - Sustituye los archivos del modelo en la ruta `src\comparative_analysis\models\K-MeansV1\` con las versiones actualizadas.
   - Reinicia el servidor para cargar los nuevos modelos.

2. **Actualización de la base de datos:**
   - Sustituye el archivo `Adidas_etiquetado.xlsx` en la ruta `src/comparative_analysis/database/`.
   - Asegúrate de que el formato del archivo sea compatible con las funciones existentes.

3. **Monitoreo del servidor:**
   - Verifica los logs para identificar errores o problemas de rendimiento.
   - Asegúrate de que el puerto de ejecución (2626) esté disponible y no haya conflictos.

4. **Resolución de errores:**
   - Consulta los mensajes de error en el log para diagnosticar problemas.
   - Realiza pruebas con los endpoints usando herramientas como Postman o cURL para verificar su correcto funcionamiento.

