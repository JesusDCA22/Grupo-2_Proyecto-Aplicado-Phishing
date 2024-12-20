# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** (nombre que se le ha dado al modelo)
- **Plataforma de despliegue:** Railway
- **Requisitos técnicos:** [Requirements.txt](/scripts/training/requirements.txt)
- **Requisitos de seguridad:** 
- **Diagrama de arquitectura:** 

## Código de despliegue

- **Archivo principal:** Chatbot_V4
- **Rutas de acceso a los archivos:** [Link para archivo Chatbot_V3.ipyn donde se despliega el modelo](/scripts/training/Chatbot_V3.ipynb)

## Documentación del despliegue

- **Instrucciones de instalación:** 
1. Clona el repositorio de tu modelo:   
```git clone https://github.com/wmarin-tech/tdsp_template/tree/Laura```
2. Configura el archivo requirements.txt
3. Crea un proyecto en Railway:
4. Inicia sesión en Railway.
5. Haz clic en "New Project" y selecciona "Deploy from GitHub repo".
6. Selecciona tu repositorio subido en GitHub.
7. Railway detectará automáticamente el archivo requirements.txt y creará el entorno de Python.
8. Configura el comando de inicio del servidor: En el panel de Railway, ve a la pestaña de configuración y agrega el siguiente comando en "Start Command":
```uvicorn app:app --host 0.0.0.0 --port $PORT```
9. Despliega el proyecto: Railway instalará las dependencias automáticamente y desplegará tu aplicación.

- **Instrucciones de configuración:** 
1. Configura las variables de entorno (opcional): Si tu modelo necesita claves API u otras configuraciones, puedes agregarlas en la sección "Variables de entorno" de Railway:
Ve a "Variables".
2. Agrega las claves necesarias en formato KEY=VALUE.
Define los recursos necesarios:
Railway asigna recursos automáticamente, pero si el modelo es pesado, verifica los límites de RAM y CPU en el plan que estás utilizando.
3. Verifica las dependencias de Transformers: Railway utiliza máquinas en la nube, por lo que todas las dependencias de Python definidas en el archivo requirements.txt deben estar correctamente especificadas.
4. Habilita los logs para depuración: Ve a la pestaña de logs en Railway para monitorear la ejecución de tu aplicación y verificar que el servidor de FastAPI esté activo.
- **Instrucciones de uso:** 