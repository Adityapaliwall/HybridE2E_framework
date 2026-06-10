import requests

class BaseAPI:

    def get(self, url, headers=None):
        return requests.get(url, headers=headers)

    def post(self, url, headers=None, json=None):
        return requests.post(url, headers=headers, json=json)

    def put(self, url, headers=None, json=None):
        return requests.put(url, headers=headers, json=json)

    def delete(self, url, headers=None):
        return requests.delete(url, headers=headers)