# Diccionario de datos

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