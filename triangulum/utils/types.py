from dataclasses import dataclass
from typing import Union

from triangulum.utils.util import map_id_to_coordinates, coordinates_to_map_id


@dataclass
class VillageId:
    x: int = None
    y: int = None
    id: Union[int, str] = None

    @property
    def as_coords(self):
        if self.x and self.y:
            return self.x, self.y
        else:
            return map_id_to_coordinates(map_id=int(self.id))

    @property
    def as_id(self):
        if self.id:
            return int(self.id)
        else:
            return coordinates_to_map_id(x=self.x, y=self.y)
