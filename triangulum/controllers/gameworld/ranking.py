from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import RankingCategory


class Ranking(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='ranking')

    async def get_kingdom_victory_points_with_treasures(self, start: int, end: int) -> dict:
        return await self.invoke_action(
            action='getKingdomVictoryPointsWithTreasures',
            params={
                'start': start,
                'end': end,
            }
        )

    async def get_kingdom_stats(self, kingdom_id: int) -> dict:
        return await self.invoke_action(
            action='getKingdomStats',
            params={
                'kingdomId': kingdom_id,
            }
        )

    async def get_ranking(
        self,
        start: int,
        end: int,
        ranking_category: RankingCategory,
        _id: None,  # Returns some info on the specific player selection in rankings board
    ) -> dict:
        params = {
            'start': start,
            'end': end,
            'rankingType': ranking_category.value['ranking_type'],
            'rankingSubtype': ranking_category.value['ranking_subtype'],
        }
        if _id:
            params['id'] = _id

        return await self.invoke_action(
            action='getRanking',
            params=params
        )

    async def get_ranking_average_points(self, ranking_category: RankingCategory) -> dict:
        return await self.invoke_action(
            action='getRankingAveragePoints',
            params={
                'rankingType': ranking_category.value['ranking_type'],
                'rankingSubtype': ranking_category.value['ranking_subtype'],
            }
        )

    async def get_rank_and_count(self, id: int, ranking_category: RankingCategory) -> dict:
        return await self.invoke_action(
            action='getRankAndCount',
            params={
                'id': id,
                'rankingType': ranking_category.value['ranking_type'],
                'rankingSubtype': ranking_category.value['ranking_subtype'],
            }
        )

    async def get_world_stats(self) -> dict:
        return await self.invoke_action(
            action='getWorldStats'
        )

    async def get_kingdom_internal_ranking(self) -> dict:
        return await self.invoke_action(
            action='getKingdomInternalRanking'
        )
