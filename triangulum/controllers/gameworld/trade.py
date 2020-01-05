from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.dataclasses import Resources
from triangulum.utils.enums import Resource, TradeRate
from triangulum.utils.exceptions import ActionNotImplementedError


class Trade(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='trade')

    # TODO
    async def change_trade_route_status(self, id: int, status: int) -> dict:
        """Activate or deactivate a trade route *

        Args:
            id: ID of the trade route
            status: Status of the trade route *
        """
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='changeTradeRouteStatus',
        #     params={
        #         'id': id,
        #         'status': status,
        #     }
        # )

    async def delete_trade_route(self, id: int) -> dict:
        """Delete a trade route

        Args:
            id: ID of the trade route

        Returns:
            dict
        """
        return await self.invoke_action(
            action='deleteTradeRoute',
            params={
                'id': id,
            }
        )

    # TODO: This is used for checking the validity of a trade route setup so needs to be inspected more
    @cached(TTLCache(MAX_SIZE, TTL))
    async def check_target(self, source_village_id: int, dest_village_id: int, dest_village_name: str) -> dict:
        """Confirm that a trade route is valid before creating one

        Args:
            source_village_id: ID of the village from which resources will be sent
            dest_village_id: ID of the village to which resources will be sent
            dest_village_name: Name of the village to which resources will be sent

        Returns:
            dict
        """
        return await self.invoke_action(
            action='checkTarget',
            params={
                'sourceVillageId': source_village_id,
                'destVillageId': dest_village_id,
                'destVillageName': dest_village_name,
            }
        )

    async def create_offer(
        self,
        village_id: int,
        offered_resource: Resource,
        offered_amount: int,
        searched_resource: Resource,
        searched_amount: int,
        kingdom_only: bool
    ) -> dict:
        """Create a marketplace resource trade offer

        Args:
            village_id: ID of the village from which to trade resources
            offered_resource: Type of the offered resource
            offered_amount: Amount of offered resources
            searched_resource: Type of the sought after resource
            searched_amount: Amount of resources sought after
            kingdom_only: Toggle whether this trade offer is only available to your kingdom members

        Returns:
            dict
        """
        return await self.invoke_action(
            action='createOffer',
            params={
                'villageId': village_id,
                'offeredResource': offered_resource.value,
                'offeredAmount': offered_amount,
                'searchedResource': searched_resource.value,
                'searchedAmount': searched_amount,
                'kingdomOnly': kingdom_only,
            }
        )

    async def cancel_offer(self, offer_id: int) -> dict:
        """Cancel a marketplace resource trade offer

        Args:
            offer_id: ID of the offer

        Returns:
            dict
        """
        return await self.invoke_action(
            action='cancelOffer',
            params={
                'offerId': offer_id,
            }
        )

    # TODO: Check this function
    async def get_offer_list(
        self,
        village_id: int,
        search: Resource,
        offer: Resource,
        rate: TradeRate,
        start: int,
        count: int
    ) -> dict:
        """Get list of resource trade offers in the marketplace

        Args:
            village_id: ID of the village from which you wish to trade
            search: Type of resource to search for
            offer: Type of resource offered in return
            rate: Rate for which to search
            start: Starting index from which to return the list of offers
            count: Amount of offers to return

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getOfferList',
            params={
                'villageId': village_id,
                'search': search.value,
                'offer': offer.value,
                'rate': rate.value,
                'start': start,
                'count': count,
            }
        )

    async def accept_offer(self, offer_id: int, village_id: int) -> dict:
        """Accept a resource trade offer in the marketplace

        Args:
            offer_id: ID of the offer
            village_id: ID of the village from which to trade the resources

        Returns:
            dict
        """
        return await self.invoke_action(
            action='acceptOffer',
            params={
                'offerId': offer_id,
                'villageId': village_id,
            }
        )

    async def send_resources(
        self,
        dest_village_id: int,
        recurrences: int,
        resources: Resources,
        source_village_id: int
    ) -> dict:
        """Send resources to another village

        Args:
            dest_village_id: ID of the destination village
            recurrences: Amount of times to repeat the sending of the resources
            resources: Resource amounts to be sent
            source_village_id: ID of the village from which to send the resources

        Returns:
            dict
        """
        return await self.invoke_action(
            action='sendResources',
            params={
                'destVillageId': dest_village_id,
                'recurrences': recurrences,
                'resources': resources.with_zeros(),
                'sourceVillageId': source_village_id,
            }
        )
