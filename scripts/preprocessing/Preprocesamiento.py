# ¿Cuantos documentos tiene el dataset?
num_documentos = data.shape[0]
print(f"El dataset tiene {num_documentos} sitios web (filas)")


# Caracteristicas de las variables
def analyze_data_structure(df):
    analysis = {}

    for column in df.columns:
        col_info = {
            'dtype': str(df[column].dtype),
            'unique_values': df[column].nunique(),
            'sample_values': list(df[column].dropna().unique()[:3])
        }

        # Detección de patrones
        if df[column].astype(str).str.match(r'^https?://').any():
            col_info['format'] = 'URL'
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            col_info['format'] = 'datetime'
        elif pd.api.types.is_numeric_dtype(df[column]):
            col_info['format'] = 'numeric'
        else:
            col_info['format'] = 'text'

        analysis[column] = col_info

    return analysis

# Ejemplo de uso
data_analysis = analyze_data_structure(data)
for col, info in data_analysis.items():
    print(f"\nColumna: {col}")
    print(f"Tipo: {info['dtype']} | Formato: {info['format']}")
    print(f"Valores únicos: {info['unique_values']}")
    print(f"Muestra de valores: {info['sample_values']}")



# Tamaño del conjunot de datos en la memoria
def get_dataframe_size(df):
    memory_usage = df.memory_usage(deep=True).sum()
    return memory_usage / (1024 ** 2)  # Convertir a MB

data_size = get_dataframe_size(data)
print(f"Tamaño total en memoria: {data_size:.2f} MB")



# Calidad de los datos

# 1. Cálculo de valores faltantes por columna
missing_counts = data.isnull().sum()
missing_percentage = (data.isnull().mean() * 100).round(2)

print("Valores faltantes por columna:")
missing_info = pd.DataFrame({
    'Valores Faltantes': missing_counts,
    'Porcentaje (%)': missing_percentage
})
print(missing_info[missing_info['Valores Faltantes'] > 0])  # Solo muestra columnas con faltantes

# 2. Detección de valores "vacíos" en columnas de texto
text_columns = data.select_dtypes(include=['object']).columns

empty_values = {}
for col in text_columns:
    empty_count = data[col].apply(lambda x: str(x).strip() == '').sum()
    if empty_count > 0:
        empty_values[col] = empty_count

if empty_values:
    print("\nRegistros con valores vacíos (texto):")
    for col, count in empty_values.items():
        print(f"- {col}: {count} registros vacíos")
else:
    print("\nNo se encontraron valores vacíos en columnas de texto")

# Detección de documentos ilegibles, mal codificados o con problemas de formato

def detect_encoding_problems(df, sample_size=100):
    encoding_problems = defaultdict(list)

    text_columns = df.select_dtypes(include=['object']).columns

    for col in text_columns:
        problematic_rows = []

        sample_data = df[col].dropna().sample(min(sample_size, len(df)))
        for idx, value in enumerate(sample_data):
            try:
                str(value).encode('utf-8').decode('utf-8')
            except (UnicodeError, UnicodeEncodeError, UnicodeDecodeError) as e:
                problematic_rows.append((idx, str(e)))

        if problematic_rows:
            encoding_problems[col] = problematic_rows

    return encoding_problems

def detect_mixed_formats(df):
    format_issues = {}

    for col in df.columns:
        unique_types = set()

        # Muestra de valores no nulos
        sample = df[col].dropna().head(1000)

        for value in sample:
            value_type = type(value).__name__

            # Detección especial para strings
            if isinstance(value, str):
                if value.isdigit():
                    value_type = 'string_numeric'
                elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
                    value_type = 'string_float'
                elif value.lower() in ('true', 'false'):
                    value_type = 'string_bool'

            unique_types.add(value_type)

            if len(unique_types) > 1:
                break

        if len(unique_types) > 1:
            format_issues[col] = {
                'types': list(unique_types),
                'example_mixed': sample.iloc[0:3].tolist()
            }

    return format_issues


# Eliminar columnas constantes (todas las filas tienen el mismo valor)
data = data.loc[:, data.nunique() > 1]
print(data.shape)
data.head()
