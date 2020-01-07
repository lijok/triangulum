from collections import Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.enums import RankingCategory


class Ranking(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='ranking')

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_kingdom_victory_points_with_treasures(self, start: int, end: int) -> dict:
        """Get kingdom victory points rankings with treasures

        Args:
            start: Index of the first ranking you wish to receive back
            end: Index of the last ranking you wish to receive back

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getKingdomVictoryPointsWithTreasures',
            params={
                'start': start,
                'end': end,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_kingdom_stats(self, kingdom_id: int) -> dict:
        """Get stats about a kingdom

        Args:
            kingdom_id: ID of the kingdom

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getKingdomStats',
            params={
                'kingdomId': kingdom_id,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_ranking(
        self,
        start: int,
        end: int,
        ranking_category: RankingCategory,
        _id: None,
    ) -> dict:
        """Get ranking information for a given ranking category

        Args:
            start: Index of the first ranking you wish to receive back
            end: Index of the last ranking you wish to receive back
            ranking_category: Ranking category you wish to receive information about
            _id: ID of an entity selection (through a UI mechanism) for which to return extra info

        Returns:
            dict
        """
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

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_ranking_average_points(self, ranking_category: RankingCategory) -> dict:
        """Get average points for a ranking category

        Args:
            ranking_category: Ranking category to get information for

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getRankingAveragePoints',
            params={
                'rankingType': ranking_category.value['ranking_type'],
                'rankingSubtype': ranking_category.value['ranking_subtype'],
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_rank_and_count(self, id: int, ranking_category: RankingCategory) -> dict:
        """[*]

        Args:
            id: UNKNOWN *
            ranking_category: Ranking category

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getRankAndCount',
            params={
                'id': id,
                'rankingType': ranking_category.value['ranking_type'],
                'rankingSubtype': ranking_category.value['ranking_subtype'],
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_world_stats(self) -> dict:
        """Get statistics about the game world such as the race and troops distributions

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getWorldStats'
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_kingdom_internal_ranking(self) -> dict:
        """Get internal kingdom rankings

        Returns:
            dict
        """
        return await self.invoke_action(
            action='getKingdomInternalRanking'
        )
