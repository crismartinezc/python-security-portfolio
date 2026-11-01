import urllib.request
import json
import ssl  # 1. Importamos el módulo ssl

print("[*] Iniciando consulta de red y petición HTTP...")

url_objetivo = "https://jsonplaceholder.typicode.com/todos/1"

# 2. Creamos un contexto que omite la validación estricta de certificados locales
contexto_inseguro = ssl._create_unverified_context()

try:
    # 3. Pasamos el contexto dentro de la función urlopen
    respuesta = urllib.request.urlopen(url_objetivo, context=contexto_inseguro)
    
    codigo_estado = respuesta.getcode()
    print(f"[+] Código de Estado HTTP recibido: {codigo_estado}")

    contenido_bytes = respuesta.read()
    contenido_texto = contenido_bytes.decode("utf-8")

    print("\n[+] Datos obtenidos del servidor remoto:")
    print(contenido_texto)

except Exception as error:
    print(f"[!] ALERTA DE RED: Ocurrió un fallo en la conexión -> {error}")

print("\n[+] Operación de red finalizada de forma segura.")