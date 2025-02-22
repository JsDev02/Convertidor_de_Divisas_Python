# Conversor de Monedas

Este proyecto es un conversor de monedas que utiliza la API de FreeCurrencyAPI para obtener tasas de cambio actualizadas.

## 1. Estructura del Proyecto

- **api_client.py:**  
  Contiene la clase `CurrencyApiClient`, que se encarga de gestionar la conexión con la API y provee métodos para verificar el estado y obtener las tasas de cambio.

- **currency_converter.py:**  
  Contiene funciones para listar monedas, calcular la tasa de conversión y convertir cantidades de una moneda a otra.

- **colors.py:**  
  Diccionario con valores de escape para imprimir colores en la consola.

- **history.py:**  
  Maneja un historial de conversiones para mostrar un registro de operaciones.

- **main.py:**  
  Punto de entrada de la aplicación. Ofrece un menú en consola para interactuar con las funcionalidades de conversión, listado de monedas, etc.

## 2. Requisitos

- Python 3.7 o superior.
- Dependencias necesarias:
  - `freecurrencyapi`
  - `flake8` (opcional, para verificar estilo)
- Biblioteca `unittest` (incluida en Python) para pruebas automatizadas.

## 3. Instalación

1. Clona el repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/JsDev02/Convertidor_de_Divisas_Python.git
   cd Convertidor_de_Divisas_Python
   ```

2. Instala las dependencias (usando uv):
   ```bash
   uv add freecurrencyapi
   uv add flake8
   ```

## 4. Ejecución

Para ejecutar el proyecto, simplemente ejecuta:
   ```bash
   uv run src/main.py
   ```

Se mostrará un menú en consola con las siguientes opciones:

1. Listado de monedas
2. Tasas de cambio
3. Convertir moneda
4. Mostrar historial de conversiones
5. Salir

## 5. Pruebas

Se incluye un archivo de pruebas unitarias para comprobar la lógica de conversión de divisas.

Para ejecutarlas:
   ```bash
   python -m unittest test.test_currency_converter
   ```
