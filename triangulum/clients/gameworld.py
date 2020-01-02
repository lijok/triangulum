import json
import aiohttp

from triangulum.clients.http.base import HttpBaseClient
from triangulum.clients.routing import URL
from triangulum.clients.util import find_token, timestamp, get_cookie
from triangulum.controllers.gameworld.player import Player
from triangulum.controllers.gameworld.farm_list import FarmList
from triangulum.controllers.gameworld.logger import Logger
from triangulum.controllers.gameworld.troops import Troops
from triangulum.controllers.gameworld.village import Village
from triangulum.controllers.gameworld.cache import Cache
from triangulum.controllers.gameworld.quest import Quest
from triangulum.controllers.gameworld.error import Error
from triangulum.controllers.gameworld.auctions import Auctions
from triangulum.controllers.gameworld.hero import Hero
from triangulum.controllers.gameworld.building import Building
from triangulum.controllers.gameworld.trade import Trade
from triangulum.controllers.gameworld.ranking import Ranking
from triangulum.controllers.gameworld.kingdom import Kingdom
from triangulum.controllers.gameworld.map import Map
from triangulum.controllers.gameworld.reports import Reports
from triangulum.controllers.gameworld.society import Society
from triangulum.controllers.gameworld.premium_feature import PremiumFeature
from triangulum.controllers.gameworld.payment import Payment
from triangulum.controllers.gameworld.kingdom_treaty import KingdomTreaty
from triangulum.controllers.gameworld.login import Login
from triangulum.utils.exceptions import NotAuthenticated


class GameworldClient(HttpBaseClient):
    def __init__(
        self,
        gameworld_id: str,
        gameworld_name: str,
        session: aiohttp.ClientSession
    ):
        super().__init__(session=session)

        self.gameworld_id = gameworld_id
        self.gameworld_name = gameworld_name.lower()

        self.player = Player(action_handler=self.invoke_action)
        self.farm_list = FarmList(action_handler=self.invoke_action)
        self.logger = Logger(action_handler=self.invoke_action)
        self.troops = Troops(action_handler=self.invoke_action)
        self.village = Village(action_handler=self.invoke_action)
        self.cache = Cache(action_handler=self.invoke_action)
        self.quest = Quest(action_handler=self.invoke_action)
        self.error = Error(action_handler=self.invoke_action)
        self.auctions = Auctions(action_handler=self.invoke_action)
        self.hero = Hero(action_handler=self.invoke_action)
        self.building = Building(action_handler=self.invoke_action)
        self.trade = Trade(action_handler=self.invoke_action)
        self.ranking = Ranking(action_handler=self.invoke_action)
        self.kingdom = Kingdom(action_handler=self.invoke_action)
        self.map = Map(action_handler=self.invoke_action)
        self.reports = Reports(action_handler=self.invoke_action)
        self.society = Society(action_handler=self.invoke_action)
        self.premium_eature = PremiumFeature(action_handler=self.invoke_action)
        self.payment = Payment(action_handler=self.invoke_action)
        self.kingdom_treaty = KingdomTreaty(action_handler=self.invoke_action)
        self.login = Login(action_handler=self.invoke_action)

    @property
    def session_key(self):
        cookie = get_cookie(
            session=self.session,
            key='t5SessionKey',
            domain=f'{self.gameworld_name}.kingdoms.com',
            unquote=True
        )
        if cookie:
            return json.loads(cookie)['key']

    async def is_authenticated(self, extensive_check=False):
        """Checks whether user is authenticated with the gameworld"""
        if not self.session_key or not self.msid:
            return False
        if extensive_check:
            try:
                if 'error' in await self.troops.get_markers():
                    return False
            except json.decoder.JSONDecodeError:
                return False

        return True

    async def authenticate(self) -> None:
        """Authenticates with the gameworld"""
        if not await self.is_authenticated(extensive_check=True):
            response = await self._get(
                URL.GAMEWORLD_JOIN.format(gameworld_id=self.gameworld_id, msid=self.msid)
            )
            token = find_token(await response.text())

            _ = await self._get(
                URL.GAMEWORLD_AUTH.format(gameworld=self.gameworld_name, token=token, msid=self.msid)
            )

    async def invoke_action(self, action: str, controller: str, params: dict = None) -> dict:
        if not await self.is_authenticated():
            raise NotAuthenticated

        response = await self._post(
            url=f'{URL.GAMEWORLD_API.format(gameworld=self.gameworld_name)}/?c={controller}&a={action}&t{timestamp()}',
            data=json.dumps(
                {
                    'action': action,
                    'controller': controller,
                    'params': params if params else {},
                    'session': self.session_key
                }
            )
        )

        return await response.json()
