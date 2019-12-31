from typing import List, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import Marker, FieldMessage
from triangulum.utils.enums import FieldMarkerPersonalMinimized


class Map(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='map')

    def get_heatmap_maximums(self) -> dict:
        return self.invoke_action(
            action='getHeatmapMaximums'
        )

    def get_by_region_ids(self, region_id_collection: dict) -> dict:
        """
        Retrieves region data by region id
        """
        return self.invoke_action(
            action='getByRegionIds',
            params={
                'regionIdCollection': region_id_collection,
            }
        )

    def edit_map_markers(self, markers: List[Marker], field_message: FieldMessage) -> dict:
        return self.invoke_action(
            action='editMapMarkers',
            params={
                'markers': [marker.as_dict() for marker in markers],
                'fieldMessage': field_message.as_dict(),
            }
        )

    def field_marker_minimize(
        self,
        cell_id: int,
        is_global: int,
        minimize_state: FieldMarkerPersonalMinimized
    ) -> dict:
        return self.invoke_action(
            action='fieldMarkerMinimize',
            params={
                'cellId': cell_id,
                'isGlobal': is_global,
                'minimizeState': minimize_state,
            }
        )

    def field_marker_close(self, id: int, is_global: int) -> dict:
        return self.invoke_action(
            action='fieldMarkerClose',
            params={
                'id': id,
                'isGlobal': is_global,
            }
        )

    def field_marker_delete(self, id: int, is_global: int) -> dict:
        return self.invoke_action(
            action='fieldMarkerDelete',
            params={
                'id': id,
                'isGlobal': is_global,
            }
        )

    def get_kingdom_influence_statistics(self, king_id: int) -> dict:
        return self.invoke_action(
            action='getKingdomInfluenceStatistics',
            params={
                'kingId': king_id,
            }
        )
