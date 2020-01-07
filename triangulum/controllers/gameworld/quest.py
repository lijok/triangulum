from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.enums import DialogActionCommand


class Quest(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='quest')

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_puzzle(self) -> dict:
        """[-]Get the map puzzle during registration
        """
        return await self.invoke_action(
            action='getPuzzle'
        )

    async def solve_puzzle(self, moves: list) -> dict:
        """[-]Provide a solution to the puzzle received using get_puzzle

        Args:
            moves: List of moves that provide a solution to the puzzle
        """
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
        """[-]Supply an action / answer to a quest dialog during registration
        such as your name, whether you wish to be a duke or a king etc

        Args:
            quest_id: ID of the quest
            dialog_id: ID of the dialog
            command: Command to supply
            input: Input for the command if the command requires one, such as when using Command.SET_NAME
        """
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
        """Check whether a reward for a quest is collectible

        Args:
            quest_id: ID of a quest
            village_id: ID of a village
        """
        return await self.invoke_action(
            action='checkRewardCollectible',
            params={
                'questId': quest_id,
                'villageId': village_id,
            }
        )

    async def collect_reward(self, quest_id: int, village_id: int) -> dict:
        """Collect a reward for a completed quest

        Args:
            quest_id: ID of the quest
            village_id: ID of the village to claim the reward in
        """
        return await self.invoke_action(
            action='collectReward',
            params={
                'questId': quest_id,
                'villageId': village_id,
            }
        )

    async def reset_daily_quest(self, quest_id: int) -> dict:
        """Swap out a daily quest for a new one

        Args:
            quest_id: ID of the daily quest
        """
        return await self.invoke_action(
            action='resetDailyQuest',
            params={
                'questId': quest_id,
            }
        )
