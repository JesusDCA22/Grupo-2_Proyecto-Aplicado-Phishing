# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis comparativo de productos de Running entre Nike, Adidas y Nation Runner

## Objetivo del Proyecto

Desarrollar una herramienta computacional que permita realizar un análisis comparativo de zapatos para running, utilizando datos obtenidos de varias tiendas retail mediante técnicas de procesamiento de lenguaje natural y preprocesamiento de datos, incluyendo el uso de Grandes Modelos de Lenguaje (LLM, por sus siglas en inglés).

## Alcance del Proyecto

El alcance del proyecto consiste en construir un modelo de recomendación basado en embeddings, capaz de generar recomendaciones basadas en la similitud de atributos de calzado deportivo para running, alineados con las necesidades del cliente.

Se propone el uso de embeddings debido a que los datos disponibles consisten en descripciones textuales de las características de diferentes tipos de calzado deportivo. Se busca aplicar técnicas de embeddings utilizando modelos LLM, con el objetivo de mejorar la precisión semántica basada en similitud contextual.

### Incluye:

- Datos de Adidas, Nike y Nation Runner, obtenidos mediante un scraper con corte de datos a mediados de noviembre.
- Un dataset organizado y etiquetado con modelos comparados.
- Un modelo que permita realizar análisis comparativos de productos de forma automática y frecuente, con información actualizada sobre los movimientos de mercado de las marcas analizadas.

### Excluye:

- La comparación de productos de marcas no incluidas en el análisis inicial (por ejemplo, Puma o Reebok).
- El desarrollo de visualizaciones avanzadas, como gráficos interactivos o dashboards personalizados, que no estén especificados como requisitos del proyecto.

## Metodología

CRISP-DM y SCRUM

## Cronograma

| Etapa                                    | Duración Estimada | Fechas                          |
|-----------------------------------------|-------------------|---------------------------------|
| Entendimiento del negocio y carga de datos | 2 semanas         | del 13 de noviembre al 28 de noviembre |
| Preprocesamiento y análisis exploratorio | 1 semana          | del 29 de noviembre al 5 de diciembre |
| Modelamiento y extracción de características | 1 semana          | del 5 de diciembre al 12 de diciembre |
| Despliegue                               | 1 semana          | del 13 de diciembre al 19 de diciembre |
| Evaluación y entrega final               | 1 semana          | del 19 de diciembre al 21 de diciembre |

## Equipo del Proyecto

- Daniel Galvis CC 1010038257 cgalvisn@unal.edu.co
- Juan Correa CC 1013653882 jumcorrealo@unal.edu.co
- Asdrúbal Zácipa Corredor CC 79139929 azacipac@unal.edu.co

## Presupuesto

## Presupuesto

Aunque no contamos con financiamiento externo, hemos estimado los costos básicos relacionados con el desarrollo del proyecto, considerando el uso de recursos personales como luz, internet y equipos de cómputo. A continuación, se detalla el presupuesto:

| Concepto                     | Costo Mensual (COP) | Proporción por Persona (COP) | Duración (meses) | Total (COP) |
|------------------------------|---------------------|------------------------------|------------------|-------------|
| Servicio de luz              | 100,000            | 33,333                       | 2                | 200,000     |
| Servicio de internet         | 150,000            | 50,000                       | 2                | 300,000     |
| Uso de equipos personales    | 200,000            | 66,667                       | 2                | 400,000     |
| Reserva para emergencias     | -                  | -                            | -                | 100,000     |
| **Total**                    | -                  | -                            | -                | **1,000,000** |

### Detalles:
- **Servicio de luz:** Se estima un consumo aproximado para las actividades relacionadas con el desarrollo del proyecto.
- **Servicio de internet:** Incluye el costo de conexión a internet necesario para reuniones, investigación y uso de herramientas en línea.
- **Uso de equipos personales:** Incluye el desgaste de hardware y el consumo eléctrico de los equipos utilizados.
- **Reserva para emergencias:** Monto adicional para cubrir imprevistos, como reparaciones de equipos.

### Notas:
- El presupuesto puede ajustarse si se identifican costos adicionales.

## Stakeholders

- Dirección comercial de empresas deportivas interesadas en el análisis de mercado.
- Equipos laborales que requieren herramientas de apoyo para la toma de decisiones estratégicas.
- Usuarios finales que necesitan una herramienta automatizada para realizar análisis comparativos de productos deportivos de varias gamas y modelos.

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]