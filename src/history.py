from colors import color


class ConversionHistory:
    def __init__(self):
        self._history = []

    def add_operation(self, operation: str):
        self._history.append(operation)

    def show_history(self):
        if self._history:
            print(color["subtitle"] + "\nHistorial de conversiones:\n")
            for operation in self._history:
                print(operation)
        else:
            print(color["info"])
            print("No hay historial de conversiones.")
