from collections import Callable

from triangulum.controllers.base import BaseController


class Gameworld(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='gameworld')

    async def get_possible_new_gameworlds(self) -> dict:
        """Get a list of possible new game worlds that can be joined
        This does not include the game worlds that this account is already a part of

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getPossibleNewGameworlds'
        )
