import requests

from triangulum.clients.http.util import random_user_agent


class HttpBaseClient:
    def __init__(
        self,
        msid: str = None,
        session_key: str = None,
        session: requests.Session = None,
        proxies: dict = None,
        headers: dict = None
    ):
        self.session = session if session else requests.Session()
        self.session.headers['User-Agent'] = random_user_agent() if not session else self.session.headers['User-Agent']
        self.session.headers.update(headers or {})
        self.proxies = proxies

        self.msid = msid
        self.session_key = session_key

    def _get(self, url):
        response = self.session.get(url=url, proxies=self.proxies)
        return response

    def _post(self, url, data):
        response = self.session.post(url=url, data=data, proxies=self.proxies)
        return response
