# triangulum

Travian Kingdoms API Client 

## Table of Contents

* [Installation](#Installation)
	* [Building from zip](#Building-from-zip)
* [Usage](#Usage)
* [Missing Controllers](#Missing-Controllers)
* [Missing Actions](#Missing-Actions)


## Installation

### Building from zip
```sh
python setup.py sdist --formats=zip
cd dist
pip install triangulum-x.x.x.zip
```

## Usage

```py
from triangulum.clients.lobby import LobbyClient
import asyncio

loop = asyncio.get_event_loop()
lobby = LobbyClient()
loop.run_until_complete(lobby.authenticate(email='', password='')

gameworld = loop.run_until_complete(lobby.connect_to_gameworld(gameworld_id='', gameworld_name=''))

loop.run_until_complete(gameworld.player.get_player_info(0))
```

There is a built in caching mechanism that, when activated, will reduce the amount of repeat network calls being made
in your program that is utilizing this client, by returning the same response, when a function is called with the same
arguments within the TTL.
Only safe to cache actions are making use of the cache, and it is by default disabled.

There are 2 environment variables that need to be set to activate the caching mechanism:
- TRIANGULUM_CACHE_MAX_SIZE = specifies the maximum number of cached entries for a given function
- TRIANGULUM_CACHE_TTL = specifies the time to live in seconds for any cached content

## Missing Controllers
> There are 3 controllers that have not yet been implemented
> * cheat
> * cheatsheat
> * adb
> * messageBoard
>
> These (except for messageBoard) do not contain any actions that can be used by a non MH client

## Missing Actions
```py
{
    "troops": [
        "fetchTributesForVillages",
        "release",
        "sendBackAll"
    ],
    "map": [
        "getConnectedVillages"
    ],
    "village": [
        "grantProtection",
        "upgradeToTown",
        "checkUnitProductionvillageId"
    ],
    "player": [
        "offerPeaceTreaty",
        "fetchReferralBonus",
        "logError",
        "sanityCheck"
    ],
    "kingdom": [
        "offerUnion",
        "assignTreasurySlot",
        "deleteTreasurySlotPermission",
        "cancelDuke",
        "checkRelocation",
        "offerRelocation",
        "checkUnion",
        "getDukeDismissalInformation"
    ],
    "hero": [
        "bandagesUpgrade",
        "transformPiles"
    ],
    "building": [
        "transformHiddenTreasury",
        "cancelTransformHiddenTreasury",
        "claimHiddenTreasuryResources",
        "makeVillageCapital",
        "produceFirst",
        "countForTransformingToTreasuryFreeSlots",
        "getWorldWonderRankByVillageId"
    ],
    "kingdomTreaty": [
        "accept"
    ],
    "society": [
        "kick",
        "leave",
        "acceptInvitation"
    ],
    "payment": [
        "getPaymentErrors"
    ],
    "ranking": [
        "getWorldEndStats",
        "getWorldEndSummary"
    ],
    "premiumFeature": [
        "tributeFetchInstantly",
        "tributeFetchAllInstantly",
        "traderSlot",
        "traderArriveInstantly"
    ]
    
}
```
