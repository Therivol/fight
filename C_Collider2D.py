from Component import Component
import pygame as p
from C_Transform import Transform


class Collider2D(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.is_trigger = False
        self.rect = p.Rect((0, 0), (0, 0))

    def set_is_trigger(self, is_trigger):
        self.is_trigger = is_trigger

    def set_rect(self, pos, size):
        self.set_pos(pos)
        self.set_size(size)

    # HOW TO DO FLAG? (p.Rect.center)
    def set_pos(self, pos):
        self.rect.center = pos

    def set_size(self, size):
        self.rect.size = size

    def update(self, delta_time):
        self.set_pos(self.owner.get_component(Transform).get_position_xy())
