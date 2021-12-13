import requests
from tests.settings import URL, HEADERS


class ApiClient:

    def get_find_by_status(self, params, path="/v2/pet/findByStatus"):
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
            params=params
        )
        response.raise_for_status()
        return response

    def get_by_id(self, params, path="/stations/{station_id}"):
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response
