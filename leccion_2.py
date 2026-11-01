# Pedimos la edad, pero la envolvemos en int() para convertir el texto a número entero
edad_texto = input("¿Cuántos años tenés? ")
edad = int(edad_texto)

# Evaluamos una condición con if / else
if edad >= 30:
    print("¡Ya estás pisando los 30 o más! Una gran etapa con mucha experiencia.")
else:
    print("¡Estás en plena juventud de los veintes!")