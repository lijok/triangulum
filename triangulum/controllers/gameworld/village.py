from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL


class Village(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='village')

    # This is for clicking on a hidden thing on the UI that gives you an achievement
    async def click_special(self, id: int) -> dict:
        """[-]Click on a special event entity in the UI which rewards you with an achievement

        Args:
            id: id of the special

        Returns:
            dict
        """
        return await self.invoke_action(
            action='clickSpecial',
            params={
                'id': id,  # TODO: These IDs should be enumerated once we discover them
            }
        )

    async def toggle_allow_tribute_collection(self, village_id: int) -> dict:
        """Toggle whether tributes can be collected by your king

        Args:
            village_id: id of the village to toggle

        Returns:
            dict
        """
        return await self.invoke_action(
            action='toggleAllowTributeCollection',
            params={
                'villageId': village_id,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_villages_with_influence_on_oasis_for_player(self, oasis_id: int, player_id: int) -> dict:
        """Fetch info on which villages a player has influence with over an oasis

        Args:
            oasis_id: id of the oasis
            player_id: id of the player

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getVillagesWithInfluenceOnOasisForPlayer',
            params={
                'oasisId': oasis_id,
                'playerId': player_id,
            }
        )

    async def get_kingdom_village_attacks(self) -> dict:
        """Fetch all incoming attacks on villages within your kingdom

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getKingdomVillageAttacks'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_production_details(self, village_id: int) -> dict:
        """Get production details of a village

        Args:
            village_id: id of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getProductionDetails',
            params={
                'villageId': village_id,
            }
        )

    async def use_oasis(self, oasis_id: int, village_id: int) -> dict:
        """Set a village to use an oasis

        Args:
            oasis_id: id of the oasis
            village_id: id of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='useOasis',
            params={
                'oasisId': oasis_id,
                'villageId': village_id,
            }
        )

    async def clear_oasis(self, oasis_id: int, village_id: int) -> dict:
        """Set a village to not use an oasis

        Args:
            oasis_id: id of the oasis
            village_id: id of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='clearOasis',
            params={
                'oasisId': oasis_id,
                'villageId': village_id,
            }
        )

    async def update_name(self, village_id: int, village_name: str) -> dict:
        """Update the name of a village

        Args:
            village_id: id of the village
            village_name: new name of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='updateName',
            params={
                'villageId': village_id,
                'villageName': village_name,
            }
        )

    async def check_unit_production(self, village_id: int) -> dict:
        """Get current units in production in a village

        Args:
            village_id: id of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='checkUnitProduction',
            params={
                'villageId': village_id,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_treasuries_capacity(self, village_id: int) -> dict:
        """Get capacity of a treasury in a village

        Args:
            village_id: id of the village the treasury is in

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getTreasuriesCapacity',
            params={
                'villageId': village_id,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_victory_points_and_influence_bonus(self, village_id: int) -> dict:
        """Get victory points and influence bonus

        Args:
            village_id: id of the village

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getVictoryPointsAndInfluenceBonus',
            params={
                'villageId': village_id,
            }
        )
