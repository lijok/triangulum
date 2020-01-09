from dataclasses import dataclass
from datetime import datetime
from time import time
from typing import Union

from triangulum.utils.util import map_id_to_coordinates, coordinates_to_map_id


class EmptyType(Exception):
    """Type has been instantiated without any parameters"""


@dataclass
class _Base:
    pass


class ScalarId(int):
    pass


class BoolInt(int):
    pass


class LocationId(int):
    pass


class BuildingLvl(int):
    pass


class TroopId(int):
    pass


@dataclass
class VillageId(_Base):
    x: int = None
    y: int = None
    id: Union[int, str] = None

    @property
    def as_coords(self):
        if self.x and self.y:
            return self.x, self.y
        elif self.id:
            return map_id_to_coordinates(map_id=int(self.id))
        else:
            raise EmptyType('id or x and y required')

    @property
    def as_id(self):
        if self.id:
            return int(self.id)
        elif self.x and self.y:
            return coordinates_to_map_id(x=self.x, y=self.y)
        else:
            raise EmptyType('id or x and y required')


@dataclass
class Timestamp(_Base):
    value: float = time()

    @property
    def as_t5_timestamp(self):
        return int('{:.2f}'.format(self.value).replace('.', ''))

    @property
    def as_datetime(self):
        return datetime.fromtimestamp(self.value)

    @property
    def as_datetime_string(self):
        return str(self.as_datetime)


@dataclass
class Coordinates(_Base):  # TODO: Could this be VillageId instead?
    x: int
    y: int

    @property
    def as_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

    @property
    def as_map_id(self):
        return coordinates_to_map_id(x=self.x, y=self.y)


