# Authentication

> To authenticate, use this code:

```python
from triangulum.clients.lobby import LobbyClient
import asyncio

loop = asyncio.get_event_loop()
lobby = LobbyClient()
loop.run_until_complete(lobby.authenticate(email='', password='')

```

> Then, to connect to a gameworld:

```python
gameworld = loop.run_until_complete(lobby.connect_to_gameworld(gameworld_id='', gameworld_name=''))
```

<aside class="notice">
To get the gameworld_id and gameworld_name, use <code>lobby.cache.get({'names':['Collection:Avatar']})</code>.
</aside>