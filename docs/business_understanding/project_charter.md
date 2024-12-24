# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis comparativo de productos de Running entre Nike, Adidas y Nation Runner

## Objetivo del Proyecto

Desarrollar una herramienta computacional que permita realizar un análisis comparativo de zapatos para running, utilizando datos obtenidos de varias tiendas retail mediante técnicas de procesamiento de lenguaje natural y preprocesamiento de datos, incluyendo el uso de Grandes Modelos de Lenguaje (LLM, por sus siglas en inglés).

<img width="842" alt="image" src="https://github.com/user-attachments/assets/1f9e5304-73f1-413f-90a2-b9f82f76d357" />

Img 1: Proceso del negocio manual para un análisis comparativo de productos

## Alcance del Proyecto

El alcance del proyecto consiste en construir un modelo de recomendación basado en embeddings, capaz de generar recomendaciones basadas en la similitud de atributos de calzado deportivo para running, alineados con las necesidades del cliente.

Se propone el uso de embeddings debido a que los datos disponibles consisten en descripciones textuales de las características de diferentes tipos de calzado deportivo. Se busca aplicar técnicas de embeddings utilizando modelos LLM, con el objetivo de mejorar la precisión semántica basada en similitud contextual.

### Incluye

- Datos de Adidas, Nike y Nation Runner, obtenidos mediante un scraper con corte de datos a mediados de noviembre.
- Un dataset organizado y etiquetado con modelos comparados.
- Un modelo que permita realizar análisis comparativos de productos de forma automática y frecuente, con información actualizada sobre los movimientos de mercado de las marcas analizadas.

### Excluye

- La comparación de productos de marcas no incluidas en el análisis inicial (por ejemplo, Puma o Reebok).
- El desarrollo de visualizaciones avanzadas, como gráficos interactivos o dashboards personalizados, que no estén especificados como requisitos del proyecto.

## Metodología

El proyecto seguirá una metodología híbrida basada en **CRISP-DM** (Cross-Industry Standard Process for Data Mining) para la estructura de las tareas técnicas y **SCRUM** para la gestión ágil del equipo y del cronograma.

### Etapas según CRISP-DM

1. **Entendimiento del Negocio**
   - Actividades:
     - Identificar necesidades del cliente.
     - Determinar los objetivos del análisis comparativo.
     - Definir métricas clave para evaluar la precisión del modelo.
   - Cronograma: 13 de noviembre al 28 de noviembre.

2. **Entendimiento de los Datos**
   - Actividades:
     - Recopilar datos de Adidas, Nike y Nation Runner mediante scraping.
     - Explorar las descripciones textuales y detectar posibles inconsistencias o valores faltantes.
     - Validar la calidad de los datos.
   - Cronograma: 13 de noviembre al 28 de noviembre.

3. **Preparación de los Datos**
   - Actividades:
     - Realizar limpieza y preprocesamiento de las descripciones.
     - Convertir datos textuales en representaciones vectoriales (embeddings).
     - Dividir los datos en conjuntos de entrenamiento, validación y prueba.
   - Cronograma: 29 de noviembre al 5 de diciembre.

4. **Modelado**
   - Actividades:
     - Diseñar y entrenar un modelo de recomendación basado en similitud semántica.
     - Optimizar hiperparámetros para maximizar el rendimiento del modelo.
   - Cronograma: 5 de diciembre al 12 de diciembre.

5. **Evaluación**
   - Actividades:
     - Validar el modelo con métricas como precisión, recall y F1-score.
     - Realizar pruebas con datos nuevos para garantizar generalización.
   - Cronograma: 19 de diciembre al 21 de diciembre.

6. **Despliegue**
   - Actividades:
     - Integrar el modelo en una herramienta funcional.
     - Documentar su uso y entrenar al equipo en su aplicación.
   - Cronograma: 13 de diciembre al 19 de diciembre.

### Gestión ágil con SCRUM

El desarrollo del proyecto se gestionará a través de iteraciones de una semana (sprints) para garantizar la flexibilidad y la adaptabilidad frente a posibles cambios en los requisitos.

#### Roles del equipo

#### **Equipo y Responsabilidades**

#### **1. Juan Correa (Product Owner y Líder Técnico)**  

- **Responsabilidades compartidas con Daniel Galvis:**  
  - Definir y priorizar los requisitos del proyecto.  
  - Asegurar el alineamiento con los objetivos del cliente y del negocio.  
- **Responsabilidades compartidas con Asdrúbal Zácipa Corredor:**  
  - Liderar las decisiones técnicas clave y supervisar el desarrollo general.  

#### **2. Daniel Galvis (Scrum Master y Desarrollador)**  

- **Responsabilidades compartidas con Juan Correa:**  
  - Coordinar las ceremonias ágiles y facilitar la comunicación entre el equipo.  
  - Eliminar impedimentos que afecten el progreso del proyecto.  
- **Responsabilidades compartidas con Asdrúbal Zácipa Corredor:**  
  - Colaborar en tareas de scraping, preprocesamiento y soporte técnico.  

#### **3. Asdrúbal Zácipa Corredor (Desarrollador y Especialista en Modelado)**  

- **Responsabilidades compartidas con Juan Correa:**  
  - Diseñar, entrenar y evaluar el modelo de recomendación.  
  - Implementar el modelo y contribuir al desarrollo técnico del proyecto.  
- **Responsabilidades compartidas con Daniel Galvis:**  
  - Asegurar la integración funcional de las soluciones desarrolladas.  

---

#### **Justificación de la Redistribución**  

Esta reorganización tiene como objetivo mitigar el riesgo operativo en caso de que algún integrante del equipo no pueda cumplir temporalmente con sus responsabilidades debido a enfermedad, emergencia u otros compromisos. Al asignar al menos dos personas a cada tarea, se asegura que el flujo de trabajo no se interrumpa y que el conocimiento clave del proyecto esté distribuido de manera uniforme entre los integrantes.  

Además, este enfoque fomenta la colaboración y la versatilidad, ya que todos los miembros se mantendrán actualizados sobre diferentes aspectos del proyecto, promoviendo una mayor resiliencia y adaptabilidad en el equipo.  

#### Ceremonias

- **Sprint Planning:** Al inicio de cada sprint, se definirán las tareas clave y los entregables.
- **Daily Standup:** Reuniones diarias de 15 minutos para revisar el progreso y resolver bloqueos.
- **Sprint Review:** Al finalizar cada sprint, se presentarán los avances al equipo y se recopilará retroalimentación.
- **Sprint Retrospective:** Se analizarán las lecciones aprendidas y se identificarán áreas de mejora para futuros sprints.

## Cronograma Integrado con Sprints

| Sprint                  | Etapa                                    | Actividades principales                          | Duración Estimada | Fechas                          |
|-------------------------|-----------------------------------------|------------------------------------------------|-------------------|---------------------------------|
| Sprint 1               | Entendimiento del negocio y carga de datos | Entendimiento del negocio y carga de datos       | 2 semanas         | Del 13 de noviembre al 28 de noviembre |
| Sprint 2               | Preprocesamiento y análisis exploratorio | Preprocesamiento y análisis exploratorio         | 1 semana          | Del 29 de noviembre al 5 de diciembre |
| Sprint 3               | Modelamiento y extracción de características | Modelamiento y extracción de características     | 1 semana          | Del 5 de diciembre al 12 de diciembre |
| Sprint 4               | Despliegue                               | Despliegue del modelo                            | 1 semana          | Del 13 de diciembre al 19 de diciembre |
| Sprint 5               | Evaluación y entrega final               | Evaluación final y entrega                       | 1 semana          | Del 19 de diciembre al 21 de diciembre |

## Equipo del Proyecto

- Daniel Galvis CC 1010038257 <cgalvisn@unal.edu.co>
- Juan Correa CC 1013653882 <jumcorrealo@unal.edu.co>
- Asdrúbal Zácipa Corredor CC 79139929 <azacipac@unal.edu.co>

## Presupuesto

Aunque no se cuenta con financiamiento externo, se estimaron los costos básicos relacionados con el desarrollo del proyecto, considerando el uso de recursos personales como luz, internet y equipos de cómputo. A continuación, se detalla el presupuesto:

| Concepto                     | Costo Mensual (COP) | Proporción por Persona (COP) | Duración (meses) | Total (COP) |
|------------------------------|---------------------|------------------------------|------------------|-------------|
| Servicio de luz              | 100,000            | 33,333                       | 2                | 200,000     |
| Servicio de internet         | 150,000            | 50,000                       | 2                | 300,000     |
| Uso de equipos personales    | 200,000            | 66,667                       | 2                | 400,000     |
| Reserva para emergencias     | -                  | -                            | -                | 100,000     |
| **Total**                    | -                  | -                            | -                | **1,000,000** |

### Detalles

- **Servicio de luz:** Incluye el costo estimado del consumo eléctrico asociado al trabajo en el proyecto.
- **Servicio de internet:** Cubre el acceso a internet necesario para reuniones virtuales, investigación y uso de herramientas online.
- **Uso de equipos personales:** Considera el desgaste de hardware y el consumo eléctrico de los equipos utilizados durante el desarrollo.
- **Reserva para emergencias:** Monto adicional para imprevistos, como la reparación de equipos o la adquisición de software adicional.

## Stakeholders

- Dirección comercial de una empresa deportiva.
- Equipo laboral interno interesado en la automatización del análisis comparativo de productos deportivos.
- Consumidores finales que podrían beneficiarse indirectamente de las recomendaciones generadas por el modelo.

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]