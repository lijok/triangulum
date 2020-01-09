from typing import Tuple


def map_id_to_coordinates(map_id: int) -> Tuple[int, int]:
    """Unpacks 2 signed shorts out of an int"""

    binary = bin(map_id)[2:].rjust(30, '0')
    x, y = binary[15:], binary[:15]
    return int(x, 2) - 16384, int(y, 2) - 16384


def coordinates_to_map_id(x: int, y: int) -> int:
    """Packs 2 signed shorts into an int"""

    return 536887296 + x + y * 32768


def unit_id_to_unit_nr(unit_id: int) -> int:
    """Translates a unit_id to unit_nr.

    unit_id is an enum, i.e 21 for phalanx, 22 for swordsman, 11 for clubswinger
    unit_nr is a number used when creating farm lists, which ends up being
        1 for phalanx, 2 for swordsman, 11 for clubswinger

    """
    return 1 + (unit_id - 1) % 10


def unit_nr_to_unit_id(unit_nr: int, tribe_id: int) -> int:
    if unit_nr == 11:  # TODO: This is hero
        return 98  # static
    else:
        return ((tribe_id - 1) * 10) + unit_nr
