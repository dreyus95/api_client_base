import base64
import urllib

import requests


class ApiMethodsInterface(object):

    def __init__(self):
        """
        Constructor. Nothing to do here.
        """
        print("[ApiMethodsInterface] __init__")

    def generate_endpoint(self, api_url: str = "", query_string: str = '') -> str:
        """
        Generates an endpoint URL string.
        :param api_url: API URL extension, to be added to the BASE_URL.
        :param query_string: dictionary with additional filters, if any.
        :return: full endpoint URL.
        """
        raise NotImplementedError("This is an abstract class, please use derived classes.")

    def request(self, endpoint: str, method: str = "GET", headers: dict = {},
                data: dict = {}) -> requests.models.Response:
        """
        Perform a request.
        :param endpoint: URL string.
        :param method: request type, currently supporting GET/POST/PUT.
        :param headers: request headers dictionary.
        :param data: request data dictionary.
        :return: Response object, must be handled from the caller side.
        """
        raise NotImplementedError("This is an abstract class, please use derived classes.")

    # METHODS
    def get_all(self, **kwargs) -> requests.models.Response:
        """
        GET request - X - all.
        :param kwargs: Keyword Arguments

        Keyword Arguments
        -----------------
        -
        -
        -
        -----------------
        :return: Response object, must be handled from the caller side.
        """
        endpoint = self.generate_endpoint(api_url="...",
                                          query_string=urllib.parse.urlencode(kwargs))
        method = "GET"
        headers = {
            "Authorization": "Basic {}".format(base64.b64encode("...".encode('ascii')).decode('ascii')),
            "Accept": 'application/json',
            'Content-Type': 'application/json'
        }
        data = {}

        return self.request(endpoint, method=method, headers=headers, data=data)

    def get_by_id(self, by_id: int) -> requests.models.Response:
        """
        GET request - X - single by id.
        :param by_id: (int) id.
        :return: Response object, must be handled from the caller side.
        """
        endpoint = self.generate_endpoint(api_url=".../{}".format(by_id))
        method = "GET"
        headers = {
            "Authorization": "Basic {}".format(base64.b64encode("...".encode('ascii')).decode('ascii')),
            "Accept": 'application/json',
            'Content-Type': 'application/json'
        }
        data = {}

        return self.request(endpoint, method=method, headers=headers, data=data)

    def post_by_id(self, by_id: int, **kwargs) -> requests.models.Response:
        """
        POST request - X - single by id.
        :param by_id: (int) id.
        :param kwargs: Keyword Arguments

        Keyword Arguments
        -----------------
        -
        -
        -
        -----------------
        :return: Response object, must be handled from the caller side.
        """
        endpoint = self.generate_endpoint(api_url=".../{}".format(by_id))
        method = "POST"
        headers = {
            "Authorization": "Basic {}".format(base64.b64encode("...".encode('ascii')).decode('ascii')),
            "Accept": 'application/json',
            'Content-Type': 'application/json'
        }
        data = kwargs

        return self.request(endpoint, method=method, headers=headers, data=data)

    def put_by_id(self, by_id: int, **kwargs) -> requests.models.Response:
        """
        PUT request - X - single by id.
        :param by_id: (int) id.
        :param kwargs: Keyword Arguments

        Keyword Arguments
        -----------------
        -
        -
        -
        -----------------
        :return: Response object, must be handled from the caller side.
        """
        endpoint = self.generate_endpoint(api_url=".../{}".format(by_id))
        method = "PUT"
        headers = {
            "Authorization": "Basic {}".format(base64.b64encode("...".encode('ascii')).decode('ascii')),
            "Accept": 'application/json',
            'Content-Type': 'application/json'
        }
        data = kwargs

        return self.request(endpoint, method=method, headers=headers, data=data)

    def delete_by_id(self, by_id: int) -> requests.models.Response:
        """
        DELETE request - X - single by id.
        :param by_id: (int) id.
        :return: Response object, must be handled from the caller side.
        """
        endpoint = self.generate_endpoint(api_url=".../{}".format(by_id))
        method = "DELETE"
        headers = {
            "Authorization": "Basic {}".format(base64.b64encode("...".encode('ascii')).decode('ascii')),
            "Accept": 'application/json',
            'Content-Type': 'application/json'
        }
        data = {}

        return self.request(endpoint, method=method, headers=headers, data=data)
