from collections import Callable

from triangulum.controllers.base import BaseController


class Gameworld(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='gameworld')

    async def get_possible_new_gameworlds(self) -> dict:
        return await self.invoke_action(
            action='getPossibleNewGameworlds'
        )
