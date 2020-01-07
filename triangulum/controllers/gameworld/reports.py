from typing import List, Callable

from cachetools import TTLCache

from triangulum.controllers.base import BaseController
from triangulum.utils.cache import cached, MAX_SIZE, TTL
from triangulum.utils.enums import ReportsCollection, ReportFilter, ShareReportWith


class Reports(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='reports')

    async def get_last_reports(
        self,
        collection: ReportsCollection,
        start: int,
        count: int,
        filters: List[ReportFilter],
        also_get_total_number: bool
    ) -> dict:
        """Get latest reports

        Args:
            collection: Report owners, i.e own, kingdom or society *
            start: Starting index of the first report to retrieve
            count: Last index of the reports to retrieve
            filters: List of filters to filter the reports through
            also_get_total_number: Also get the total number of reports
        """
        return await self.invoke_action(
            action='getLastReports',
            params={
                'collection': collection.value,
                'start': start,
                'count': count,
                'filters': [i.value for i in filters],
                'alsoGetTotalNumber': also_get_total_number,
            }
        )

    @cached(TTLCache(MAX_SIZE, TTL))
    async def get_full_report(
        self,
        id: str,
        collection: ReportsCollection,
        security_code: str = ""  # Not sure what this is, could be for sharing reports
    ) -> dict:
        """Get a full report

        Args:
            id: ID of the report
            collection: Report owners, i.e own, kingdom or society *
            security_code: UNKNOWN *
        """
        return await self.invoke_action(
            action='getFullReport',
            params={
                'id': id,
                'collection': collection.value,
                'securityCode': security_code
            }
        )

    async def mark_as_favorite(self, id: str, collection: ReportsCollection, security_code: str) -> dict:
        """Mark a report as favorite

        Args:
            id: ID of the report
            collection: Report owners, i.e own, kingdom or society *
            security_code: UNKNOWN *
        """
        return await self.invoke_action(
            action='markAsFavorite',
            params={
                'id': id,
                'collection': collection.value,
                'securityCode': security_code,
            }
        )

    async def share_report(
        self,
        id: str,
        share_with: ShareReportWith,
        share_with_id: int,
        share_message: str,
        collection: ReportsCollection
    ) -> dict:
        """Share a report with a player, kingdom or a society

        Args:
            id: ID of the report
            share_with: Type of entity to share the report with
            share_with_id: ID of the entity to share the report with
                i.e kingdom ID if share_with == ShareReportWith.KINGDOM
            share_message: Message to send together with the report
            collection: Report owners, i.e own, kingdom or society *
        """
        return await self.invoke_action(
            action='shareReport',
            params={
                'id': id,
                'shareWith': share_with,
                'shareParam': share_with_id,
                'shareMessage': share_message,
                'collection': collection.value,
            }
        )

    async def remove_as_favorite(self, body_id: str) -> dict:
        """Remove a report from your favorites

        Args:
            body_id: UNKNOWN *
        """
        return await self.invoke_action(
            action='removeAsFavorite',
            params={
                'bodyId': body_id,
            }
        )
