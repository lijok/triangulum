from collections import Callable

from triangulum.controllers.base import BaseController


class Achievements(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='achievements')

    async def update(self) -> dict:
        return await self.invoke_action(
            action='update'
        )

    async def collect_reward(self, achievement_id: int) -> dict:
        return await self.invoke_action(
            action='collectReward',
            params={
                'achievementId': achievement_id
            }
        )
