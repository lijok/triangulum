from collections import Callable

from triangulum.controllers.base import BaseController


class Achievements(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='achievements')

    def update(self) -> dict:
        return self.invoke_action(
            action='update'
        )

    def collect_reward(self, achievement_id: int) -> dict:
        return self.invoke_action(
            action='collectReward',
            params={
                'achievementId': achievement_id
            }
        )
