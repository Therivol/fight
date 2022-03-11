import pygame as p
from enum import Enum
from dataclasses import dataclass


class DrawLayers(Enum):
    terrain = "Terrain"
    default = "Default"
    entities = "Entities"
    ui = "UI"


class Canvas:
    def __init__(self, res):
        self.RES = res
        self.surface = p.Surface(res)
        self.scroll = p.Vector2(0, 0)

        self.render_bank = {}
        self.set_render_bank()

    def set_render_bank(self):
        self.render_bank = {layer.value: [] for layer in DrawLayers}

    def render(self, surface, destination, layer):
        self.render_bank[layer].append(RenderObject(surface=surface, destination=destination))

    def fill(self, color):
        self.surface.fill(color)

    def set_scroll(self, destination):
        new_destination = destination[0] + self.RES[0] / 2, destination[1] + self.RES[1] / 2
        self.scroll.update(new_destination)

    def blit(self, surface, destination):
        new_destination = destination[0] + self.scroll.x, destination[1] + self.scroll.y
        self.surface.blit(surface, new_destination)

    def blit_ui(self, surface, destination):
        self.surface.blit(surface, destination)

    def draw(self):
        for layer in DrawLayers:
            if layer.value == "UI":
                continue
            for render_object in self.render_bank[layer.value]:
                self.blit(render_object.surface, render_object.destination)

        for render_object in self.render_bank["UI"]:
            self.blit_ui(render_object.surface, render_object.destination)

        self.set_render_bank()


@dataclass
class RenderObject:
    surface: p.Surface = None
    destination: tuple = None
