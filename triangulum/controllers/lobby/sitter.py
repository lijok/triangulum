from collections import Callable

from triangulum.controllers.base import BaseController


class Sitter(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='sitter')

    async def add(self, avatar_identifier: int, consumers_id: str, avatar_name: str, email: str) -> dict:
        """Add a sitter to the game world

        Args:
            avatar_identifier: UNKNOWN *
            consumers_id: UNKNOWN *
            avatar_name: UNKNOWN *
            email: UNKNOWN *

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

    async def set_permissions(
        self,
        avatar_identifier: int,
        sitter_account_identifier: int,
        can_raid_other_players: bool,
        can_send_reinforcements: bool,
        can_send_resources: bool,
        can_buy_and_spend_gold: bool
    ) -> dict:
        """Set the functions a sitter has access to

        Args:
            avatar_identifier: ID of your avatar on a particular game world
            sitter_account_identifier: ID of the sitters avatar on a particular game world
            can_raid_other_players: Toggle whether the sitter can raid other players
            can_send_reinforcements: Toggle whether the sitter can send reinforcements
            can_send_resources: Toggle whether the sitter can send resources
            can_buy_and_spend_gold: Toggle whether the sitter can buy and spend gold

        Returns:
            dict
        """
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
        """Remove a sitter

        Args:
            avatar_identifier: ID of your avatar on a particular game world
            sitter_account_identifier: ID of the sitters avatar on a particular game world

        Returns:
            dict
        """
        return await self.invoke_action(
            action='remove',
            params={
                'avatarIdentifier': avatar_identifier,
                'sitterAccountIdentifier': sitter_account_identifier,
            }
        )

