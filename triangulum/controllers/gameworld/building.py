from typing import Union, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import CelebrationType, BuildingType, RomanUnit, TeutonUnit, GaulUnit
from triangulum.utils.dataclasses import RomanUnits, TeutonUnits, GaulUnits


class Building(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='building')

    def get_celebration_list(self, village_id: int, location_id: int) -> dict:
        return self.invoke_action(
            action='getCelebrationList',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def start_celebration(self, village_id: int, celebration_type: CelebrationType) -> dict:
        return self.invoke_action(
            action='startCelebration',
            params={
                'villageId': village_id,
                'type': celebration_type.value,
            }
        )

    def get_building_list(self, village_id: int, location_id: int) -> dict:
        return self.invoke_action(
            action='getBuildingList',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def get_trapper_infos(self, village_id: int, location_id: int) -> dict:
        return self.invoke_action(
            action='getTrapperInfos',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def build_traps(self, village_id: int, location_id: int, amount: int) -> dict:
        return self.invoke_action(
            action='buildTraps',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'amount': amount,
            }
        )

    def upgrade(self, village_id: int, location_id: int, building_type: BuildingType) -> dict:
        return self.invoke_action(
            action='upgrade',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'buildingType': building_type.value,
            }
        )

    def get_recruit_list(self, village_id: int, location_id: int) -> dict:
        return self.invoke_action(
            action='getRecruitList',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def recruit_units(
            self,
            village_id: int,
            location_id: int,
            units: Union[RomanUnits, TeutonUnits, GaulUnits]
    ) -> dict:
        return self.invoke_action(
            action='recruitUnits',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'units': units.without_zeros(),
            }
        )

    def use_master_builder(
        self,
        village_id: int,
        location_id: int,
        building_type: BuildingType,
        reserve_resources: bool,
        count: int = 1
    ) -> dict:
        return self.invoke_action(
            action='useMasterBuilder',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'buildingType': building_type.value,
                'reserveResources': reserve_resources,
                'count': count
            }
        )

    def get_oasis_list(self, village_id: int) -> dict:
        return self.invoke_action(
            action='getOasisList',
            params={
                'villageId': village_id,
            }
        )

    def get_culture_point_balance(self, village_id: int) -> dict:
        return self.invoke_action(
            action='getCulturePointBalance',
            params={
                'villageId': village_id,
            }
        )

    def reserve_resources(self, village_id: int, entry_id: int) -> dict:
        return self.invoke_action(
            action='reserveResources',
            params={
                'villageId': village_id,
                'entryId': entry_id,
            }
        )

    def cancel(self, village_id: int, event_id: int) -> dict:
        return self.invoke_action(
            action='cancel',
            params={
                'villageId': village_id,
                'eventId': event_id,
            }
        )

    def research_unit(
        self,
        village_id: int,
        location_id: int,
        building_type: BuildingType,
        unit_type: Union[RomanUnit, TeutonUnit, GaulUnit]
    ) -> dict:
        return self.invoke_action(
            action='researchUnit',
            params={
                'villageId': village_id,
                'locationId': location_id,
                'buildingType': building_type.value,
                'unitType': unit_type.value,
            }
        )

    def shift_master_builder(self, village_id: int, shift_from: int, shift_to: int) -> dict:
        return self.invoke_action(
            action='shiftMasterBuilder',
            params={
                'villageId': village_id,
                'from': shift_from,
                'to': shift_to
            }
        )

    def destroy(self, village_id: int, location_id: int) -> dict:
        return self.invoke_action(
            action='destroy',
            params={
                'villageId': village_id,
                'locationId': location_id
            }
        )

    def get_treasury_transformations(self) -> dict:
        return self.invoke_action(
            action='getTreasuryTransformations'
        )

    def transform_treasury(self, village_id: int, location_id: int) -> dict:
        return self.invoke_action(
            action='transformTreasury',
            params={
                'villageId': village_id,
                'locationId': location_id,
            }
        )

    def get_cp_data(self, village_id: int) -> dict:
        return self.invoke_action(
            action='getCpData',
            params={
                'villageId': village_id,
            }
        )
