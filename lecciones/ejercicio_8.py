print("Buscando archivos credenciales en el sistema!")

try:
    with open("registro_faltante.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo 'registro_faltante.txt':")
        print(contenido)
except FileNotFoundError:
    print("[!] ADVERTENCIA: El registro de evidencias 'registro_faltante.txt' no esta disponible en el directorio.")
    print("[*] Generando registro de advertencia y continuando con la ejecución...")

    print("[+] El programa finalizó de forma segura y controlada (sin crashearse).")