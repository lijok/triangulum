from typing import List, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import ReportsCollection, ReportFilter, ShareReportWith


class Reports(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='reports')

    def get_last_reports(
        self,
        collection: ReportsCollection,
        start: int,
        count: int,
        filters: List[ReportFilter],
        also_get_total_number: bool
    ) -> dict:
        return self.invoke_action(
            action='getLastReports',
            params={
                'collection': collection.value,
                'start': start,
                'count': count,
                'filters': [i.value for i in filters],
                'alsoGetTotalNumber': also_get_total_number,
            }
        )

    def get_full_report(
        self,
        id: str,
        collection: ReportsCollection,
        security_code: str = ""  # Not sure what this is, could be for sharing reports
    ) -> dict:
        return self.invoke_action(
            action='getFullReport',
            params={
                'id': id,
                'collection': collection.value,
                'securityCode': security_code
            }
        )

    def mark_as_favorite(self, id: str, collection: ReportsCollection, security_code: str) -> dict:
        return self.invoke_action(
            action='markAsFavorite',
            params={
                'id': id,
                'collection': collection.value,
                'securityCode': security_code,
            }
        )

    def share_report(
        self,
        id: str,
        share_with: ShareReportWith,
        share_with_id: int,  # ID of the Society or Player to share with
        share_message: str,
        collection: ReportsCollection
    ) -> dict:
        return self.invoke_action(
            action='shareReport',
            params={
                'id': id,
                'shareWith': share_with,
                'shareParam': share_with_id,
                'shareMessage': share_message,
                'collection': collection.value,
            }
        )

    def remove_as_favorite(self, body_id: str) -> dict:
        return self.invoke_action(
            action='removeAsFavorite',
            params={
                'bodyId': body_id,
            }
        )
