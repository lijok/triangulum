from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import Resource, Gender


class Hero(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='hero')

    def get_value_points(self):
        return self.invoke_action(
            action='getValuePoints'
        )

    def add_attribute_points(
        self,
        fight_strength_points: int,
        att_bonus_points: int,
        def_bonus_points: int,
        res_bonus_points: int,
        res_bonus_type: Resource
    ) -> dict:
        return self.invoke_action(
            action='addAttributePoints',
            params={
                'fightStrengthPoints': fight_strength_points,
                'attBonusPoints': att_bonus_points,
                'defBonusPoints': def_bonus_points,
                'resBonusPoints': res_bonus_points,
                'resBonusType': res_bonus_type.value,
            }
        )

    def merge_item(self, id: int, amount: int, village_id: int) -> dict:
        return self.invoke_action(
            action='mergeItem',
            params={
                'id': id,
                'amount': amount,
                'villageId': village_id,
            }
        )

    def save_face(
        self,
        mouth: int,
        hair: int,
        eye: int,
        eyebrow: int,
        ear: int,
        nose: int,
        hair_color: int,
        gender: Gender,
        player_id: int,
        beard: int = None,
        fetched_from_lobby: bool = True
    ) -> dict:
        """Sets the face properties for the hero
        Each property is an integer corresponding to a file in
        assets/game/{version}/layout/images/heroAvatar/{gender}/thumb/head/{property}
        """

        return self.invoke_action(
            action='saveFace',
            params={
                'face': {
                    'mouth': mouth,
                    'beard': beard,
                    'hair': hair,
                    'eye': eye,
                    'eyebrow': eyebrow,
                    'ear': ear,
                    'nose': nose,
                },
                'gender': gender.value,
                'hairColor': hair_color,
                'playerId': player_id,
                'fetchedFromLobby': fetched_from_lobby,
            }
        )

    def get_last_inventory_view(self) -> dict:
        return self.invoke_action(
            action='getLastInventoryView'
        )

    def get_treasure_sell_price(self) -> dict:
        return self.invoke_action(
            action='getTreasureSellPrice'
        )

    def get_duration_to_closest_village_with_influence(self, village_id: int) -> dict:
        return self.invoke_action(
            action='getDurationToClosestVillageWithInfluence',
            params={
                'villageId': village_id,
            }
        )

    def use_item(self, id: int, amount: int, village_id: int) -> dict:
        return self.invoke_action(
            action='useItem',
            params={
                'id': id,
                'amount': amount,
                'villageId': village_id,
            }
        )

    def set_last_inventory_view(self) -> dict:
        return self.invoke_action(
            action='setLastInventoryView'
        )

    def get_resource_for_resource_chest(self, percent: int, resource_type: Resource) -> dict:
        return self.invoke_action(
            action='getResourceForResourceChest',
            params={
                'percent': percent,
                'type': resource_type.value,
            }
        )

    def upgrade_item(self, upgrade_item_id: int, target_item_id: int) -> dict:
        return self.invoke_action(
            action='upgradeItem',
            params={
                'upgradeItemId': upgrade_item_id,
                'targetItemId': target_item_id,
            }
        )

    def revive(self, village_id: int) -> dict:
        return self.invoke_action(
            action='revive',
            params={
                'villageId': village_id,
            }
        )

    def confirm_hero_level_up(self) -> dict:
        return self.invoke_action(
            action='confirmHeroLevelUp'
        )

    def switch_items(self, id1: int, id2: int) -> dict:
        return self.invoke_action(
            action='switchItems',
            params={
                'id1': id1,
                'id2': id2,
            }
        )
