from typing import List, Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.dataclasses import Marker, FieldMessage
from triangulum.utils.enums import FieldMarkerPersonalMinimized


class Map(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='map')

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_heatmap_maximums(self) -> dict:
        """[*]

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getHeatmapMaximums'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_by_region_ids(self, region_id_collection: dict) -> dict:
        """Retrieves region data by region id

        Args:
            region_id_collection: List of region IDs to fetch the information for

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getByRegionIds',
            params={
                'regionIdCollection': region_id_collection,
            }
        )

    async def edit_map_markers(self, markers: List[Marker], field_message: FieldMessage) -> dict:
        """Edit markers on a map cell

        Args:
            markers: List of Marker objects to be edited / added on the map cell
            field_message: Message to be placed on the cell

        Returns:
            dict
        """
        return await self.invoke_action(
            action='editMapMarkers',
            params={
                'markers': [marker.as_dict() for marker in markers],
                'fieldMessage': field_message.as_dict(),
            }
        )

    async def field_marker_minimize(
        self,
        cell_id: int,
        is_global: bool,
        minimize_state: FieldMarkerPersonalMinimized
    ) -> dict:
        """[-]Minimizes / maximizes a field marker so that it's (not)shown by default next time
        the player enters the map over the UI

        Args:
            cell_id: ID of the cell on which the marker is placed
            is_global: Whether the toggle is global *
            minimize_state: State of the toggle (minimzed/maximized)

        Returns:
            dict
        """
        return await self.invoke_action(
            action='fieldMarkerMinimize',
            params={
                'cellId': cell_id,
                'isGlobal': is_global,
                'minimizeState': minimize_state,
            }
        )

    async def field_marker_close(self, id: int, is_global: bool) -> dict:
        """[-]Closes a field marker so that it's no longer shown on the UI

        Args:
            id: ID of the marker
            is_global: Whether the closure is global *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='fieldMarkerClose',
            params={
                'id': id,
                'isGlobal': is_global,
            }
        )

    async def field_marker_delete(self, id: int, is_global: bool) -> dict:
        """[-]Delete a field marker

        Args:
            id: ID of the marker
            is_global: Whether the deletion is global *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='fieldMarkerDelete',
            params={
                'id': id,
                'isGlobal': is_global,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_kingdom_influence_statistics(self, king_id: int) -> dict:
        """Get statistics about a kingdoms influence on surrounding map cells

        Args:
            king_id: Player ID of the king of the kingdom

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getKingdomInfluenceStatistics',
            params={
                'kingId': king_id,
            }
        )
