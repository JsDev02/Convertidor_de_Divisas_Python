from api_client import CurrencyApiClient
from currency_converter import convertir_moneda
from history import HistorialConversiones
from colors import color


def mostrar_monedas(tasas: dict):
    print(color["subtitulo"] + "\nMonedas disponibles para convertir:")
    for moneda in tasas.keys():
        print(color["info"], moneda)


def mostrar_tasas(tasas: dict, divisa_base: str):
    print(f"{color['subtitulo']} \nTasas de cambio (en relación con "
          f"{color['reset']}{divisa_base}{color['subtitulo']}): "
          f"{color['reset']}")
    for moneda, tasa in tasas.items():
        print(color["info"] + f"{moneda}: {tasa} $")


def seleccionar_divisa(tasas: dict, client: CurrencyApiClient):
    mostrar_monedas(tasas)
    divisa_seleccionada = input((
        f"{color['contenido']} \nIngrese la divisa que quiere revisar: "
        f"{color['reset']}"
    )).upper()

    # Validación
    while divisa_seleccionada not in tasas:
        divisa_seleccionada = input((
            f"{color['error']}\nError. Ingrese una divisa válida: "
            f"{color['reset']}"
        )).upper()

    tasa_seleccionada = client.obtener_tasas_de_cambio(divisa_seleccionada)
    mostrar_tasas(tasa_seleccionada, divisa_seleccionada)


def convertir_moneda_ui(tasas: dict, historial: HistorialConversiones):
    mostrar_monedas(tasas)

    # Moneda de origen
    moneda_origen = input((
        f"{color['contenido']} \nIngrese la moneda de origen: "
        f"{color['reset']}")).upper()

    while moneda_origen not in tasas:
        moneda_origen = input((
            f"{color['error']}\nMoneda inválida. "
            f"Intente de nuevo la moneda de origen: "
            f"{color['reset']}"
        )).upper()

    # Moneda de destino
    moneda_destino = input((
        f"{color['contenido']} \nIngrese la moneda de destino: "
        f"{color['reset']}")).upper()
    while moneda_destino not in tasas:
        moneda_destino = input((
            f"{color['error']} \nMoneda inválida. "
            f"Intente de nuevo la moneda de destino: "
            f"{color['reset']}"
        )).upper()

    # Cantidad a convertir
    while True:
        try:
            print(color["contenido"] + "\nIngrese la cantidad a convertir")
            cantidad = float(input(
                f"(los decimales se definen con punto. "
                f"no se admite cero o números negativos): "
                f"{color['reset']}"))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")
            break
        except ValueError:
            print(f"{color['error']}\nError en el valor ingresado. "
                  f"Intente de nuevo.")

    resultado = convertir_moneda(tasas, moneda_origen,
                                 moneda_destino, cantidad)

    # Resultado
    print(color["info"])
    print(f"{color['reset']}{cantidad} {moneda_origen}{color['info']} "
          f"equivalen a {color['reset']}{resultado:.2f} "
          f"{moneda_destino}{color['info']}\n")

    # Guardar en historial
    operacion = (f"{color['reset']}{cantidad} {moneda_origen} "
                 f"{color['info']}convertido a{color['reset']} "
                 f"{moneda_destino}{color['info']} es igual a "
                 f"{color['reset']}{resultado:.2f}\n")
    historial.agregar(operacion)


def main():

    API_KEY = "fca_live_C95X2ASB5R7mWyiX7gXI7k5W7xUjW9kinnmbeFVu"
    client = CurrencyApiClient(API_KEY)

    historial = HistorialConversiones()

    # Disponibilidad de la API
    try:
        client.verificar_status()
    except Exception:
        print(color["error-api"] + "\nOcurrió un error con la API.\n")
        return

    # Obtenemos tasas iniciales (ej: USD como base)
    tasas = client.obtener_tasas_de_cambio('USD')

    while True:
        print(color['titulo'] + "\n   Menú")
        print(color['menu'] + "1. Listado de monedas")
        print("2. Tasas de cambio")
        print("3. Convertir moneda")
        print("4. Mostrar historial de conversiones")
        print("5. Salir\n")

        opcion = input(f"{color['reset']}Seleccione una opción (1-5): ")

        if opcion == '1':
            mostrar_monedas(tasas)
        elif opcion == '2':
            seleccionar_divisa(tasas, client)
        elif opcion == '3':
            convertir_moneda_ui(tasas, historial)
        elif opcion == '4':
            historial.mostrar()
        elif opcion == '5':
            print(color['bye'] + "\n¡Adiós!\n")
            break
        else:
            print(f"{color['error']}\nOpción no válida. "
                  f"Escriba un número entre 1 y 5.\n")


if __name__ == "__main__":
    main()
