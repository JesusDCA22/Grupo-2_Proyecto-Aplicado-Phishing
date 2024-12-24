# Resumen de Datos

## Resumen general de los datos

El dataset incluye productos obtenidos de tres tiendas en línea: Adidas, Nike y Nation Runner. A continuación, se presenta un resumen:

- **Número total de observaciones**: 10,000 registros (aproximado).  
- **Número total de variables**: 12.  
- **Tipos de variables**:  
  - 10 variables categóricas (string).  
  - 1 variable numérica (precios, almacenados como string).  
  - 1 variable temporal (datetime).  

## Resumen de calidad de los datos

- **Valores faltantes**:  
  - Variables críticas como `id`, `title` y `url` no presentan valores nulos.  
  - `gender`, `category`, `undiscounted_price` y `characteristics` presentan un porcentaje alto de valores faltantes y no hay mas columnas con valores faltantes.  
- **Duplicados**: No se encontraron registros duplicados.  

### Acciones tomadas

- **Valores faltantes**: Se planea imputar valores genéricos como "unisex" para descripciones faltantes en columnas como "genero" pero se necesita hacer una revision exahustiva para decidir esto.  

## Variable objetivo

Este proyecto no define explícitamente una variable objetivo. Sin embargo, las similitudes semánticas basadas en `details` y `characteristics` serán la base para construir el modelo de recomendación.  

## Variables individuales

- **`category`**:  
  - Mayor proporción de productos para mujeres (60%).  
  - El segmento `Running` es común en todas las tiendas.  

## Ranking de variables

En base al análisis preliminar, las variables más influyentes para el análisis comparativo son:  

1. `characteristics` - Detalles técnicos del producto.  
2. `details` - Información estructurada y semiestructurada del producto.  
3. `category` - Segmentación de productos según género y propósito.  
4. `regularPrice` - Precio del producto sin descuento.  
5. `undiscounted_price` - Precio del producto después de aplicar descuento (si aplica).  
6. `store` - Tienda que vende el producto.  
7. `manufacturer` - Empresa/Marca del producto.  
8. `gender` - Género del público objetivo del producto.  

## Análisis exploratorio

### Variables categóricas más relevantes

- **Categorías más frecuentes en `store`**:  
  - Adidas: 59%.  
  - Nike: 30%.  
  - Nation Runner: 11%.  

![Distribución de "store"][def3]

- **Categorías más frecuentes en `manufacturer`**:  

![Distribución de "manufacturer"][def]

- **Categorías más frecuentes en `gender`**:  

![Distribución de "gender"][def2]

### Relación entre `category` y `regularPrice`

- Se explorarán las relaciones entre variables como `category` y `regularPrice` para identificar patrones relevantes en las recomendaciones. Los embeddings se construirán utilizando modelos LLM para capturar similitudes contextuales.  

## Visualizaciones

1. **Análisis de categorías**:  
   - Gráficos de barras con la proporción de distintas características de los datos.  

## Conclusiones

- Las categorías y características técnicas (`details` y `characteristics`) son clave para el análisis comparativo.  
- Es necesario normalizar distintos valores, como los precios, para futuros análisis.  


[def]: ../../scripts\eda\edaImages\manufacturerDistribution.png
[def2]: ../../scripts\eda\edaImages\genderDistribution.png
[def3]: ../../scripts/eda/edaImages/storeDistribution.png