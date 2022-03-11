import pygame as p
from Component import Component
from C_Transform import Transform
from C_BoxCollider import BoxCollider


class Image(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.surface = p.Surface((0, 0))
        self.draw_layer = "Default"

    def set_draw_layer(self, layer):
        self.draw_layer = layer

    def load(self, file_path):
        surf = p.image.load(file_path)
        self.set_surface(surf)

    def draw(self, canvas):
        transform = self.owner.get_component(Transform).get_position_xy()
        destination = transform[0] - self.surface.get_width() / 2, transform[1] - self.surface.get_height() / 2
        canvas.render(self.surface, destination, self.draw_layer)

    def set_surface(self, surface):
        self.surface = surface

    def fill(self, color):
        self.surface.fill(color)
