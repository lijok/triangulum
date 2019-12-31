from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import HeroItemType, HeroItemSlot


class Auctions(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='auctions')

    def get_running_auction_amount(
        self,
        filter_item_type: HeroItemType = HeroItemType.NONE,
        filter_slot: HeroItemSlot = HeroItemSlot.NONE,
        page: int = 0
    ) -> dict:
        return self.invoke_action(
            action='getRunningAuctionAmount',
            params={
                'filterItemType': filter_item_type.value,
                'filterSlot': filter_slot.value,
                'page': page,
            }
        )

    def get_running_auction_page(
        self,
        filter_item_type: HeroItemType = HeroItemType.NONE,
        filter_slot: HeroItemSlot = HeroItemSlot.NONE,
        page: int = 0
    ) -> dict:
        return self.invoke_action(
            action='getRunningAuctionPage',
            params={
                'filterItemType': filter_item_type.value,
                'filterSlot': filter_slot.value,
                'page': page,
            }
        )

    def place_bid(self, auction_id: int, bid_amount: int) -> dict:
        return self.invoke_action(
            action='placeBid',
            params={
                'auctionId': auction_id,
                'bidAmount': bid_amount,
            }
        )

    def get_seller_payout(self, item_id: int, amount: int) -> dict:
        return self.invoke_action(
            action='getSellerPayout',
            params={
                'itemId': item_id,
                'amount': amount,
            }
        )

    def sell_item(self, item_id: int, amount: int) -> dict:
        return self.invoke_action(
            action='sellItem',
            params={
                'itemId': item_id,
                'amount': amount,
            }
        )
