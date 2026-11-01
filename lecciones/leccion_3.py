# Definimos la contraseña correcta
pin_secreto = "1234"
pin_ingresado = ""

# El bucle while se repite MIENTRAS el pin ingresado sea DISTINTO (!=) al secreto
while pin_ingresado != pin_secreto:
    pin_ingresado = input("Por favor, ingresa el PIN correcto: ")
    if pin_ingresado != pin_secreto:
        print("PIN incorrecto. Inténtalo de nuevo.")

print("¡Acceso concedido! Bienvenido al sistema.")