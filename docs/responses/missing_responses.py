import os

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

from triangulum.controllers.lobby.achievements import Achievements
from triangulum.controllers.lobby.cache import Cache as LobbyCache
from triangulum.controllers.lobby.dual import Dual
from triangulum.controllers.lobby.gameworld import Gameworld
from triangulum.controllers.lobby.login import Login as LobbyLogin
from triangulum.controllers.lobby.notification import Notification
from triangulum.controllers.lobby.player import Player as LobbyPlayer
from triangulum.controllers.lobby.sitter import Sitter


def action(controller):
    return [i for i in dir(controller) if not i.startswith('__') and i != 'invoke_action']


actions = {
    'gameworld': {
        'Player': action(Player),
        'FarmList': action(FarmList),
        'Logger': action(Logger),
        'Troops': action(Troops),
        'Village': action(Village),
        'Cache': action(Cache),
        'Quest': action(Quest),
        'Error': action(Error),
        'Auctions': action(Auctions),
        'Hero': action(Hero),
        'Building': action(Building),
        'Trade': action(Trade),
        'Ranking': action(Ranking),
        'Kingdom': action(Kingdom),
        'Map': action(Map),
        'Reports': action(Reports),
        'Society': action(Society),
        'PremiumFeature': action(PremiumFeature),
        'Payment': action(Payment),
        'KingdomTreaty': action(KingdomTreaty),
        'Login': action(Login)
    },
    'lobby': {
        'Achievements': action(Achievements),
        'Cache': action(LobbyCache),
        'Dual': action(Dual),
        'Gameworld': action(Gameworld),
        'Login': action(LobbyLogin),
        'Notification': action(Notification),
        'Player': action(LobbyPlayer),
        'Sitter': action(Sitter)
    }
}

for scope, controllers in actions.items():
    for controller, actions in controllers.items():
        for action in actions:
            if not os.path.exists(f'docs/responses/{scope}/{controller}/{action}.json'):
                print(f'{scope}.{controller}.{action}')
