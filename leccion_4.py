# Creamos una lista con nombres de herramientas o tecnologías que vamos a usar
herramientas = ["Python", "VS Code", "Terminal", "Git"]

# Mostramos la lista completa
print("Lista completa:", herramientas)

# En Python, cada elemento tiene una posición llamada "índice", empezando desde el 0:
# 0 = "Python"
# 1 = "VS Code"
# 2 = "Terminal"
# 3 = "Git"

# Accedemos a un elemento específico usando su índice entre corchetes
print("Primer elemento:", herramientas[0])
print("Tercer elemento:", herramientas[2])




# Tenemos nuestra lista inicial
herramientas = ["Python", "VS Code", "Terminal", "Git"]

# Agregamos una nueva herramienta a la lista usando .append()
herramientas.append("Docker")
print("Lista actualizada:", herramientas)

# Recorremos la lista completa automáticamente con un bucle 'for'
print("\nRecorriendo todas las herramientas:")
for herramienta in herramientas:
    print(f"- Usando la herramienta: {herramienta}")