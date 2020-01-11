from dataclasses import dataclass, is_dataclass
from enum import Enum
from typing import List, Union, Dict

from triangulum.utils import enums
from triangulum.utils.types import ScalarId, Timestamp, BoolInt, LocationId, MapId, TroopId, FilterScalar, \
    ResourceFieldDistribution
from triangulum.utils.util import unit_id_to_unit_nr


@dataclass
class _Base:
    def __iter__(self):
        for key, val in self.__dict__.items():
            if not key.startswith('_'):
                yield key, val

    @classmethod
    def _load(cls, obj, params):
        """Dummy _load method for when one is not defined in the child class"""
        return obj, params

    @classmethod
    def load(cls, params):
        # instantiate an empty object
        obj = cls(**{key: None for key in cls.__dataclass_fields__.keys()})

        # let any custom loading happen first
        obj, params = cls._load(obj, params)
        for key, val in params.items():
            val_type = obj.__annotations__[key]

            if is_dataclass(val_type):
                obj.__dict__[key] = val_type.load(val)
            else:
                obj.__dict__[key] = val_type(val)

        return obj


@dataclass
class _NumberedDict(_Base):
    _ENUM: Enum

    def with_zeros(self):
        return {
            str(self._ENUM[name].value): quantity
            for name, quantity in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[name].value): quantity
            for name, quantity in dict(self).items() if quantity > 0
        }


@dataclass
class _Units(_NumberedDict):
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
    _ENUM: Enum = enums.RomanUnit
    _TRIBE: enums.PlayerTribe = enums.PlayerTribe.ROMAN.value

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
    _ENUM: Enum = enums.TeutonUnit
    _TRIBE: enums.PlayerTribe = enums.PlayerTribe.TEUTON.value

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
    _ENUM: Enum = enums.GaulUnit
    _TRIBE: enums.PlayerTribe = enums.PlayerTribe.GAUL.value

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
    TYPE: enums.MarkerType
    COLOR: enums.MarkerColor
    EDIT_TYPE: enums.MarkerEditType
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
    TYPE: enums.FieldMessageType
    DURATION: enums.MarkerDuration
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
class Resources(_NumberedDict):
    _ENUM = enums.Resource

    WOOD: int
    CLAY: int
    IRON: int
    CROP: int


@dataclass
class Bonuses(_NumberedDict):
    _ENUM = enums.HeroItemBonus

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


@dataclass
class Auction(_Base):
    id: ScalarId
    tribe_id: enums.PlayerTribe
    item_type_id: enums.HeroItemType
    strength: int
    bonuses: Bonuses
    amount: int
    status: enums.AuctionStatus
    time_start: Timestamp
    time_end: Timestamp
    price: int
    bids: int
    highest_bid: int
    highest_bidder_player_id: ScalarId
    highest_bidder_name: str
    slot: enums.HeroItemSlot
    images: List[str]  # List of strings such as "artwork", "axe0_2", "helmet2_1" etc
    stackable: bool


@dataclass
class Avatar(_Base):  # Lobby
    user_account_identifier: ScalarId
    avatar_identifier: int
    avatar_name: str
    consumers_id: int
    world_name: str
    country: enums.Country
    account_name: str
    is_banned: bool
    is_suspended: bool
    suspension_time: int
    limitation: int  # TODO: Check what this is, could be an enum, could be PlayerPunishmentType
    ban_reason: enums.PlayerPunishmentStrikeReason
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
    building_type: enums.BuildingType
    village_id: MapId
    location_id: LocationId
    lvl: int
    lvl_next: int
    is_max_lvl: bool
    lvl_max: int
    upgrade_costs: Resources
    next_upgrade_costs: Dict[int, Resources]  # TODO: Is there a better way to express this?
    upgrade_time: int
    next_upgrade_times: dict  # TODO: Is there a better way to express this?
    upgrade_supply_usage: int  # crop usage / pop increase of next lvl
    upgrade_supply_usage_sums: dict  # TODO: Is there a better way to express this?
    category: enums.BuildingCategory
    sort_order: enums.BuildingType  # TODO: Unsure what this is but it's always the same as building_type
    effect: List[int]  # TODO: Is there a better way to express this?


@dataclass
class BuildingQueue(_Base):
    village_id: MapId
    tribe_id: enums.PlayerTribe
    free_slots: dict  # TODO: Is there a better way to express this?
    queues: Dict[int, List[dict]]  # TODO: Is there a better way to express this?
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
    village_ids: List[MapId]
    entry_ids: List[ScalarId]
    is_default: bool
    max_entries_count: int


@dataclass
class FarmListEntry(_Base):
    entry_id: ScalarId
    village_id: MapId
    village_name: str
    units: Union[GaulUnits, RomanUnits, TeutonUnits]  # TODO: This is the complex ones with unit_nr
    target_owner_id: ScalarId
    belongs_to_king: ScalarId
    population: int
    coords: MapId
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
    village_id: MapId
    dest_village_id: MapId
    status: enums.HeroStatus
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
    gender: enums.Gender
    hair_color: int  # As in assets
    face: dict  # TODO: Is there a better way to express this?


@dataclass
class HeroItem(_Base):
    id: ScalarId
    player_id: ScalarId
    tribe_id: enums.PlayerTribe
    in_slot: BoolInt
    item_id: enums.HeroItemType
    item_type: enums.HeroItemType
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
    kingdom_role: enums.PlayerKingdomRole
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
    type: enums.KingdomState
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
    kingdom_type: enums.KingdomType
    description: GroupDescription
    diplomacy: Diplomacy


@dataclass
class MapDetails(_Base):
    is_oasis: bool
    oasis_type: enums.VillageOasisStatus  # TODO: Double check this
    has_village: BoolInt
    has_npc: BoolInt
    res_type: ResourceFieldDistribution
    is_habitable: BoolInt
    landscape: int  # TODO: Enum this?
    player_id: ScalarId
    player_name: str
    kingdom_id: ScalarId
    kingdom_tag: str
    population: int
    tribe: enums.PlayerTribe
    treasures: int


@dataclass
class Merchants(_Base):
    village_id: MapId
    max: int
    in_offers: int
    in_transport: int
    carry: int
    speed: int


@dataclass
class Notepad(_Base):
    id: ScalarId
    position_x: int
    position_y: int
    size_x: int
    size_y: int
    text: str


@dataclass
class ResourceBonuses(_NumberedDict):
    _ENUM = enums.Resource

    WOOD: int
    CLAY: int
    IRON: int
    CROP: int


@dataclass
class OasisTroopRanking(_Base):
    id: ScalarId
    oasis_id: MapId
    oasis_type: int  # TODO: Enum this
    player_id: ScalarId
    rank: int
    amount: int
    max_usable_troops: int
    used_by_village: MapId
    village_influence: int
    bonus: ResourceBonuses
    troop_production: int


@dataclass
class Stars(_Base):
    bronze: int
    silver: int
    gold: int


@dataclass
class Storage(_NumberedDict):
    _ENUM = enums.Resource

    WOOD: float
    CLAY: float
    IRON: float
    CROP: float


@dataclass
class Village(_Base):
    village_id: MapId
    player_id: ScalarId
    name: str
    tribe_id: enums.PlayerTribe
    belongs_to_king: ScalarId
    belongs_to_kingdom: ScalarId
    type: int  # TODO: Enum this
    population: int
    coordinates: MapId
    is_main_village: bool
    is_town: bool
    treasures_usable: int
    treasures: int
    allow_tribute_collection: BoolInt
    protection_granted: BoolInt
    tribute_collector_player_id: ScalarId
    real_tribute_percent: float
    supply_buildings: int  # TODO: What's this?
    supply_troops: int  # TODO: What's this?
    production: Resources
    storage: Storage
    treasury: dict  # TODO: What's this?
    storage_capacity: Storage
    used_control_points: int  # TODO: What's this?
    available_control_points: int  # TODO: What's this?
    culture_points: float
    celebration_type: enums.CelebrationType
    celebration_end: Timestamp
    culture_point_production: int
    treasure_resource_bonus: int
    acceptance: int  # TODO: What's this?
    acceptance_production: float
    tributes: Resources
    tributes_capacity: int
    tribute_treasures: int
    tribute_production: int
    tribute_production_detail: Resources
    tribute_time: Timestamp
    tributes_required_to_fetch: int
    estimated_warehouse_level: int


@dataclass
class Player(_Base):
    player_id: ScalarId
    name: str
    tribe_id: enums.PlayerTribe
    kingdom_id: ScalarId
    kingdom_tag: str
    kingdom_role: enums.PlayerKingdomRole
    is_king: bool
    king_id: ScalarId
    kingstatus: int  # TODO: Enum this
    villages: List[Village]
    population: int
    active: BoolInt
    prestige: int
    level: int
    stars: Stars
    next_level_prestige: int
    has_noob_protection: bool
    filter_information: bool
    signup_time: Timestamp
    vacation_state: enums.PlayerVacationState
    ui_limitations: int  # TODO: Enum this
    gold: int
    silver: int
    deletion_time: Timestamp
    coronation_duration: int
    brew_celebration: BoolInt
    ui_status: int  # TODO: What's this?
    hint_status: int  # TODO: What's this?
    spawned_on_map: Timestamp
    is_activated: BoolInt
    is_instant: BoolInt
    production_bonus_time: Timestamp
    crop_production_bonus_time: Timestamp
    premium_feature_auto_extend_flags: int  # TODO: How does this behave?
    plus_account_time: Timestamp
    limited_premium_feature_flags: int  # TODO: How does this behave?
    last_payment_time: Timestamp
    is_punished: bool
    limitation_flags: int  # TODO: Enum this
    limitation: int  # TODO: Enum this
    is_banned_from_messaging: bool
    banned_from_messaging: BoolInt  # TODO: Could be a Timestamp
    quest_version: enums.QuestVersion
    next_daily_quest_time: Timestamp
    daily_quests_exchanged: BoolInt  # TODO: Could be an int
    avatar_identifier: ScalarId
    vacation_state_start: Timestamp
    vacation_state_end: Timestamp
    used_vacation_days: int


@dataclass
class PlayerProfile(_Base):
    description: str


@dataclass
class PlayerProgressTrigger(_Base):
    id: str  # TODO: These look weird, could possible be an enum
    player_id: ScalarId
    type: enums.PlayerProgressTriggerType
    sub_type: int  # TODO: Enum these
    triggered: bool
    last_use: Timestamp
    data: dict  # TODO: What's this?


@dataclass
class Quest(_Base):
    id: int
    quest_giver: enums.QuestGiver
    status: enums.QuestStatus
    progress: int
    finished_steps: int
    final_step: int
    data: list  # TODO: What's this?
    rewards: dict  # TODO: Express this better


@dataclass
class QuestGiver(_Base):
    npc_id: enums.QuestGiver
    quest_id: int
    dialog: int  # TODO: What's this?
    quest_status: enums.QuestStatus


@dataclass
class UnitStats(_Base):
    attack: float
    defence: float
    defence_cavalry: float


@dataclass
class UnitResearchStats(UnitStats):
    level: int


@dataclass
class Unit(_Base):
    unit_type: Union[enums.RomanUnit, enums.TeutonUnit, enums.GaulUnit]  # TODO: We probably need a non union for these
    unit_level: int
    costs: Resources
    time: int
    can_research: bool
    can_upgrade: bool
    units_in_upgrade: int
    required: list  # TODO: What's this?
    max_level: int
    current_strength: UnitStats
    research_strength: List[UnitResearchStats]


@dataclass
class Research(_Base):
    research_queue_full: bool
    upgrade_queue_full: bool
    units: List[Unit]


@dataclass
class Session(_Base):
    session_id: str
    avatar_identifier: ScalarId
    user_account_identifier: ScalarId
    type: int  # TODO: Enum this
    rights: str  # TODO: Enum this


@dataclass
class Settings(_Base):
    player_id: ScalarId
    premium_confirmation: enums.SettingsPremiumConfirmation
    lang: enums.Language
    online_status_filter: enums.OnlineStatusFilter
    extended_simulator: bool
    music_volume: int
    sound_volume: int
    ui_sound_volume: int
    mute_all: bool
    time_type: enums.SettingsTimeType
    time_zone: float
    time_zone_string: str  # TODO: This is that weird time formatting
    time_zone_switcher: BoolInt
    time_format: enums.SettingsTimeFormat
    attacks_filter: FilterScalar
    map_filter: FilterScalar
    disable_tab_notifications: BoolInt
    enable_tab_notifications: bool
    disable_animations: bool
    notpads_visible: bool
    disable_help_notifications: bool
    enable_help_notifications: BoolInt
    enable_welcome_screen: BoolInt


@dataclass
class SocietyMember(_Base):
    player_id: ScalarId
    name: str
    is_founder: bool
    is_king: bool
    kingdom_id: ScalarId
    population: int
    villages: int


@dataclass
class SocietyProfile(_Base):
    group_id: ScalarId
    description: str


@dataclass
class Society(_Base):
    group_id: ScalarId
    name: str
    members: List[SocietyMember]
    society_id: ScalarId
    attitude: enums.SocietyAttitude
    target_type: Union[enums.BrightSocietyTarget, enums.DarkSocietyTarget]
    target_id: MapId
    shared_informations: int  # TODO: Enum these values and add a scalar filter like val
    profile: SocietyProfile


@dataclass
class TradeOffer(_Base):
    offer_id: ScalarId
    player_id: ScalarId
    player_name: str
    kingdom_id: ScalarId
    village_id: MapId
    blocked_merchants: int
    offered_resource: enums.Resource
    offered_amount: int
    searched_resource: enums.Resource
    searched_amount: int
    maximum_duration: int
    duration: int
    limit_kingdom: bool
    limit_duration: bool


@dataclass
class TroopsMovementInfo(_Base):
    troop_id: TroopId
    village_id_start: MapId
    village_id_target: MapId
    player_id_target: ScalarId
    coordinate_id: int  # TODO: What's this?
    time_start: Timestamp
    time_finish: Timestamp
    movement_type: enums.TroopMovementType
    resources: Resources
    treasures: int
    spy_target: enums.SpyMissionType  # TODO: Could be an int enum
    catapult_target1: enums.BuildingType  # TODO: Can you target every single BuildingType?
    catapult_target2: enums.BuildingType  # TODO: Can you target every single BuildingType?
    merchants: int
    recurrences: int
    recurrences_total: int


@dataclass
class Troops(_Base):
    troop_id: TroopId
    tribe_id: enums.PlayerTribe
    player_id: ScalarId
    player_name: str
    village_id: MapId
    village_name: str
    village_id_location: MapId
    village_name_location: str  # TODO: What's this?
    player_id_location: int  # TODO: What's this?
    player_name_location: str  # TODO: What's this?
    filter: str  # TODO: What's this?
    village_id_supply: int  # TODO: What's this?
    status: enums.TroopStatus
    units: Union[RomanUnits, TeutonUnits, GaulUnits]
    supply_troops: int  # TODO: What's this?
    capacity: int  # TODO: What'st his?
    movement: TroopsMovementInfo


@dataclass
class UnitQueueItem(_Base):
    unit_type: Union[enums.RomanUnit, enums.TeutonUnit, enums.GaulUnit]  # TODO: We probably need a non union for these
    count: int
    duration_per_unit: int
    time_finished_next: Timestamp
    time_finished_last: Timestamp
    pause: BoolInt


@dataclass
class UnitResearchQueueItem(_Base):
    unit_type: Union[enums.RomanUnit, enums.TeutonUnit, enums.GaulUnit]  # TODO: We probably need a non union for these
    research_level: int
    start_time: Timestamp
    finished: Timestamp
    pause: BoolInt


@dataclass
class UnitQueue(_Base):
    village_id: MapId
    building_types: dict  # TODO
    # building_types: {
    #     36: List[UnitQueueItem]
    # }


@dataclass
class UnitResearchQueue(_Base):
    village_id: MapId
    building_types: dict  # TODO
    # building_types: {
    #     22: List[UnitResearchQueueItem]
    # }
