import requests

while True:
    url = input("Ingrese la URL del sitio web (con http/https): ").strip()

    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            print("El sitio está en línea ✅")
        else:
            print(f"El sitio respondió con código: {respuesta.status_code}")
    except requests.exceptions.RequestException:
        print("No se pudo conectar con el sitio ❌")

    if input("¿Desea verificar otro sitio? (s/n): ").strip().lower() != 's':
        break
