import pygame as p
from Object import Object
from C_Collider2D import Collider2D
from C_Image import Image


class Button(Object):
    def __init__(self, name, pos, size, text, color):
        super().__init__(name)

        self.collider = Collider2D(self)
        self.collider.set_rect(pos, size)

        self.fill = Image(self)
        self.fill.fill(color)

    def update(self, delta_time):
        pass
