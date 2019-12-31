import json
import requests

from triangulum.clients.http.base import HttpBaseClient
from triangulum.clients.http.routing import URL
from triangulum.clients.gameworld import GameworldClient
from triangulum.clients.util import get_session_key, find_token, find_msid
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
            msid: str = None,
            session_key: str = None,
            session: requests.Session = None,
            proxies: dict = None,
            headers: dict = None,
            email: str = None,
            password: str = None
    ):
        super().__init__(
            msid=msid,
            session_key=session_key,
            session=session,
            proxies=proxies,
            headers=headers
        )

        if email and password:
            self.authenticate(email, password)

        self.achievements = Achievements(action_handler=self.invoke_action)
        self.cache = Cache(action_handler=self.invoke_action)
        self.dual = Dual(action_handler=self.invoke_action)
        self.gameworld = Gameworld(action_handler=self.invoke_action)
        self.login = Login(action_handler=self.invoke_action)
        self.notification = Notification(action_handler=self.invoke_action)
        self.player = Player(action_handler=self.invoke_action)
        self.sitter = Sitter(action_handler=self.invoke_action)

    def is_authenticated(self):
        """Checks whether user is authenticated with the lobby portal"""

        if 'error' in self.gameworld.get_possible_new_gameworlds():
            return False
        else:
            return True

    def authenticate(self, email: str, password: str) -> None:
        """Authenticates with the lobby portal"""

        response = self._get(URL.LOBBY_AUTH)
        self.msid = find_msid(response.text)

        response = self._post(
            url=URL.LOBBY_AUTH_STEP_2.format(msid=self.msid),
            data={'email': email, 'password': password}
        )
        token = find_token(response.text)
        _ = self._get(URL.LOBBY_AUTH_STEP_3.format(token=token, msid=self.msid))

        self.session_key = get_session_key(
            session=self.session,
            key_name='gl5SessionKey',
            domain='.kingdoms.com'
        )

    def connect_to_gameworld(self, gameworld_id: str, gameworld_name: str) -> GameworldClient:
        """Connect to a gameworld"""

        return GameworldClient(
            gameworld_id=gameworld_id,
            gameworld_name=gameworld_name,
            msid=self.msid,
            proxies=self.proxies
        )

    def invoke_action(self, action: str, controller: str, params: dict = None) -> dict:
        response = self._post(
            url=URL.LOBBY_API,
            data=json.dumps(
                {
                    'action': action,
                    'controller': controller,
                    'params': params if params else {},
                    'session': self.session_key
                }
            )
        )

        return response.json()
