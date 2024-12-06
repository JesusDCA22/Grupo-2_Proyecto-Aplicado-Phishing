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
  - `details` y `characteristics` presentan un 5% de valores faltantes.
- **Duplicados**: No se encontraron registros duplicados en la columna `id`.
- **Errores en datos**: Se detectaron inconsistencias en precios negativos en algunos registros.
- **Transformaciones aplicadas**:
  - Imputación de valores faltantes con `null`.
  - Filtrado de valores extremos en los precios.
- **Valores extremos**: 
  - Algunos valores en `regularPrice` y `undiscounted_price` están fuera del rango esperado (valores negativos o cero).

### Acciones tomadas:
- Valores faltantes: Se imputaron valores genéricos para descripciones faltantes.
- Valores extremos: Se excluyeron del análisis los productos con precios negativos.

## Variable objetivo

Este proyecto no define explícitamente una variable objetivo. Sin embargo, las similitudes semánticas basadas en `details` y `characteristics` serán la base para construir el modelo de recomendación.

## Variables individuales


- **`category`**:
  - Mayor proporción de productos para mujeres (60%).
  - Segmento `Running` común en todas las tiendas.

## Ranking de variables

En base al análisis preliminar, las variables más influyentes para el análisis comparativo son:

1. `characteristics` - Detalles técnicos del producto.
2. `details` - Información estructurada y semiestructurada del producto.
3. `category` - Segmentación de productos según género y propósito.

## Análisis exploratorio

### Variables categóricas más relevantes
- **Categorías más frecuentes en `store`**:
  - Adidas: 40%.
  - Nike: 35%.
  - Nation Runner: 25%.
  
### Distribución de precios
- **`regularPrice`**:
  - Rango: $150,000 - $600,000 COP.
  - Promedio: $380,000 COP.

### Relación entre `category` y `regularPrice`
- Se explorarán las relaciones entre variables como `category` y `regularPrice` para identificar patrones relevantes en las recomendaciones. Los embeddings se construirán utilizando modelos LLM para capturar similitudes contextuales.
- Los productos en la categoría `Mujer • Running` tienden a estar en el rango superior de precios.

## Visualizaciones
1. **Distribución de precios**:
   - Histograma mostrando la densidad de precios.
2. **Análisis de categorías**:
   - Gráfico de barras con la proporción de productos por tienda.
3. **Mapa de calor de correlaciones**:
   - Muestra una correlación moderada entre `undiscounted_price` y `regularPrice`.

## Conclusiones
- Las categorías y características técnicas (`details` y `characteristics`) son clave para el análisis comparativo.
- Es necesario continuar depurando valores faltantes y normalizando precios para futuros análisis.