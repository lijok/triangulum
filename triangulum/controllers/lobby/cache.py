from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.exceptions import ActionNotImplementedError
from cachetools import TTLCache
from triangulum.utils.cache import cached, MAX_SIZE, TTL


class Cache(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='cache')

    # @cached(TTLCache(MAX_SIZE, TTL))
    async def get(self, names: list) -> dict:
        """[*]

        Args:
            names: UNKNOWN *
        """
        # raise ActionNotImplementedError

        return await self.invoke_action(
            action='get',
            params={
                'names': names,  # TODO: Enum these
            }
        )
