# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

EXTRACCIÓN DE CARACTERÍSTICAS

Dado que nuestro proyecto corresponde al tratamiento de texto y análisis no supervisado, en la etapa de extracción de características utilizamos técnicas como modelado de tópicos, generación de nubes de palabras y representaciones gráficas, que permitieron una mejor comprensión inicial de los datos. Para ello, empleamos la técnica TF-IDF útil para trabajar con bolsas de palabras al asignar pesos a términos en función de su relevancia dentro del corpus. Sin embargo, debido a las limitaciones de TF-IDF (como la incapacidad para capturar el contexto semántico y las relaciones entre palabras), adoptamos posteriormente un modelo pre-entrenado para enriquecer las representaciones textuales y obtener características más robustas para el modelamiento.
El análisis exploratorio de características mediante TF-IDF y modelado de tópicos permitió validar la relevancia del corpus y su alineación con el negocio. Esto garantizó que los datos utilizados eran adecuados, proporcionando una buena base para la etapa de modelamiento. Además, los resultados obtenidos en el análisis de la bolsa de palabras y la identificación de tópicos relevantes ayudaron a ajustar decisiones de preprocesamiento, como la inclusión de stop words al trabajar con modelos pre-entrenados. Estas decisiones resultaron cruciales para mejorar el rendimiento del modelo seleccionado, dado que técnicas como RoBERTa dependen del contexto completo para generar respuestas precisas y relevantes.

MODELAMIENTO

Para abordar el problema, evaluamos cuatro modelos pre-entrenados de Hugging Face:

1.	"bert-large-uncased-whole-word-masking-finetuned-squad"
2.	"dccuchile/bert-base-spanish-wwm-cased"
3.	"deepset/xlm-roberta-large-squad2"
4.	"deepset/roberta-large-squad2"

Utilizamos las siguientes métricas de evaluación:

Validation Loss: Mide qué tan bien el modelo se ajusta a los datos de validación y ayuda a identificar posibles problemas de sobreajuste.  
Exact Match (EM): Mide el porcentaje de respuestas predichas que coinciden exactamente con las respuestas reales.  
F1 Score: Proporciona una medida equilibrada entre precisión y exhaustividad, especialmente útil cuando las respuestas no coinciden exactamente, pero contienen los mismos conceptos clave.  
Precision y Recall: Miden, respectivamente, qué tan precisas son las respuestas predichas y qué tan completas son en relación con las respuestas esperadas.  

El modelo con mejores métricas fue “deepset/roberta-large-squad2”, afinado con el conjunto de datos SQuAD 2.0, que está diseñado para responder preguntas extractivas dentro de un contexto dado. 

El conjunto de datos SQuAD (Stanford Question Answering Dataset) es un conjunto de referencia ampliamente utilizado para entrenar y evaluar modelos de comprensión de lectura y tareas de preguntas y respuestas (Q&A).

Evaluación del mejor modelo:

![image](https://github.com/user-attachments/assets/6f332005-7444-422d-9c28-413ab497fd2f)

El modelo “deepset/roberta-large-squad2” tuvo la menor pérdida de validación entre todos los modelos, lo que indica que se ajustó mejor a los datos de validación. Además, logró puntuaciones perfectas en todas las métricas (Exact Match, F1 Score, Precision y Recall), lo que sugiere que encontró todas las respuestas correctas en el conjunto de validación.  

BUSQUEDA DE HIPERPARAMETROS CON OPTUNA

Se creo la función objetivo para la búsqueda de los siguientes hiperparámetros:
1.	learning_rate:  Controla la magnitud de las actualizaciones de los pesos del modelo durante el entrenamiento.  Rango: 1e-6 a 1e-4.
2.	batch_size: Número de muestras procesadas antes de actualizar los parámetros del modelo. Valores posibles: 8, 16, 32.
3.	weight_decay: Decaimiento de los pesos. Regularización para evitar el sobreajuste penalizando grandes pesos. Rango: 1e-5 a 1e-2.
4.	num_train_epochs: Número de veces que el modelo verá el conjunto de datos completo durante el entrenamiento. Rango: 2 a 6.
5.	warmup_steps: Número de pasos durante los cuales la tasa de aprendizaje aumenta linealmente desde cero hasta el valor inicial. Rango: 100 a 1000, con incrementos de 100.
6.	evaluation_strategy: Define cuándo se realiza la evaluación del modelo. Valores posibles: "no", "steps", "epoch".

Conclusiones sobre los hiperparámetros y el rendimiento del modelo:

Se realizó un estudio con Optuna para minimizar la pérdida de validación (Validation Loss) por que las otras métricas tenían un resultado perfecto.
Los mejores Hiperparametros encontrados fueron:
learning_rate: 0.00005484280815953229
batch_size: 8
weight_decay: 0.00009942270232851624
num_train_epochs: 5
warmup_steps: 700
evaluation_strategy: 'steps'

Interpretación:
Learning Rate bajo: Un valor bajo sugiere que el modelo necesita aprender lentamente para evitar grandes oscilaciones en la optimización, lo que es ideal para modelos preentrenados como el utilizado.
Batch Size Facilita la estabilidad en los gradientes a cambio de mayor tiempo de entrenamiento.
Weight Decay Indica que regularizar los pesos del modelo es importante para evitar el sobreajuste.
5 épocas: Parece ser el punto de convergencia adecuado para el conjunto de datos utilizado.
Los resultados del entrenamiento final muestran un buen rendimiento del modelo:

![image](https://github.com/user-attachments/assets/70355bc0-424c-42ea-a24d-054e12d1e0c6)

Interpretación de los Resultados
Training Loss y Validation Loss: La pérdida de entrenamiento y la pérdida de validación son bajas, lo que indica que el modelo se ajusta bien a los datos de entrenamiento y generaliza bien a los datos de validación.
Exact Match, F1 Score, Precision y Recall: Todas estas métricas tienen un valor perfecto de 1.000000, lo que significa que el modelo está proporcionando respuestas precisas y equilibradas, encontrando todas las respuestas correctas y todas las respuestas proporcionadas son correctas.
En el resultado final las métricas fueron perfectas y el eval_loss mejoro.

CONCLUSION:

En resumen, el modelo “deepset/roberta-large-squad2” demostró ser el más adecuado para este proyecto, gracias a su capacidad para capturar relaciones semánticas y proporcionar respuestas precisas. Este resultado muestra la importancia de utilizar modelos pre-entrenados para superar las limitaciones de técnicas más básicas como TF-IDF, y representa un paso importante hacia la comprensión automatizada del texto en nuestro caso de negocio.

## Lecciones aprendidas

1. Manejo de los datos:
Uno de los principales desafíos fue procesar un corpus extenso y no estructurado, asegurando que los datos fueran representativos del problema de negocio. 
Finalmente, la recomendación del profesor Oscar de utilizar un corpus más pequeño para hacer pruebas y atendiendo su recomendación de utilizar modelos pre-entrenados de Hugging-Face fue de gran utilidad ya que logramos tener un modelo que funcione bien en cada una de sus etapas. La eliminación de stop words en el análisis exploratorio presentó ventajas iniciales para identificar patrones claros, pero descubrimos que su inclusión era crucial en etapas posteriores, especialmente con modelos pre-entrenados, ya que las stop words contribuyen al contexto semántico necesario para las tareas de preguntas y respuestas.
Lección aprendida:
Es fundamental ajustar dinámicamente las técnicas de preprocesamiento según el tipo de modelo utilizado, ya que lo que es beneficioso en una etapa puede no serlo en otra.
2. Modelamiento:
Comparar varios modelos pre-entrenados presentó un reto en términos de evaluación y también requería un alto procesamiento de máquina. Algunos modelos, aunque robustos, no lograron buenas métricas de evaluación.
Lección aprendida:
La elección de modelos pre-entrenados debe basarse no solo en su tamaño o cantidad de parámetros, sino también en la alineación con el idioma y el dominio del negocio. Por ejemplo, el modelo deepset/roberta-large-squad2 se destacó sin ser el más robusto, pero creemos que fue gracias a su capacidad para manejar relaciones semánticas complejas.
3. Implementación del modelo:
Validar los resultados perfectos del modelo seleccionado (100% en Exact Match, F1 Score, Precision y Recall) planteó dudas iniciales sobre posibles sesgos en los datos de validación o sobreajuste. Fue necesario revisar cuidadosamente los datos y las métricas para confirmar la validez de los resultados.
Lección aprendida:
Es importante combinar métricas automáticas, así como hacer inspección manual, para garantizar la validez de los resultados.


Recomendaciones para futuros proyectos
Calidad del corpus:
Antes de iniciar cualquier modelamiento, invertir tiempo en validar que los datos son relevantes y representativos del problema de negocio. Un análisis exploratorio temprano puede identificar posibles problemas en el corpus.
Preprocesamiento flexible:
Considerar que en las diferentes etapas del proyecto se pueden requerir ajustes en el preprocesamiento de los datos. Por ejemplo, eliminar stop words puede ser útil para análisis exploratorio, pero su inclusión es crucial para tareas como preguntas y respuestas.
Experimentación con modelos preentrenados:
Probar modelos preentrenados que estén afinados en el idioma y dominio específico del proyecto. Esto ahorra tiempo y aumenta la probabilidad de éxito en comparación con modelos genéricos.
Revisión continua del proceso:
Documentar cada decisión y sus resultados en cada etapa para facilitar la identificación de ajustes necesarios.
Relevancia para el negocio:
Asegurarse de que los resultados técnicos se traduzcan en valor para el negocio. Incluir métricas interpretables por stakeholders no técnicos es clave para validar el impacto del proyecto.

## Impacto del proyecto

El desarrollo del proyecto nos impactó en varios aspectos.
Primero en la comprensión de como existen herramientas para el procesamiento y generación del texto, entender como funciona un modelo de inteligencia artificial fue realmente interesante. Entender que el modelo se entrena con una cantidad de datos considerablemente grande comparado con el resultado o archivo ejecutable que son unos pocos bytes con fórmulas matemáticas fue impactante.
Por otro lado, el modelo desarrollado representa un avance en la capacidad de análisis automatizado de texto, proporcionando una herramienta para responder preguntas con alta precisión. Este impacto es especialmente relevante para el negocio, ya que permite mejorar la eficiencia en la búsqueda de información dentro de documentos extensos, reduciendo tiempos operativos y optimizando la toma de decisiones basadas en datos.
En términos de oportunidades futuras, se identificaron áreas de mejora, como el perfeccionamiento del modelo mediante la incorporación de más datos, así como la exploración para lograr un chatbot que sea lo mas parecido a un LLM pero con un alcance especifico.


## Conclusiones

El proyecto logró implementar un modelo de preguntas y respuestas basado en deepset/roberta-large-squad2, que destacó por sus métricas perfectas en Exact Match, F1 Score, Precision y Recall, confirmando su capacidad para identificar respuestas precisas dentro del corpus. Los principales logros incluyen la validación del corpus como representativo del negocio y la selección de un modelo pre-entrenado que maximiza el contexto semántico.
Como conclusión general, el éxito del modelo demuestra la importancia de combinar análisis exploratorio, técnicas de preprocesamiento flexibles y modelos adecuados. 


## Agradecimientos

Agradecemos especialmente a el equipo de profesores de la universidad, que proporcionaron datos clave y retroalimentación técnica durante todo el proceso, su apoyo fue crucial para alcanzar los objetivos planteados. A todos los que de una u otra forma aportaron para lograr que el curso de Machine Learnig terminara con éxito. Al equipo de trabajo por su dedicación y entusiasmo por aprender nuevas tecnologías de inteligencia artificial.
