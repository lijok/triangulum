import inspect
import codecs
import jinja2
import json

from docstring_parser import parse

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


template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath='./docs/_templates')
)
TEMPLATE = template_env.get_template('action.jinja2')


# List of objects not to document
# TODO: Any members on this list should be made into private methods / functions
NODOC = [
    'invoke_action'
]


class DescriptionNotFoundError(Exception):
    """Description for a method argument was not found"""
    pass


def actions(controller):
    return [i for i in inspect.getmembers(controller) if not i[0].startswith('__') and i[0] not in NODOC]


def annotations(method, docstring):
    result = []
    for annotation_name, annotation_type in method.__annotations__.items():
        found = False
        if annotation_name != 'return':
            for arg in docstring.params:
                if arg.arg_name == annotation_name:

                    try:
                        _type = annotation_type.__name__
                    except AttributeError:
                        # Things such as typing.Union don't have __name__
                        # TODO: Express Unions as "One of" in docs
                        _type = str(annotation_type)

                    result.append(
                        {
                            'name': annotation_name,
                            'type': _type,
                            'description': arg.description
                        }
                    )
                    found = True
            else:
                if not found:
                    raise DescriptionNotFoundError(
                        f'No description found for {str(method)} {annotation_name} {annotation_type}'
                    )

    return result


actions = {
    'gameworld': {
        'Player': actions(Player),
        'FarmList': actions(FarmList),
        'Logger': actions(Logger),
        'Troops': actions(Troops),
        'Village': actions(Village),
        'Cache': actions(Cache),
        'Quest': actions(Quest),
        'Error': actions(Error),
        'Auctions': actions(Auctions),
        'Hero': actions(Hero),
        'Building': actions(Building),
        'Trade': actions(Trade),
        'Ranking': actions(Ranking),
        'Kingdom': actions(Kingdom),
        'Map': actions(Map),
        'Reports': actions(Reports),
        'Society': actions(Society),
        'PremiumFeature': actions(PremiumFeature),
        'Payment': actions(Payment),
        'KingdomTreaty': actions(KingdomTreaty),
        'Login': actions(Login)
    },
    'lobby': {
        'Achievements': actions(Achievements),
        'Cache': actions(LobbyCache),
        'Dual': actions(Dual),
        'Gameworld': actions(Gameworld),
        'Login': actions(LobbyLogin),
        'Notification': actions(Notification),
        'Player': actions(LobbyPlayer),
        'Sitter': actions(Sitter)
    }
}


if __name__ == '__main__':
    docs = {}

    for scope, controllers in actions.items():
        docs[scope] = {}
        for controller, actions in controllers.items():
            docs[scope][controller] = {}

            for action in actions:
                name, method = action
                docstring = parse(inspect.getdoc(method))
                args = annotations(method, docstring)

                try:
                    with open(f'docs/responses/{scope}/{controller}/{name}.json') as f:
                        response = json.load(f)
                except FileNotFoundError:
                    # TODO: Log warning here
                    response = None

                docs[scope][controller][name] = {
                    'short_description': docstring.short_description,
                    'long_description': docstring.long_description,
                    'args': args,
                    'returns': json.dumps(response, indent=4)
                }

    with codecs.open(f'docs/slate/source/includes/_actions.md', 'w', 'utf-8') as f:
        f.write(TEMPLATE.render(docs=docs))
