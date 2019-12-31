from typing import Union, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import RomanUnits, TeutonUnits, GaulUnits


class FarmList(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='farmList')

    def toggle_entry(self, village_id: int, list_id: int) -> dict:
        return self.invoke_action(
            action='toggleEntry',
            params={
                'villageId': village_id,
                'listId': list_id,
            }
        )

    def get_attack_info(self, current_village_id: int, farm_list_ids: list) -> dict:
        return self.invoke_action(
            action='getAttackInfo',
            params={
                'currentVillageId': current_village_id,
                'farmlistIds': farm_list_ids,
            }
        )

    def edit_troops(self, entry_ids: list, units: Union[RomanUnits, TeutonUnits, GaulUnits]) -> dict:
        return self.invoke_action(
            action='editTroops',
            params={
                'entryIds': entry_ids,
                'units': units.without_zeros(),
            }
        )

    def create_list(self, name: str) -> dict:
        return self.invoke_action(
            action='createList',
            params={
                'name': name,
            }
        )

    def copy_entry(self, village_id: int, new_list_id: int, entry_id: int) -> dict:
        return self.invoke_action(
            action='copyEntry',
            params={
                'villageId': village_id,
                'newListId': new_list_id,
                'entryId': entry_id,
            }
        )

    def delete_list(self, list_id: int) -> dict:
        return self.invoke_action(
            action='deleteList',
            params={
                'listId': list_id,
            }
        )

    def delete_entry(self, entry_id: int) -> dict:
        return self.invoke_action(
            action='deleteEntry',
            params={
                'entryId': entry_id,
            }
        )

    def check_target(self, village_id: int) -> dict:
        return self.invoke_action(
            action='checkTarget',
            params={
                'villageId': village_id,
            }
        )

    def add_entry(self, village_id: int, list_id: int) -> dict:
        return self.invoke_action(
            action='addEntry',
            params={
                'villageId': village_id,
                'listId': list_id,
            }
        )

    def edit_list(self, name: str, list_id: int) -> dict:
        """Edits a lists name"""

        return self.invoke_action(
            action='editList',
            params={
                'name': name,
                'listId': list_id,
            }
        )

    def change_list_order(self, list_ids: list) -> dict:  # TODO: Check this
        return self.invoke_action(
            action='changeListOrder',
            params={
                'listIds': list_ids,
            }
        )
