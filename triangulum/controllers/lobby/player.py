from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import Country


class Player(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='player')

    def switch_country(self, country: Country) -> dict:
        return self.invoke_action(
            action='switchCountry',
            params={
                'country': country.value,
            }
        )

    def save_name(self, account_name: str) -> dict:
        return self.invoke_action(
            action='saveName',
            params={
                'accountName': account_name,
            }
        )

    def get_all(self) -> dict:
        return self.invoke_action(
            action='getAll'
        )

    def get_avatar_data(self) -> dict:
        return self.invoke_action(
            action='getAvatarData'
        )

    def get_prestige_on_worlds(self) -> dict:
        return self.invoke_action(
            action='getPrestigeOnWorlds',
            params={
                'type': 'Finished',  # Seems to only be one option right now
            }
        )

    def get_account_details(self) -> dict:
        return self.invoke_action(
            action='getAccountDetails'
        )

    def delete_avatar(self, avatar_identifier: int) -> dict:
        return self.invoke_action(
            action='deleteAvatar',
            params={
                'avatarIdentifier': avatar_identifier,
            }
        )

    def abort_deletion(self, avatar_identifier: int) -> dict:
        return self.invoke_action(
            action='abortDeletion',
            params={
                'avatarIdentifier': avatar_identifier,
            }
        )
