from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import ShopVersion
from triangulum.utils.exceptions import ActionNotImplementedError


class Payment(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='payment')

    async def get_payment_shop_url(self, shop_version: ShopVersion) -> dict:
        """UNKNOWN *

        Args:
            shop_version: UNKNOWN *

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getPaymentShopUrl',
            params={
                'shopVersion': shop_version,
            }
        )

    async def get_smallest_package(self, feature_price: int) -> dict:
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='getSmallestPackage',
        #     params={
        #         'featurePrice': feature_price,  # TODO: Enum this
        #     }
        # )
