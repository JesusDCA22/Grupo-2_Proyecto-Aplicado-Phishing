# Definición de los datos

## Origen de los datos

- Los documentos se obtienen de una página web de intermediarios de una compañía de seguros. 
Son 18 documentos que se encuentran en formato PDF. En promedio cada documento tiene 2 MB de tamaño para un total de 36 MB.
Los documentos se encuentran en español y corresponden a procedimientos de una empresa de seguros.

- Nuestro proyecto tiene tipo de análisis no supervisado por lo tanto no se tiene una variable objetivo ni etiquetas; tampoco se tienen variables adicionales y los documentos son tipo PDFs con información no estructurada. Para la lectura y manipulación de los documentos se utiliza la libreria PyMuPDF.
 

## Especificación de los scripts para la carga de datos

- [Chatbot](/docs/scripts/preprocessing/Chatbot_preprocessing.ipynb) se encuentra el analisis exploratorio de los datos, en este se incluye la eliminación de los stop words para un analisis más claro y consiso, si embargo, ese paso es obviado en la obtención de datos para el modelo puesto que el Chatbot necesita las stop word para dar mejores respuestas.

**Descripción**: Primero, se utilizan comandos “wget” para descargar 18 archivos PDF desde Google Drive, cada comando “wget” toma un enlace y guarda el archivo descargado con un nombre específico en el sistema local.
Aquí se muestra un ejemplo de uno de estos comandos:

`!wget 'https://drive.google.com/uc?id=19jXdP0q6XikFyge-lfCeSYqARkcZQnwy&export=download' -O 'pdf01.pdf'  # 0.Guia de Actividades Autonomas .pdf`

Una vez descargados todos los archivos, se calcula el tamaño total de los mismos. Para ello, se utiliza un bucle “for” que itera sobre los archivos PDF descargados, en cada iteración y se determina el tamaño utilizando "os.stat(pdf_filename).st_size".
Finalmente, se convierte el tamaño total de bytes a megabytes y se muestra en pantalla.

**El total es 33.6 megas cargados.**

La función "preprocess" recibe un texto y aplica una serie de transformaciones para limpiar y estandarizar el contenido:
1. Compilación de Patrones con "re.compile"
2. Primero se utilizan dos patrones regulares (regex) compilados para facilitar el procesamiento del texto.
3. El primero coincide con cualquier carácter que no sea una palabra (\w), un espacio (\s) o el símbolo de porcentaje (%).
4. El segundo coincide con dos o más espacios consecutivos.
5. Reemplazo de Cadenas Específicas:
	Se eliminan o modifican ciertas cadenas específicas del texto
	Se eliminan cadenas con fechas y códigos específicos que contienen los PDFs en cada salto de pagina.
    Se aplica la normalización del texto para convertir caracteres acentuados a sus equivalentes sin acento y convertir todo el texto a minúsculas:
    Se reemplazan palabras específicas para ocultar o evitar datos sensibles. 
    Se buscan todas las URLs presentes en el texto y se reemplazan temporalmente con identificadores "URL{i}":
    Se eliminación de Caracteres Especiales y se reemplaza múltiples espacios por un solo espacio.
    Se eliminan los saltos de línea y retornos de carro.
    Finalmente, se restauran las URLs originales en el texto.
    La función retorna el texto procesado.

Esta rutina asegura que el texto esté limpio y en un formato consistente para su posterior procesamiento o análisis. 

### Base de datos de destino

- Los archivos se cargan y se utilizan en el mismo Collab.
