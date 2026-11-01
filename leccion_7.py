# Creamos un diccionario para almacenar los datos detallados de un incidente de red
incidente_seguridad = {
    "ip_origen": "192.168.1.100",
    "puerto": 22,
    "nivel_riesgo": "Alto",
    "bloqueado": True
}

# Mostramos el diccionario completo
print("Registro del incidente:", incidente_seguridad)

# Accedemos a valores específicos llamando a su clave entre corchetes
print(f"\nAnalizando IP de origen: {incidente_seguridad['ip_origen']}")
print(f"El nivel de amenaza es: {incidente_seguridad['nivel_riesgo']}")

# Podemos modificar o agregar nuevos datos sobre la marcha
incidente_seguridad["analista"] = "Chris"
print("\nDiccionario actualizado con el responsable:", incidente_seguridad)