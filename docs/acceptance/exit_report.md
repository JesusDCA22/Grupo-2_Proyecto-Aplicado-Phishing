# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso. A lo largo del ciclo de vida del proyecto, se aplicó una metodología híbrida basada en CRISP-DM y la gestión ágil de SCRUM, que permitió estructurar las tareas técnicas y facilitar la colaboración entre los miembros del equipo. 

El objetivo primordial fue el desarrollo de un análisis comparativo de calzado deportivo para running, abarcando la extracción, limpieza y transformación de datos provenientes de diferentes marcas y tiendas (Adidas, Nike y Nation Runner), su posterior modelado y la implementación de un modelo de recomendación basado en similitud semántica.

## Resultados del proyecto

- **Resumen de los entregables y logros alcanzados en cada etapa del proyecto**  
  1. **Entendimiento del Negocio**: Se definió el alcance y los objetivos, estableciendo como meta la creación de un análisis comparativo de productos de running a partir de descripciones textuales, utilizando técnicas de embeddings para lograr mayor precisión semántica.  
  2. **Entendimiento de los Datos**: Se recopilaron datos mediante scraping de tres fuentes (Adidas, Nike y Nation Runner), dispuestos en una API conectada a Firebase, y finalmente se consolidaron en archivos CSV para su posterior manipulación.  
  3. **Preparación de los Datos**: Se realizó etiquetado con la ayuda de un LLM, normalización de campos (especialmente precios), y transformación de textos en representaciones vectoriales (embeddings).  
  4. **Modelado**: Se implementó un primer modelo baseline de clustering (K-Means) para segmentar productos de Adidas según características como peso, drop, precio y tecnologías. Posteriormente, se exploraron otros algoritmos de clustering (Agglomerative, DBSCAN y HDBSCAN) y se entrenó una red neuronal para asignar productos de  Decathlon a los clusters previamente establecidos.  
  5. **Evaluación y Despliegue**: Se midió la calidad del clustering con métricas de evaluación como Silhouette Score y Davies-Bouldin Score. Aunque los valores no fueron óptimos (-0.107 en Silhouette y ~3.78 en Davies-Bouldin), sí permitieron establecer una línea base para futuros refinamientos. El despliegue contempló la creación de un pipeline reproducible capaz de actualizar los resultados conforme se disponga de datos nuevos.  

- **Evaluación del modelo final y comparación con el modelo base**  
  El modelo baseline de clustering (K-Means) presentaba un Silhouette Score negativo y un Davies-Bouldin Score relativamente alto, evidenciando una segmentación difusa de los productos. El modelo final, que incluyó mejoras en la selección de variables y la utilización de embeddings más avanzados para el preprocesamiento, mostró ligeras mejoras en la interpretación y clasificación de productos. Sin embargo, las métricas de evaluación aún indican oportunidades de refinamiento para capturar mejor la similitud real entre los productos de calzado deportivo.

- **Descripción de los resultados y su relevancia para el negocio**  
  A pesar de que las métricas cuantitativas no alcanzaron los valores deseados, se consiguieron los siguientes avances relevantes:
  - Se estableció un proceso de comparación de productos que facilita la detección de patrones en atributos clave (materiales, tecnologías, precios, peso, etc.).  
  - Se generó una estructura de datos y un pipeline reproducible, lo que sienta las bases para iteraciones futuras que mejoren la precisión y la utilidad del sistema de recomendación.  
  - El equipo directivo y comercial dispone ahora de un modelo básico para comprender la distribución y características principales de su catálogo, así como la comparativa con la competencia.

![nuevoProceso (1)](https://github.com/user-attachments/assets/558ff02f-750a-4898-ac6c-9682f701cce0)

## Lecciones aprendidas

- **Identificación de los principales desafíos y obstáculos**  
  - La calidad e inconsistencia de los datos (valores faltantes o con formatos heterogéneos) representó el principal reto para la normalización y preprocesamiento.  
  - El uso de descripciones textuales de productos exigió un enfoque especializado (embeddings) para capturar la semántica y evitar la pérdida de información relevante.  
  - La implementación de un modelo híbrido (LLM + algoritmos de clustering) requiere asegurar la coherencia entre las variables categóricas y numéricas, lo que implicaría un trabajo adicional de mapeo y unificación de criterios.  

- **Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación**  
  - Un pipeline reproducible, desde el scraping y la limpieza de datos hasta la aplicación de técnicas de modelado, resulta esencial para escalar y mantener el proyecto en el largo plazo.  
  - Utilizar un LLM para normalizar descripciones textuales puede aportar gran valor, pero se debe contar con supervisión y validaciones adicionales para evitar etiquetados inconsistentes o la propagación de errores semánticos.  
  - La selección de características y la ingeniería de atributos (feature engineering) juega un papel crítico en el desempeño del modelo. Es vital evaluar periódicamente la relevancia de cada variable.  

- **Recomendaciones para futuros proyectos de machine learning**  
  - Adoptar estrategias de validación de datos más exhaustivas desde el inicio, asegurando la calidad y consistencia de la información.  
  - Explorar algoritmos de clustering más adecuados a la naturaleza de los datos, como HDBSCAN, que no requiere especificar de antemano el número de clusters y puede manejar clusters de forma más orgánica.  
  - Considerar la integración con herramientas de visualización más interactivas (como dashboards) para que el equipo de negocio pueda monitorear y ajustar el modelo de forma continua.

## Impacto del proyecto

- **Descripción del impacto del modelo en el negocio o en la industria**  
  - El modelo de recomendación ofrece una vista preliminar de cómo se agrupan los productos de calzado deportivo, favoreciendo la identificación de nichos de mercado y oportunidades de diferenciación frente a competidores.  
  - Permite a las áreas comercial y de mercadeo obtener insights rápidos sobre precios, tecnologías y composición de los productos, lo que impulsa decisiones informadas y el desarrollo de nuevas estrategias de posicionamiento.  

- **Identificación de las áreas de mejora y oportunidades de desarrollo futuras**  
  - Se abre la posibilidad de complementar el modelo con datos de otras marcas no incluidas inicialmente (por ejemplo, Puma o Reebok), ampliando la comparativa y enriqueciendo la visión global del mercado.  
  - Incluir información de ventas, reseñas de clientes o ratings para correlacionar la efectividad de ciertos atributos del calzado con el desempeño comercial.  
  - Desarrollar dashboards interactivos y visualizaciones avanzadas que faciliten la interpretación y uso de los resultados por parte de los equipos de negocio y stakeholders.

## Conclusiones

- **Resumen de los resultados y principales logros del proyecto**  
  - Se logró crear un pipeline integral, desde la extracción de datos con web scraping hasta la generación de clusters de productos, con un primer prototipo de recomendación basado en similitud semántica.  
  - A pesar de que las métricas de calidad de clustering no fueron óptimas, el proceso sienta las bases para una mejora continua y demuestra el valor de la combinación entre técnicas de embeddings y métodos de clustering/segmentación.  

- **Conclusiones finales y recomendaciones para futuros proyectos**  
  - El uso de metodologías ágiles y la estructura de CRISP-DM propiciaron un orden claro en la ejecución y un enfoque iterativo para el desarrollo del proyecto.  
  - Para elevar el valor práctico del modelo, se recomienda profundizar en el perfeccionamiento de las representaciones vectoriales, la selección de algoritmos de clustering más robustos y la incorporación de más variables relevantes (como reseñas de usuarios).  
  - La escalabilidad del sistema se beneficiaría de un monitoreo periódico de la calidad de datos y la reentrenamiento automático del modelo al integrarse nuevos productos o marcas.
