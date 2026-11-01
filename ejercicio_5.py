def analizar_puerto(puerto):
    if puerto in [22, 80, 443]:
        return f"El puerto {puerto} está en la lista de puertos seguros."
    else:
        return f"El puerto {puerto} no está en la lista de puertos seguros."

# Llamamos a la función y mostramos los resultados
print(analizar_puerto(22))
print(analizar_puerto(8080))