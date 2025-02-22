import freecurrencyapi


class CurrencyApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._client = freecurrencyapi.Client(self.api_key)

    def check_status(self):
        return self._client.status()

    def get_exchange_rates(self, base_currency: str) -> dict:
        result = self._client.latest(base_currency=base_currency)
        return result["data"]
