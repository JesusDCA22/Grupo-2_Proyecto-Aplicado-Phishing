# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto
Sistema de Detección de Phishing para Protección Financiera en Colombia
## Objetivo del Proyecto
Desarrollar e implementar un modelo de deep learning capaz de detectar en tiempo real URLs con alta probabilidad de ser utilizadas para ataques de phishing. El propósito es proteger a los usuarios de plataformas financieras contra fraudes, estafas, robo de identidad y filtración de información bancaria. Este sistema busca ser replicable y escalable, fortaleciendo la ciberseguridad y la confianza en los servicios digitales financieros.
## Alcance del Proyecto
El presente proyecto tiene como alcance el desarrollo, entrenamiento e implementación de un modelo de deep learning para la detección temprana de URLs maliciosas asociadas con ataques de phishing. Este modelo será integrado en un entorno de producción con el objetivo de generar alertas automáticas cuando se detecte una URL sospechosa, permitiendo actuar de manera preventiva tanto al usuario como a la entidad financiera. La alerta podrá presentarse en formato binario (riesgosa / no riesgosa) o como una probabilidad numérica, y servirá como una herramienta de ciberseguridad para mitigar el riesgo de fraudes electrónicos y robo de información.
### Incluye:
- Los datos utilizados para entrenar el modelo provienen de conjuntos públicos disponibles en Kaggle.com (https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset?resource=download), los cuales contienen registros reales de URLs etiquetadas como legítimas o de phishing. Se trata de un conjunto de datos equilibrado, lo cual permite un entrenamiento robusto y controlado, con representación equivalente de ambos tipos de URL.
- El conjunto incluye un total de 87 variables predictoras, distribuidas de la siguiente manera:
56 características extraídas de la estructura y sintaxis de las URLs (por ejemplo, longitud, uso de símbolos especiales, uso de HTTPS, número de subdominios, entre otros).
24 características derivadas del contenido de las páginas web correspondientes (por ejemplo, presencia de formularios sospechosos, enlaces externos, uso de scripts).
7 características obtenidas mediante consultas a servicios externos, como verificaciones WHOIS, reputación de dominios o datos de registro.
- Entrenamiento exitoso de un modelo de deep learning con capacidad predictiva significativa. Un modelo replicable, de bajo costo computacional, que pueda operar en tiempo real. Implementación del modelo en un entorno de prueba o producción que permita la evaluación continua y la generación de alertas tempranas. Generación de una alerta binaria (0 = seguro, 1 = phishing) o una puntuación de propensión al phishing (entre 0 y 1), que pueda ser usada por interfaces de usuario o sistemas de monitoreo automático. Mejora en la prevención de incidentes de phishing a través de la disuasión del usuario o el bloqueo automático de URLs maliciosas.
- Precisión del modelo: Lograr una precisión superior al 90% en la clasificación de URLs en el conjunto de validación. Tasa de Falsos Positivos aceptable: Minimizar la cantidad de URLs legítimas clasificadas erróneamente como phishing (idealmente <5%). Tasa de detección: Identificar al menos el 95% de las URLs de phishing presentes en el conjunto de pruebas o en producción. Latencia de predicción: El modelo debe generar una predicción en menos de 1 segundo por URL, permitiendo su uso en tiempo real. Implementación en producción: Integración exitosa del modelo en un sistema funcional que emita alertas preventivas para usuarios y entidades. Escalabilidad: Posibilidad de replicar el modelo en otros contextos o entidades financieras con ajustes mínimos.

### Excluye:
- Desarrollo de plugins o extensiones para navegadores web
- Evaluación de impacto legal o normativo
- Entrenamiento con datos en vivo o recolección automatizada de nuevas URLs

## Metodología

Se llevo a cabo el proyecto mediante la metodología CRISP-DM dividida en sus 6 fases.
- Entendimiento de negocio : Entender el comportamiento de 
- Entendimiento de los datos : Realizar un análisis exploratirio de los datos, verificando la calidad y completitud.
- Preparación de los datos : Un anánlisis más robusto de los datos y seleccionando los campos que realmente aporten información al modelo.
- Entrenamiento del modelo : Desarrollar un Pipeline que permita el entrenamiento segmentado de los datos para una posterior validación. Usar diferentes hiperparametros para un modelo de Red profunda con el objetivo de obtener la mejor combinación de hiperparametros que mejor represente la realidad del comportamiento de los datos. 
- Evaluación del modelo : Se realiza una evaluación mediante diferentes metricas como Accuracy, Recall o F1-Score para optar por el modelo más adecuado a los objetivos del proyecto. En este caso el modelo con mayor Recall es escogido, dado que el objetivo más importante es capturar la mayor candida de phishing posible.
- Despliegue a producción : Esta fase a producción no será desarrollada por el equipo de Data Scientist, por lo que se delega la responsabilidad al equipo de MLOps. El equipo de Data Scientist realiza un entregable estandarizado donde incluye : 1. Modelo en .h5 o .joblib 2. Base de datos de entrenamiento 3. Query de datos de despliegue 4. Preproceador de datos 5. Script de ejemplo con datos reales.  


## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 1 de mayo al 8 de mayo |
| Preprocesamiento, análisis exploratorio | 1 semanas | del 9 de mayo al 15 de mayo |
| Modelamiento y extracción de características | 2 semanas | del 16 de mayo al 29 de mayo |
| Evaluación y entrega final | 1 semanas | del 30 de mayo al 6 de junio |

## Equipo del Proyecto

- Federico Negret : Lead Data Scientist
- Miguel Ángel Medina : Senior Data Scientist
- Jesus Castro : Senior Data Scientist

## Presupuesto
Para el desarrollo del proyecto se requiere de uso de AWS para todas las fases.
El recuerso humano son ambos Data Scientits en tiempo completo durante 5 semanas. 
Añadiendo la supervisión del lider a medio tiempo para este proyecto.
- $5.000 USD para los recursos digitales 
- $10.000 USD para recurso humano
- $5.000 USD para Lead Data Scientist 


## Stakeholders

- El stakeholder es Juan Sebastian Malagón
- El experto en detección de fraude y Phishing de la entidad bancaria.
- Las espectativas del stakeholder para el proyecto es obtener una redución significativa de los casos de fraude y robo de identidad en la entidad financiera por parte de los usuarios en las plataformas digitales. 

## Aprobaciones

- Juan Sebastian Malagón
- ___________________________
- 1 Mayo 2025
