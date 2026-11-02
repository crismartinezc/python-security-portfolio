from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os
from datetime import datetime

app = FastAPI(
    title="Python Security & Forensic API",
    version="2.1.0",
    description="API backend de alto rendimiento para auditoría y monitoreo de ciberseguridad con persistencia relacional."
)

# Modelo Pydantic para validar los datos que entran por POST de forma estricta
class SecurityEvent(BaseModel):
    evento: str
    nivel_riesgo: str

# Función auxiliar para conectar a la base de datos de forma segura
def obtener_conexion():
    ruta_db = os.path.join(os.path.dirname(__file__), "../database/seguridad.db")
    conexion = sqlite3.connect(ruta_db)
    return conexion

@app.get("/")
def leer_raiz():
    return {
        "status": "ONLINE",
        "system": "Cybersecurity & Forensic Backend",
        "author": "Chris"
    }

# Endpoint GET: Consulta los registros almacenados en SQLite
@app.get("/auditoria/logs")
def consultar_logs_seguridad():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, timestamp, evento, nivel_riesgo FROM auditoria_accesos")
        filas = cursor.fetchall()
        conexion.close()
        
        lista_logs = []
        for fila in filas:
            lista_logs.append({
                "id": fila[0],
                "timestamp": fila[1],
                "evento": fila[2],
                "nivel_riesgo": fila[3]
            })
            
        return {
            "total_records": len(lista_logs),
            "logs": lista_logs
        }
    except Exception as error:
        return {"error": f"Database error: {str(error)}"}

# Endpoint POST: Permite registrar un nuevo evento de seguridad en la base de datos
@app.post("/auditoria/logs")
def registrar_incidente(incidente: SecurityEvent):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        timestamp_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT INTO auditoria_accesos (timestamp, evento, nivel_riesgo)
            VALUES (?, ?, ?)
        """, (timestamp_actual, incidente.evento, incidente.nivel_riesgo))
        
        conexion.commit()
        conexion.close()
        
        return {
            "status": "SUCCESS",
            "message": "Incidente de seguridad registrado correctamente en la base de datos",
            "data": {
                "timestamp": timestamp_actual,
                "evento": incidente.evento,
                "nivel_riesgo": incidente.nivel_riesgo
            }
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al registrar incidente: {str(error)}")