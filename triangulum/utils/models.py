from dataclasses import dataclass
from enum import Enum
from typing import List, Union, Dict

from triangulum.utils.enums import RomanUnit, TeutonUnit, GaulUnit, MarkerType, MarkerColor, MarkerEditType, \
    MarkerDuration, FieldMessageType, MapFilterValues, AttacksFilterValues, Resource, HeroItemBonus, PlayerTribe, \
    HeroItemType, AuctionStatus, HeroItemSlot, Country, PlayerPunishmentStrikeReason, BuildingType, BuildingCategory, \
    HeroStatus, Gender, PlayerKingdomRole, KingdomType, KingdomState
from triangulum.utils.types import ScalarId, Timestamp, BoolInt, VillageId, LocationId, Coordinates
from triangulum.utils.util import unit_id_to_unit_nr


@dataclass
class _Base:
    def __iter__(self):
        for key, val in self.__dict__.items():
            if not key.startswith('_'):
                yield key, val


@dataclass
class _Units(_Base):
    _ENUM: Enum

    def with_zeros(self):
        return {
            str(self._ENUM[unit_name].value): unit_qty
            for unit_name, unit_qty in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[unit_name].value): unit_qty
            for unit_name, unit_qty in dict(self).items() if unit_qty > 0
        }

    def combat_format_with_zeros(self):
        return {
            str(unit_id_to_unit_nr(self._ENUM[unit_name].value)): unit_qty
            for unit_name, unit_qty in dict(self).items()
        }

    def combat_format_without_zeros(self):
        return {
            str(unit_id_to_unit_nr(self._ENUM[unit_name].value)): unit_qty
            for unit_name, unit_qty in dict(self).items() if unit_qty > 0
        }


@dataclass
class RomanUnits(_Units):
    _ENUM: Enum = RomanUnit
    _TRIBE: PlayerTribe = PlayerTribe.ROMAN.value

    LEGIONNAIRE: int = 0
    PRAETORIAN: int = 0
    IMPERIAN: int = 0
    EQUITES_LEGATI: int = 0
    EQUITES_IMPERATORIS: int = 0
    EQUITES_CAESARIS: int = 0
    BATTERING_RAM: int = 0
    FIRE_CATAPULT: int = 0
    SENATOR: int = 0
    SETTLER: int = 0
    HERO: int = 0


@dataclass
class TeutonUnits(_Units):
    _ENUM: Enum = TeutonUnit
    _TRIBE: PlayerTribe = PlayerTribe.TEUTON.value

    CLUBSWINGER: int = 0
    SPEARFIGHTER: int = 0
    AXEFIGHTER: int = 0
    SCOUT: int = 0
    PALADIN: int = 0
    TEUTONIC_KNIGHT: int = 0
    RAM: int = 0
    CATAPULT: int = 0
    CHIEF: int = 0
    SETTLER: int = 0
    HERO: int = 0


@dataclass
class GaulUnits(_Units):
    _ENUM: Enum = GaulUnit
    _TRIBE: PlayerTribe = PlayerTribe.GAUL.value

    PHALANX: int = 0
    SWORDSMAN: int = 0
    PATHFINDER: int = 0
    THEUTATES_THUNDER: int = 0
    DRUIDRIDER: int = 0
    HAEDUAN: int = 0
    RAM: int = 0
    TREBUCHET: int = 0
    CHIEFTAIN: int = 0
    SETTLER: int = 0
    HERO: int = 0


@dataclass
class Marker:
    OWNER: int
    TYPE: MarkerType
    COLOR: MarkerColor
    EDIT_TYPE: MarkerEditType
    OWNER_ID: int
    TARGET_ID: int

    def as_dict(self):
        return {
            'owner': self.OWNER,
            'type': self.TYPE,
            'color': self.COLOR,
            'editType': self.EDIT_TYPE,
            'ownerId': self.OWNER_ID,
            'targetId': self.TARGET_ID
        }


@dataclass
class FieldMessage:
    TEXT: str
    TYPE: FieldMessageType
    DURATION: MarkerDuration
    CELL_ID: int
    TARGET_ID: int

    def as_dict(self):
        return {
            'text': self.TEXT,
            'type': self.TYPE,
            'duration': self.DURATION,
            'cellId': self.CELL_ID,
            'targetId': self.TARGET_ID
        }


@dataclass
class _FilterScalar(_Base):
    _ENUM: Enum

    def sum(self):
        scalar = 0

        for toggle_name, toggle_val in dict(self).items():
            if toggle_val:
                scalar += self._ENUM[toggle_name].value

        return scalar


@dataclass
class MapFilter(_FilterScalar):
    _ENUM: Enum = MapFilterValues

    NONE: bool = False
    KINGDOM_BORDERS: bool = True
    CAPITAL_VILAGES: bool = True
    OWN_MARKERS: bool = True
    GAME_MESSAGES: bool = True
    PLAYER_MESSAGES: bool = True
    TREASURES: bool = True


@dataclass
class AttacksFilter(_FilterScalar):
    _ENUM: Enum = AttacksFilterValues

    NONE: bool = False
    KINGDOM: bool = True


@dataclass
class _Resources(_Base):
    _ENUM: Enum

    def with_zeros(self):
        return {
            str(self._ENUM[resource_name].value): resource_qty
            for resource_name, resource_qty in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[resource_name].value): resource_qty
            for resource_name, resource_qty in dict(self).items() if resource_qty > 0
        }


@dataclass
class Resources(_Resources):
    _ENUM = Resource

    WOOD: int
    CLAY: int
    IRON: int
    CROP: int


@dataclass
class Bonuses(_Base):
    _ENUM = HeroItemBonus

    XP: int = None
    BARRACKS: int = None
    STABLE: int = None
    WORKSHOP: int = None
    SPEED_RETURN: int = None
    SPEED_OWN_VILLAGES: int = None
    SPEED_KINGDOM_VILLAGES: int = None
    SPEED_STAMINA: int = None
    RAID: int = None
    NATARS: int = None
    UNIT_ID: int = None
    UNIT_STRENGTH: int = None
    FIGHT_STRENGTH: int = None
    HEALTH_REGEN: int = None
    CULTURE_POINTS: int = None
    ARMOR: int = None
    SPEED_HERO: int = None
    SPEED_HORSE: int = None
    RESKILL: int = None
    TROOP_HEALING: int = None
    EYESIGHT: int = None
    CHICKEN: int = None
    RESOURCES: int = None
    CROP: int = None
    POTION: int = None

    def with_zeros(self):
        return {
            str(self._ENUM[bonus_type].value): bonus_value
            for bonus_type, bonus_value in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[bonus_type].value): bonus_value
            for bonus_type, bonus_value in dict(self).items() if bonus_value > 0
        }


@dataclass
class Auction(_Base):
    id: ScalarId
    tribe_id: PlayerTribe
    item_type_id: HeroItemType
    strength: int
    bonuses: Bonuses
    amount: int
    status: AuctionStatus
    time_start: Timestamp
    time_end: Timestamp
    price: int
    bids: int
    highest_bid: int
    highest_bidder_player_id: ScalarId
    highest_bidder_name: str
    slot: HeroItemSlot
    images: List[str]  # List of strings such as "artwork", "axe0_2", "helmet2_1" etc
    stackable: bool


@dataclass
class Avatar(_Base):  # Lobby
    user_account_identifier: ScalarId
    avatar_identifier: int
    avatar_name: str
    consumers_id: int
    world_name: str
    country: Country
    account_name: str
    is_banned: bool
    is_suspended: bool
    suspension_time: int
    limitation: int  # TODO: Check what this is, could be an enum, could be PlayerPunishmentType
    ban_reason: PlayerPunishmentStrikeReason
    ban_payment_provider: str


@dataclass
class AvatarInformation(_Base):  # Lobby
    avatar_identifier: int
    user_account_identifier: ScalarId
    signup_time: Timestamp
    ranking: int
    population: int
    villages: int
    last_login: Timestamp
    last_click: Timestamp
    building_queue: int
    building_queue_master: int
    incoming_attacks: int
    next_incoming_attack: Timestamp
    spawned_on_map: Timestamp
    deletion_time: Timestamp


@dataclass
class Bid(_Base):
    id: ScalarId
    player_id: ScalarId
    auction_id: ScalarId
    max_bid: int
    time: Timestamp
    deleted: BoolInt


@dataclass
class Building(_Base):
    building_type: BuildingType
    village_id: VillageId
    location_id: LocationId
    lvl: int
    lvl_next: int
    is_max_lvl: bool
    lvl_max: int
    upgrade_costs: Resources
    next_upgrade_costs: Dict[Resources]  # TODO: Is there a better way to express this?
    upgrade_time: int
    next_upgrade_times: dict  # TODO: Is there a better way to express this?
    upgrade_supply_usage: int  # crop usage / pop increase of next lvl
    upgrade_supply_usage_sums: dict  # TODO: Is there a better way to express this?
    category: BuildingCategory
    sort_order: BuildingType  # TODO: Unsure what this is but it's always the same as building_type
    effect: List[int]  # TODO: Is there a better way to express this?


@dataclass
class BuildingQueue(_Base):
    village_id: VillageId
    tribe_id: PlayerTribe
    free_slots: dict  # TODO: Is there a better way to express this?
    queues: Dict[List[Dict]]  # TODO: Is there a better way to express this?
    can_use_instant_construction: bool
    can_use_instant_construction_only_in_village: bool


@dataclass
class CardgameRolls(_Base):
    player_id: ScalarId
    free_rolls: int
    has_daily_roll: BoolInt


@dataclass
class FarmList(_Base):
    list_id: ScalarId
    list_name: str
    last_sent: Timestamp
    last_changed: Timestamp
    units: Union[GaulUnits, RomanUnits, TeutonUnits]  # TODO: This is the complex ones with unit_nr
    order_nr: int
    village_ids: List[VillageId]
    entry_ids: List[ScalarId]
    is_default: bool
    max_entries_count: int


@dataclass
class FarmListEntry(_Base):
    entry_id: ScalarId
    village_id: VillageId
    village_name: str
    units: Union[GaulUnits, RomanUnits, TeutonUnits]  # TODO: This is the complex ones with unit_nr
    target_owner_id: ScalarId
    belongs_to_king: ScalarId
    population: int
    coords: Coordinates
    is_oasis: bool
    last_report: int  # TODO: Possible a ScalarId


@dataclass
class GroupInvitation(_Base):
    id: ScalarId
    group_id: ScalarId
    group_name: str
    player_id: ScalarId
    player_name: str
    invited_by: ScalarId
    invited_by_name: str
    invited_as: int  # TODO: This is probably an enum that we don't have
    invitation_time: Timestamp
    custom_text: str
    cell_id: int  # TODO: This might be something else than an int
    invited_by_role: int  # TODO: same as invited_as


@dataclass
class Hero(_Base):
    player_id: ScalarId
    village_id: VillageId
    dest_village_id: VillageId
    status: HeroStatus
    health: float
    last_health_time: Timestamp
    base_regeneration_rate: int
    regeneration_rate: int
    fight_strength: int
    fight_strength_points: int
    att_bonus_points: int
    def_bonus_points: int
    res_bonus_points: int
    res_bonus_type: int
    free_points: int
    speed: int
    until_time: Timestamp
    bonuses: Bonuses  # TODO: Has a unitBonuses inside that wont render with this model
    max_scrolls_per_day: int
    scrolls_used_today: int
    waterbucket_used_today: int
    ointments_used_today: int
    adventure_point_card_used_today: int
    resource_chests_used_today: int
    crop_chests_used_today: int
    artwork_used_today: int
    is_moving: bool
    adventure_points: int
    adventure_point_time: Timestamp
    level_up: BoolInt
    xp: int
    xp_this_level: int
    xp_next_level: int
    level: int


@dataclass
class HeroFace(_Base):
    player_id: ScalarId
    fetched_from_lobby: BoolInt
    gender: Gender
    hair_color: int  # As in assets
    face: dict  # TODO: Is there a better way to express this?


@dataclass
class HeroItem(_Base):
    id: ScalarId
    player_id: ScalarId
    tribe_id: PlayerTribe
    in_slot: BoolInt
    item_id: HeroItemType
    item_type: HeroItemType
    amount: int
    strength: int
    images: List[str]
    bonuses: Bonuses
    stackable: bool
    slot: int  # TODO: Enum Hero slots
    last_change: Timestamp
    has_speed_bonus: bool
    inventory_slot_nr: int
    previous_owners: int
    upgrade_level: int
    upgradable_item_type: bool
    item_quality: int
    item_tier: int
    base_upgrade_bonus: Bonuses
    card_game_item: bool
    premium_item: bool
    upgraded_item: bool


@dataclass
class KingdomMember(_Base):
    player_id: ScalarId
    name: str
    is_king: bool
    is_duke: bool
    kingdom_role: PlayerKingdomRole
    kingdom_id: ScalarId
    population: int
    victory_points: int
    villages: int
    viceking_connection: int  # TODO: What's this?


@dataclass
class GroupDescription(_Base):
    group_id: ScalarId
    public_description: str
    internal_description: str


@dataclass
class Treaty(_Base):
    id: ScalarId
    kingdom_id: ScalarId
    other_kingdom_id: ScalarId
    type: KingdomState
    offered: Timestamp
    other_kingdom_tag: str
    status: int = 2  # TODO: Can a status be other than 2?


@dataclass
class Diplomacy(_Base):
    treaties: List[Treaty]
    own_offers: List[Treaty]  # TODO: Double check this
    foreign_offers: List[Treaty]  # TODO: Double check this


@dataclass
class Kingdom(_Base):
    group_id: ScalarId
    members: List[KingdomMember]
    tag: str
    creation_time: Timestamp
    kingdom_type: KingdomType
    description: GroupDescription
    diplomacy: Diplomacy
