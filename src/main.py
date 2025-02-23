from api_client import CurrencyApiClient
from currency_converter import convert_currency
from history import ConversionHistory
from colors import color


def show_currencies(rates: dict):
    print(color["subtitle"] + "\nMonedas disponibles para convertir:")
    for currency in rates.keys():
        print(color["info"], currency)


def show_exchange_rates(rates: dict, base_currency: str):
    print(f"{color['subtitle']} \nTasas de cambio (en relación con "
          f"{color['reset']}{base_currency}{color['subtitle']}): "
          f"{color['reset']}")
    for currency, rate in rates.items():
        print(color["info"] + f"{currency}: {rate} $")


def select_currency(rates: dict, client: CurrencyApiClient):
    show_currencies(rates)
    selected_currency = input(
        f"{color['content']} \nIngrese la divisa que quiere revisar: "
        f"{color['reset']}"
    ).upper()

    # Validación
    while selected_currency not in rates:
        selected_currency = input(
            f"{color['error']}\nError. Ingrese una divisa válida: "
            f"{color['reset']}"
        ).upper()

    selected_rate = client.get_exchange_rates(selected_currency)
    show_exchange_rates(selected_rate, selected_currency)


def convert_currency_ui(rates: dict, history: ConversionHistory):

    show_currencies(rates)

    while True:
        # Moneda de origen
        origin = input(
            f"{color['content']} \nIngrese la moneda de origen: "
            f"{color['reset']}").upper()

        while origin not in rates:
            origin = input((
                f"{color['error']}\nMoneda inválida. "
                f"Intente de nuevo la moneda de origen: "
                f"{color['reset']}"
            )).upper()

        # Moneda de destino
        target = input((
            f"{color['content']} \nIngrese la moneda de destino: "
            f"{color['reset']}")).upper()
        while target not in rates:
            target = input((
                f"{color['error']} \nMoneda inválida. "
                f"Intente de nuevo la moneda de destino: "
                f"{color['reset']}"
            )).upper()

        # Verificar si son iguales
        if origin == target:
            print(f"{color['error']}\nLa moneda de origen y de "
                  f"destino deben ser distintas.")
            continue
        else:
            while True:
                try:
                    print(f"{color['content']}\nIngrese la cantidad "
                          f"a convertir")
                    amount = float(input(
                        f"(los decimales se definen con punto. "
                        f"no se admite cero o números negativos): "
                        f"{color['reset']}"))
                    if amount <= 0:
                        raise ValueError("La cantidad debe ser mayor a cero.")
                    break
                except ValueError:
                    print(f"{color['error']}\nError en el valor ingresado. "
                          f"Intente de nuevo.")

            result = convert_currency(rates, origin, target, amount)

            # Resultado
            print(color["info"])
            print(f"{color['reset']}{amount} {origin}{color['info']} "
                  f"equivalen a {color['reset']}{result:.2f} "
                  f"{target}{color['info']}\n")

            # Guardar en historial
            operation = (f"{color['reset']}{amount} {origin} "
                         f"{color['info']}convertido a{color['reset']} "
                         f"{target}{color['info']} es igual a "
                         f"{color['reset']}{result:.2f}\n")
            history.add_operation(operation)

            break


def main():
    API_KEY = "fca_live_C95X2ASB5R7mWyiX7gXI7k5W7xUjW9kinnmbeFVu"
    client = CurrencyApiClient(API_KEY)

    history = ConversionHistory()

    # Disponibilidad de la API
    try:
        client.check_status()
    except Exception:
        print(color["api_error"] + "\nOcurrió un error con la API.\n")
        return

    # Obtenemos tasas iniciales (ej: USD como base)
    rates = client.get_exchange_rates('USD')

    while True:
        print(color['title'] + "\n   Menú")
        print(color['menu'] + "1. Listado de monedas")
        print("2. Tasas de cambio")
        print("3. Convertir moneda")
        print("4. Mostrar historial de conversiones")
        print("5. Salir\n")

        option = input(f"{color['reset']}Seleccione una opción (1-5): ")

        if option == '1':
            show_currencies(rates)
        elif option == "2":
            select_currency(rates, client)
        elif option == "3":
            convert_currency_ui(rates, history)
        elif option == "4":
            history.show_history()
        elif option == "5":
            print(color['bye'] + "\n¡Adiós!\n")
            break
        else:
            print(f"{color['error']}\nOpción no válida. "
                  f"Escriba un número entre 1 y 5.\n")


if __name__ == "__main__":
    main()
