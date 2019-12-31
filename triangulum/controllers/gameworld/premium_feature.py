from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import Resources
from triangulum.utils.enums import PremiumFeatureAutoExtendFlags, CurrencyType, FinishNowCost, BuildingQueueType


class PremiumFeature(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='premiumFeature')

    async def save_auto_extend_flags(self, auto_extend_flags: PremiumFeatureAutoExtendFlags) -> dict:
        return await self.invoke_action(
            action='saveAutoExtendFlags',
            params={
                'autoExtendFlags': auto_extend_flags.value,
            }
        )

    async def treasure_resources_instant(self, troop_id: int) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'treasureResourcesInstant',
                'params': {
                    'troopId': troop_id
                }
            }
        )

    async def cardgame_single(self, selected_card: int) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'cardgameSingle',
                'params': {
                    'selectedCard': selected_card
                }
            }
        )

    async def cardgame4of5(self) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'cardgame4of5'
            }
        )

    async def starter_package(self) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'starterPackage'
            }
        )

    async def building_master_slot(self) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'buildingMasterSlot'
            }
        )

    async def exchange_office(self, amount: int, currency_type: CurrencyType) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'exchangeOffice',
                'params': {
                    'amount': amount,
                    'type': currency_type.value,
                }
            }
        )

    async def npc_trader(self, village_id: int, distribute_res: Resources) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'NPCTrader',
                'params': {
                    'villageId': village_id,
                    'distributeRes': distribute_res.with_zeros()
                }
            }
        )

    async def finish_now(self, village_id: int, queue_type: BuildingQueueType, price: FinishNowCost) -> dict:
        params = {
            'featureName': 'finishNow',
            'params': {
                'villageId': village_id,
                'queueType': queue_type.value,
                'price': price.value
            }
        }

        key_name = 'buildingType' if queue_type == BuildingQueueType.SMITHY else 'queueType'
        params['params'][key_name] = queue_type.value

        return await self.invoke_action(
            action='bookFeature',
            params=params
        )

    async def plus_account(self) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'plusAccount'
            }
        )

    async def production_bonus(self) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'productionBonus'
            }
        )

    async def crop_production_bonus(self) -> dict:
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'cropProductionBonus'
            }
        )
