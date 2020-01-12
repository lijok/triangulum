from typing import Union, List, Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.models import Units
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
        """[*]

        Args:
            troop_id: UNKNOWN *
        """
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='setMarker',
        #     params={
        #         'troopId': troop_id,
        #         'marker': marker.value,
        #     }
        # )

    async def abort_troop_movement(self, troop_id: int) -> dict:
        """Abort the movement of troops

        Args:
            troop_id: ID of the movement
        """
        return await self.invoke_action(
            action='abortTroopMovement',
            params={
                'troopId': troop_id,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def check_target(
        self,
        dest_village_name: str,
        dest_village_id: int,
        village_id: int,
        movement_type: TroopMovementType,
        redeploy_hero: bool,
        hero_present: bool,
        selected_units: Units
    ) -> dict:
        """Check whether a desired troop movement is valid prior to begining the movement

        Args:
            dest_village_name: Movement destination village id
            dest_village_id: Movement destination village name
            village_id: ID of the village from which the movement will take place
            movement_type: Type of the movement, i.e attack, raid, siege
            redeploy_hero: Whether to send the hero along *
            hero_present: Whether to send the hero along *
            selected_units: Units to be sent
        """
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
        units: Units,
        spy_mission: SpyMissionType = None
    ) -> dict:
        """Send troops

        Args:
            dest_village_id: Movement destination village name
            village_id: ID of the village from which the movement will take place
            movement_type: Type of the movement, i.e attack, raid, siege
            redeploy_hero: Whether to send the hero along *
            units: Units to be sent
            spy_mission: Type of the spy mission (spy for resources or defences and troops)
                this will be ignored if the movement type is not TroopMovementType.SPY
        """
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
        """Begin a farm list raid on some of the targets in the farm list

        Args:
            list_id: ID of the farm list
            entry_ids: List of entry IDs of the farm list
            village_id: ID of the village from which to begin the raid
        """
        return await self.invoke_action(
            action='startPartialFarmListRaid',
            params={
                'listId': list_id,
                'entryIds': entry_ids,
                'villageId': village_id,
            }
        )

    async def start_farm_list_raid(self, list_ids: List[int], village_id: int) -> dict:
        """Start a farm list raid

        Args:
            list_ids: ID of the farm list
            village_id: ID of the village from which to begin the raid
        """
        return await self.invoke_action(
            action='startFarmListRaid',
            params={
                'listIds': list_ids,
                'villageId': village_id,
            }
        )

    # TODO: Finish this off, need an elegant solution as the data structure is complex
    @cached(TTLCache(MAX_SIZE, TTL))
    async def fight_simulate(
            self,
            attack_type: int,
            attacker_tribe: PlayerTribe,
            attacker_units: Units,
            defender_tribe: PlayerTribe,
            defender_units: Units,
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
        """[*]

        Args:
            attack_type: UNKNOWN *
            attacker_tribe: UNKNOWN *
            attacker_units: UNKNOWN *
            defender_tribe: UNKNOWN *
            defender_units: UNKNOWN *
            hero_off_bonus: UNKNOWN *
            hero_def_bonus: UNKNOWN *
            hero_item_type: UNKNOWN *
            hero_fight_strength: UNKNOWN *
            attacker_research: UNKNOWN *
            defender_research: UNKNOWN *
            att_population: UNKNOWN *
            def_population: UNKNOWN *
            catapult_target_level: UNKNOWN *
            catapult_target_level2: UNKNOWN *
            mason_level: UNKNOWN *
            wall_level: UNKNOWN *
            palace_level: UNKNOWN *
            moat_level: UNKNOWN *
            natar_bonus: UNKNOWN *
            hero_mounted: UNKNOWN *
        """
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

    async def move_troops_home(self, troop_id: int, units: Units) -> dict:
        """[*]

        Args:
            troop_id: ID of the movement
            units: Units to move home
        """
        return await self.invoke_action(
            action='moveTroopsHome',
            params={
                'troopId': troop_id,
                'units': units.combat_format_without_zeros(),
            }
        )

    async def disband(self, troop_id: int) -> dict:
        """[*]

        Args:
            troop_id: UNKNOWN *
        """
        return await self.invoke_action(
            action='disband',
            params={
                'troopId': troop_id,
            }
        )

    async def release(self, troop_id: int) -> dict:
        """[*]Release troops being held in traps

        Args:
            troop_id: UNKNOWN *
        """
        return await self.invoke_action(
            action='release',
            params={
                'troopId': troop_id,
            }
        )
