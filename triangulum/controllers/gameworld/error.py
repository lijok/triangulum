from collections import Callable

from triangulum.controllers.base import BaseController


class Error(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='error')

    def log_javascript_error(self, player_id: int, error: str) -> dict:
        return self.invoke_action(
            action='logJavascriptError',
            params={
                'playerId': player_id,
                'error': error,
            }
        )
