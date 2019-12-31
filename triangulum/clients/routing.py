class RootURL:
    LOBBY = 'https://lobby.kingdoms.com/api'
    MELLON = 'https://mellon-t5.traviangames.com'
    GAMEWORLD = 'https://{gameworld}.kingdoms.com'


class URL:
    LOBBY_API = f'{RootURL.LOBBY}/index.php'

    LOBBY_AUTH = f'{RootURL.MELLON}/authentication/login'
    LOBBY_AUTH_STEP_2 = f'{RootURL.MELLON}/authentication/login/ajax/form-validate?msid={{msid}}&msname=msid'
    LOBBY_AUTH_STEP_3 = f'{RootURL.LOBBY}/login.php?token={{token}}&msid={{msid}}&msname=msid'

    GAMEWORLD_API = f'{RootURL.GAMEWORLD}/api'
    GAMEWORLD_JOIN = f'{RootURL.MELLON}/game-world/join/gameWorldId/{{gameworld_id}}?msid={{msid}}&msname=msid'
    GAMEWORLD_AUTH = f'{RootURL.GAMEWORLD}/api/login.php?token={{token}}&msid={{msid}}&msname=msid'
