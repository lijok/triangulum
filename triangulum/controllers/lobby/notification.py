from collections import Callable

from triangulum.controllers.base import BaseController


class Notification(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='notification')

    def mark_as_read(self, id: int) -> dict:
        return self.invoke_action(
            action='markAsRead',
            params={
                'id': id,
            }
        )
