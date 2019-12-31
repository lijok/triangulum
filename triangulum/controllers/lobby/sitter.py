from collections import Callable

from triangulum.controllers.base import BaseController


class Sitter(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='sitter')

    async def add(self, avatar_identifier: int, consumers_id: str, avatar_name: str, email: str) -> dict:
        return await self.invoke_action(
            action='add',
            params={
                'avatarIdentifier': avatar_identifier,
                'consumersId': consumers_id,
                'avatarName': avatar_name,
                'email': email,
            }
        )

    async def set_permissions(
        self,
        avatar_identifier: int,
        sitter_account_identifier: int,
        can_raid_other_players: bool,
        can_send_reinforcements: bool,
        can_send_resources: bool,
        can_buy_and_spend_gold: bool
    ) -> dict:
        return await self.invoke_action(
            action='setPermissions',
            params={
                'avatarIdentifier': avatar_identifier,
                'sitterAccountIdentifier': sitter_account_identifier,
                'permissions': {
                    '1': can_raid_other_players,
                    '2': can_send_reinforcements,
                    '3': can_send_resources,
                    '4': can_buy_and_spend_gold
                },
            }
        )

    async def remove(self, avatar_identifier: int, sitter_account_identifier: int) -> dict:
        return await self.invoke_action(
            action='remove',
            params={
                'avatarIdentifier': avatar_identifier,
                'sitterAccountIdentifier': sitter_account_identifier,
            }
        )

