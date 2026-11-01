import urllib.request
import json
import ssl

print("[*] Iniciando auditoría automatizada de conectividad y endpoints...")

# Endpoint de prueba para simular una verificación de estado de servidor
url_servidor = "https://jsonplaceholder.typicode.com/users/1"

# Contexto de seguridad para entornos de desarrollo local en macOS
contexto_seguro = ssl._create_unverified_context()

try:
    # Realizamos la petición HTTP GET al servidor objetivo
    respuesta = urllib.request.urlopen(url_servidor, context=contexto_seguro)
    codigo_estado = respuesta.getcode()
    
    # Validamos si el servidor responde de manera óptima (Código 200)
    if codigo_estado == 200:
        print(f"[+] ÉXITO: El servidor respondió con estado HTTP {codigo_estado} (ONLINE).")
        
        # Procesamos la respuesta JSON del servidor
        datos_brutos = respuesta.read().decode("utf-8")
        datos_json = json.loads(datos_brutos)
        
        print("\n[+] Extracción de metadatos del sistema remoto:")
        print(f" -> Nombre de Usuario / Entidad: {datos_json.get('name')}")
        print(f" -> Correo de contacto: {datos_json.get('email')}")
        print(f" -> Sitio Web: {datos_json.get('website')}")
        
    else:
        print(f"[!] ADVERTENCIA: El servidor respondió con un código inusual: {codigo_estado}")

except urllib.error.URLError as error_red:
    print(f"[!] ERROR CRÍTICO DE RED: No se pudo establecer conexión -> {error_red.reason}")
except Exception as error_general:
    print(f"[!] ERROR INESPERADO: {error_general}")

print("\n[+] Auditoría de red finalizada de forma segura.")