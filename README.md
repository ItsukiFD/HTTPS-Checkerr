# HTTPS-Checker
Este programa ayuda a comprobar el estatus de una pagina web para confirmar si esta levantada o tumbada
Este programa permite verificar si un sitio web está en línea o no, enviando una solicitud HTTP y analizando la respuesta.

## 📌 Requisitos
- Python 3.x
- Módulo `requests` (si no lo tienes, instálalo con `pip install requests`).

## 🚀 Instalación y Configuración
1. Descarga el archivo `HTTPS-Checker.py` en tu computadora.
2. Asegúrate de tener Python instalado.
3. Instala el módulo `requests` si es necesario con el siguiente comando:
   ```sh
   pip install requests

-------------------------
## Ejemplo 

- Ingrese la URL del sitio web (con http/https): https://www.google.com
- El sitio está en línea ✅
- ¿Desea verificar otro sitio? (s/n): s
- 
- Ingrese la URL del sitio web (con http/https): https://www.ejemploinexistente.com
- No se pudo conectar con el sitio ❌
- ¿Desea verificar otro sitio? (s/n): n
