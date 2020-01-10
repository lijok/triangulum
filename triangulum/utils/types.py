from datetime import datetime

from triangulum.utils.util import map_id_to_coordinates, coordinates_to_map_id, filter_value_to_enums


class EmptyType(Exception):
    """Type has been instantiated without any parameters"""


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


class VillageId(int):

    @property
    def as_coords(self):
        return map_id_to_coordinates(map_id=int(self.real))


class Coordinates(int):
    def __new__(cls, map_id=None, x=None, y=None):
        if not map_id:
            if not x and not y:
                raise EmptyType('map_id or x and y required')

        if not map_id:
            map_id = coordinates_to_map_id(x=x, y=y)

        new = super().__new__(cls, map_id)
        new.x = x
        new.y = y

        return new

    @property
    def as_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

    @property
    def as_map_id(self):
        return coordinates_to_map_id(x=self.x, y=self.y)


class Timestamp(int):

    @property
    def as_t5_timestamp(self):
        return int('{:.2f}'.format(self.real).replace('.', ''))

    @property
    def as_datetime(self):
        return datetime.fromtimestamp(float(self.real))

    @property
    def as_datetime_string(self):
        return str(self.as_datetime)


class FilterScalar(int):
    def __new__(cls, value, enum):
        new = super().__new__(cls, value)
        new.enum = enum

        return new

    @property
    def as_enums(self):
        return filter_value_to_enums(enum=self.enum, value=self.real)

