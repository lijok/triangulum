import aiohttp
import yarl

from triangulum.clients.util import random_user_agent, get_msid


class HttpBaseClient:
    def __init__(
        self,
        session: aiohttp.ClientSession = None,
        cookie_file: str = None,
        headers: dict = None
    ):
        self.session = session if session else aiohttp.ClientSession()
        self.headers = {
            'User-Agent': random_user_agent()
        } if not session else {}
        self.headers.update(headers or {})

        self.cookie_file = cookie_file
        if cookie_file:
            self.load_cookies(cookie_file)

    async def close(self):
        await self.session.close()

    def save_cookies(self, filepath: str) -> None:
        self.session.cookie_jar.save(filepath)

    def load_cookies(self, filepath: str) -> None:
        self.session.cookie_jar.load(filepath)

    def add_cookie(self, key: str, value: str, domain: str) -> None:
        self.session.cookie_jar.update_cookies(
            cookies={
                key: value
            },
            response_url=yarl.URL(domain)
        )

    @property
    def msid(self):
        return get_msid(self.session)

    async def _get(self, url):
        return await self.session.get(url=url)

    async def _post(self, url, data):
        return await self.session.post(url=url, data=data)
