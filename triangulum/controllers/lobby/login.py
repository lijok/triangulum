from collections import Callable

from triangulum.controllers.base import BaseController


class Login(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='login')

    def logout(self) -> dict:
        return self.invoke_action(
            action='logout'
        )
