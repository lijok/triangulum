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

lobby = LobbyClient(email='', password='')
gameworld = lobby.connect_to_gameworld(gameworld_id='', gameworld_name='')

gameworld.player.get_player_info(0)
```


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
