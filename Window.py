import pygame as p
from Debug import Debug
from Canvas import Canvas


class Window:
    def __init__(self, size, title, controller):
        self.canvas = Canvas((1920, 1080))

        self.view = p.Surface(size)
        self.view_destination = (0, 0)

        self.controller = controller

        self.window_size = size
        self.window = p.display.set_mode(size, p.RESIZABLE)
        p.display.set_caption(title)
        p.display.set_icon(p.image.load("assets/player/player_front1.png"))

        self.aspect_ratio = 16 / 9

    def update(self, dt):
        if self.controller.get_key_down('f11'):
            Debug.log("Full Screen")

    def begin_draw(self):
        self.canvas.fill((110, 120, 145))

    def end_draw(self):
        self.view.blit(p.transform.scale(self.canvas.surface, self.view.get_size()), (0, 0))
        self.view_destination = (self.window.get_width() / 2 - self.view.get_width() / 2,
                                 self.window.get_height() / 2 - self.view.get_height() / 2)
        self.window.blit(self.view, self.view_destination)
        p.display.update()

    def resize(self, size):
        if size[1] * self.aspect_ratio > size[0]:
            self.view = p.Surface((size[0], size[0] / self.aspect_ratio))
        else:
            self.view = p.Surface((size[1] * self.aspect_ratio, size[1]))

    def get_mouse_pos(self):
        return (p.mouse.get_pos()[0] - self.view_destination[0] * (self.RES[0] / self.view.get_width()),
                p.mouse.get_pos()[1] - self.view_destination[1] * (self.RES[1] / self.view.get_height()))
