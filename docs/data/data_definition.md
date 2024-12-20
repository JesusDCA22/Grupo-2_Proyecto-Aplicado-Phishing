# Definición de los datos

## Origen de los datos

Los datos se extrajeron mediante web scraping de las siguientes fuentes:

- **Adidas**: [https://www.adidas.co/](https://www.adidas.co/)
- **Nike**: [https://www.nike.com.co/](https://www.nike.com.co/)
- **Nation Runner**: [https://nacionrunner.com/](https://nacionrunner.com/)

Posteriormente, los datos fueron almacenados en una API conectada a Firebase para su gestión y análisis posterior. Las descripciones de productos y características técnicas se estructuraron en un formato JSON para facilitar su manipulación.

## Especificación de los scripts para la carga de datos

- **Script principal**: `api_reader.py` - Este script realiza las siguientes tareas:
  - Se conecta a la API para obtener datos JSON.
  - Almacena los datos en un archivo Excel local para su análisis.
  - Incluye mecanismos para manejo de errores en caso de fallos en la conexión o almacenamiento.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- **Ubicación de los archivos de origen**: Los datos se encuentran disponibles en Firebase, accesibles mediante una API interna desarrollada para consulta y análisis.
- **Estructura de los datos de origen**:
  - Base de datos no relacional con documentos organizados por producto y tienda.
  - Formato JSON, donde cada registro corresponde a un producto, con campos específicos como `id`, `details`, `category`, entre otros.
  -   - Cada documento contiene las variables descritas en el diccionario de datos.
- **Procedimientos de transformación y limpieza**: 
  - Conversión de datos monetarios a un formato uniforme.
  - Limpieza de caracteres especiales y espacios redundantes en los campos de texto. (usando expresiones regulares).
  - Normalización de nombres en `store` y `manufacturer` para evitar inconsistencias.

### Base de datos de destino

- **Ubicación**: Los datos limpios se almacenan en un archivo Excel o en un DataFrame de Pandas.
- **Estructura**:
  - Formato tabular con columnas correspondientes a las variables del diccionario de datos.
- **Procedimientos de carga y transformación**:
  - Detección y eliminación de duplicados.
  - Inclusión de campos adicionales, como la fecha de extracción `createdAt`.