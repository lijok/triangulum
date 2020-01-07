from collections import Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.enums import LogType
from triangulum.utils.exceptions import ActionNotImplementedError


class Logger(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='logger')

    async def log_message(self, message: str, prefix: str, log_type: LogType, details: str) -> dict:
        """[*-]

        Args:
            message: UNKNOWN *
            prefix: UNKNOWN *
            log_type: UNKNOWN *
            details: UNKNOWN *
        """
        raise ActionNotImplementedError

        # return await self.invoke_action(
        #     action='logMessage',
        #     params={
        #         'message': message,
        #         'prefix': prefix,
        #         'logType': log_type.value,
        #         'details': details,
        #     }
        # )
