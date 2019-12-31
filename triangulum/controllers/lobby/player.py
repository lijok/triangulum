from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import Country


class Player(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='player')

    async def switch_country(self, country: Country) -> dict:
        return await self.invoke_action(
            action='switchCountry',
            params={
                'country': country.value,
            }
        )

    async def save_name(self, account_name: str) -> dict:
        return await self.invoke_action(
            action='saveName',
            params={
                'accountName': account_name,
            }
        )

    async def get_all(self) -> dict:
        return await self.invoke_action(
            action='getAll'
        )

    async def get_avatar_data(self) -> dict:
        return await self.invoke_action(
            action='getAvatarData'
        )

    async def get_prestige_on_worlds(self) -> dict:
        return await self.invoke_action(
            action='getPrestigeOnWorlds',
            params={
                'type': 'Finished',  # Seems to only be one option right now
            }
        )

    async def get_account_details(self) -> dict:
        return await self.invoke_action(
            action='getAccountDetails'
        )

    async def delete_avatar(self, avatar_identifier: int) -> dict:
        return await self.invoke_action(
            action='deleteAvatar',
            params={
                'avatarIdentifier': avatar_identifier,
            }
        )

    async def abort_deletion(self, avatar_identifier: int) -> dict:
        return await self.invoke_action(
            action='abortDeletion',
            params={
                'avatarIdentifier': avatar_identifier,
            }
        )
