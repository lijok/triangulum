from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.exceptions import ActionNotImplementedError


class Cache(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='cache')

    # TODO: Implement proper cache control
    # @cached(TTLCache(MAX_SIZE, TTL))
    async def get(self, names: list) -> dict:
        """UNKNOWN *

        Args:
            names: UNKNOWN *
        """
        # raise ActionNotImplementedError

        return await self.invoke_action(
            action='get',
            params={
                'names': names,
            }
        )
