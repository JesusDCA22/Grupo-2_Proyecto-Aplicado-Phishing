import pandas as pd
import requests
import json

def consume_endpoint(data, url="http://127.0.0.1:2626/predict"):
    """
    Envía una solicitud POST al endpoint con los datos proporcionados.

    Args:
        data (dict): Información en formato JSON a enviar.
        url (str): URL del endpoint.
    
    Returns:
        dict: Respuesta del servidor.
    """
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        # Verificar si la respuesta está vacía
        if response.status_code != 200:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
        
        # Intentar convertir la respuesta a JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"error": "Respuesta no es JSON válida", "response": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def process_excel_and_add_clusters(input_file_path, output_file_path):
    """
    Lee un archivo Excel, envía cada fila al endpoint, agrega una columna con el clúster
    y guarda el resultado en un nuevo archivo Excel.

    Args:
        input_file_path (str): Ruta del archivo Excel de entrada.
        output_file_path (str): Ruta donde se guardará el archivo Excel con los resultados.
    """
    try:
        # Cargar Excel en un DataFrame
        df = pd.read_excel(input_file_path, header=0)
        
        # Manejar celdas vacías (reemplazar por None)
        df = df.where(pd.notnull(df), None)
        
        # Nueva columna para clústeres
        clusters = []

        # Iterar sobre las filas del DataFrame
        for _, row in df.iterrows():
            # Convertir la fila a diccionario
            data = row.to_dict()
            
            # Consumir el endpoint y extraer la predicción
            response = consume_endpoint(data)
            cluster = response.get("prediction", None)  # Obtener el clúster de la respuesta
            clusters.append(cluster)
        
        # Agregar la columna al DataFrame
        df['Cluster'] = clusters

        # Guardar el DataFrame actualizado en un nuevo archivo Excel
        df.to_excel(output_file_path, index=False)
        print(f"Archivo guardado en: {output_file_path}")
    except Exception as e:
        print(f"Error procesando el archivo Excel: {e}")

# Ejecución
input_file_path = r"src\comparative_analysis\database\Decathlon.xlsx"
output_file_path = r"src\comparative_analysis\evaluation\DecathlonWithClusters.xlsx"
process_excel_and_add_clusters(input_file_path, output_file_path)