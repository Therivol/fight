import pygame as p


class Canvas:
    def __init__(self, res):
        self.RES = res
        self.surface = p.Surface(res)
        self.scroll = p.Vector2(0, 0)

    def blit(self, surface, destination):
        new_destination = destination[0] + self.scroll.x, destination[1] + self.scroll.y
        self.surface.blit(surface, new_destination)

    def blit_ui(self, surface, destination):
        self.surface.blit(surface, destination)

    def fill(self, color):
        self.surface.fill(color)

    def set_scroll(self, destination):
        new_destination = destination[0] + self.RES[0] / 2, destination[1] + self.RES[1] / 2
        self.scroll.update(new_destination)
