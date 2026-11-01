# Definimos una función usando la palabra clave 'def' (de definición)
# Le ponemos un nombre descriptivo y entre paréntesis el dato que va a recibir (argumento)
def saludar_agente(nombre_agente):
    print(f"[ACCESO AUTORIZADO] Bienvenido al sistema forense, {nombre_agente}.")
    print("Iniciando protocolos de seguridad y análisis de logs...")

# --- Acá termina la definición de la función ---
# Para que la función haga algo, tenemos que "llamarla" o invocarla:

saludar_agente("Chris")
print("-" * 40)
saludar_agente("Oficial de Ciberseguridad")