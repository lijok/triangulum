from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import Resources
from triangulum.utils.enums import Resource, TradeRate
from triangulum.utils.exceptions import ActionNotImplementedError


class Trade(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='trade')

    # TODO
    def change_trade_route_status(self, id: int, status: int) -> dict:
        raise ActionNotImplementedError

        # return self.invoke_action(
        #     action='changeTradeRouteStatus',
        #     params={
        #         'id': id,
        #         'status': status,
        #     }
        # )

    def delete_trade_route(self, id: int) -> dict:
        return self.invoke_action(
            action='deleteTradeRoute',
            params={
                'id': id,
            }
        )

    # TODO: This is used for checking the validity of a trade route setup so needs to be inspected more
    def check_target(self, source_village_id: int, dest_village_id: int, dest_village_name: str) -> dict:
        return self.invoke_action(
            action='checkTarget',
            params={
                'sourceVillageId': source_village_id,
                'destVillageId': dest_village_id,
                'destVillageName': dest_village_name,
            }
        )

    def create_offer(
        self,
        village_id: int,
        offered_resource: Resource,
        offered_amount: int,
        searched_resource: Resource,
        searched_amount: int,
        kingdom_only: bool
    ) -> dict:
        return self.invoke_action(
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

    def cancel_offer(self, offer_id: int) -> dict:
        return self.invoke_action(
            action='cancelOffer',
            params={
                'offerId': offer_id,
            }
        )

    # TODO: Check this function
    def get_offer_list(
        self,
        village_id: int,
        search: Resource,
        offer: Resource,
        rate: TradeRate,
        start: int,
        count: int
    ) -> dict:
        return self.invoke_action(
            action='getOfferList',
            params={
                'villageId': village_id,
                'search': search.value,
                'offer': offer.value,
                'rate': TradeRate.value,
                'start': start,
                'count': count,
            }
        )

    def accept_offer(self, offer_id: int, village_id: int) -> dict:
        return self.invoke_action(
            action='acceptOffer',
            params={
                'offerId': offer_id,
                'villageId': village_id,
            }
        )

    def send_resources(
        self,
        dest_village_id: int,
        recurrences: int,
        resources: Resources,
        source_village_id: int
    ) -> dict:
        return self.invoke_action(
            action='sendResources',
            params={
                'destVillageId': dest_village_id,
                'recurrences': recurrences,
                'resources': resources.with_zeros(),
                'sourceVillageId': source_village_id,
            }
        )
