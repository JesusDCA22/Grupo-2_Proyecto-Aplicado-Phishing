# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline, el cual consiste en una primera aproximación al clustering de productos. El objetivo es sentar las bases para modelos posteriores y guiar el proceso de mejora continua.

## Descripción del modelo

El modelo baseline se enfocó en realizar un proceso de clustering sobre un conjunto de productos obtenidos desde un endpoint con productos de Adidas. El flujo del proyecto incluye:

1. **Obtención de datos**: Se obtienen productos desde un endpoint (Adidas).
2. **Normalización de datos con un LLM**: Un modelo de lenguaje (LLM) se utiliza para normalizar y etiquetar las características de los productos.
3. **Clustering**: Utilizando las variables numéricas ya procesadas, se aplicó un algoritmo de clustering (ej. K-Means) para agrupar productos similares.

Este pipeline busca identificar patrones, similitudes y diferencias entre los productos de la marca.

Además de los modelos de clustering utilizados para agrupar los productos de Adidas, se realizó un entrenamiento de red neuronal con el objetivo de asignar los productos de **Decathlon** a los clusters previamente establecidos. Para ello, se utilizó el modelo de **k-means** al final del proceso, con la finalidad de poder comparar ambos conjuntos de productos.

Es importante aclarar que esta modificación fue necesaria porque, al aplicar el modelo de k-means original (que agrupa los productos de Adidas), los productos de Decathlon terminaban agrupándose todos en un mismo cluster debido a diferencias en la forma de los productos y otros factores. Esto no resultaba útil para encontrar productos similares entre Decathlon y su competencia, Adidas. Por esta razón, se entrenó una **red neuronal**, la cual, en las pruebas realizadas, logró distribuir mejor los productos de Decathlon en los clusters ya definidos para Adidas.

## Variables de entrada

Las variables de entrada utilizadas en el modelo son aquellas extraídas y normalizadas a partir del procesamiento con el LLM. Entre las principales variables se encuentran:

- **Weight** (Peso del producto, en gramos)
- **Drop (heel-to-toe differential)** (Diferencial de altura entre talón y punta, en mm)
- **regularPrice** (Precio regular del producto, en valor numérico flotante)
- **undiscounted_price** (Precio sin descuento, en valor numérico flotante)
- Otras variables numéricas o categóricas codificadas (por ejemplo, materiales del upper, midsole, outsole convertidas en variables dummies)

Los IDs de los productos se han mantenido para identificar a qué cluster pertenece cada uno, pero no se utilizaron para el embedding.

## Variable objetivo

No existe una variable objetivo propiamente dicha, ya que el enfoque es no supervisado. El objetivo es descubrir grupos (clusters) de productos similares.

## Evaluación del modelo

### Métricas de evaluación

Se han utilizado métricas de evaluación típicas para modelos de clustering no supervisados:

- **Silhouette Score**: Mide la separación y cohesión de los clusters. Un valor cercano a 1 indica que las muestras están bien agrupadas, un valor cercano a -1 indica lo contrario.
- **Davies-Bouldin Score**: Mide la calidad del clustering en función de las distancias entre clusters. Valores más bajos indican mejores separaciones entre clusters.

### Resultados de evaluación

**Distribución de productos por cluster:**

| Cluster | Conteo | Porcentaje |
|---------|---------|------------|
| 0       | 2       | 0.44%      |
| 1       | 3       | 0.66%      |
| 2       | 22      | 4.85%      |
| 3       | 64      | 14.10%     |
| 4       | 93      | 20.48%     |
| 5       | 268     | 59.03%     |
| 6       | 1       | 0.22%      |
| 7       | 1       | 0.22%      |

**Métricas globales:**

- Silhouette Score: -0.10727046484513526  
- Davies-Bouldin Score: 3.820317442353896

## Análisis de los resultados

El Silhouette Score negativo (-0.1072) sugiere que la mayoría de los productos no están bien asignados a sus clusters o que los clusters se solapan significativamente. Esto indica que el agrupamiento no capta adecuadamente las similitudes reales entre los productos.

El Davies-Bouldin Score (3.8203) es relativamente alto, lo que también indica que los clusters no están bien definidos, presentando una baja separación entre ellos.

La distribución de productos por cluster está muy desbalanceada. Un solo cluster (el número 5) contiene alrededor del 59% de los productos, mientras que otros clusters contienen muy pocos elementos, incluso uno solo. Esto sugiere que la configuración actual de k (el número de clusters) o la forma en que se están representando los datos no es la más adecuada.

### Fortalezas

- **Primer paso hacia la segmentación:** Establece una línea base desde la cual se pueden proponer mejoras.
- **Proceso reproducible:** El pipeline desde la extracción de datos, normalización con LLM y clustering está bien definido y puede repetirse con ajustes futuros.

### Debilidades

- **Baja calidad de agrupamiento:** Las métricas indican que los clusters no reflejan adecuadamente las similitudes entre productos.
- **Desbalance en los clusters:** Un cluster concentra la mayor parte de los productos, lo que dificulta interpretaciones útiles.
- **Falencia en el embedding actual:** Es posible que la selección de variables o su codificación no capture suficientemente las diferencias relevantes entre los productos.

### Áreas de mejora

- **Refinamiento de la representación de datos:** Incluir embeddings más representativos (por ejemplo, usando técnicas de NLP más avanzadas en descripciones, o embeddings más sofisticados en variables categóricas).
- **Ajuste del número de clusters:** Probar diferentes valores de k con el método del codo o métricas de validación más robustas.
- **Selección de características:** Evaluar qué variables realmente aportan información útil para segmentar los productos y eliminar aquellas que introduzcan ruido.
- **Experimentar con diferentes algoritmos de clustering:** Además de K-Means, probar DBSCAN o HDBSCAN para detectar estructuras no esféricas.

## Conclusiones

El modelo baseline de clustering no ofrece una segmentación claramente útil, según las métricas de validación. Sin embargo, resulta valioso como punto de partida para comprender el problema y orientar mejoras. Ajustes en la selección de variables, técnicas de embedding y el número de clusters, así como la experimentación con otros algoritmos de clustering, podrían mejorar significativamente los resultados.

## Referencias

- Documentation of scikit-learn for Clustering: [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)
- Introducción a la Evaluación del Clustering (Silhouette Score, Davies-Bouldin): [https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
- Documentación de K-Means: [https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
