from triangulum.utils.enums import BuildingType, HeroItemType, QuestGiver, NotificationType, ReportCollection, \
    ReportDisplayType

BUILDING_WALL_TYPES = [
    BuildingType.CITY_WALL,
    BuildingType.NATAR_CITY_WALL,
    BuildingType.EARTH_WALL,
    BuildingType.PALLISADE,
]

HERO_ITEM_UPGRADE_ITEMS = [
    HeroItemType.ARMOR_UPGRADE,
    HeroItemType.WEAPON_UPGRADE,
    HeroItemType.LEFT_HAND_UPGRADE,
    HeroItemType.HELMET_UPGRADE,
    HeroItemType.SHOE_UPGRADE
]

# Quest givers which stand in the main village
QUEST_GIVER_VILLAGERS = [
    QuestGiver.WREN,
    QuestGiver.SCOUT,
    QuestGiver.CHIEF,
    QuestGiver.ENVOY,
    QuestGiver.ADVENTURER
]

NOTIFICATION_FIGHT_AND_SPY_REPORTS = [
    NotificationType.REPORT_ATTACKER_WON_WITHOUT_LOSSES,
    NotificationType.REPORT_ATTACKER_WON_WITH_LOSSES,
    NotificationType.REPORT_ATTACKER_LOST,
    NotificationType.REPORT_DEFENDER_WON_WITHOUT_LOSSES,
    NotificationType.REPORT_DEFENDER_WON_WITH_LOSSES,
    NotificationType.REPORT_DEFENDER_LOST_WITH_LOSSES,
    NotificationType.REPORT_DEFENDER_LOST_WITHOUT_LOSSES,
    NotificationType.REPORT_SPY_SUCCESS_UNDETECTED,
    NotificationType.REPORT_SPY_SUCCESS_DETECTED,
    NotificationType.REPORT_SPY_FAILURE,
    NotificationType.REPORT_SPY_DEFENDED,
    NotificationType.REPORT_SPY_NOT_DEFENDED
]

REPORT_ALL_COLLECTIONS = [
    ReportCollection.PERSONAL,
    ReportCollection.KING,
    ReportCollection.KING_MINIONS,
    ReportCollection.SOCIETY,
    ReportCollection.FAVORITE,
    ReportCollection.SEARCH,
    ReportCollection.PRESTIGE
]

REPORT_DISPLAY_TYPES_FIGHT = [
    ReportDisplayType.FIGHT,
    ReportDisplayType.SPY,
    ReportDisplayType.VISIT,
    ReportDisplayType.SUPPORT_ATTACKED,
    ReportDisplayType.ANIMALS_CAPTURE
]

BUILDING_EXPANSION_SLOTS = {
    '25': 2,
    '26': 3
}

BUILDING_RESIDENCE_EXPANSION_UNLOCKS = {
    '0': 10,
    '1': 20
}

BUILDING_PALACE_EXPANSION_UNLOCKS = {
    '0': 10,
    '1': 15,
    '2': 20
}

BUILDING_EXPANSION_SLOT_UNLOCKS = {
    '25': BUILDING_RESIDENCE_EXPANSION_UNLOCKS,
    '26': BUILDING_PALACE_EXPANSION_UNLOCKS
}

HERO_ITEM_IMPROVEMENTS = {
    HeroItemType.BANDAGE_25: {
        'id': HeroItemType.BANDAGE_25_UPGRADED,
        'bonus': 5
    },
    HeroItemType.BANDAGE_33: {
        'id': HeroItemType.BANDAGE_33_UPGRADED,
        'bonus': 5
    },
    HeroItemType.RESOURCE_BONUS_3: {
        'id': HeroItemType.RESOURCE_BONUS_4,
        'bonus': 1
    },
    HeroItemType.RESOURCE_BONUS_4: {
        'id': HeroItemType.RESOURCE_BONUS_5,
        'bonus': 1
    },
    HeroItemType.CROP_BONUS_3: {
        'id': HeroItemType.CROP_BONUS_4,
        'bonus': 1
    },
    HeroItemType.CROP_BONUS_4: {
        'id': HeroItemType.CROP_BONUS_5,
        'bonus': 1
    }
}
