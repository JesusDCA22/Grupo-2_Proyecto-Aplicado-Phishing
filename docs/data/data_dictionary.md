# Diccionario de datos

## Estructura del dataset

| Variable          | Descripción                                                                 | Tipo de dato | Rango/Valores posibles      | Valor de ejemplo                               |
|--------------------|-----------------------------------------------------------------------------|--------------|-----------------------------|-----------------------------------------------|
| `id`              | Identificador único del producto                                           | string       | Único por producto          | `046zSiHm8Cz0fZYwMJlL`                        |
| `details`         | Detalles técnicos del producto                                             | string       | -                           | `{Horma clásica} {Parte superior sintética}`  |
| `store`           | Nombre de la tienda que vende el producto                                  | string       | adidas, nike, nacionrunner  | `adidas`                                      |
| `manufacturer`    | Marca o empresa que fabrica el producto                                    | string       | adidas, Asics,  nike, Hoka, otros         | `adidas`                                      |
| `url`             | URL del producto en la tienda                                              | string       | -                           | `https://www.adidas.co/...`                   |
| `title`           | Nombre o título del producto                                               | string       | -                           | `Tenis Duramo SL`                            |
| `regularPrice`    | Precio sin descuento                                                       | string       | Valores en COP    | `$379.950`                                   |
| `undiscounted_price` | Precio con descuento aplicado                                           | string       | Valores en COP    | `$265.965`                                   |
| `description`     | Descripción general del producto                                           | string       | -                           | `"Los Adizero Adios Pro 3 son la ..."`        |
| `category`        | Categoría asignada al producto por la tienda                               | string       | -    | `Mujer • Running`                            |
| `createdAt`       | Fecha y hora de creación del registro                                      | datetime     | -                   | `2023-12-05T10:30:00Z`                       |
| `characteristics` | Características adicionales, como materiales o tecnologías utilizadas      | string       | -                           | `Parte superior de malla diseñada...`        |
| `gender`          | Género objetivo del producto                                               | string       | Hombre, Mujer, Niño       | `Mujer`                                      |

## Fuente de los datos

Los datos están disponibles mediante una API conectada a Firebase. Cada registro se consulta y almacena de forma estructurada en un DataFrame para análisis posterior.
