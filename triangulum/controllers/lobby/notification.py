from collections import Callable

from triangulum.controllers.base import BaseController


class Notification(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='notification')

    async def mark_as_read(self, id: int) -> dict:
        """[*]

        Args:
            id: UNKNOWN *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='markAsRead',
            params={
                'id': id,
            }
        )
