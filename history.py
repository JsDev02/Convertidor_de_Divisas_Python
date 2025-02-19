from colors import color


class HistorialConversiones:
    def __init__(self):
        self._historial = []

    def agregar(self, operacion: str):
        self._historial.append(operacion)

    def mostrar(self):
        if self._historial:
            print(color["subtitulo"] + "\nHistorial de conversiones: \n")
            for operacion in self._historial:
                print(operacion)
        else:
            print(color["info"])
            print("No hay historial de conversiones.")
