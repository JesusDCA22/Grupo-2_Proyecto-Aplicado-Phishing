import pandas as pd
import matplotlib.pyplot as plt

def analyze_clusters(file_path):
    """
    Analiza las métricas de distribución de los clústeres en el archivo Excel proporcionado.

    Args:
        file_path (str): Ruta del archivo Excel con los datos y clústeres.
    
    Returns:
        dict: Métricas clave de la distribución de clústeres.
    """
    try:
        # Leer el archivo Excel
        df = pd.read_excel(file_path)

        # Validar si la columna 'Cluster' existe
        if 'Cluster' not in df.columns:
            raise ValueError("La columna 'Cluster' no está presente en el archivo.")

        # Calcular métricas básicas
        cluster_counts = df['Cluster'].value_counts()
        total_elements = len(df)
        cluster_percentages = (cluster_counts / total_elements) * 100

        # Calcular métricas adicionales
        unique_clusters = cluster_counts.index.tolist()
        num_clusters = len(unique_clusters)
        max_cluster = cluster_counts.idxmax()
        min_cluster = cluster_counts.idxmin()

        # Resultados en un diccionario
        metrics = {
            "Número total de elementos": total_elements,
            "Número de clústeres únicos": num_clusters,
            "Distribución por clúster": cluster_counts.to_dict(),
            "Porcentaje por clúster": cluster_percentages.to_dict(),
            "Clúster con más elementos": {"Clúster": max_cluster, "Cantidad": cluster_counts[max_cluster]},
            "Clúster con menos elementos": {"Clúster": min_cluster, "Cantidad": cluster_counts[min_cluster]},
        }

        # Imprimir las métricas
        print("Métricas de distribución de clústeres:")
        for key, value in metrics.items():
            print(f"{key}: {value}")

        # Graficar la distribución de clústeres
        plt.figure(figsize=(10, 6))
        cluster_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Distribución de elementos por clúster")
        plt.xlabel("Clúster")
        plt.ylabel("Cantidad de elementos")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return metrics
    except Exception as e:
        print(f"Error al analizar los clústeres: {e}")
        return None

# Ejecución
file_path = r"src\comparative_analysis\evaluation\DecathlonWithClusters.xlsx"
analyze_clusters(file_path)