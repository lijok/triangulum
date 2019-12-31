from typing import Union, List, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import GaulUnits, TeutonUnits, RomanUnits
from triangulum.utils.enums import TroopMovementType, SpyMissionType, PlayerTribe
from triangulum.utils.exceptions import ActionNotImplementedError


class Troops(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='troops')

    async def get_markers(self) -> dict:
        return await self.invoke_action(
            action='getMarkers'
        )

    # TODO
    async def set_marker(
        self,
        troop_id: int,
        # marker: Marker
    ) -> dict:
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='setMarker',
        #     params={
        #         'troopId': troop_id,
        #         'marker': marker.value,
        #     }
        # )

    async def abort_troop_movement(self, troop_id: int) -> dict:
        return await self.invoke_action(
            action='abortTroopMovement',
            params={
                'troopId': troop_id,
            }
        )

    async def check_target(
        self,
        dest_village_name: str,
        dest_village_id: int,
        village_id: int,
        movement_type: TroopMovementType,
        redeploy_hero: bool,
        hero_present: bool,
        selected_units: Union[RomanUnits, TeutonUnits, GaulUnits]
    ) -> dict:
        return await self.invoke_action(
            action='checkTarget',
            params={
                'destVillageName': dest_village_name,
                'destVillageId': dest_village_id,
                'villageId': village_id,
                'movementType': movement_type.value,
                'redeployHero': redeploy_hero,
                'heroPresent': hero_present,
                'selectedUnits': selected_units.combat_format_without_zeros(),
            }
        )

    async def send(
        self,
        dest_village_id: int,
        village_id: int,
        movement_type: TroopMovementType,
        redeploy_hero: int,
        units: Union[RomanUnits, TeutonUnits, GaulUnits],
        spy_mission: SpyMissionType = None
    ) -> dict:
        return await self.invoke_action(
            action='send',
            params={
                'destVillageId': dest_village_id,
                'villageId': village_id,
                'movementType': movement_type.value,
                'redeployHero': redeploy_hero,
                'units': units.combat_format_without_zeros(),
                'spyMission': spy_mission.value if spy_mission else SpyMissionType.RESOURCES.value,  # Oddly enough, is required even during non spy missions
            }
        )

    async def start_partial_farm_list_raid(self, list_id: int, entry_ids: List[int], village_id: int) -> dict:
        return await self.invoke_action(
            action='startPartialFarmListRaid',
            params={
                'listId': list_id,
                'entryIds': entry_ids,
                'villageId': village_id,
            }
        )

    async def start_farm_list_raid(self, list_ids: List[int], village_id: int) -> dict:
        return await self.invoke_action(
            action='startFarmListRaid',
            params={
                'listIds': list_ids,
                'villageId': village_id,
            }
        )

    # TODO: Finish this off, need an elegant solution as the data structure is complex
    async def fight_simulate(
            self,
            attack_type: int,
            attacker_tribe: PlayerTribe,
            attacker_units: Union[RomanUnits, TeutonUnits, GaulUnits],
            defender_tribe: PlayerTribe,
            defender_units: Union[RomanUnits, TeutonUnits, GaulUnits],
            hero_off_bonus: list,  # List of bonuses?
            hero_def_bonus: list,  # List of bonuses?
            hero_item_type: list,  # List of item types?
            hero_fight_strength: list,
            attacker_research: dict,
            defender_research: list,
            att_population: int,
            def_population: int,
            catapult_target_level: int,
            catapult_target_level2: int,
            mason_level: int,
            wall_level: int,
            palace_level: int,
            moat_level: int,
            natar_bonus: int,
            hero_mounted: list
    ) -> dict:
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='fightSimulate',
        #     params={
        #         'attackType': attack_type,
        #         'attackerTribe': attacker_tribe.value,
        #         'attackerUnits': attacker_units,
        #         'defenderTribe': defender_tribe.value,
        #         'defenderUnits': defender_units,
        #         'heroOffBonus': hero_off_bonus,
        #         'heroDefBonus': hero_def_bonus,
        #         'heroItemType': hero_item_type,
        #         'heroFightStrength': hero_fight_strength,
        #         'attackerResearch': attacker_research,
        #         'defenderResearch': defender_research,
        #         'attPopulation': att_population,
        #         'defPopulation': def_population,
        #         'catapultTargetLevel': catapult_target_level,
        #         'catapultTargetLevel2': catapult_target_level2,
        #         'masonLevel': mason_level,
        #         'wallLevel': wall_level,
        #         'palaceLevel': palace_level,
        #         'moatLevel': moat_level,
        #         'natarBonus': natar_bonus,
        #         'heroMounted': hero_mounted,
        #     }
        # )

    async def move_troops_home(self, troop_id: int, units: Union[RomanUnits, TeutonUnits, GaulUnits]) -> dict:
        return await self.invoke_action(
            action='moveTroopsHome',
            params={
                'troopId': troop_id,
                'units': units.combat_format_without_zeros(),
            }
        )

    async def disband(self, troop_id: int) -> dict:
        return await self.invoke_action(
            action='disband',
            params={
                'troopId': troop_id,
            }
        )