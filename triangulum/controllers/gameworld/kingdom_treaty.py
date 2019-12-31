from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import KingdomTreatyType
from triangulum.utils.exceptions import ActionNotImplementedError


class KingdomTreaty(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='kingdomTreaty')

    def offer(self, kingdom_id: int, type: KingdomTreatyType) -> dict:
        raise ActionNotImplementedError

        # return self.invoke_action(
        #     action='offer',
        #     params={
        #         'kingdomId': kingdom_id,
        #         'type': type,  # TODO: Enum this
        #     }
        # )

    def deny(self, id: int) -> dict:
        return self.invoke_action(
            action='deny',
            params={
                'id': id,
            }
        )

    def cancel(self, id: int) -> dict:
        return self.invoke_action(
            action='cancel',
            params={
                'id': id,
            }
        )
