# Definición de los datos

## Origen de los datos

- **Fuente principal**:  
  Dataset "Web page phishing detection" de Hannousse & Yahiouche (2021) publicado en Mendeley Data (V3)  
  DOI: [10.17632/c2gw7fy2j4.3](https://data.mendeley.com/datasets/c2gw7fy2j4/3)  
  Disponible también en Kaggle: [Web page Phishing Detection Dataset](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)

- **Método de obtención**:  
  Descarga directa del archivo CSV desde Kaggle/Mendeley  
  Dataset original contiene 11,430 registros con 87 características + variable objetivo

## Especificación de los scripts para la carga de datos

### Script principal (Python)
```python
import pandas as pd

# Carga desde archivo CSV
data = pd.read_csv('phishing_dataset.csv')

# Validación básica
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
print(f"Distribución de clases:\n{df['status'].value_counts()}")
```

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

**Ubicación original**:
- Kaggle: `/kaggle/input/web-page-phishing-detection-dataset/dataset_phishing.csv`
- Mendeley: `Data Files/dataset_phishing.csv`

**Estructura de archivos origen**:
- Formato: CSV (delimitado por comas)
- Tamaño: ~4.5 MB
- Campos: 87 features + 1 target (status)
- Codificación: UTF-8
- Header: Sí (nombres de columnas en primera fila)

**Transformación y limpieza**:
1. Eliminación de URLs duplicadas
2. Conversión de variables categóricas a numéricas
3. Manejo de valores missing (-1 → NA)
4. Normalización de rangos numéricos
5. Balanceo de clases (ya viene balanceado 50-50)
6. Eliminación de variables constantes para toda url o sin información

### Base de datos de destino

**Base de destino**:
- Nombre: `data`
- Motor: MySQL 8.0
- Tabla principal: `phishing_dataset`

**Estructura destino**:
```sql
CREATE TABLE data (
  id SERIAL PRIMARY KEY,
  url TEXT NOT NULL,
  length_url INT,
  ip BOOLEAN,
  nb_dots INT,
  -- ... (todas las 87 características)
  status VARCHAR(10) CHECK (status IN ('phishing', 'legitimate')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  source VARCHAR(20) DEFAULT 'kaggle'
);
```

### Procedimiento de carga:

1) Carga incremental via Python
2) Validación de tipos de datos
3) Indices en campos clave (url, status)
4) Backup diario en S3/Azure Blob Storage
5) Documentación con Data Dictionary
