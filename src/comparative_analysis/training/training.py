import pandas as pd

# Ruta del archivo de Excel
ruta_excel = r"C:\Users\cdgn2\OneDrive\Escritorio\Maestría\Maestria\Metodologias Agiles\Proyecto\Comparative-analysis-of-products\src\comparative_analysis\database\Adidas_etiquetado.xlsx"

# Crear el DataFrame
df = pd.read_excel(ruta_excel, header=0)

# Mostrar las primeras filas del DataFrame
print(df.head())