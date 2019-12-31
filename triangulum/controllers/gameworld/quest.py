from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import DialogActionCommand


class Quest(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='quest')

    async def get_puzzle(self) -> dict:
        return await self.invoke_action(
            action='getPuzzle'
        )

    async def solve_puzzle(self, moves: list) -> dict:
        return await self.invoke_action(
            action='solvePuzzle',
            params={
                'moves': moves,  # TODO: Moves enums (1 -> 2 etc)
            }
        )

    async def dialog_action(
        self,
        quest_id: int,
        dialog_id: int,
        command: DialogActionCommand,
        input: str = ""
    ) -> dict:
        return await self.invoke_action(
            action='dialogAction',
            params={
                'questId': quest_id,
                'dialogId': dialog_id,
                'command': command,  # TODO: Check this, it's probably enum
                'input': input
            }
        )

    async def check_reward_collectible(self, quest_id: int, village_id: int) -> dict:
        return await self.invoke_action(
            action='checkRewardCollectible',
            params={
                'questId': quest_id,
                'villageId': village_id,
            }
        )

    async def collect_reward(self, quest_id: int, village_id: int) -> dict:
        return await self.invoke_action(
            action='collectReward',
            params={
                'questId': quest_id,
                'villageId': village_id,
            }
        )

    async def reset_daily_quest(self, quest_id: int) -> dict:
        return await self.invoke_action(
            action='resetDailyQuest',
            params={
                'questId': quest_id,
            }
        )
