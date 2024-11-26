from scripts.data_acquisition.api_reader import ApiReader

def main():
    # Crear instancia de ApiReader
    api_url = "https://scraping-firestore-178159629911.us-central1.run.app//v1/scraping/"
    output_path = "src/comparative_analysis/database/raw_data.xlsx"
    
    api_reader = ApiReader(api_url, output_path)
    
    # Leer datos de la API y guardar en Excel
    api_reader.fetch_and_save_data()

if __name__ == "__main__":
    main()
