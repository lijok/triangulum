class ActionNotImplementedError(Exception):
    """This action has not yet been implemented.
    Possibly due to lack of information regarding this action.
    If you have the required data for this action, or know how
    to reproduce it in the UI, please raise a PR
    """
    pass


class AuthenticationError(Exception):
    """An unknown error occured during authentication"""
    pass


class NotAuthenticated(Exception):
    """User not authenticated"""
    pass
