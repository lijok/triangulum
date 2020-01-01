import json
import aiohttp

from triangulum.clients.http.base import HttpBaseClient
from triangulum.clients.routing import URL
from triangulum.clients.gameworld import GameworldClient
from triangulum.clients.util import find_token, find_msid, get_cookie
from triangulum.controllers.lobby.achievements import Achievements
from triangulum.controllers.lobby.cache import Cache
from triangulum.controllers.lobby.dual import Dual
from triangulum.controllers.lobby.gameworld import Gameworld
from triangulum.controllers.lobby.login import Login
from triangulum.controllers.lobby.notification import Notification
from triangulum.controllers.lobby.player import Player
from triangulum.controllers.lobby.sitter import Sitter


class LobbyClient(HttpBaseClient):
    def __init__(
        self,
        cookie_file: str = None,
        headers: dict = None
    ):
        super().__init__(cookie_file=cookie_file, headers=headers)

        self.achievements = Achievements(action_handler=self.invoke_action)
        self.cache = Cache(action_handler=self.invoke_action)
        self.dual = Dual(action_handler=self.invoke_action)
        self.gameworld = Gameworld(action_handler=self.invoke_action)
        self.login = Login(action_handler=self.invoke_action)
        self.notification = Notification(action_handler=self.invoke_action)
        self.player = Player(action_handler=self.invoke_action)
        self.sitter = Sitter(action_handler=self.invoke_action)

    @property
    def gl5_session_key(self):
        return json.loads(
            get_cookie(
                session=self.session,
                key='gl5SessionKey',
                domain='kingdoms.com',
                unquote=True
            )
        )['key']

    async def is_authenticated(self):
        """Checks whether user is authenticated with the lobby portal"""

        if 'error' in await self.gameworld.get_possible_new_gameworlds():
            return False
        else:
            return True

    async def authenticate(self, email: str, password: str) -> None:
        """Authenticates with the lobby portal"""

        response = await self._get(URL.LOBBY_AUTH)
        self.add_cookie(
            key='msid',
            value=find_msid(await response.text()),
            domain='https://kingdoms.com'
        )

        response = await self._post(
            url=URL.LOBBY_AUTH_STEP_2.format(msid=self.msid),
            data={'email': email, 'password': password}
        )
        token = find_token(await response.text())
        _ = await self._get(URL.LOBBY_AUTH_STEP_3.format(token=token, msid=self.msid))

    async def connect_to_gameworld(self, gameworld_id: str, gameworld_name: str) -> GameworldClient:
        """Connect to a gameworld"""

        gameworld_client = GameworldClient(
            gameworld_id=gameworld_id,
            gameworld_name=gameworld_name,
            session=self.session
        )
        await gameworld_client.authenticate()

        return gameworld_client

    async def invoke_action(self, action: str, controller: str, params: dict = None) -> dict:
        response = await self._post(
            url=URL.LOBBY_API,
            data=json.dumps(
                {
                    'action': action,
                    'controller': controller,
                    'params': params if params else {},
                    'session': self.gl5_session_key
                }
            )
        )

        return await response.json()
