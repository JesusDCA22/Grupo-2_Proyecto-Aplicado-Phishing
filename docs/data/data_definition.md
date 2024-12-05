# Definición de los datos

## Origen de los datos

Los datos se extrajeron mediante web scraping de las siguientes fuentes:

- **Adidas**: [https://www.adidas.co/](https://www.adidas.co/)
- **Nike**: [https://www.nike.com.co/](https://www.nike.com.co/)
- **Nation Runner**: [https://nacionrunner.com/](https://nacionrunner.com/)

Posteriormente, los datos fueron almacenados en una API conectada a Firebase para su gestión.

## Especificación de los scripts para la carga de datos

- **Script principal**: `api_reader.py` - utilizado para conectarse a la API, extraer los datos y almacenarlos localmente en un formato estructurado para su análisis.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- **Ubicación de los archivos de origen**: Los datos se encuentran disponibles en Firebase, accedidos a través de una API interna desarrollada para este propósito.
- **Estructura de los datos de origen**: Los datos están organizados en registros JSON, con claves para las variables mencionadas en el diccionario de datos.
- **Procedimientos de transformación y limpieza**: 
  - Conversión de valores monetarios a un formato uniforme.
  - Eliminación de caracteres especiales y espacios redundantes en los campos de texto.
  - Normalización de las categorías y fabricantes para evitar duplicados.

### Base de datos de destino

- **Ubicación**: Firebase, utilizando la API desarrollada para consulta y análisis.
- **Estructura**: 
  - Base de datos no relacional con documentos organizados por producto y tienda.
  - Cada documento contiene las variables descritas en el diccionario de datos.
- **Procedimientos de carga y transformación**: 
  - Validación de datos para evitar duplicados.
  - Inclusión de campos adicionales como `createdAt` para registrar la fecha de extracción.