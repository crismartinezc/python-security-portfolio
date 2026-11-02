from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# Configuramos un sistema de logging profesional de nivel empresarial
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("SecurityAPI")

app = FastAPI(
    title="Python Security & Forensic API",
    version="2.2.0",
    description="API backend de alto rendimiento con logging profesional y persistencia relacional."
)

class SecurityEvent(BaseModel):
    evento: str
    nivel_riesgo: str

def obtener_conexion():
    db_path = os.getenv("DATABASE_PATH", "database/seguridad.db")
    ruta_db = os.path.join(os.path.dirname(__file__), "..", db_path)
    conexion = sqlite3.connect(ruta_db)
    return conexion

@app.get("/")
def leer_raiz():
    logger.info("Petición recibida en el endpoint raíz (GET /)")
    return {
        "status": "ONLINE",
        "system": "Cybersecurity & Forensic Backend",
        "environment": os.getenv("APP_ENV", "production"),
        "author": "Chris"
    }

@app.get("/auditoria/logs")
def consultar_logs_seguridad():
    try:
        logger.info("Consultando registros de auditoría en la base de datos...")
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
            
        logger.info(f"Se consultaron {len(lista_logs)} registros exitosamente.")
        return {
            "total_records": len(lista_logs),
            "logs": lista_logs
        }
    except Exception as error:
        logger.error(f"Error al conectar con la base de datos: {str(error)}")
        return {"error": f"Database error: {str(error)}"}

@app.post("/auditoria/logs")
def registrar_incidente(incidente: SecurityEvent):
    try:
        logger.warning(f"¡Alerta de seguridad recibida! Nivel: {incidente.nivel_riesgo} - Evento: {incidente.evento}")
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        timestamp_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT INTO auditoria_accesos (timestamp, evento, nivel_riesgo)
            VALUES (?, ?, ?)
        """, (timestamp_actual, incidente.evento, incidente.nivel_riesgo))
        
        conexion.commit()
        conexion.close()
        
        logger.info("Incidente registrado y persistido en SQLite correctamente.")
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
        logger.error(f"Error crítico al registrar incidente: {str(error)}")
        raise HTTPException(status_code=500, detail=f"Error al registrar incidente: {str(error)}")