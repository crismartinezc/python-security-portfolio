import sqlite3
import os

print("[*] Iniciando gestión de base de datos SQLite para ciberseguridad...\n")

# 1. Conectarnos a una base de datos local (si no existe, Python la crea automáticamente)
conexion = sqlite3.connect("seguridad.db")
cursor = conexion.cursor()

# 2. Crear una tabla profesional estructurada para auditoría de accesos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS auditoria_accesos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        evento TEXT,
        nivel_riesgo TEXT
    )
""")
print("[+] Tabla 'auditoria_accesos' verificada o creada con éxito.")

# 3. Insertar un registro simulando un evento de seguridad detectado por nuestros scripts
cursor.execute("""
    INSERT INTO auditoria_accesos (timestamp, evento, nivel_riesgo)
    VALUES ('2026-11-01 20:30:00', 'Intento de acceso fallido detectado en puerto 22', 'ALTO')
""")

# ¡Fundamental! Hacemos un commit para guardar los cambios permanentemente en el disco
conexion.commit()
print("[+] Nuevo registro de seguridad insertado en la base de datos.")

# 4. Consultar (Leer) los registros almacenados en la base de datos
print("\n[+] Consultando historial de auditoría desde SQLite:")
cursor.execute("SELECT * FROM auditoria_accesos")
registros = cursor.fetchall()

for reg in registros:
    print(f" -> ID: {reg[0]} | Fecha: {reg[1]} | Evento: {reg[2]} | Nivel de Riesgo: {reg[3]}")

# 5. Cerrar la conexión para liberar recursos del sistema
conexion.close()
print("\n[+] Conexión a la base de datos cerrada de forma segura.")