from dataclasses import dataclass
from enum import Enum

from triangulum.utils.enums import RomanUnit, TeutonUnit, GaulUnit, MarkerType, MarkerColor, MarkerEditType, \
    MarkerDuration, FieldMessageType, MapFilterValues, AttacksFilterValues, Resource


@dataclass
class _Base:
    def __iter__(self):
        for key, val in self.__dict__.items():
            if key != '_ENUM':
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
            str(self._ENUM.simulator_order().index(self._ENUM[unit_name]) + 1): unit_qty
            for unit_name, unit_qty in dict(self).items()
        }

    def combat_format_without_zeros(self):
        return {
            str(self._ENUM.simulator_order().index(self._ENUM[unit_name]) + 1): unit_qty
            for unit_name, unit_qty in dict(self).items() if unit_qty > 0
        }

# TODO:
# The following Units classes have HERO attribute which their
# corresponding _ENUMs do not.
# This is because the ENUMs express unique values for each
# unit type, while the "combat" mechanisms such as fight_simulate
# and send, in the troops controller, do not care for the enumerable
# unique values, but instead require the positional values such as 1, 2, 3..
# for the unit selection.
# Which means that in all cases, for the combat mechanisms, the HERO comes up
# as the 11th index, while it in itself does not have a unique ENUM
# This needs to be made cleaner, however, as of writing this
# I couldn't come up with anything better


@dataclass
class RomanUnits(_Units):
    _ENUM: Enum = RomanUnit

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
