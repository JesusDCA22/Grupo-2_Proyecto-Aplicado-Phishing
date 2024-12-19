# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:11:45 2024

@author: azaci
"""
# importar librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

class Utilities:
    image_path = r"..\\visualization\\clustering model//"

    def __init__(self):
        pass

    @staticmethod
    def null_or_zero_values(df):
        """"
        Función null_or_zero_values: Genera un resumen de los valores cero o nulos para las columnas de tipo numérico del dataframe
        
        Parámetros:
            df (dataframe): dataframe sobre el cual se realizara el análisis
            
        Return:
                data_table: Dataframe con el resultado del análisis
                
        Ejemplo:
                    
                >>> null_or_zero_values(df = df_icfes)
                   
                El tamaño del dataframe es 42 columnas y 3316179 filas.
                Cantidad de columnas con valores 0 o nulos: 32 
        ...
        """
        zero_val = (df == 0.00).astype(int).sum(axis=0)
        null_val = df.isnull().sum()
        null_val_percent = 100 * df.isnull().sum() / len(df)
        data_table = pd.concat([zero_val, null_val, null_val_percent], axis=1)
        data_table = data_table.rename(columns = {0 : 'Valores 0', 1 : 'Valores Nulos', 2 : '% Valores nulos'})
        data_table['Total valores 0 o nulos'] = data_table['Valores 0'] + data_table['Valores Nulos']
        data_table['% Total valores 0 o nulo'] = 100 * data_table['Total valores 0 o nulos'] / len(df)
        data_table['Tipo de Dato'] = df.dtypes
        data_table = data_table[data_table.iloc[:,1] != 0].sort_values('% Valores nulos', ascending=False).round(1)
        print ("El tamaño del dataframe es " + str(df.shape[1]) + " columnas y " + str(df.shape[0]) + " filas.\n"
               "Cantidad de columnas con valores 0 o nulos: " + str(data_table.shape[0]))
        return data_table

    @staticmethod
    def plot_col(df, col, ax, kde = False):
        """"
        Función plot_col: Genera gráfico de tipo Histplot para la columna que se indica
    
        Parámetros:
            df  (dataframe)    : Dataframe con los datos
            col (string)       : Columna del dataframe respecto a la cual se generará el histograma
            ax  (int)          : Posición en la que se mostrará el gráfico del histograma
            kde (boolean)      : Si True, se calcula Estimación de Densidad de Kernel (KDE), para representar una aproximación a la función 
                                 de densidad de probabilidad del conjunto de datos del dataframe y la columna indicados.
    
        Return:
            hist (sns.histplot): Objeto con el histograma generado
    
        Ejemplo:
    
            >>> plot = plot_col(df = df, col = col_age, ax = axs[0])

        """
        # Plotting a basic histogram
        sns.set(font_scale=0.5)
        hist = sns.histplot(data = df[col], kde = kde, color = 'blue', bins = 10, ax = ax)
        hist.set_title(col + ' Histogram', fontsize=8)
        return hist

    @staticmethod
    def plot_box(df, col, ax):
        """"
        Función plot_box: Genera gràfico de tipo Box para la columna que se indica
        
        Paràmetros:
        df  (dataframe)    : Dataframe con los datos
        col (string)       : Columna del dataframe respecto a la cual se generará el gráfico de caja
        ax  (int)          : Posición en la que se mostrará el gráfico de caja
    
        Return:
            hist (sns.boxplot): Objeto con el gráfico Box generado
    
        Ejemplo:
    
            >>> box  = plot_box(df = df_icfes, col = col_age, ax = axs[1])

        """
        #box = sns.boxplot(data = df, x = col, palette='afmhot', ax=ax)
        sns.set(font_scale=0.5)
        box = sns.boxplot(data = df, x = col, palette='Blues', ax=ax)
        # Adding labels and title
        box.set_xlabel(col, fontsize=8)
        box.set_title(col + ' Box plot', fontsize=8)
        return box

    @staticmethod
    def analyze_columns(df, cols, top_n = 999999):
        """"
        Función analyze_column: Realizar análisis sobre la columna del dataframe que se indica
                                Muestra estadísticas de la columna col_age, asi como gráficos de tipo Histplot y Boxplot
    
        Parámetros:
            df  (dataframe): Dataframe con los datos
            cola     (list): Lista de columnas del dataframe a analizar
    
        Return:
            None
    
        Ejemplo:
            
            >>> analyze_columns(df = df_icfes, cols = ['PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS'])
            ...
            """
        sns.set_style("whitegrid")
        sns.set_palette("pastel")
        new_row_group = {}
        if (len(cols) != 1):
            fig, axs = plt.subplots(nrows = len(cols), ncols = 1, figsize=(10,15))
        else:
            fig, ax = plt.subplots(figsize=(15,7))
        ind = 0
        for col in cols:
            new_row_group[col] = df.groupby([col])[col].count().sort_values(ascending=False).head(top_n)
            if (len(cols) != 1):
                plot = Utilities.plot_col(df = df, col = col, ax = axs[ind])
            else:
                plot = Utilities.plot_col(df = df, col = col, ax = ax)
            ind += 1
            plt.savefig(Utilities.image_path + col.replace("-","_") + ".png")
        plt.tight_layout()
        #
        data_table = pd.DataFrame             
        data_table = df[cols].describe(include="all")
        print("Estadisticas por columna")
        print(data_table.head(top_n))
        print("\nAgrupacion")
        print(new_row_group)
        #
        return None

    @staticmethod
    def preprocess(text, regex_list):
        """"
        Función preprocess: Preprocesamiento de texto

        Parámetros:
            text  (string)   : Dataframe con los datos
            regex_list (list): Columna del dataframe respecto a la cual se generará el histograma

        Return:
            preprocess_text (string): Cadena con el texto preprocesado

        Ejemplo:

            >>> preprocess_text = preprocess(texto, [special_chars, spaces], nlp)

        """
        #
        # Normalizamos el texto

        # Eliminamos caracteres especiales segun se indica en la lista de expresiones regulares
        for reg in regex_list:
            norm_text = re.sub(reg, "", text)

        preprocess_text = norm_text.strip()
        return preprocess_text