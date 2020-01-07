from collections import Callable

from triangulum.controllers.base import BaseController
from cachetools import TTLCache
from triangulum.utils.cache import cached, MAX_SIZE, TTL


class Gameworld(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='gameworld')

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_possible_new_gameworlds(self) -> dict:
        """Get a list of possible new game worlds that can be joined
        This does not include the game worlds that this account is already a part of
        """
        return await self.invoke_action(
            action='getPossibleNewGameworlds'
        )
