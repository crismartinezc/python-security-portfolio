evidencia = {
    "nombre archivo" : "contrasenias.txt",
    "tamanio_kb" : 45,
    "tipo" : "texto plano",
    "cuarentena" : True
    }

print(f"el archivo {evidencia['nombre archivo']} de tipo {evidencia['tipo']} ha sido aislado {evidencia['cuarentena']}")
evidencia["hash"] = "a1b2c3d4_falsificado"