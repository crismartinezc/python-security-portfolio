archivo_nuevo = open("alerta_sistema.txt", "w")

archivo_nuevo.write("nombre de la herramienta\n")
archivo_nuevo.write("ip sospechosa detectada\n")
archivo_nuevo.write("nivel de severidad: alto\n")

archivo_nuevo.close()
print("¡Archivo 'alerta_sistema.txt' creado y escrito con éxito!\n")

read_archivo = open("alerta_sistema.txt", "r")

contenido = read_archivo.read()

print("Leyendo el contenido desde el archivo guardado en el disco:")
print(contenido)
read_archivo.close()