# Diccionario de datos

## Base de datos 1

La estructura del dataset obtenido de las URL de las tiendas indicadas es:

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Example Value |
| --- | --- | --- | --- | --- |
| id | Descripción de la variable 1 | string |  | 046zSiHm8Cz0fZYwMJlL |
| details | detalles del producto scrapeado, data semi estructurada que contiene detalles técnicos del mismo | string | - | '{Horma clásica} {Parte superior sintética}...' |
| store | nombre de la tienda que vende el producto | string |  | adidas |
| manufacturer | nombre de la empresa que crea el producto | string |  | adidas |
| url | url desde la que se extrajo el producto | string |  | https://www.adidas.co/tenis-duramo-sl/IF7884.html |
| title | nombre del producto | string |  | Tenis Duramo SL |
| regularPrice | precio del producto sin descuento | string |  | $379.950 |
| undiscounted_price | precio con descuento aplicado | string |  | $265.965 |
| description | descripción general del producto | string |  | 'description': "Los Adizero Adios Pro 3 son la ..." |
| category | categoria que la página scrapeada asigna al producto | string |  | Mujer • Running |
| createdAt | fecha de creación del registro | string |  | '_seconds': 1731975445, '_nanoseconds': 42700.. |
| characteristics | características adicionales del producto | string |  | Parte superior de malla diseñada estratégicam.. |
| gender | genero del producto | string |  | Mujer |


- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Example Value**: Ejemplo de un valor que se puede encontrar en el campo.
- **Fuente de datos**: API en la que se disponibilizan los datos scrapeados.

## Estructura del dataset

| Variable          | Descripción                                                                 | Tipo de dato | Rango/Valores posibles | Valor de ejemplo                               |
|--------------------|-----------------------------------------------------------------------------|--------------|-------------------------|-----------------------------------------------|
| `id`              | Identificador único del producto                                           | string       | -                       | `046zSiHm8Cz0fZYwMJlL`                        |
| `details`         | Detalles técnicos del producto                                             | string       | -                       | `{Horma clásica} {Parte superior sintética}`  |
| `store`           | Nombre de la tienda que vende el producto                                  | string       | adidas, nike, nacionrunner | `adidas`                                     |
| `manufacturer`    | Marca o empresa que fabrica el producto                                    | string       | adidas, nike, otros      | `adidas`                                     |
| `url`             | URL del producto en la tienda                                              | string       | -                       | `https://www.adidas.co/...`                   |
| `title`           | Nombre o título del producto                                               | string       | -                       | `Tenis Duramo SL`                            |
| `regularPrice`    | Precio sin descuento                                                       | string       | -                       | `$379.950`                                   |
| `undiscounted_price` | Precio con descuento aplicado                                           | string       | -                       | `$265.965`                                   |
| `description`     | Descripción general del producto                                           | string       | -                       | `"Los Adizero Adios Pro 3 son la ..."`        |
| `category`        | Categoría asignada al producto por la tienda                               | string       | Hombre, Mujer, Running  | `Mujer • Running`                            |
| `createdAt`       | Fecha y hora de creación del registro                                      | datetime     | -                       | `'_seconds': 1731975445`                     |
| `characteristics` | Características adicionales, como materiales o tecnologías utilizadas      | string       | -                       | `Parte superior de malla diseñada...`        |
| `gender`          | Género objetivo del producto                                               | string       | Hombre, Mujer, Unisex   | `Mujer`                                      |

## Fuente de los datos

Los datos están disponibles mediante una API conectada a Firebase, la cual permite consultar y extraer los registros en tiempo real.