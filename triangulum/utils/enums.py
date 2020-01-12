from enum import Enum

from triangulum.utils.util import unit_id_to_unit_nr


class FriendStatus(Enum):
    AVAILABLE = -1
    OFFLINE = 0
    ONLINE = 1
    AFK = 2


class ChatUserStatus(Enum):
    NOT_AVAILABLE = -1
    OFFLINE = 0
    ONLINE = 1
    AFK = 2


class ChatRoomUserStatus(Enum):
    NOT_AVAILABLE = -1
    OFFLINE = 0
    ONLINE = 1
    AFK = 2


class ChatRoomType(Enum):
    PRIVATE = 1
    GROUP = 3
    PUBLIC = 4
    KINGDOM = 5
    SECRET_SOCIETY = 7


class ChatNotification(Enum):
    PLAYER_JOINED = 1
    PLAYER_LEFT = 2
    PLAYER_ONLINE = 3
    PLAYER_OFFLINE = 4


class VillageType(Enum):
    NORMAL = 0
    MAIN = 1
    TOWN = 2
    MAIN_TOWN = 3
    WORLD_WONDER_VILLAGE = 4
    ROBBER_VILLAGE = 5
    GOVERNOR_NPC_VILLAGE = 6
    WORLD_WONDER_TOWN = 7
    KINGDOM_ROBBER = 8
    OASIS = 10


class ReportsCollection(Enum):
    OWN = 'own'
    KINGDOM = 'kingdom'
    NPC = 'npc'
    SOCIETY = 'society'


class VillageProductionType(Enum):
    BUILDING = 1
    OASIS = 2
    HERO = 3
    TREASURES = 5
    GOLD = 6
    OASIS_TROOPS = 7


class VillageOasisStatus(Enum):
    NO_OASIS = 0
    OCCUPIED = 1
    WILD = 3


class TroopStatus(Enum):
    HOME = 'home'
    TRANSIT = 'transit'
    SUPPORT = 'support'
    TRAP = 'trap'


class TroopMovementInfoCollection(Enum):
    ATTACK_VILLAGE = "attackVillage"


class TroopCollection(Enum):
    STATIONARY = 'stationary'
    MOVING = 'moving'
    TRAPPED = 'trapped'
    ELSEWHERE = 'elsewhere'
    ALL = 'all'


class TroopMovementType(Enum):
    ATTACK = 3
    RAID = 4
    SUPPORT = 5
    SPY = 6
    TRANSPORT = 7
    RETURN = 9
    SETTLE = 10
    TRIBUTE_COLLECT = 12
    ADVENTURE = 20
    RETURN_ADVENTURE = 27
    TRANSPORT_RETURN = 33
    REGENERATION = 36
    SIEGE = 47
    TREASURE_RESOURCES = 50


class TroopType(Enum):
    RAM = 7
    CATAPULT = 8
    LEADER = 9
    SETTLER = 10
    HERO = 11
    TRAPS = 79


class SocietyCondition(Enum):
    WHITE_SEND_RESOURCES = 1
    WHITE_LOST_UNITS = 2
    WHITE_PROVIDED_UNITS = 3
    BLACK_STOLE_RESOURCES = 4
    BLACK_DEFEAT_UNITS = 5
    BLACK_STOLE_TREASURE = 6


class Society(Enum):
    Cc = 1
    Dc = 2
    Pd = 3
    Qd = 4


class AchievementType(Enum):
    WON_A_GAMEWORLD = 62
    FINISHED_A_GAMEWORLD = 63


class AuctionStatus(Enum):
    RUNNING = 1
    FINISHED = 2
    CANCELED = 3


class BuildingType(Enum):
    WOOD = 1  # BuildingCategory.RESOURCES
    CLAY = 2  # BuildingCategory.RESOURCES
    IRON = 3  # BuildingCategory.RESOURCES
    CROP = 4  # BuildingCategory.RESOURCES
    SAWMILL = 5  # BuildingCategory.RESOURCES
    CLAY_BAKERY = 6  # BuildingCategory.RESOURCES
    IRON_FOUNDRY = 7  # BuildingCategory.RESOURCES
    MILL = 8  # BuildingCategory.RESOURCES
    BAKERY = 9  # BuildingCategory.RESOURCES
    WAREHOUSE = 10  # BuildingCategory.INFRASTRUCTURE
    GRANARY = 11  # BuildingCategory.INFRASTRUCTURE
    BLACKSMITH = 13  # BuildingCategory.MILITARY
    TOURNAMENT_SQUARE = 14  # BuildingCategory.INFRASTRUCTURE
    MAIN_BUILDING = 15  # BuildingCategory.INFRASTRUCTURE
    RALLY_POINT = 16  # BuildingCategory.MILITARY
    MARKET = 17  # BuildingCategory.INFRASTRUCTURE
    EMBASSY = 18  # BuildingCategory.INFRASTRUCTURE
    BARRACKS = 19  # BuildingCategory.MILITARY
    STABLE = 20  # BuildingCategory.MILITARY
    WORKSHOP = 21  # BuildingCategory.MILITARY
    ACADEMY = 22  # BuildingCategory.MILITARY
    CRANNY = 23  # BuildingCategory.INFRASTRUCTURE
    TOWN_HALL = 24  # BuildingCategory.INFRASTRUCTURE
    RESIDENCE = 25  # BuildingCategory.INFRASTRUCTURE
    PALACE = 26  # BuildingCategory.INFRASTRUCTURE
    TREASURY = 27  # BuildingCategory.INFRASTRUCTURE
    TRADE_OFFICE = 28  # BuildingCategory.INFRASTRUCTURE
    GREAT_BARRACKS = 29  # BuildingCategory.MILITARY
    GREAT_STABLE = 30  # BuildingCategory.MILITARY
    CITY_WALL = 31  # roman wall BuildingCategory.MILITARY
    NATAR_CITY_WALL = 43  # natar wall BuildingCategory.MILITARY
    EARTH_WALL = 32  # teuton wall BuildingCategory.MILITARY
    PALLISADE = 33  # gaul wall BuildingCategory.MILITARY
    STONEMASON = 34  # BuildingCategory.INFRASTRUCTURE
    BREWERY = 35  # BuildingCategory.INFRASTRUCTURE
    TRAPPER = 36  # BuildingCategory.MILITARY
    GREAT_WAREHOUSE = 38  # BuildingCategory.INFRASTRUCTURE
    GREAT_GRANARY = 39  # BuildingCategory.INFRASTRUCTURE
    WONDER_OF_WORLD = 40  # BuildingCategory.INFRASTRUCTURE
    HORSE_DRINKING_TROUGH = 41  # BuildingCategory.INFRASTRUCTURE
    MOAT = 42  # BuildingCategory.INFRASTRUCTURE
    TEAHOUSE = 44  # BuildingCategory.INFRASTRUCTURE
    HIDDEN_TREASURY = 45  # BuildingCategory.INFRASTRUCTURE


class BuildingCategory(Enum):
    INFRASTRUCTURE = 1
    MILITARY = 2
    RESOURCES = 3


class BuildingUpgrade(Enum):
    POSSIBLE = 'possible'  # free slot in building queue and enough resources
    NOT_NOW = 'notNow'  # building queue full or not enough resources
    MAX_LEVEL = 'maxLevel'  # fully upgraded
    NOT_AT_ALL = 'notAtAll'  # not enough free supply
    DEMOLISH = 'demolish'  # currently demolished


class BuildingQueueType(Enum):
    VILLAGE = 1
    RESOURCES = 2
    MASTER_BUILDER = 4
    DESTRUCTION = 5
    SMITHY = 13  # This shouldn't be here but T5 put Smithy Troop Improvements in premium feature finish_now queue_type as BuildingType


class ExchangeOfficeType(Enum):
    SILVER = 'silver'
    GOLD = 'gold'


class FarmListAction(Enum):
    ADD = 1
    COPY = 2
    TOGGLE = 3


class FieldMarkerGlobalType(Enum):
    GOVERNOR_RELOCATE = 'FieldMarker.GovernorRelocate'


class FieldMarkerPersonalMinimized(Enum):
    DEFAULT = 0
    MINIMIZED = 1
    MAXIMIZED = 2


class FieldMessageType(Enum):
    KINGDOM = 2
    SOCIETY = 4
    ME = 5
    PLAYER = 5  # PLAYER and ME are treated the same


class GameworldStatus(Enum):
    OPEN = 0
    CLOSED = 1
    ENDED = 2
    SETUP = 3


class GroupInvitationType(Enum):
    SECRET_SOCIETY = 2
    KINGDOM = 3


class HeroStatus(Enum):
    IDLE = 0
    RETURNING = 1
    TO_VILLAGE = 2
    TO_OASIS = 3
    TO_ADVENTURE = 4
    SUPPORTING = 5
    TRAPPED = 6
    DEAD = 7
    REVIVING = 8


class HeroItemSlot(Enum):
    NONE = -2
    INSTANT_USE = -1
    INVENTORY = 0
    HELMET = 1
    RIGHT_HAND = 2
    LEFT_HAND = 3
    BODY = 4
    SHOES = 5
    HORSE = 6
    BAG = 7


class HeroItemBonus(Enum):
    XP = 1
    BARRACKS = 2
    STABLE = 3
    WORKSHOP = 4
    SPEED_RETURN = 5
    SPEED_OWN_VILLAGES = 6
    SPEED_KINGDOM_VILLAGES = 7
    SPEED_STAMINA = 8
    RAID = 9
    NATARS = 10
    UNIT_ID = 11
    UNIT_STRENGTH = 12
    FIGHT_STRENGTH = 13
    HEALTH_REGEN = 14
    CULTURE_POINTS = 15
    ARMOR = 16
    SPEED_HERO = 17
    SPEED_HORSE = 18
    RESKILL = 20
    TROOP_HEALING = 21
    EYESIGHT = 22
    CHICKEN = 23
    RESOURCES = 24
    CROP = 25
    POTION = 26


class HeroItemType(Enum):
    NONE = 0

    # Helmet of Health
    HELMET_OF_REGENERATION = 3
    HELMET_OF_HEALTH = 5
    HELMET_OF_HEALING = 6

    # Helmet of Culture
    HELMET_OF_THE_GLADIATOR = 7
    HELMET_OF_THE_TRIBUNE = 8
    HELMET_OF_THE_CONSUL = 9

    # Helmet of Cavalry
    HELMET_OF_THE_HORSEMAN = 10
    HELMET_OF_THE_CAVALRY = 11
    HELMET_OF_THE_HEAVY_CAVALRY = 12

    # Helmet of Infantry
    HELMET_OF_THE_MERCENARY = 13
    HELMET_OF_THE_WARRIOR = 14
    HELMET_OF_THE_ARCHON = 15

    # Swords of the Legionnaire
    SHORT_SWORD_OF_THE_LEGIONNAIRE = 16
    SWORD_OF_THE_LEGIONNAIRE = 17
    LONG_SWORD_OF_THE_LEGIONNAIRE = 18

    # Swords of the Praetorian
    SHORT_SWORD_OF_THE_PRAETORIAN = 19
    SWORD_OF_THE_PRAETORIAN = 20
    LONG_SWORD_OF_THE_PRAETORIAN = 21

    # Swords of the Imperian
    SHORT_SWORD_OF_THE_IMPERIAN = 22
    SWORD_OF_THE_IMPERIAN = 23
    LONG_SWORD_OF_THE_IMPERIAN = 24

    # Sword of the Imperatoris
    SHORT_SWORD_OF_THE_IMPERATORIS = 25
    SWORD_OF_THE_IMPERATORIS = 26
    LONG_SWORD_OF_THE_IMPERATORIS = 27

    # Lance of the Caesaris
    LIGHT_LANCE_OF_THE_CAESARIS = 28
    LANCE_OF_THE_CAESARIS = 29
    HEAVY_LANCE_OF_THE_CAESARIS = 30

    # Spear of the Phalanx
    SPEAR_OF_THE_PHALANX = 31
    PIKE_OF_THE_PHALANX = 32
    LANCE_OF_THE_PHALANX = 33

    # Sword of the Swordsman
    SHORT_SWORD_OF_THE_SWORDSMAN = 34
    SWORD_OF_THE_SWORDSMAN = 35
    LONG_SWORD_OF_THE_SWORDSMAN = 36

    # Bow of the Theutates
    SHORT_BOW_OF_THE_THEUTATES = 37
    BOW_OF_THE_THEUTATES = 38
    LONG_BOW_OF_THE_THEUTATES = 39

    # Staff of the Druidrider
    WALKING_STAFF_OF_THE_DRUIDRIDER = 40
    STAFF_OF_THE_DRUIDRIDER = 41
    FIGHTING_STAFF_OF_THE_DRUIDRIDER = 42

    # Lance of the Haeduan
    LIGHT_LANCE_OF_THE_HAEDUAN = 43
    LANCE_OF_THE_HAEDUAN = 44
    HEAVY_LANCE_OF_THE_HAEDUAN = 45

    # Club of the Barbarian
    CLUB_OF_THE_CLUBSWINGER = 46
    MACE_OF_THE_CLUBSWINGER = 47
    MORNING_STAR_OF_THE_CLUBSWINGER = 48

    # Spear of the Spearfighter
    SPEAR_OF_THE_SPEARFIGHTER = 49
    SPIKE_OF_THE_SPEARFIGHTER = 50
    LANCE_OF_THE_SPEARFIGHTER = 51

    # Axe of the Axeman
    HATCHET_OF_THE_AXEMAN = 52
    AXE_OF_THE_AXEMAN = 53
    BATTLE_AXE_OF_THE_AXEMAN = 54

    # Hammer of the Paladin
    LIGHT_HAMMER_OF_THE_PALADIN = 55
    HAMMER_OF_THE_PALADIN = 56
    HEAVY_HAMMER_OF_THE_PALADIN = 57

    # Sword of the Teutonic Knight
    SHORT_SWORD_OF_THE_TEUTON_KNIGHT = 58
    SWORD_OF_THE_TEUTON_KNIGHT = 59
    LONG_SWORD_OF_THE_TEUTON_KNIGHT = 60

    # Map
    SMALL_MAP = 61
    MAP = 62
    LARGE_MAP = 63

    # Pennant
    SMALL_PENNANT = 64
    PENNANT = 65
    GREAT_PENNANT = 66

    # Large Standard
    SMALL_STANDARD = 67
    STANDARD = 68
    GREAT_STANDARD = 69

    # Spy Glass
    SMALL_SPY_GLASS = 70
    SPY_GLASS = 71
    GREAT_SPY_GLASS = 72

    # Pouch
    POUCH_OF_THE_THIEF = 73
    BAG_OF_THE_THIEF = 74
    SACK_OF_THE_THIEF = 75

    # Shield
    SMALL_SHIELD = 76
    SHIELD = 77
    LARGE_SHIELD = 78

    # Horn
    SMALL_HORN_OF_THE_NATARIAN = 79
    HORN_OF_THE_NATARIAN = 80
    HUGE_HORN_OF_THE_NATARIAN = 81

    # Armors of Health
    ARMOR_OF_REGENERATION = 82
    ARMOR_OF_HEALTH = 83
    ARMOR_OF_HEALING = 84

    # Scale Armors
    LIGHT_SCALE_ARMOR = 85
    SCALE_ARMOR = 86
    HEAVY_SCALE_ARMOR = 87

    # Breast-Plate Armors
    LIGHT_BREAST_PLATE_ARMOR = 88
    BREAST_PLACE_ARMOR = 89
    HEAVY_BREAST_PLATE_ARMOR = 90

    # Chainmail Armors
    LIGHT_CHAINMAIL = 91
    CHAINMAIL = 92
    HEAVY_CHAINMAIL = 93

    # Shoes of Awareness
    BOOTS_OF_KNOWLEDGE = 94
    BOOTS_OF_ENLIGHTEMENT = 95
    BOOTS_OF_WISDOM = 96

    # Shoes of Endurance
    BOOTS_OF_THE_MERCENARY = 97
    BOOTS_OF_THE_WARRIOR = 98
    BOOTS_OF_THE_ARCHON = 99

    # Spurs
    SMALL_SPURS = 100
    SPURS = 101
    NASTY_SPURS = 102

    # Black Horse
    BLACK_GELDING = 103
    BLACK_THOROUGHBRED = 104
    BLACK_WARHORSE = 105

    # White Horse
    WHITE_GELDING = 106
    WHITE_THOROUGHBRED = 107
    WHITE_WARHORSE = 108

    # Brown Horse
    BROWN_GELDING = 109
    BROWN_THOROUGHBRED = 110
    BROWN_WARHORSE = 111

    OINTMENT = 112
    SCROLLS = 113
    WATERBUCKET = 114
    BOOK = 115
    ARTWORK = 116
    BANDAGE_25 = 117
    BANDAGE_33 = 118
    CAGES = 119
    TREASURES = 120

    # Boots of the Chicken
    # All of these are named the same
    BOOTS_OF_THE_CHICKEN_TIER_1 = 121
    BOOTS_OF_THE_CHICKEN_TIER_2 = 122
    BOOTS_OF_THE_CHICKEN_TIER_3 = 123

    HEALING_POTION = 124
    ARMOR_UPGRADE = 125
    WEAPON_UPGRADE = 126
    LEFT_HAND_UPGRADE = 127
    HELMET_UPGRADE = 128
    SHOE_UPGRADE = 129
    RESOURCE_BONUS_3 = 130
    RESOURCE_BONUS_4 = 131
    RESOURCE_BONUS_5 = 132
    CROP_BONUS_3 = 133
    CROP_BONUS_4 = 134
    CROP_BONUS_5 = 135
    ADVENTURE_POINT = 136
    BUILDING_GROUND = 137
    FINISH_IMMEDIATELY = 138
    NPC_TRADER = 139
    INSTANT_TRADE_DELIVERY = 140
    BANDAGE_25_UPGRADED = 141
    BANDAGE_33_UPGRADED = 142
    PILE_WOOD_SMALL = 143
    PILE_WOOD_MEDIUM = 144
    PILE_WOOD_LARGE = 145
    PILE_CLAY_SMALL = 146
    PILE_CLAY_MEDIUM = 147
    PILE_CLAY_LARGE = 148
    PILE_IRON_SMALL = 149
    PILE_IRON_MEDIUM = 150
    PILE_IRON_LARGE = 151
    PILE_CROP_SMALL = 152
    PILE_CROP_MEDIUM = 153
    PILE_CROP_LARGE = 154


class KingdomType(Enum):
    NORMAL = 0
    UNITED = 1


class KingdomState(Enum):
    NAP = 0  # Non attack pact
    BND = 1  # Allied
    WAR = 2  # War


class KingdomFightValuesType(Enum):
    OFF_STRENGTH = 1
    DEF_STRENGTH = 2
    OFF_POINTS = 3
    DEF_POINTS = 4


class MarkerOwner(Enum):
    PLAYER = 1
    KINGDOM = 2


class MarkerType(Enum):
    PLAYER = 1
    KINGDOM = 2
    COORDINATES = 3
    TROOP_MOVEMENT = 4
    KING_VILLAGE = 5


class MarkerEditType(Enum):
    EDIT = 1
    DELETE = 2
    CREATE = 3


class MarkerColor(Enum):
    BLUE = 1
    YELLOW = 2
    BROWN = 3
    OWN = 4
    TEAL = 5
    DARK_GREEN = 6
    LIGHT_GREEN = 7
    DARK_BLUE = 8
    ALLIANCE = 9
    PURPLE = 10
    PINK = 11
    RED = 12
    ENEMY = 13
    NEUTRAL = 15
    NAP = 16
    BND = 17


class MedalType(Enum):
    CLIMBER = 1
    ATTACKER = 2
    DEFENDER = 3
    ROBBER = 4


class MedalTypeString(Enum):
    CLIMBER = 'climber'
    ATTACKER = 'attacker'
    DEFENDER = 'defender'
    ROBBER = 'robber'


class NotificationPromptType(Enum):
    FLASH = 'flashNotification'
    NORMAL = ''
    TIMED = 'timed'
    CHAT = 'chatNotification'
    IN_GAME_HELP = 'inGameHelp'


class NotificationType(Enum):
    REPORT_ATTACKER_WON_WITHOUT_LOSSES = 1
    REPORT_ATTACKER_WON_WITH_LOSSES = 2
    REPORT_ATTACKER_LOST = 3
    REPORT_DEFENDER_WON_WITHOUT_LOSSES = 4
    REPORT_DEFENDER_WON_WITH_LOSSES = 5
    REPORT_DEFENDER_LOST_WITH_LOSSES = 6
    REPORT_DEFENDER_LOST_WITHOUT_LOSSES = 7
    REPORT_SUPPORT_ARRIVED = 8
    REPORT_TRADE = 10
    REPORT_TRADE_WOOD = 11
    REPORT_TRADE_CLAY = 12
    REPORT_TRADE_IRON = 13
    REPORT_TRADE_CROP = 14
    REPORT_SPY_SUCCESS_UNDETECTED = 15
    REPORT_SPY_SUCCESS_DETECTED = 16
    REPORT_SPY_FAILURE = 17
    REPORT_SPY_DEFENDED = 18
    REPORT_SPY_NOT_DEFENDED = 19
    REPORT_CAPTURED_ANIMALS = 20
    REPORT_ADVENTURE = 21
    REPORT_WORLD_PEACE = 22
    REPORT_PRESTIGE = 23
    TRIBUTE_COLLECTED = 31
    TROOPS_SEND = 32
    CONSTRUCTION_STARTED = 33
    TRADER_STARTED = 34
    TROOPS_RETURNED = 36
    TROOPS_RELEASED = 37
    TROOPS_DISBANDED = 38
    BUILDING_FINISHED = 39
    BUILDING_COMPLETELY_DESTROYED = 41
    UNIT_RESEARCH_COMPLETED = 42
    NEW_VILLAGE_SETTLED = 43
    ATTACK_VILLAGE_STARTED = 44
    AUCTION_OVERBID = 46
    AUCTION_WON = 47
    FRIEND_REQUEST_RECEIVED = 48
    SOCIETY_INVITATION_RECEIVED = 49
    TRADER_SENT = 50
    CELEBRATION_STARTED = 51
    CELEBRATION_ENDED = 52
    TROOPS_RECRUITING_STARTED = 53
    UNIT_RESEARCH_STARTED = 54
    TROOPS_SUPPORT_SEND_HOME = 55
    TROOPS_INCOMING_FOREIGN_SUPPORT = 57
    PLAYER_IS_ATTACKED = 58
    REPORT_SHARED_OWN = 60
    REPORT_SHARED_KINGDOM = 61
    REPORT_SHARED_SOCIETIES = 63
    REPORT_SHARED = 64  # T5 Source Comment: we may decide in the future to display a single unified icon for all shared reports
    KINGDOM_CHANGED = 66
    REQUEST_SENT = 67
    KING_REQUEST_RECEIVED = 68
    TROOPS_RELEASED_OTHER_TROOPS = 69
    TIMER_CORONATION = 72
    TIMER_NOOB_PROTECTION = 73
    TIMER_DELETION = 74
    TIMER_STARVATION_DEACTIVATED = 75
    TIMER_WORLD_PEACE = 76
    TIMER_GOLD_PROMOTION = 78
    TIMER_PLUS_RUNS_OUT = 79
    TIMER_RES_BONUS_RUNS_OUT = 80
    TIMER_CROP_BONUS_RUNS_OUT = 81
    SYSTEM_MESSAGE = 82
    AUTO_EXTEND_RES_PRODUCTION_BONUS_NOT_ENOUGH_GOLD = 86
    AUTO_EXTEND_CROP_PRODUCTION_BONUS_NOT_ENOUGH_GOLD = 87
    AUTO_EXTEND_PLUS_NOT_ENOUGH_GOLD = 88
    RES_BONUS_ENDS = 89
    CROP_BONUS_ENDS = 90
    PLUS_BONUS_ENDS = 91
    KINGDOM_OASIS_LOST = 92
    KINGDOM_OASIS_WON = 93
    OASIS_BONUS_CHANGED = 94
    TIMER_NATAR_SPIES_ATTACK = 95
    HELP_CENTER_MESSAGE_RECEIVED = 97
    TIMER_WORLD_PEACE_TO_BE_ACTIVATED = 98
    TIMER_WORLD_PEACE_DISABLE_ONLY_STARVATION = 99
    ENOUGH_CULTURE_POINTS_FOR_VILLAGE = 100
    ENOUGH_CULTURE_POINTS_FOR_VILLAGE_SOON = 101
    NEW_ROBBER_CAMPS = 102
    GLOBAL_WORLD_ENDED = 104
    DUKE_REQUEST_RECEIVED = 105
    DUKE_REQUEST_DECLINED = 106
    DUKE_REQUEST_ACCEPTED = 107
    DUKE_ABDICATED = 108
    DUKE_DISMISSED = 109
    ACTIVATION_NEEDED = 110  # T5 Source Comment: Pseudo Notification, no event
    ADDED_CARDGAME_FREE_ROLL = 111
    COOP_PACKAGE_GRANTED = 112
    INVITATION_EMAIL_SENT = 113
    REFERRAL_REWARD_CAN_COLLECT = 114
    REPORT_FARMLIST_RAID = 115
    ACHIEVEMENT = 116
    REPORT_FARMLIST_COMPLETED_WITHOUT_LOSSES = 118
    REPORT_FARMLIST_COMPLETED_WITH_LOSSES = 119
    REPORT_FARMLIST_COMPLETED_WITH_FULL_LOSSES = 120
    USED_ITEM_ARTWORK = 121
    CELEBRATION_STARTED_POINTS_GAINED = 122
    CELEBRATION_STARTED_IN_QUEUE = 123
    REPORT_FARMLIST_SINGLE_COMPLETED_WITHOUT_LOSSES = 124
    REPORT_FARMLIST_SINGLE_COMPLETED_WITH_LOSSES = 125
    REPORT_FARMLIST_SINGLE_COMPLETED_WITH_FULL_LOSSES = 126
    FARMLIST_ADDED_VILLAGE = 127
    FARMLIST_REMOVED_VILLAGE = 128
    KINGDOM_CHANGED_KING = 129
    CAN_INVITE_NEUTRAL_GOVERNOR = 130
    TIMER_VACATION_ACTIVATION = 131
    TIMER_VACATION_MODE = 132
    TIMER_VACATION_BOOST = 133
    PEACE_OFFER = 134
    UNITED_KINGDOM_VICEKING_RESIGNS = 135
    UNITED_KINGDOM_DISSOLVES = 136
    UNION_REQUEST_RECEIVED = 137
    KINGDOM_UNION_AVAILABLE_SOON = 138
    KINGDOM_UNION_AVAILABLE = 139
    KINGDOM_UNIFIED = 140
    REPORT_RELOCATION = 141


class ReportFilter(Enum):
    ATTACKER_WON_WITHOUT_LOSSES = 1
    ATTACKER_WON_WITH_LOSSES = 2
    ATTACKER_LOST = 3
    DEFENDER_WON_WITHOUT_LOSSES = 4
    DEFENDER_WON_WITH_LOSSES = 5
    DEFENDER_LOST_WITH_LOSSES = 6
    DEFENDER_LOST_WITHOUT_LOSSES = 7
    SUPPORT_ARRIVED = 8
    TRADE = 10
    TRADE_WOOD = 11
    TRADE_CLAY = 12
    TRADE_IRON = 13
    TRADE_CROP = 14
    SPY_SUCCESS_UNDETECTED = 15
    SPY_SUCCESS_DETECTED = 16
    SPY_FAILURE = 17
    SPY_DEFENDED = 18
    SPY_NOT_DEFENDED = 19
    CAPTURED_ANIMALS = 20
    ADVENTURE = 21
    WORLD_PEACE = 22
    PRESTIGE = 23
    SHARED_OWN = 60
    SHARED_KINGDOM = 61
    SHARED_SOCIETIES = 63
    SHARED = 64  # T5 Source Comment: we may decide in the future to display a single unified icon for all shared reports
    FARMLIST_RAID = 115
    FARMLIST_COMPLETED_WITHOUT_LOSSES = 118
    FARMLIST_COMPLETED_WITH_LOSSES = 119
    FARMLIST_COMPLETED_WITH_FULL_LOSSES = 120
    FARMLIST_SINGLE_COMPLETED_WITHOUT_LOSSES = 124
    FARMLIST_SINGLE_COMPLETED_WITH_LOSSES = 125
    FARMLIST_SINGLE_COMPLETED_WITH_FULL_LOSSES = 126
    RELOCATION = 141


class NotificationTypeString(Enum):
    REPORT_ATTACKER_WON_WITHOUT_LOSSES = 'attackerWonWithoutLosses'
    REPORT_ATTACKER_WON_WITH_LOSSES = 'attackerWonWithLosses'
    REPORT_ATTACKER_LOST = 'attackerLost'
    REPORT_DEFENDER_WON_WITHOUT_LOSSES = 'defenderWonWithoutLosses'
    REPORT_DEFENDER_WON_WITH_LOSSES = 'defenderWonWithLosses'
    REPORT_DEFENDER_LOST_WITH_LOSSES = 'defenderLostWithLosses'
    REPORT_DEFENDER_LOST_WITHOUT_LOSSES = 'defenderLostWithoutLosses'
    REPORT_SPY_SUCCESS_UNDETECTED = 'spyAttackerWonWithoutLosses'
    REPORT_SPY_SUCCESS_DETECTED = 'spyAttackerWonWithLosses'
    REPORT_SPY_FAILURE = 'spyAttackerLost'
    REPORT_SPY_DEFENDED = 'spyDefenderWon'
    REPORT_SPY_NOT_DEFENDED = 'spyDefenderLost'
    REPORT_ADVENTURE_WON = 'adventureWon'
    REPORT_ADVENTURE_LOST = 'adventureLost'
    REPORT_CAPTURED_ANIMALS = 'capturedAnimals'
    REPORT_SUPPORT_ARRIVED = 'support'
    REPORT_TRADE = 'trade'
    REPORT_TRADE_WOOD = 'trade'
    REPORT_TRADE_CLAY = 'trade'
    REPORT_TRADE_IRON = 'trade'
    REPORT_TRADE_CROP = 'trade'


class PlayerID(Enum):
    NATAR = 1
    NATURE = 0
    ROBBER = -1
    GOVERNOR_NPC = -2


class PlayerTribe(Enum):
    NONE = 0
    ROMAN = 1
    TEUTON = 2
    GAUL = 3
    NATURE = 4
    NATAR = 5


class PlayerTribeName(Enum):
    ROMAN = 'roman'
    TEUTON = 'teuton'
    GAUL = 'gaul'
    NATURE = 'nature'
    NATAR = 'natar'


class PlayerAction(Enum):
    DELETE_ACCOUNT = 1


class PlayerCoronationStatus(Enum):
    CROWNED = 1
    IN_CEREMONY = 2
    NONE = 3


class PlayerKingdomRole(Enum):
    GOVERNOR = 0
    KING = 1
    DUKE = 2
    VICEKING = 3


class PlayerKingdomRoleString(Enum):
    GOVERNOR = 'governor'
    KING = 'king'
    DUKE = 'duke'
    VICEKING = 'viceking'


class PlayerCollection(Enum):
    KINGDOM = 'kingdom'


class PlayerVacationState(Enum):
    INACTIVE = 0
    ACTIVATING = 1
    ACTIVE = 2
    BOOST = 3


class PlayerProgressTriggerType(Enum):
    OPEN_PREMIUM_MENU = 1
    ROBBER_GOODS = 2
    ADVENTURE = 3
    ANNEX_OASIS = 4
    INVITE_A_FRIEND = 5
    IN_GAME_HELP = 6


class PlayerProgressTriggerTopic(Enum):
    VILLAGE = 'Village'
    ROBBERS = 'Robbers'
    KINGDOM = 'Kingdom'
    HERO = 'Hero'
    ITEMS = 'Items'
    OASES = 'Oases'
    TRADING = 'Trading'
    MILITARY_DIPLOMACY = 'MilitaryAndDiplomacy'
    PREMIUM = 'Premium'


class PlayerProgressTriggerHelpPage(Enum):
    ROBBER_HIDEOUTS = 'RobberHideouts'  # Tutorial done & detail view or "send troops" view for a Robber Hideout is opened
    DUKES = 'Dukes'   # "Kingdom" tab of "Societies" window is opened
    MAP_DETAIL_VIEW = 'MapAndDetailView'  # Tutorial done & map view opened
    ADVENTURES = 'Adventures'  # Adventure menu opened
    HERO_PRODUCTION = 'HeroProduction'  # Hero attribute menu opened
    AUCTIONS = 'Auctions'  # Auction menu visited
    ASSIGN_OASIS = 'AssignOasis'  # Embassy built & opened "Oases" tab in Embassy window
    TROOPS_IN_OASIS = 'TroopsInOases'  # "Assign Oasis" quest was solved & opened non-wild oasis detail view
    WILD_OASES = 'WildOases'  # Detail view of wild Oasis opened
    TRADING_RESOURCES = 'TradingResources'  # "Buy" tab of marketplace opened
    OFFERING_RESOURCES = 'OfferingResources'  # "Sell" tab of marketplace opened
    CARD_GAME = 'CardGame'  # Card game screen opened
    RUNTIME_FEATURES = 'RuntimeFeatures'  # Premium menu opened
    MASTER_BUILDER = 'MasterBuilder'  # Building queue full
    TRADE_ROUTES = 'TradeRoutes'  # 3 or more villages owned & marketplace opened & Plus Account active
    ATTACK_TYPES = 'AttackTypes'  # Beginner protection ended & "Send troops" screen opened
    STRATEGIC_MAP = 'StrategicMap'  # Entered strategic (maximally zoomed out) map view
    FARM_LISTS = 'FarmLists'  # Sum of outgoing attacks and raids is at least 3 at the same time OR opened farm list tab
    VICTORY_POINTS = 'VictoryPoints'  # Second duke slot was unlocked in the kingdom
    INVITE_FRIEND = 'InviteAFriend'  # "Invite a Friend" tab opened
    SUPPORTING = 'SupportOtherPlayers'  # Beginner protection ended & player in kingdom is under attack & opened map view


class PlayerProgressTriggerCheck(Enum):
    ASSIGN_OASIS_QUEST_SOLVED = 1
    THREE_VILLAGES_OWNED = 2


class PlayerPunishmentType(Enum):
    AUTO_BAN = 'playerBanned'
    SUSPENDED = 'playerSuspended'
    LOCKED = 'playerLocked'
    ISOLATED = 'playerIsolated'


class PlayerPunishmentStrikeReason(Enum):
    GENERAL = 1
    MULTI_ACCOUNT = 2
    PASSWORD_SHARING = 3
    BUG_ABUSE = 4
    BOT_OR_SCRIPT_USING = 5
    SILVER_FRAUD = 6
    PAYMENT = 7
    HARASSMENT_INSULT = 8
    ACP_DELETION = 9
    ACP_PAYMENT = 10
    SPAM = 11
    ADVERTISING = 12


class PlayerPunishmentAction(Enum):
    ISOLATED = 1
    LOCK = 2


class PremiumFeatureName(Enum):
    FINISH_NOW = 'finishNow'
    EXCHANGE_OFFICE = 'exchangeOffice'
    PRODUCTION_BONUS = 'productionBonus'
    CROP_PRODUCTION_BONUS = 'cropProductionBonus'
    PLUS_ACCOUNT = 'plusAccount'
    NPC_TRADER = 'NPCTrader'
    FETCH_TRIBUTE_INSTANTLY = 'tributeFetchInstantly'
    FETCH_ALL_TRIBUTE_INSTANTLY = 'tributeFetchAllInstantly'
    TREASURE_RESOURCES_INSTANT = 'treasureResourcesInstant'
    STARTER_PACKAGE = 'starterPackage'
    BOOK_BUILD_MASTER_SLOT = 'buildingMasterSlot'
    TRADER_SLOT = 'traderSlot'
    TRADER_ARRIVE_INSTANTLY = 'traderArriveInstantly'
    CARDGAME_SINGLE = 'cardgameSingle'
    CARDGAME_4OF5 = 'cardgame4of5'


class PremiumFeatureAutoExtendFlag(Enum):
    RES_BONUS = 0
    CROP_BONUS = 1
    PLUS_BONUS = 2


# Limited Premium Features
class PremiumFeatureLimitedFlag(Enum):
    STARTER_PACKAGE = 0
    FIRST_BUILD_MASTER_SLOT = 1
    SECOND_BUILD_MASTER_SLOT = 2
    THIRD_BUILD_MASTER_SLOT = 3
    TRADER_SLOT_FIRST = 4
    TRADER_SLOT_SECOND = 5


class PremiumFeatureStarterPackageVersion(Enum):
    VERSION_1 = 1
    VERSION_2 = 2


class PrestigeCondition(Enum):
    LEVELUP_HERO = 1
    COMPLETE_ADVENTURE = 2
    COMPLETE_DAILY_QUEST = 3
    COMPLETE_RESEARCH = 4
    POPULATION_GROW = 5
    WRITE_MESSAGE = 6
    ACQUIRE_VILLAGE = 7
    TREASURES = 8
    IMPROVE_RANK_POPULATION = 9
    IMPROVE_RANK_ATTACKER = 10
    IMPROVE_RANK_DEFENDER = 11
    IMPROVE_RANK_VILLAGES = 12
    IMPROVE_RANK_HEROES = 13
    HOLD_TOP_RANKING = 14
    ATTACK_DEFEND_PLAYER = 15


class QuestStatus(Enum):
    INACTIVE = 1
    ACTIVATABLE = 2
    ACTIVE = 3
    DONE = 4
    FINISHED = 5


class QuestGiver(Enum):
    DAILY = -1
    MYSELF = 0
    WREN = 1
    FARMER = 2
    SCOUT = 3
    WOODCUTTER = 4
    CLAY_MAN = 5
    MINER = 6
    TRADER = 7
    ROBBER = 8
    CHIEF = 9
    ENVOY = 10
    ADVENTURER = 11
    GENERAL = 12


class QuestGiverString(Enum):
    DAILY = 'daily'
    MYSELF = 'myself'
    WREN = 'wren'
    FARMER = 'farmer'
    SCOUT = 'scout'
    WOODCUTTER = 'woodcutter'
    CLAY_MAN = 'clayMan'
    MINER = 'miner'
    TRADER = 'trader'
    ROBBER = 'robber'
    CHIEF = 'chief'
    ENVOY = 'envoy'
    ADVENTURER = 'adventurer'
    GENERAL = 'general'


class ReportCollection(Enum):
    PERSONAL = 'own'
    KING = 'king'
    KING_MINIONS = 'king_minions'
    SOCIETY = 'society'
    FAVORITE = 'favorite'
    SEARCH = 'search'
    PRESTIGE = 'prestige'


class ReportDisplayType(Enum):
    SUPPORT = 1
    TRADE = 2
    ADVENTURE = 3
    FIGHT = 4
    SPY = 5
    VISIT = 6
    SUPPORT_ATTACKED = 7
    TROOP_RELEASE = 8
    ANIMALS_CAPTURE = 9
    PRESTIGE = 10
    FARMLIST_RAID = 11
    FARMLIST_RAID_COMPLETE = 12
    RELOCATION = 13


class ReportAdventureLootType(Enum):
    NOTHING = 0
    RESOURCES = 3
    SILVER = 4
    TROOPS = 5


class Resource(Enum):
    WOOD = 1
    CLAY = 2
    IRON = 3
    CROP = 4


class ResourceString(Enum):
    RESOURCES_ALL = 'resourcesAll'
    WOOD = 'wood'
    CLAY = 'clay'
    IRON = 'iron'
    CROP = 'crop'


class SessionType(Enum):
    PLAYER = 0
    DUAL = 1
    SITTER = 2
    ADMIN = 3


class SessionRight(Enum):
    SEND_RAIDS = 1
    SEND_SUPPORT = 1
    SEND_MERCHANTS = 3
    SPEND_GOLD = 4
    ACCESS_CHAT = 5


class SettingsTimeFormat(Enum):
    EU = 0
    US = 1
    UK = 2
    ISO = 3


class SettingsTimeType(Enum):
    UTC = 0
    LOCAL = 1
    GAMEWORLD = 2


class SettingsPremiumConfirmationFlag(Enum):
    DISABLE_GOLD_USAGE_CONFIRMATION = 0
    DISABLE_PREMIUM_USAGE_CONFIRMATION = 1


class SettingsPremiumConfirmation(Enum):
    # When should Premium Item Confirmation window pop up
    GOLD_AND_PREMIUM_ITEM_USAGE = 0
    GOLD_USAGE = 1
    NONE = 2


class Language(Enum):
    ENGLISH = 'en'
    DUTCH = 'de'
    PORTUGUESE = 'pt'
    SPANISH = 'es'
    ITALIAN ='it'
    POLISH = 'pl'
    RUSSIAN = 'ru'
    ARABIC = 'ae'
    TURKISH = 'tr'
    FRENCH = 'fr'
    CZECH = 'cz'


class SilverChangeType(Enum):
    EXCHANGE_OFFICE = 1
    AUCTION = 2
    SELL_TO_INTERMEDIARY = 3
    ADVENTURE = 4
    COOP_PACKAGE = 5
    QUEST = 6
    STARTER_PACKAGE = 7
    CARD_GAME = 8


class TradeOfferCollection(Enum):
    OWN = 'own'
    ALL = 'all'


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class CelebrationType(Enum):
    SMALL = 1
    LARGE = 2


class Unit(Enum):
    # Roman
    LEGIONNAIRE = 1
    PRAETORIAN = 2
    IMPERIAN = 3
    EQUITES_LEGATI = 4
    EQUITES_IMPERATORIS = 5
    EQUITES_CAESARIS = 6
    BATTERING_RAM = 7
    FIRE_CATAPULT = 8
    SENATOR = 9
    ROMAN_SETTLER = 10

    # Teuton
    CLUBSWINGER = 11
    SPEARFIGHTER = 12
    AXEFIGHTER = 13
    SCOUT = 14
    PALADIN = 15
    TEUTONIC_KNIGHT = 16
    TEUTON_RAM = 17
    CATAPULT = 18
    CHIEF = 19
    TEUTON_SETTLER = 20

    # Gaul
    PHALANX = 21
    SWORDSMAN = 22
    PATHFINDER = 23
    THEUTATES_THUNDER = 24
    DRUIDRIDER = 25
    HAEDUAN = 26
    GAUL_RAM = 27
    TREBUCHET = 28
    CHIEFTAIN = 29
    GAUL_SETTLER = 30

    # TODO: Add nature and natar

    @property
    def as_nr(self):
        return unit_id_to_unit_nr(self.value)


class RomanUnit(Enum):
    LEGIONNAIRE = 1
    PRAETORIAN = 2
    IMPERIAN = 3
    EQUITES_LEGATI = 4
    EQUITES_IMPERATORIS = 5
    EQUITES_CAESARIS = 6
    BATTERING_RAM = 7
    FIRE_CATAPULT = 8
    SENATOR = 9
    SETTLER = 10


class TeutonUnit(Enum):
    CLUBSWINGER = 11
    SPEARFIGHTER = 12
    AXEFIGHTER = 13
    SCOUT = 14
    PALADIN = 15
    TEUTONIC_KNIGHT = 16
    RAM = 17
    CATAPULT = 18
    CHIEF = 19
    SETTLER = 20


class GaulUnit(Enum):
    PHALANX = 21
    SWORDSMAN = 22
    PATHFINDER = 23
    THEUTATES_THUNDER = 24
    DRUIDRIDER = 25
    HAEDUAN = 26
    RAM = 27
    TREBUCHET = 28
    CHIEFTAIN = 29
    SETTLER = 30


class LogType(Enum):
    # TODO
    pass


class MarkerDuration(Enum):
    SIX_HOURS = 6
    TWELVE_HOURS = 12
    TWENTY_FOUR_HOURS = 24
    FOURTY_EIGHT_HOURS = 48


class ShopVersion(Enum):
    VERSION_1 = 1
    VERSION_2 = 2


class OnlineStatusFilter(Enum):
    FRIENDS_AND_KINGDOM_MEMBERS = 0
    FRIENDS = 1
    NOBODY = 2


class MapFilterValues(Enum):
    NONE = 0
    KINGDOM_BORDERS = 1
    CAPITAL_VILAGES = 4
    OWN_MARKERS = 8
    GAME_MESSAGES = 16
    PLAYER_MESSAGES = 32
    TREASURES = 64


class AttacksFilterValues(Enum):
    NONE = 0
    KINGDOM = 2


class RequestAction(Enum):
    # TODO
    pass


class ReportPlayerReason(Enum):
    # TODO
    pass


class DialogActionCommand(Enum):
    SET_NAME = 'setName'
    ACTIVATE = 'activate'
    VICTORY = 'victory'
    BACK_TO_VILLAGE = 'backToVillage'
    ATTACK = 'attack'
    BECOME_GOVERNOR = 'become_governor'
    BECOME_KING = 'become_king'  # TODO: Doublecheck
    DIRECTION0 = 'direction0'
    DIRECTION1 = 'direction1'  # TODO: Doublecheck
    DIRECTION2 = 'direction2'  # TODO: Doublecheck
    DIRECTION3 = 'direction3'  # TODO: Doublecheck
    DIRECTION4 = 'direction4'  # TODO: Doublecheck
    FINISH = 'finish'
    SET_LAST_USE = 'setLastUse'


class RankingType(Enum):
    PLAYER = 'ranking_Player'
    VILLAGE = 'ranking_Village'
    KINGDOM = 'ranking_Kingdom'


class RankingSubtype(Enum):
    POPULATION = 'population'
    OFFENSIVE_POINTS = 'offPoints'
    DEFENSIVE_POINTS = 'deffPoints'
    HEROES = 'heroes'
    SIZE = 'size'


class RankingCategory(Enum):
    PLAYER_POPULATION = {
        'ranking_type': RankingType.PLAYER.value,
        'ranking_subtype': RankingSubtype.POPULATION.value
    }
    PLAYER_OFFENSIVE_POINTS = {
        'ranking_type': RankingType.PLAYER.value,
        'ranking_subtype': RankingSubtype.OFFENSIVE_POINTS.value
    }
    PLAYER_DEFFENSIVE_POINTS = {
        'ranking_type': RankingType.PLAYER.value,
        'ranking_subtype': RankingSubtype.DEFENSIVE_POINTS.value
    }
    PLAYER_HEROES = {
        'ranking_type': RankingType.PLAYER.value,
        'ranking_subtype': RankingSubtype.HEROES.value
    }
    VILLAGE_POPULATION = {
        'ranking_type': RankingType.VILLAGE.value,
        'ranking_subtype': RankingSubtype.POPULATION.value
    }
    KINGDOM_POPULATION = {
        'ranking_type': RankingType.KINGDOM.value,
        'ranking_subtype': RankingSubtype.POPULATION.value
    }
    KINGDOM_SIZE = {
        'ranking_type': RankingType.KINGDOM.value,
        'ranking_subtype': RankingSubtype.SIZE.value
    }
    KINGDOM_OFFENSIVE_POINTS = {
        'ranking_type': RankingType.KINGDOM.value,
        'ranking_subtype': RankingSubtype.OFFENSIVE_POINTS.value
    }
    KINGDOM_DEFFENSIVE_POINTS = {
        'ranking_type': RankingType.KINGDOM.value,
        'ranking_subtype': RankingSubtype.DEFENSIVE_POINTS.value
    }


class ShareReportWith(Enum):
    SOCIETY = 'secretSociety'
    KINGDOM = 'kingdom'
    PLAYER = 'player'


class SocietyAttitude(Enum):
    BRIGHT = 1
    DARK = 2


class BrightSocietyTarget(Enum):
    PROTECT_VILLAGE = 1
    PROTECT_PLAYER = 2
    PROTECT_KINGDOM = 3
    PROTECT_EACH_OTHER = 5


class DarkSocietyTarget(Enum):
    COMBAT_VILLAGE = 1
    COMBAT_PLAYER = 2
    COMBAT_KINGDOM = 3


class BrightSocietyAdmissionCondition(Enum):
    NO_REQUIREMENT = 0
    RESOURCES_SENT = 1
    TROOPS_LOST_IN_DEFENSE = 2
    TROOPS_CURRENTLY_PROVIDED = 4


class DarkSocietyAdmissionCondition(Enum):
    NO_REQUIREMENT = 0
    RESOURCES_STOLEN = 1
    TROOPS_KILLED = 2
    TREASURES_STOLEN = 3


class SocietySharedInformation(Enum):
    BATTLE_AND_SCOUT_REPORTS = 'reports'
    DISPLAY_OF_NEXT_ATTACK_ON_VILLAGE = 'nextAttacks'
    ADDITIONAL_VILLAGE_INFORMATION = 'villageDetails'  # crop production, troops


class TradeRate(Enum):
    ALL_RATES = 0
    ONE_TO_ONE_OR_BETTER = 1


class SpyMissionType(Enum):
    RESOURCES = 'resources'
    DEFENCES = 'defence'


class PremiumFeatureAutoExtendFlags(Enum):
    TRAVIAN_PLUS_ON = 4
    TRAVIAN_PLUS_OFF = 3
    RESOURCES_BONUS_ON = 5
    RESOURCES_BONUS_OFF = 2
    CROP_BONUS_ON = 7
    CROP_BONUS_OFF = 0


class CurrencyType(Enum):
    SILVER = 'silver'
    GOLD = 'gold'


class FinishNowCost(Enum):
    ZERO = 0
    ONE = -1
    TWO = -2


class Country(Enum):
    TURKEY = 'tr'
    INTERNATIONAL = 'en'
    UNITED_KINGDOM = 'gb'
    UNITED_STATUS = 'us'
    RUSSIA = 'ru'
    FRANCE = 'fr'
    SPAIN = 'es'
    PORTUGAL = 'pt'
    GERMANY = 'de'
    ITALY = 'it'
    POLAND = 'pl'
    CZECH_REPUBLIC = 'cz'
    SAUDI_ARABIA = 'ae'


class AuctionImages(Enum):
    SCROLL = 'scroll'
    WATER_BUCKET = 'water_bucket'


class QuestVersion(Enum):
    ONE = 1
    TWO = 2
