import os
import re
import pandas as pd
import numpy as np
from tqdm import tqdm

from functions.prompt_generator import PromptGenerator
from functions.model_inference import ModelInference
from functions.response_processor import ResponseProcessor

# Definir las etiquetas con definiciones
labels_with_definitions = [
    ("Weight", "Indicates the lightness of the shoe, usually expressed in grams. Weight can influence performance and comfort during running."),
    ("Upper Material", "Describes the materials used in the shoe's upper part, such as mesh, synthetic leather, or technical fabrics, which affect breathability, flexibility, and support."),
    ("Midsole Material", "Refers to the compounds used in the midsole, such as EVA foams or proprietary technologies, which provide cushioning and shock absorption."),
    ("Outsole", "Details the type of rubber or material used in the sole and the traction pattern design, which influence grip and durability on various surfaces."),
    ("Cushioning System", "Specifies the technologies or materials aimed at reducing impact during strides, contributing to comfort and joint protection."),
    ("Drop (heel-to-toe differential)", "Indicates the height difference between the heel and the toe of the shoe, measured in millimeters. A higher drop typically offers more heel cushioning, while a lower drop promotes a more natural stride."),
    ("Pronation Type", "Classifies the shoe according to its suitability for different pronation types: neutral, overpronation, or supination. This is essential for choosing footwear that matches the runner's biomechanics."),
    ("Usage Type", "Defines the primary purpose of the shoe, such as daily training, racing, trail running, or casual use, guiding its specific design and features."),
    ("Gender", "Indicates whether the shoe is designed for men, women, or is a unisex model, considering anatomical and sizing differences."),
    ("Available Sizes", "Specifies the range of sizes in which the shoe is offered, ensuring the runner can find a suitable fit."),
    ("Width", "Some brands offer different widths (narrow, standard, wide) to accommodate various foot shapes."),
    ("Additional Technologies", "Includes special features such as waterproofing, reflectivity, customized fit systems, or stability elements that enhance the shoe's functionality."),
]

# Asumimos que spark está inicializado en el entorno
spark_df = spark.table("preprod_colombia.scraping_pp_adidas")
df_adidas = spark_df.toPandas()

# Crear lista de productos
productos = [
    {
        "id": row['id'],
        "regularPrice" : row["regularPrice"],
        "undiscounted_price": row["undiscounted_price"],
        "details": row['details_transformado'],
        "description": row['description'],
        "category": row['category'],
        "characteristics": row['characteristics']
    }
    for _, row in df_adidas.iterrows()
    if row['details_transformado'] != '{}'
]

# Instanciar las clases
prompt_generator = PromptGenerator(labels_with_definitions)
model_inference = ModelInference()
response_processor = ResponseProcessor(labels_with_definitions)

option_model = 2
dfs = []
for producto in tqdm(productos, desc="Procesando productos"):
    user_message = prompt_generator.generate_prompt(producto)
    respuesta = model_inference.obtener_respuesta(user_message, option_model)
    df = response_processor.procesar_respuesta(respuesta)

    if df is not None:
        attribute_columns = df.columns[:-3]  # Ajustar según cuántas columnas sean las de atributos
        df['id'] = producto['id']
        df['regularPrice'] = producto['regularPrice']
        df['undiscounted_price'] = producto['undiscounted_price']
        df["details"] = producto['details']
        df["description"] = producto['description']
        df["category"] = producto['category']
        df["characteristics"] = producto['characteristics']
        df = df[~df[attribute_columns].eq('---').all(axis=1)]
        df = df.dropna(how='all')
        dfs.append(df)
    else:
        print("No se pudo extraer la tabla.\n")

if dfs:
    df_total = pd.concat(dfs, ignore_index=True)
    # Guardar df_total como Excel
    os.makedirs("src/database", exist_ok=True)
    df_total.to_excel("src/database/df_total.xlsx", index=False)
else:
    print("Fail")
