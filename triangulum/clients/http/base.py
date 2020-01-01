import aiohttp

from triangulum.clients.util import random_user_agent


class HttpBaseClient:
    def __init__(
        self,
        msid: str = None,
        session_key: str = None,
        session: aiohttp.ClientSession = None,
        headers: dict = None
    ):
        self.session = session if session else aiohttp.ClientSession()
        self.headers = {
            'User-Agent': random_user_agent()
        } if not session else {}
        self.headers.update(headers or {})

        self.msid = msid
        self.session_key = session_key

    async def close(self):
        await self.session.close()

    async def save_cookies(self, filepath: str) -> None:
        self.session.cookie_jar.save(filepath)

    async def load_cookies(self, filepath: str) -> None:
        self.session.cookie_jar.load(filepath)

    async def _get(self, url):
        return await self.session.get(url=url)

    async def _post(self, url, data):
        return await self.session.post(url=url, data=data)
