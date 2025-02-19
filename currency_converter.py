def listar_monedas_disponibles(tasas: dict) -> list:
    return list(tasas.keys())


def calcular_tasa_conversion(tasas: dict, moneda_origen: str,
                             moneda_destino: str) -> float:
    return tasas[moneda_destino] / tasas[moneda_origen]


def convertir_moneda(tasas: dict, moneda_origen: str, moneda_destino: str,
                     cantidad: float) -> float:
    tasa_conversion = calcular_tasa_conversion(tasas, moneda_origen,
                                               moneda_destino)
    return cantidad * tasa_conversion
