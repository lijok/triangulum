from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.exceptions import ActionNotImplementedError


class Cache(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='cache')

    # TODO: Implement proper cache control
    async def get(self, names: list) -> dict:
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='get',
        #     params={
        #         'names': names,
        #     }
        # )
