import pygame as p
from Component import Component
from C_Transform import Transform


class Sprite(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.surface = p.Surface((0, 0))

    def load(self, file_path):
        surf = p.image.load(file_path)
        self.set_surface(surf)

    def draw(self, canvas):
        transform = self.owner.transform.get_position_xy()
        destination = transform[0] - self.surface.get_width() / 2, transform[1] - self.surface.get_height() / 2
        canvas.blit(self.surface, destination)

    def set_surface(self, surface):
        self.surface = surface
