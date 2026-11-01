# --- 1. ESCRIBIR EN UN ARCHIVO ---
# Abrimos un archivo en modo escritura ("w" de write). 
# Si el archivo no existe, Python lo crea automáticamente en tu compu.
archivo_reporte = open("reporte_seguridad.txt", "w")

archivo_reporte.write("--- REPORTE DE INCIDENTE FORENSE ---\n")
archivo_reporte.write("IP Analizada: 192.168.1.100\n")
archivo_reporte.write("Estado: Amenaza neutralizada y aislada.\n")

# ¡Siempre es una buena práctica cerrar el archivo al terminar de usarlo!
archivo_reporte.close()
print("¡Archivo 'reporte_seguridad.txt' creado y escrito con éxito!\n")

# --- 2. LEER UN ARCHIVO ---
# Abrimos el mismo archivo en modo lectura ("r" de read)
archivo_lectura = open("reporte_seguridad.txt", "r")

# Leemos todo el contenido de golpe usando .read()
contenido = archivo_lectura.read()

print("Leyendo el contenido desde el archivo guardado en el disco:")
print(contenido)

archivo_lectura.close()