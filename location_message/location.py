from typing import Optional
from mcdreforged.api.utils import Serializable
from location_message.position import Position


class Location(Serializable):
    name: str
    desc: Optional[str] = None
    dim: int
    pos: Position
