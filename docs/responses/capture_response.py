"""Captures responses from action invocations.

This is a helper module for capturing responses returned by the game
server for later analysis and documentation.
This is best used in a python repl, to which you can just copy paste
the code.
In order to run, you will need to supply EMAIL, PASSWORD, GAMEWORLD_ID
and GAMEWORLD_NAME, either through the environment variables equivalent
to the aforementioned but prepended with TRIANGULUM_ or by replacing the
below os.environ calls with string literals.

Examples:
    run(gameworld.player.get_all())
    run(gameworld.player.get_midnight())
    for i in [
        gameworld.player.get_invitations_list(),
        gameworld.player.get_cardgame_result(),
        gameworld.change_vacation_state()
    ]:
        run(i)
"""

from triangulum.clients.lobby import LobbyClient
import asyncio
import json
import os

EMAIL = os.environ['TRIANGULUM_EMAIL']
PASSWORD = os.environ['TRIANGULUM_PASSWORD']
GAMEWORLD_ID = os.environ['TRIANGULUM_GAMEWORLD_ID']
GAMEWORLD_NAME = os.environ['TRIANGULUM_GAMEWORLD_NAME']

loop = asyncio.get_event_loop()

lobby = LobbyClient()
loop.run_until_complete(lobby.authenticate(email=EMAIL, password=PASSWORD))
assert loop.run_until_complete(lobby.is_authenticated()) is True

gameworld = loop.run_until_complete(
    lobby.connect_to_gameworld(
        gameworld_id=GAMEWORLD_ID,
        gameworld_name=GAMEWORLD_NAME
    )
)


def run(coro):
    loop = asyncio.get_event_loop()
    rsp = loop.run_until_complete(coro)
    name = str(coro).split('<coroutine object ')[1].split(' at')[0]
    controller, action = name.split('.')
    if not os.path.exists(f'docs/responses/{controller}'):
        os.mkdir(f'docs/responses/{controller}')
    with open(f'docs/responses/{controller}/{action}.json', 'w') as f:
        f.write(json.dumps(rsp, indent=4))
