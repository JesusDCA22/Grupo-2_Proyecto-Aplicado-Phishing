import re
import pandas as pd
from io import StringIO

class ResponseProcessor:
    def __init__(self, labels_with_definitions):
        self.labels_with_definitions = labels_with_definitions

    def procesar_respuesta(self, respuesta_texto):
        try:
            # Extraer solo los nombres de las etiquetas
            etiquetas = [label for label, _ in self.labels_with_definitions]
            # Limpiar los nombres de las etiquetas
            etiquetas_limpias = [
                re.sub(r"[ ,;{}()\n\t=]", "_", etiqueta.strip()) for etiqueta in etiquetas
            ]

            # Buscar el inicio de la tabla
            inicio_tabla = respuesta_texto.find('|')
            if inicio_tabla == -1:
                print("No se encontró una tabla en la respuesta.")
                return None

            # Extraer la tabla desde el primer '|'
            tabla_texto = respuesta_texto[inicio_tabla:].strip()
            # Extraer solo las líneas que contengan '|'
            lineas = tabla_texto.split('\n')
            lineas_tabla = []
            for linea in lineas:
                if '|' in linea:
                    linea = linea.strip().strip('|').strip()
                    lineas_tabla.append(linea)
                else:
                    break

            if not lineas_tabla:
                print("No se encontraron líneas válidas de tabla.")
                return None

            # Verificar si hay separadores '---'
            tiene_separador = any(
                all(c.strip('-') == '' for c in fila.split('|')) 
                for fila in lineas_tabla
            )

            # Caso 1: Hay separadores (modo normal de Markdown)
            if tiene_separador:
                tabla_completa = '\n'.join(lineas_tabla)
                df = pd.read_csv(StringIO(tabla_completa), sep='|', engine='python', skipinitialspace=True)
                df.columns = [re.sub(r"[ ,;{}()\n\t=]", "_", col.strip()) for col in df.columns]
                for col in df.columns:
                    if df[col].dtype == object:
                        df[col] = df[col].str.strip()
                df = df.reset_index(drop=True)
                return df

            # Caso 2: No hay separadores
            if len(lineas_tabla) == 2:
                # Primera línea columnas, segunda datos
                columnas = [re.sub(r"[ ,;{}()\n\t=]", "_", c.strip()) for c in lineas_tabla[0].split('|')]
                datos = [c.strip() for c in lineas_tabla[1].split('|')]
                df = pd.DataFrame([datos], columns=columnas)
                for col in df.columns:
                    if df[col].dtype == object:
                        df[col] = df[col].str.strip()
                df = df.reset_index(drop=True)
                return df
            elif len(lineas_tabla) == 1:
                # Solo datos, usar etiquetas limpias como columnas
                datos = [c.strip() for c in lineas_tabla[0].split('|')]
                if len(etiquetas_limpias) != len(datos):
                    print("Advertencia: El número de etiquetas no coincide. Se ajustará.")
                    col_names = etiquetas_limpias[:len(datos)]
                else:
                    col_names = etiquetas_limpias

                df = pd.DataFrame([datos], columns=col_names)
                for col in df.columns:
                    if df[col].dtype == object:
                        df[col] = df[col].str.strip()
                df = df.reset_index(drop=True)
                return df
            else:
                # Más de 2 líneas sin separador
                columnas = [re.sub(r"[ ,;{}()\n\t=]", "_", c.strip()) for c in lineas_tabla[0].split('|')]
                filas_datos = [ [x.strip() for x in fila.split('|')] for fila in lineas_tabla[1:] ]
                df = pd.DataFrame(filas_datos, columns=columnas)
                for col in df.columns:
                    if df[col].dtype == object:
                        df[col] = df[col].str.strip()
                df = df.reset_index(drop=True)
                return df

        except Exception as e:
            print(f"Error al procesar la tabla: {e}")
            return None
