import json

import requests

from src.api_methods import ApiMethodsInterface


class ApiClient(ApiMethodsInterface):
    BASE_URL = 'https://...'

    def __init__(self) -> None:
        """
        Constructor.
        """
        print("[ApiClient] __init__")
        super(ApiMethodsInterface, self).__init__()

    def request(self, endpoint: str, method: str = "GET", headers: dict = {},
                data: dict = {}) -> requests.models.Response:
        print("{}\t{}\t{}".format(method, endpoint, headers))
        if method == "GET":
            return requests.get(endpoint, headers=headers, data=json.dumps(data))
        elif method == "POST":
            return requests.get(endpoint, headers=headers, data=json.dumps(data))
        elif method == "PUT":
            return requests.get(endpoint, headers=headers, data=json.dumps(data))
        elif method == "DELETE":
            return requests.delete(endpoint, headers=headers, data=json.dumps(data))
        elif method == "PATCH":
            return requests.patch(endpoint, headers=headers, data=json.dumps(data))
        else:
            raise ValueError("Unsupported method requested: {}".format(method))

    def generate_endpoint(self, api_url: str = "", query_string: str = '') -> str:
        querystring = ''
        if len(query_string):
            querystring += "?" + query_string
        # print("Query String: {}".format(querystring))
        endpoint = '{}/{}{}'.format(self.BASE_URL, api_url, querystring)
        # print("Endpoint: {}".format(endpoint))
        return endpoint
