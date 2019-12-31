from typing import Tuple


def map_id_to_coordinates(map_id: int) -> Tuple[int, int]:
    """Unpacks 2 signed shorts out of an int"""

    binary = bin(map_id)[2:].rjust(30, '0')
    x, y = binary[15:], binary[:15]
    return int(x, 2) - 16384, int(y, 2) - 16384


def coordinates_to_map_id(x: int, y: int) -> int:
    """Packs 2 signed shorts into an int"""

    return 536887296 + x + y * 32768
