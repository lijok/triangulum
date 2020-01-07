from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import Country
from cachetools import TTLCache
from triangulum.utils.cache import cached, MAX_SIZE, TTL


class Player(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='player')

    async def switch_country(self, country: Country) -> dict:
        """Switch the country your account is in
        This will grant you access to different game worlds specific to
        the selected country

        Args:
            country: Country to switch to
        """
        return await self.invoke_action(
            action='switchCountry',
            params={
                'country': country.value,
            }
        )

    async def save_name(self, account_name: str) -> dict:
        """[*]Change your account name

        Args:
            account_name: New name for the account *
        """
        return await self.invoke_action(
            action='saveName',
            params={
                'accountName': account_name,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_all(self) -> dict:
        """Get all information about the account including the information about all avatars *
        """
        return await self.invoke_action(
            action='getAll'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_avatar_data(self) -> dict:
        """Get data about your account on a particular game world
        """
        return await self.invoke_action(
            action='getAvatarData'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_prestige_on_worlds(self) -> dict:
        """Get the prestige quantities obtained on different game worlds the account
        is currently a part of
        """
        return await self.invoke_action(
            action='getPrestigeOnWorlds',
            params={
                'type': 'Finished',  # Seems to only be one option right now
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_account_details(self) -> dict:
        """Get details about the account *
        """
        return await self.invoke_action(
            action='getAccountDetails'
        )

    async def delete_avatar(self, avatar_identifier: int) -> dict:
        """Delete your avatar on a particular game world

        Args:
            avatar_identifier: ID of the avatar
        """
        return await self.invoke_action(
            action='deleteAvatar',
            params={
                'avatarIdentifier': avatar_identifier,
            }
        )

    async def abort_deletion(self, avatar_identifier: int) -> dict:
        """Abort the deletion of an avatar

        Args:
            avatar_identifier: ID of the avatar
        """
        return await self.invoke_action(
            action='abortDeletion',
            params={
                'avatarIdentifier': avatar_identifier,
            }
        )
