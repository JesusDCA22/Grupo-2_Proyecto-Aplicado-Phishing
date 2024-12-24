# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final se construyó con el objetivo de agrupar productos de Adidas con características similares, partiendo de datos obtenidos desde un endpoint, luego normalizados y etiquetados mediante un LLM. Para lograr esto, se aplicó un método de clustering (K-Means) a las variables numéricas y categóricas transformadas.

En términos de métricas de evaluación, el **Silhouette Score** alcanzó un valor de **-0.10726032825390042**, mientras que el **Davies-Bouldin Score** fue de **3.7837546892816856**. Estas métricas indican que el clustering no logró una segmentación claramente separada ni cohesiva. Sin embargo, estos resultados proporcionan una línea base para mejoras futuras.

Con el fin de realizar la comparación de diferentes modelos de clustering, se utiliza la libreria Clusteval con el fin de comparar los siguientes algoritmos de clustering:

* **KMeans**
* **Agglomeratrive**
* **DBScan**
* **HDBScan**

## Descripción del Problema

La problemática abordada consiste en organizar y segmentar una amplia gama de productos Adidas en grupos homogéneos, con el fin de facilitar análisis comparativos. El objetivo es identificar patrones ocultos en las características de los productos, tales como peso, materiales, precios y tecnologías implementadas. Este tipo de segmentación es útil para la toma de decisiones estratégicas, el análisis de competitividad y el desarrollo de nuevas líneas de productos orientadas a grupos específicos de mercado.

Justificación: La agrupación no supervisada de productos permite a la empresa comprender mejor sus catálogos, detectar nichos y mejorar la experiencia del cliente recomendando artículos similares. Además, sienta las bases para análisis más profundos, tales como análisis de correlación con el rendimiento de ventas o el perfil de cliente.

## Descripción del Modelo

El modelo final se basa en el siguiente flujo de trabajo:

1. **Obtención de datos**: Se extrajeron productos desde un endpoint con información de Adidas.
2. **Normalización y etiquetado con LLM**: Un modelo de lenguaje se utilizó para transformar las descripciones crudas del producto en variables estructuradas y etiquetadas.
3. **Limpieza y transformación**: Se procesaron valores nulos, se convirtieron precios y métricas a formato numérico flotante, y se realizaron codificaciones dummies para variables categóricas.
4. **Clustering (K-Means)**: Se aplicó K-Means con un determinado número de clusters, seleccionado tras un análisis inicial con el método del codo. La elección final de k se basó en la interpretación de las métricas y la naturaleza de los datos.

El resultado fue un conjunto de clusters, cada uno agrupando productos con ciertas características predominantes. Por ejemplo:
* El **Cluster 2** (22 elementos) presentó productos con un peso promedio de alrededor de 569 g, un drop cercano a 9.4 mm, y precios promedio de ~401.7. Las tecnologías más comunes fueron "Mediasuela Bounce" y "Suela de caucho", con mayoría de productos para "Mujer" y "Running".
* El **Cluster 3** (60 elementos) mostró productos más ligeros (259.9 g) con drop de ~9.65 mm y precios promedio cercanos a 474. En este cluster destacó el material "Parte superior de malla" y el sistema "Dreamstrike+", mayormente orientado a calzado de "Mujer" y "Running".

## Evaluación del Modelo

**Métricas:**
* **Silhouette Score:** -0.10726032825390042  
  Un valor negativo sugiere que la mayoría de los puntos podrían asignarse mejor a otros clusters, indicando una baja cohesión/separación.
  
* **Davies-Bouldin Score:** 3.7837546892816856  
  Un valor relativamente alto indica que los clusters no están bien separados ni son internamente cohesivos.

Al realizar la comparacion entre diferentes modelos obtenemos las siguientes métricas:

| Modelo        | Número de Clusters | Silhouette Score      | Davies-Bouldin Score |
|---------------|--------------------|-----------------------|----------------------|
| KMeans        | 3                  | 0.3468094215555982    |   0.5095857881425025 |
| Agglomerative | 2                  | 0.2774924967946853    |   2.795591016138718  |
| DBScan        | 9                  | -0.19920787551009733  |  2.6226063126770205  |
| HDBSCan       | 38                 | -0.025542353420798247 |  2.455807218880036   |

Estas métricas reflejan la complejidad del conjunto de datos y la necesidad de refinar la representación de las variables o ajustar el número y el tipo de clustering usado.

A nivel descriptivo, se logró observar patrones de materiales y tecnologías predominantes por cluster, lo que puede ser útil como insumo para análisis posteriores, a pesar de que la calidad cuantitativa del clustering no fue óptima.

## Conclusiones y Recomendaciones

**Fortalezas:**
* Se estableció un proceso reproducible para extraer, normalizar y clústerizar datos de productos.
* Se identificaron patrones básicos en la composición de algunos clusters.

**Debilidades:**
* Métricas bajas de calidad de clusters indican que la segmentación no es nítida.
* Alta heterogeneidad en las características, posibles variables irrelevantes o ruido dificultan la formación de grupos cohesivos.

**Limitaciones:**
* El modelo depende en gran medida de la calidad de las etiquetas generadas por el LLM.
* No se exploraron otros algoritmos de clustering ni se realizaron exhaustivos ajustes de hiperparámetros.

**Áreas de mejora:**
* Refinar la selección de características y la representación de datos, por ejemplo, utilizando embeddings semánticos para descripciones textuales.
* Probar técnicas de reducción de dimensionalidad (PCA, UMAP) para mejorar la separabilidad de los datos.
* Experimentar con algoritmos de clustering alternativos (DBSCAN, HDBSCAN) que podrían adaptarse mejor a la forma real de los datos.

## Referencias

* Scikit-learn Documentation: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
* Evaluación de Clustering (Silhouette y Davies-Bouldin): [https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
* Documentación de K-Means: [https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
* Técnicas de reducción de dimensionalidad: [https://scikit-learn.org/stable/modules/decomposition.html](https://scikit-learn.org/stable/modules/decomposition.html)
  