from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import Resources
from triangulum.utils.enums import PremiumFeatureAutoExtendFlags, CurrencyType, FinishNowCost, BuildingQueueType


class PremiumFeature(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='premiumFeature')

    async def save_auto_extend_flags(self, auto_extend_flags: PremiumFeatureAutoExtendFlags) -> dict:
        """Toggle auto extension flags for features such as Travian Plus and resource bonuses.
        Toggling this means the features will automatically be extended upon expiry and the
        gold cost will be automatically deducted from the account balance

        Args:
            auto_extend_flags: Premium feature auto extension flags to be toggled

        Returns:
            dict
        """
        return await self.invoke_action(
            action='saveAutoExtendFlags',
            params={
                'autoExtendFlags': auto_extend_flags.value,
            }
        )

    async def treasure_resources_instant(self, troop_id: int) -> dict:
        """Instantly deliver resources from a sale of a treasure at the cost of 3 gold

        Args:
            troop_id: ID of the trade movement

        Returns:
            dict
        """
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
        """Purchase a cardgame with a single possible selection for 5 gold

        Args:
            selected_card: Number representing the card selection from 1 to 5

        Returns:
            dict
        """
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
        """Purchase a cardgame with 4 card selections for 20 gold
        Note that you will need to play the card game using Player.select_cards

        Returns:
            dict
        """
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'cardgame4of5'
            }
        )

    async def starter_package(self) -> dict:
        """Purchase a starter package for 60 gold
        This usually contains:
            4x NPC Trader
            5x Finish Now
            6000 Silver
            1x Book of Wisdom
            20x Ointment
            20x Small Bandage

        Returns:
            dict
        """
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'starterPackage'
            }
        )

    async def building_master_slot(self) -> dict:
        """Purchase another building master slot
        Cost per slot:
            1st slot: 50 Gold
            2nd slot: 75 Gold
            3rd slot: 100 Gold

        Returns:
            dict
        """
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'buildingMasterSlot'
            }
        )

    async def exchange_office(self, amount: int, currency_type: CurrencyType) -> dict:
        """Exchange Silver for Gold or Gold for Silver
        Exchange rate:
            200 Silver -> 1 Gold
            1 Gold -> 100 Silver

        If you wish to exchange 200 Silver for 1 Gold, call the function with
        amount=200, currency_type=CurrencyType.SILVER

        Args:
            amount: Amount to exchange
            currency_type: Currency type to exchange from

        Returns:
            dict
        """
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
        """Use NPC Trader feature to redistribute your resources

        Args:
            village_id: ID of the village whose resources to redistribute
            distribute_res: Resource distribution values

        Returns:
            dict
        """
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
        """Use the Finish Now feature to instantly finish an action in a queue
        such as a builder or a smithy

        Args:
            village_id: ID of the village in which the queue resides
            queue_type: Type of the queue to use Finish Now on
            price: UNKNOWN *

        Returns:
            dict
        """
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

    # TODO: How does this work when purchasing for the whole round?
    async def plus_account(self) -> dict:
        """Purchase a Travian Plus account for 10 Gold for a variable duration based
        on the speed of the game world

        Returns:
            dict
        """
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'plusAccount'
            }
        )

    # TODO: How does this work when purchasing for the whole round?
    async def production_bonus(self) -> dict:
        """Purchase a 25% wood, clay and iron production bonus for 20 Gold
        for a variable duration based on the speed of the game world

        Returns:
            dict
        """
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'productionBonus'
            }
        )

    # TODO: How does this work when purchasing for the whole round?
    async def crop_production_bonus(self) -> dict:
        """Purchase a 25% crop production bonus for 10 Gold
        for a variable duration based on the speed of the game world

        Returns:
            dict
        """
        return await self.invoke_action(
            action='bookFeature',
            params={
                'featureName': 'cropProductionBonus'
            }
        )
