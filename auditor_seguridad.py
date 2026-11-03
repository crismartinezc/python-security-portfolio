import requests
import sys

def auditar_cabeceras(url):
    print(f"\n[*] Iniciando auditoría de seguridad para: {url}\n")
    
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
    except requests.exceptions.RequestException as e:
        print(f"[!] Error al conectar con el objetivo: {e}")
        sys.exit(1)

    # Cabeceras críticas de seguridad a verificar
    cabeceras_esperadas = {
        "Strict-Transport-Security": "Protege contra ataques de degradación de HTTPS (HSTS).",
        "Content-Security-Policy": "Mitiga ataques de Inyección de Código (XSS).",
        "X-Frame-Options": "Previene ataques de Clickjacking.",
        "X-Content-Type-Options": "Evita el sniffing de tipos MIME por parte del navegador.",
        "Server": "Revela información sensible sobre la tecnología del servidor."
    }

    print("-" * 60)
    for cabecera, descripcion in cabeceras_esperadas.items():
        if cabecera in headers:
            print(f"[+] [PRESENTE] {cabecera}")
            print(f"    Valor: {headers[cabecera]}")
        else:
            print(f"[-] [FALTA / ADVERTENCIA] {cabecera}")
            print(f"    Propósito: {descripcion}")
        print("-" * 60)

if __name__ == "__main__":
    # Puedes probar con cualquier URL de ejemplo, por ejemplo, https://google.com o una propia
    url_objetivo = input("Ingresa la URL a auditar (ej. https://ejemplo.com): ").strip()
    if not url_objetivo.startswith("http"):
        url_objetivo = "https://" + url_objetivo
    auditar_cabeceras(url_objetivo)