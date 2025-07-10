# Reporte de Datos

Este proyecto tiene como objetivo desarrollar un modelo de clasificación para la detección de URLs de tipo phishing. En esta sección se presenta el análisis exploratorio de datos (EDA), el cual incluye una evaluación de la calidad de los datos, una revisión de la variable objetivo, un vistazo inicial a las variables explicativas y sus principales características. Asimismo, se describen las estrategias implementadas para la preparación y limpieza de la base de datos, en función de las falencias y patrones identificados durante el análisis.


## Resumen general de los datos
Los datos utilizados fueron obtenidos de la plataforma Kaggle, donde se encuentran disponibles como un conjunto de entrenamiento para modelos de clasificación binaria. El dataset incluye más de 11.000 URLs (entre legítimas y de phishing) y un total de 87 variables explicativas:

56 variables relacionadas con la estructura y sintaxis de la URL.

7 variables que consultan servicios externos.

24 variables sobre el contenido interno de cada página.

Es importante destacar que el dataset está balanceado, con una proporción equitativa entre URLs legítimas y de phishing. Algunas variables incluyen una breve descripción sobre su propósito y significado.

## Resumen de calidad de los datos

Durante el análisis exploratorio se evaluaron los siguientes aspectos:

Balance de clases: La variable objetivo está perfectamente balanceada (50% legítimas, 50% phishing), lo cual elimina la necesidad de aplicar técnicas de balanceo de clases.

Variabilidad de variables: Se identificaron y eliminaron aquellas variables que no presentaban variabilidad (varianza cero), ya que no aportan información relevante para el modelo. Más de cuatro variables fueron descartadas por este motivo.

Valores nulos: No se encontraron valores faltantes en ninguno de los registros del dataset.

Este preprocesamiento garantiza que los datos estén limpios y listos para el entrenamiento del modelo.

## Variable objetivo

La variable objetivo es binaria, con dos categorías:

legitimate (0)

phishing (1)

Durante la fase de preparación de datos, esta variable fue codificada numéricamente como 0 (legítima) y 1 (phishing), facilitando su uso en modelos de clasificación supervisada.

![image](https://github.com/user-attachments/assets/d9972924-27e6-4142-9a7e-518842673650)



## Variables individuales
Se analizan a continuación algunas variables seleccionadas por su importancia y características particulares:

length_url: Número de caracteres de la URL. La mayoría de URLs no superan los 100 caracteres. Se observan valores atípicos por encima de los 200 caracteres.

Media: 61

Mediana: 47

Moda: 26
![image](https://github.com/user-attachments/assets/154b5f84-6567-44f3-ad4a-70497ef21131)


length_hostname: Longitud del host de la página. Muestra una distribución asimétrica, con valores generalmente más bajos que length_url.

Media: 21

Mediana: 19

Moda: 16
![image](https://github.com/user-attachments/assets/78bcb3aa-96d0-44b4-89a5-a6602d626ac9)

domain_age: Edad del dominio en días. Las páginas legítimas tienden a tener mayor antigüedad.

Media: 4.062 días (~11 años)

Mediana: ~4.000 días
![image](https://github.com/user-attachments/assets/82410f71-5d35-4cca-841f-71e0eff82452)


avg_word_host: Promedio de palabras en el host. Se observa una tendencia a un mayor número promedio de palabras en URLs de phishing, con mayor presencia de outliers.
![image](https://github.com/user-attachments/assets/8059d1ef-7c43-4eed-91b7-acf9bc1bc624)

domain_with_copyright: Indica si el dominio tiene derechos de autor. Se observa que las URLs con copyright tienden a ser legítimas, mientras que la mayoría de URLs sin esta protección son de phishing.
![image](https://github.com/user-attachments/assets/8ed5998c-edf8-4d9b-80d3-411ae078d2a9)

## Ranking de variables e Importancia
Para determinar la importancia relativa de las variables explicativas, se implementó una metodología basada en:

Análisis de Correlación: Se construyó una matriz de correlación utilizando el coeficiente de Pearson. Aquellas variables altamente correlacionadas (≥ 0.85) fueron evaluadas para evitar redundancia.

Reducción de Dimensionalidad (PCA): Se aplicó Análisis de Componentes Principales para evaluar la varianza explicada por cada variable y determinar cuál de las variables correlacionadas debía ser conservada.

Como resultado, se eliminaron solo dos variables:

nb_eq (correlación del 90% con nb_and)

longest_words_raw (correlación del 96% con longest_word_path)

Esta selección permite mejorar la eficiencia del modelo y evitar el sobreajuste, asegurando que cada variable aporte información única y relevante a la predicción de URLs de phishing.

![image](https://github.com/user-attachments/assets/5675e542-bfd1-4799-891e-a473b94c7e5a)

