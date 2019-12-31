from collections import Callable

from triangulum.controllers.base import BaseController


class Dual(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='dual')

    def add(self, avatar_identifier: int, consumers_id: str, avatar_name: str, email: str) -> dict:
        return self.invoke_action(
            action='add',
            params={
                'avatarIdentifier': avatar_identifier,
                'consumersId': consumers_id,
                'avatarName': avatar_name,
                'email': email,
            }
        )
