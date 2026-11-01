import os

print("[*] Consultando información del sistema operativo...\n")

ruta_actual = os.getcwd()
print(f"Directorio de trabajo actual: {ruta_actual}")

print("\n[+] Archivos encontrados en el workspace:")
archivos_en_carpeta = os.listdir(ruta_actual)
for archivo in archivos_en_carpeta:
    if archivo.endswith(".py"):
        print(f" -> Script detectado: {archivo}")

print("\n[+] Interacción con el sistema operativo completada con éxito.")

archivo_dictamen = open("inventario_proyecto.txt", "w")