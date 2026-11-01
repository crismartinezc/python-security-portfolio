# Definimos una Clase profesional para nuestro toolkit de ciberseguridad
class AuditorSeguridad:
    
    # 1. El Constructor: inicializa los datos base del objeto (como el objetivo a auditar)
    def __init__(self, objetivo, operador):
        self.objetivo = objetivo
        self.operador = operador
        print(f"[*] Inicializando toolkit de auditoría para el objetivo: {self.objetivo}")
        print(f"[*] Operador a cargo: {self.operador}\n")

    # 2. Método (función de la clase) para simular un análisis
    def escanear_puertos(self):
        print(f"[+] Ejecutando escaneo de puertos en {self.objetivo}...")
        puertos_abiertos = [22, 80, 443] # Puertos críticos simulados
        return puertos_abiertos

    # 3. Método para generar un reporte con los resultados
    def generar_reporte(self):
        puertos = self.escanear_puertos()
        print(f"[+] REPORTE OFICIAL:")
        print(f" -> Objetivo auditado: {self.objetivo}")
        print(f" -> Puertos activos detectados: {puertos}")
        print(f" -> Auditor responsable: {self.operador}")
        print("[+] Análisis concluido y verificado.\n")


print("=== INICIO DEL SISTEMA OOP ===")

# Instanciamos (creamos) objetos concretos a partir de nuestra Clase
auditor_1 = AuditorSeguridad("192.168.1.100", "Chris")
auditor_1.generar_reporte()

# Podemos crear otro objeto totalmente independiente con otros datos en segundos
auditor_2 = AuditorSeguridad("servidor-produccion.local", "Admin_Sec")
auditor_2.generar_reporte()

print("=== FIN DEL SISTEMA OOP ===")