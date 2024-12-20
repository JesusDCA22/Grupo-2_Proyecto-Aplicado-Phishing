import os
import requests
import pandas as pd

class ApiReader:
    def __init__(self, api_url, output_path):
        """
        Inicializa el objeto ApiReader con la URL de la API y la ruta de salida.
        
        :param api_url: URL de la API
        :param output_path: Ruta donde se guardará el archivo Excel
        """
        self.api_url = api_url
        self.output_path = output_path

    def fetch_data(self):
        """
        Realiza la solicitud GET a la API y devuelve los datos en formato JSON.
        
        :return: Datos JSON de la API
        :raises Exception: Si la solicitud falla
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error al obtener datos de la API: {response.status_code}")

    def save_to_excel(self, data):
        """
        Guarda los datos en un archivo Excel.
        
        :param data: Datos en formato JSON
        """
        # Crear un DataFrame con los datos
        df_raw = pd.DataFrame(data)
        
        # Asegurarse de que la carpeta de salida exista
        output_dir = os.path.dirname(self.output_path)
        os.makedirs(output_dir, exist_ok=True)
        
        # Guardar el DataFrame en un archivo Excel
        df_raw.to_excel(self.output_path, index=False)
        print(f"Datos guardados exitosamente en {self.output_path}")

    def fetch_and_save_data(self):
        """
        Realiza la lectura de datos desde la API y los guarda en un archivo Excel.
        """
        try:
            data = self.fetch_data()
            self.save_to_excel(data)
        except Exception as e:
            print(f"Error: {e}")
