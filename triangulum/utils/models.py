from dataclasses import dataclass
from typing import List

from triangulum.utils.dataclasses import Bonuses
from triangulum.utils.enums import PlayerTribe, HeroItemType, HeroItemSlot, AuctionImages
from triangulum.utils.types import BoolInt, Timestamp, ScalarId


@dataclass
class _Base:
    pass


@dataclass
class Auction(_Base):
    id: int
    tribe_id: PlayerTribe
    item_type_id: HeroItemType
    strength: int
    bonuses: Bonuses
    amount: int
    status: BoolInt
    time_start: Timestamp
    time_end: Timestamp
    price: int
    bids: int
    highest_bid: int
    highest_bid_player_id: ScalarId
    highest_bidder_name: str
    slot: HeroItemSlot
    images: List[AuctionImages]
    stackable: bool
