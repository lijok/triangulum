from collections import Callable


class BaseController:
    def __init__(self, action_handler: Callable, controller: str):
        self._action_handler = action_handler
        self.controller = controller

    def invoke_action(self, action: str, params: dict = None) -> dict:
        return self._action_handler(
            action=action,
            controller=self.controller,
            params=params
        )
