# --- SIMULACIÓN DE ANÁLISIS FORENSE (BLUE TEAM) ---

# 1. Creamos una lista con registros de logs simulados de un servidor
registros_servidor = [
    "INFO: Usuario admin inició sesión correctamente desde 192.168.1.50",
    "WARNING: Intento de acceso fallido con contraseña incorrecta desde 203.0.113.42",
    "WARNING: Intento de acceso fallido con contraseña incorrecta desde 203.0.113.42",
    "ALERTA CRÍTICA: Múltiples fallos de autenticación (Fuerza Bruta) detectados desde 203.0.113.42 en puerto 22",
    "INFO: Usuario soporte técnico realizó mantenimiento rutinario",
]

print("[*] Iniciando motor de análisis forense y revisión de logs...")

# 2. Procesamos el archivo y filtramos las alertas críticas
hallazgos_criticos = []

for linea in registros_servidor:
    # Buscamos si la línea contiene la palabra "ALERTA" o "WARNING"
    if "ALERTA" in linea or "WARNING" in linea:
        hallazgos_criticos.append(linea)

# 3. Generamos automáticamente el dictamen pericial en un archivo de texto
archivo_dictamen = open("dictamen_pericial.txt", "w")
archivo_dictamen.write("=== DICTAMEN TÉCNICO FORENSE - INFORME DE INCIDENTE ===\n")
archivo_dictamen.write("Analista a cargo: Chris\n")
archivo_dictamen.write("Objetivo: Auditoría de registros de acceso y detección de intrusiones.\n\n")
archivo_dictamen.write("ANOMALÍAS Y AMENAZAS DETECTADAS:\n")

# Escribimos cada hallazgo detectado en el archivo del dictamen
for alerta in hallazgos_criticos:
    archivo_dictamen.write(f"-> {alerta}\n")

archivo_dictamen.close()

print("[+] ¡Análisis completado con éxito!")
print("[+] Se ha generado y guardado el archivo 'dictamen_pericial.txt' en el disco.")