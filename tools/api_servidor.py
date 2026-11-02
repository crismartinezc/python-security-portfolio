from fastapi import FastAPI
import sqlite3
import os

app = FastAPI(
    title="Python Security & Forensic API",
    version="2.0.0",
    description="API backend conectada a base de datos relacional para auditoría de ciberseguridad."
)

# Función auxiliar para conectar a la base de datos de forma segura
def obtener_conexion():
    # Aseguramos la ruta correcta hacia la carpeta database
    ruta_db = os.path.join(os.path.dirname(__file__), "../database/seguridad.db")
    conexion = sqlite3.connect(ruta_db)
    return conexion

@app.get("/")
def leer_raiz():
    return {
        "estado": "ONLINE",
        "sistema": "Backend de Ciberseguridad y Auditoría",
        "autor": "Chris"
    }

# Endpoint que consulta los registros reales de SQLite
@app.get("/auditoria/logs")
def consultar_logs_seguridad():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        # Consultamos la tabla de auditoría que creamos previamente
        cursor.execute("SELECT id, timestamp, evento, nivel_riesgo FROM auditoria_accesos")
        filas = cursor.fetchall()
        conexion.close()
        
        # Transformamos los resultados a una estructura JSON limpia para la web
        lista_logs = []
        for fila in filas:
            lista_logs.append({
                "id": fila[0],
                "timestamp": fila[1],
                "evento": fila[2],
                "nivel_riesgo": fila[3]
            })
            
        return {
            "total_registros": len(lista_logs),
            "registros": lista_logs
        }
        
    except Exception as error:
        return {"error": f"No se pudo acceder a la base de datos: {str(error)}"}