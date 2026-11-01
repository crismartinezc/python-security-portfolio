# Importamos el módulo 'os' (Operating System) de Python
import os

print("[*] Consultando información del sistema operativo...\n")

# 1. Ver en qué directorio (carpeta) estamos parados actualmente
directorio_actual = os.getcwd()
print(f"Directorio de trabajo actual: {directorio_actual}")

# 2. Listar todos los archivos que hay en esta carpeta de manera automatizada
print("\n[+] Archivos encontrados en el workspace:")
archivos_en_carpeta = os.listdir(directorio_actual)

for archivo in archivos_en_carpeta:
    # Filtramos para mostrar solo los archivos de Python (.py)
    if archivo.endswith(".py"):
        print(f" -> Script detectado: {archivo}")

print("\n[+] Interacción con el sistema operativo completada con éxito.")
