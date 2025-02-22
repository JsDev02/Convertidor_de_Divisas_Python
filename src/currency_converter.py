def list_available_currencies(rates: dict) -> list:
    return list(rates.keys())


def calculate_conversion_rate(rates: dict, origin: str,
                              target: str) -> float:
    return rates[target] / rates[origin]


def convert_currency(rates: dict, origin: str, target: str,
                     amount: float) -> float:
    rate = calculate_conversion_rate(rates, origin, target)
    return amount * rate
