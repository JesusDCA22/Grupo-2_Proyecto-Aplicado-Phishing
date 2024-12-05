# Reporte de Datos

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
  - Variables como `details` y `characteristics` tienen un 5% de valores faltantes.
- **Duplicados**: 
  - No se encontraron duplicados en la variable `id`.
- **Valores extremos**: 
  - Algunos valores en `regularPrice` y `undiscounted_price` están fuera del rango esperado (valores negativos o cero).

### Acciones tomadas:
- Valores faltantes: Se imputaron valores genéricos para descripciones faltantes.
- Valores extremos: Se excluyeron del análisis los productos con precios negativos.

## Variable objetivo

Este proyecto no define explícitamente una variable objetivo. Sin embargo, las similitudes semánticas basadas en `details` y `characteristics` serán la base para construir el modelo de recomendación.

## Variables individuales

- **`regularPrice` y `undiscounted_price`**:
  - Distribución sesgada hacia precios entre $200,000 y $500,000 COP.
  - Promedio de descuento aplicado: 30%.

- **`category`**:
  - Mayor proporción de productos para mujeres (60%).
  - Segmento `Running` común en todas las tiendas.

## Ranking de variables

En base al análisis preliminar, las variables más influyentes para el análisis comparativo son:

1. `characteristics` - Detalles técnicos del producto.
2. `details` - Información estructurada y semiestructurada del producto.
3. `category` - Segmentación de productos según género y propósito.

## Relación entre variables explicativas y variable objetivo

Se explorarán las relaciones entre variables como `category` y `regularPrice` para identificar patrones relevantes en las recomendaciones. Los embeddings se construirán utilizando modelos LLM para capturar similitudes contextuales.