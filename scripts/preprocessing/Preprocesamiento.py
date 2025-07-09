# Preprocesamiento de datos de phishing

import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import pearsonr, spearmanr, kendalltau
import matplotlib.pyplot as plt

# -----------------------------
# Análisis general del dataset
# -----------------------------

# Cantidad de documentos (sitios web)
num_documentos = data.shape[0]
print(f"El dataset tiene {num_documentos} sitios web (filas)")

# Características de las variables
def analyze_data_structure(df):
    analysis = {}
    for column in df.columns:
        col_info = {
            'dtype': str(df[column].dtype),
            'unique_values': df[column].nunique(),
            'sample_values': list(df[column].dropna().unique()[:3])
        }
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

# Mostrar resumen de cada variable
data_analysis = analyze_data_structure(data)
for col, info in data_analysis.items():
    print(f"\nColumna: {col}")
    print(f"Tipo: {info['dtype']} | Formato: {info['format']}")
    print(f"Valores únicos: {info['unique_values']}")
    print(f"Muestra de valores: {info['sample_values']}")

# Tamaño del conjunto de datos en memoria
def get_dataframe_size(df):
    return df.memory_usage(deep=True).sum() / (1024 ** 2)  # MB

data_size = get_dataframe_size(data)
print(f"Tamaño total en memoria: {data_size:.2f} MB")

# -----------------------------
# Revisión de calidad de datos
# -----------------------------

# Valores faltantes por columna
missing_counts = data.isnull().sum()
missing_percentage = (data.isnull().mean() * 100).round(2)
print("Valores faltantes por columna:")
print(pd.DataFrame({'Valores Faltantes': missing_counts, 'Porcentaje (%)': missing_percentage}).query("`Valores Faltantes` > 0"))

# Valores vacíos (texto en blanco)
text_columns = data.select_dtypes(include=['object']).columns
empty_values = {col: data[col].apply(lambda x: str(x).strip() == '').sum() for col in text_columns if data[col].apply(lambda x: str(x).strip() == '').sum() > 0}
if empty_values:
    print("\nRegistros con valores vacíos (texto):")
    for col, count in empty_values.items():
        print(f"- {col}: {count} registros vacíos")
else:
    print("\nNo se encontraron valores vacíos en columnas de texto")

# Detección de problemas de codificación en texto
def detect_encoding_problems(df, sample_size=100):
    encoding_problems = defaultdict(list)
    for col in df.select_dtypes(include=['object']).columns:
        sample_data = df[col].dropna().sample(min(sample_size, len(df)))
        for idx, value in enumerate(sample_data):
            try:
                str(value).encode('utf-8').decode('utf-8')
            except Exception as e:
                encoding_problems[col].append((idx, str(e)))
    return encoding_problems

# Detección de formatos mixtos en columnas
def detect_mixed_formats(df):
    format_issues = {}
    for col in df.columns:
        unique_types = set()
        sample = df[col].dropna().head(1000)
        for value in sample:
            if isinstance(value, str):
                if value.isdigit():
                    unique_types.add('string_numeric')
                elif value.replace('.', '', 1).isdigit():
                    unique_types.add('string_float')
                elif value.lower() in ('true', 'false'):
                    unique_types.add('string_bool')
                else:
                    unique_types.add('str')
            else:
                unique_types.add(type(value).__name__)
            if len(unique_types) > 1:
                format_issues[col] = {
                    'types': list(unique_types),
                    'example_mixed': sample.iloc[0:3].tolist()
                }
                break
    return format_issues

# Eliminar columnas constantes
data = data.loc[:, data.nunique() > 1]

# -----------------------------
# Análisis de correlación y PCA
# -----------------------------

def calculate_correlation(df):
    numeric_df = df.select_dtypes(include=[np.number])
    scaler = StandardScaler()
    normalized_df = pd.DataFrame(scaler.fit_transform(numeric_df), columns=numeric_df.columns)
    corr_methods = ['pearson', 'spearman', 'kendall']
    corr_fields_data = pd.DataFrame(columns = ['var1','var2','Method','Corr','P-value'])
    i = 0
    for col1 in normalized_df.columns:
        for col2 in normalized_df.columns:
            if col1 != col2:
                for method in corr_methods:
                    if method == 'pearson':
                        corr, pval = pearsonr(normalized_df[col1], normalized_df[col2])
                    elif method == 'spearman':
                        corr, pval = spearmanr(normalized_df[col1], normalized_df[col2])
                    elif method == 'kendall':
                        corr, pval = kendalltau(normalized_df[col1], normalized_df[col2])
                    corr_fields_data.loc[i] = [col1, col2, method, corr, pval]
                    i += 1
    return corr_fields_data

def matriz_corr_fields(corr_fields_data, p=0.75):
    corr_fields_data = corr_fields_data[(abs(corr_fields_data['Corr'])>p)&(corr_fields_data['P-value']<0.05)]
    return (
        corr_fields_data[corr_fields_data['Method']=='pearson'],
        corr_fields_data[corr_fields_data['Method']=='spearman'],
        corr_fields_data[corr_fields_data['Method']=='kendall']
    )

def assign_explained_variance_to_variables(df, pca):
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
    explained_variance = np.square(loadings).sum(axis=1)
    variance_explained_per_variable = explained_variance / explained_variance.sum()
    return pd.DataFrame({'Variable': df.columns,'Variance Explained': variance_explained_per_variable})

def select_var(matrix_corr_fields, variance_explained_df):
    df = matrix_corr_fields.merge(variance_explained_df, how='left', left_on='var1', right_on='Variable')
    df = df.rename(columns={'Variance Explained': 'var1_explained'}).drop(columns='Variable')
    df = df.merge(variance_explained_df, how='left', left_on='var2', right_on='Variable')
    df = df.rename(columns={'Variance Explained': 'var2_explained'}).drop(columns='Variable')
    df['ABS_Corr'] = abs(df['Corr'])
    df = df.sort_values('ABS_Corr', ascending=False)
    df['var1_win_var2'] = (df['var1_explained'] > df['var2_explained']).astype(int)
    porc_var1 = df.groupby('var1')['var1_win_var2'].mean().mul(100).reset_index()
    list1 = porc_var1.query("var1_win_var2 == 100")['var1']
    list2 = set(df[df['var1'].isin(list1)]['var2'])
    list3 = porc_var1.query("var1_win_var2 == 0")['var1']
    list4 = set(df['var1']) - set(list1) - set(list2) - set(list3)
    df['var_select'] = np.select([
        df['var1'].isin(list1),
        df['var1'].isin(list2),
        df['var1'].isin(list3),
        df['var1'].isin(list4)
    ], [1, -1, -1, -1])
    matrix_corr_fields3 = df[['var1', 'var_select']].drop_duplicates('var1')
    list_var_corr = list(matrix_corr_fields3.query("var_select == 1")['var1'])
    list_var_nocorr = list(set(variance_explained_df['Variable']) - set(matrix_corr_fields3['var1']))
    return list_var_corr, list_var_nocorr

def get_scalar_variables(df):
    return [col for col in df.select_dtypes(include=[np.number]).columns if len(df[col].dropna().unique()) > 2 or not set(df[col].dropna().unique()).issubset({0, 1})]

# Selección de variables
list_num = get_scalar_variables(data)
corr_fields_data = calculate_correlation(data[list_num])
matrix_corr_fields = matriz_corr_fields(corr_fields_data, p=0.85)[0]

# PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[list_num])
pca = PCA()
principal_components = pca.fit_transform(scaled_data)
df_pca = pd.DataFrame(principal_components, columns=[f'PC{i+1}' for i in range(principal_components.shape[1])])

# Gráfico de varianza explicada
plt.figure(figsize=(10, 5))
plt.bar(range(1, 11), pca.explained_variance_ratio_[:10], alpha=0.7, align='center', label='Varianza individual')
plt.step(range(1, 11), np.cumsum(pca.explained_variance_ratio_[:10]), where='mid', linestyle='--', color='red', label='Varianza acumulada')
plt.xlabel('Componentes Principales')
plt.ylabel('Proporción de Varianza Explicada')
plt.title('Varianza Explicada por Componente Principal')
plt.legend()
plt.grid(True)
plt.show()

# Variables con mayor varianza explicada
variance_explained_df = assign_explained_variance_to_variables(data[list_num], pca)

# Selección de variables a eliminar o conservar
columnas_a_eliminar, list_var_nocorr = select_var(matrix_corr_fields, variance_explained_df)
print("Columnas a eliminar:", columnas_a_eliminar)
print("Columnas no correlacionadas:", list_var_nocorr)

# Eliminación de columnas seleccionadas
data = data.drop(columns=columnas_a_eliminar)
print(data.shape)



