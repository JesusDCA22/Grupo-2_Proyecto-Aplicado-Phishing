# ===========================
# Importación de Librerías
# ===========================

# Librerías para manejo de datos
import os  # Para operaciones con el sistema de archivos
import pandas as pd  # Para análisis y manipulación de datos

# Librerías para realizar solicitudes a la API
import requests  # Para hacer solicitudes HTTP

# Librerías para visualización de datos
import matplotlib.pyplot as plt  # Para gráficos básicos
import seaborn as sns  # Para gráficos avanzados y mapas de calor

# Librerías para manejo de excepciones
import warnings  # Para controlar advertencias
warnings.filterwarnings("ignore")  # Opcional, para evitar mensajes de advertencia

# Configuración opcional para gráficos (opcional pero útil)
plt.style.use('ggplot')  # Estilo para gráficos de Matplotlib
sns.set_theme(style="whitegrid")  # Estilo para gráficos de Seaborn



def load_data(filepath):
    """
    Carga los datos desde un archivo Excel.
    
    :param filepath: Ruta del archivo Excel.
    :return: DataFrame con los datos cargados.
    """
    try:
        df = pd.read_excel(filepath)
        print(f"Datos cargados exitosamente desde {filepath}.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None


def summarize_data(df):
    """
    Imprime un resumen general de los datos.
    
    :param df: DataFrame con los datos.
    """
    print("Resumen General de los Datos")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    print("\nPrimeras filas del DataFrame:")
    print(df.head())
    print("\nInformación del DataFrame:")
    print(df.info())
    print("\nEstadísticas descriptivas:")
    print(df.describe(include='all'))


def check_missing_values(df):
    """
    Verifica valores faltantes en el DataFrame.
    
    :param df: DataFrame con los datos.
    :return: DataFrame con el porcentaje de valores faltantes por columna.
    """
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100
    missing_summary = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_percent})
    print("\nValores Faltantes:")
    print(missing_summary[missing_summary['Missing Values'] > 0])
    return missing_summary


def plot_numeric_distributions(df):
    """
    Grafica la distribución de las variables numéricas.
    
    :param df: DataFrame con los datos.
    """
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns].hist(figsize=(15, 10), bins=20)
    plt.suptitle("Distribuciones de Variables Numéricas", fontsize=16)
    plt.tight_layout()
    plt.show()


def analyze_categorical_data(df, column_name):
    """
    Analiza las categorías de una columna específica.
    
    :param df: DataFrame con los datos.
    :param column_name: Nombre de la columna categórica.
    """
    if column_name in df.columns:
        counts = df[column_name].value_counts()
        print(f"\nAnálisis de la columna '{column_name}':")
        print(counts)
        counts.plot(kind='bar', title=f"Distribución de {column_name}")
        plt.show()
    else:
        print(f"La columna '{column_name}' no existe en el DataFrame.")


def plot_correlations(df):
    """
    Muestra un mapa de calor con las correlaciones entre variables numéricas.
    
    :param df: DataFrame con los datos.
    """
    numeric_df = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_df.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title("Mapa de Calor de Correlaciones")
    plt.show()


def check_duplicates(df):
    """
    Verifica y muestra registros duplicados en el DataFrame.
    
    :param df: DataFrame con los datos.
    :return: Número de registros duplicados.
    """
    duplicates = df.duplicated().sum()
    print(f"Número de registros duplicados: {duplicates}")
    if duplicates > 0:
        print("\nRegistros duplicados:")
        print(df[df.duplicated()])
    return duplicates