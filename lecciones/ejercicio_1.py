pin_secreto = "1234"

pin_secreto = input ("Ingrese su codigo PIN:")

print("¿Cual es el pin secreto?")
if pin_secreto == "1234":
    print("Acceso concedido. Bienvenido al sistema")
else:
    print("Alerta: Codigo incorrecto. Acceso denegado")