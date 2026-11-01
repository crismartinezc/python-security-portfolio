edad_texto = input("¿Cuántos años tenés? ")
edad = int(edad_texto)
if edad >= 18:
    print("Puedes ingresar a la zona VIP y adquirir tu entrada.")
else:
    print("Lo siento, acceso exclusivo para mayores de edad.")