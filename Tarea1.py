# si ocurren problemas con la libreria, instalar libreria:
# pip install freecurrencyapi

import freecurrencyapi

API = "fca_live_C95X2ASB5R7mWyiX7gXI7k5W7xUjW9kinnmbeFVu"

client = freecurrencyapi.Client(API)

historial = []

# Colores para la consola
color = {
    'reset': "\033[0m",
    'titulo': "\033[38;5;81m",
    'menu': "\033[38;5;159m",
    'subtitulo': "\033[38;5;141m",
    'info': "\033[38;5;75m",
    'contenido': "\033[38;5;110m",
    'bye': "\033[32m",
    'error': "\033[38;5;208m",
    'error-api': "\033[31m"
    }


def obtener_tasas_de_cambio(divisa):
    result = client.latest(base_currency=divisa)
    return result['data']


def mostrar_monedas(tasas):
    print(color["subtitulo"] + "\nMonedas disponibles para convertir:")
    for moneda in tasas:
        print(color["info"])
        print(moneda)


def seleccionar_divisa(tasas):
    mostrar_monedas(tasas)
    divisa_seleccionada = input((
        f"{color["contenido"]} \nIngrese la divisa que quiere revisar: "
        f"{color['reset']}"
    )).upper()
    while divisa_seleccionada not in tasas:
        divisa_seleccionada = input((
            f"{color['error']}\nError. Ingrese una divisa válida: "
            f"{color['reset']}"
        )).upper()

    tasa_seleccionada = obtener_tasas_de_cambio(divisa_seleccionada)
    print(f"{color["subtitulo"]} \nTasas de cambio (en relación con "
          f"{color["reset"]}{divisa_seleccionada}{color["subtitulo"]}): ")
    mostrar_tasas(tasa_seleccionada)


def mostrar_tasas(tasa_seleccionada):
    for moneda, tasa in tasa_seleccionada.items():
        print(color["info"])
        print(f"{moneda}: {tasa} $")


def convertir_moneda(tasas, historial):
    mostrar_monedas(tasas)

    moneda_origen = input((
        f"{color["contenido"]} \nIngrese la moneda de origen: "
        f"{color["reset"]}")).upper()

    while moneda_origen not in tasas:
        moneda_origen = input((
            f"{color['error']}\nMoneda inválida. "
            f"Intente de nuevo la moneda de origen: "
            f"{color["reset"]}"
        )).upper()

    moneda_destino = input((
        f"{color["contenido"]} \nIngrese la moneda de destino: "
        f"{color["reset"]}")).upper()
    while moneda_destino not in tasas:
        moneda_destino = input((
            f"{color['error']} \nMoneda inválida. "
            f"Intente de nuevo la moneda de destino: "
            f"{color["reset"]}")).upper()

    while True:
        try:
            print(color["contenido"] + "\nIngrese la cantidad a convertir")
            cantidad = float(input(
                f"(los decimales se definen con punto. "
                f"no se admite cero o números negativos): "
                f"{color["reset"]}"))
            if cantidad <= 0:
                raise ValueError(f"{color['error']}"
                                 f"La cantidad debe ser mayor que cero.")
            break
        except ValueError:
            print(f"{color['error']}\nError en el valor ingresado. "
                  f"Intente de nuevo.")

    tasa_conversion = tasas[moneda_destino] / tasas[moneda_origen]
    resultado = cantidad * tasa_conversion

    print(color["info"])
    print(f"{color['reset']}{cantidad} {moneda_origen}{color['info']}"
          f" equivalen a {color['reset']}{resultado:.2f}"
          f" {moneda_destino}{color['info']}\n")

    historial.append(f"{color['reset']} {cantidad} {moneda_origen} "
                     f"{color['info']} convertido a {color['reset']} "
                     f"{moneda_destino} {color['info']} es igual a "
                     f"{color['reset']} {resultado:.2f}\n")


def mostrar_historial(historial):
    if historial:
        print(color["subtitulo"] + "\nHistorial de conversiones: \n")
        for operacion in historial:
            print(operacion)
    else:
        print(color["info"])
        print("No hay historial de conversiones.")


def main():
    try:
        client.status()
    except Exception:
        print(color["error-api"] + "\n Ocurrió un error con la API \n")
        return

    tasas = obtener_tasas_de_cambio('USD')

    while True:
        print(color['titulo'] + "\n   Menú")
        print(color['menu'] + "1. Listado de monedas")
        print("2. Tasas de cambio")
        print("3. Convertir moneda")
        print("4. Mostrar historial de conversiones")
        print("5. Salir\n")

        opcion = input(f"{color['reset']}Seleccione una opción "
                       f"(Escriba un número entre 1 y 5): ")
        if opcion == '1':
            mostrar_monedas(tasas)
        elif opcion == '2':
            seleccionar_divisa(tasas)
        elif opcion == '3':
            convertir_moneda(tasas, historial)
        elif opcion == '4':
            mostrar_historial(historial)
        elif opcion == '5':
            print(color['bye'] + "\n¡Adiós!\n")
            break
        else:
            print(f"{color['error']}\nOpción no válida. "
                  f"Escriba un número entre 1 y 5.\n")


if __name__ == "__main__":
    main()
