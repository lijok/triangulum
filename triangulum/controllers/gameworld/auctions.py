from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.enums import HeroItemType, HeroItemSlot


class Auctions(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='auctions')

    async def get_running_auction_amount(
        self,
        filter_item_type: HeroItemType = HeroItemType.NONE,
        filter_slot: HeroItemSlot = HeroItemSlot.NONE,
        page: int = 0
    ) -> dict:
        """Get prices of running auctions matching filters

        Args:
            filter_item_type: Item type to filter by
            filter_slot: Hero item slot to filter by
            page: Running auction page

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getRunningAuctionAmount',
            params={
                'filterItemType': filter_item_type.value,
                'filterSlot': filter_slot.value,
                'page': page,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_running_auction_page(
        self,
        filter_item_type: HeroItemType = HeroItemType.NONE,
        filter_slot: HeroItemSlot = HeroItemSlot.NONE,
        page: int = 0
    ) -> dict:
        """Get items in running auction page

        Args:
            filter_item_type: Item type to filter by
            filter_slot: Hero item slot to filter by
            page: Running auction page

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getRunningAuctionPage',
            params={
                'filterItemType': filter_item_type.value,
                'filterSlot': filter_slot.value,
                'page': page,
            }
        )

    async def place_bid(self, auction_id: int, bid_amount: int) -> dict:
        """Place bid on an auction item

        Args:
            auction_id: ID of the auction entry
            bid_amount: Amount in Silver to bid for the item

        Returns:
            dict
        """
        return await self.invoke_action(
            action='placeBid',
            params={
                'auctionId': auction_id,
                'bidAmount': bid_amount,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_seller_payout(self, item_id: int, amount: int) -> dict:
        """Get the payout value of an auctionable item

        Args:
            item_id: ID of an item you wish to auction
            amount: Amount of items you wish to auction

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getSellerPayout',
            params={
                'itemId': item_id,
                'amount': amount,
            }
        )

    async def sell_item(self, item_id: int, amount: int) -> dict:
        """Sell an item on the auction

        Args:
            item_id: ID of an item you wish to auction
            amount: Amount of items you wish to auction

        Returns:
            dict
        """
        return await self.invoke_action(
            action='sellItem',
            params={
                'itemId': item_id,
                'amount': amount,
            }
        )
