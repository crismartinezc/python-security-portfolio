# Simulamos una tarea de auditoría que intenta abrir un archivo crítico de sistema
print("[*] Buscando archivo de credenciales o logs del sistema...")

try:
    # Intentamos abrir un archivo que sabemos que quizás no exista
    archivo_critico = open("archivo_confidencial_inexistente.txt", "r")
    contenido = archivo_critico.read()
    print(contenido)
    archivo_critico.close()

except FileNotFoundError:
    # Si ocurre un error de tipo "Archivo no encontrado", Python salta acá en vez de romperse
    print("[!] ALERTA: El archivo buscado no se encuentra en el directorio.")
    print("[*] Generando registro de advertencia y continuando con la ejecución...")

print("[+] El programa finalizó de forma segura y controlada (sin crashearse).")