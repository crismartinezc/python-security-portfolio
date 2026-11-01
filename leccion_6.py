# Una función que recibe una dirección IP y simula verificar si es segura o sospechosa
def evaluar_ip(direccion_ip):
    # Supongamos que la IP "192.168.1.100" está en una lista negra simulada
    if direccion_ip == "192.168.1.100":
        return "¡ALERTA! IP sospechosa detectada (Maliciosa)"
    else:
        return "IP segura (Tráfico limpio)"

# Llamamos a la función y guardamos lo que nos "devuelve" (return) en una variable
resultado_1 = evaluar_ip("192.168.1.50")
resultado_2 = evaluar_ip("192.168.1.100")

# Mostramos los resultados obtenidos
print(resultado_1)
print(resultado_2)