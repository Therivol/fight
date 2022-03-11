from enum import Enum
from dataclasses import dataclass
from Component import Component


class CollisionLayer(Enum):
    Default = 1
    Player = 2
    Tile = 3


@dataclass
class Manifold:
    colliding = False
    other = None


class Collider(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.layer = CollisionLayer

    def set_layer(self, layer):
        self.layer = layer

    def intersects(self, other):
        pass

    def resolve_overlap(self, manifold):
        pass
