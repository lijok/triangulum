from collections import Callable

from triangulum.controllers.base import BaseController


class Dual(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='dual')

    async def add(self, avatar_identifier: int, consumers_id: str, avatar_name: str, email: str) -> dict:
        """Add a dual player to the account

        Args:
            avatar_identifier: Name of the player
            consumers_id: UNKNOWN *
            avatar_name: UNKNOWN *
            email: Email address of the player *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='add',
            params={
                'avatarIdentifier': avatar_identifier,
                'consumersId': consumers_id,
                'avatarName': avatar_name,
                'email': email,
            }
        )
