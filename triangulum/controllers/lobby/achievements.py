from collections import Callable

from triangulum.controllers.base import BaseController


class Achievements(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='achievements')

    async def update(self) -> dict:
        """[*]

        Returns:
            dict
        """
        return await self.invoke_action(
            action='update'
        )

    async def collect_reward(self, achievement_id: int) -> dict:
        """Collect an achievement reward

        Args:
            achievement_id: ID of the achievement

        Returns:
            dict
        """
        return await self.invoke_action(
            action='collectReward',
            params={
                'achievementId': achievement_id
            }
        )
