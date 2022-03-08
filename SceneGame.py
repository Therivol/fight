import pygame as p
from Scene import Scene
from ObjectCollection import ObjectCollection
from O_Player import Player


class SceneGame(Scene):
    def __init__(self, window, controller):
        super().__init__("Game", window)

        self.controller = controller

        self.objects = ObjectCollection()

        self.player = Player(window, controller)
        self.objects.add(self.player)

    def on_destroy(self):
        pass

    def on_activate(self):
        pass

    def early_update(self, delta_time):
        pass

    def update(self, delta_time):
        self.objects.process_removals()
        self.objects.process_new_objects()
        self.objects.update(delta_time)

    def late_update(self, delta_time):
        self.objects.late_update(delta_time)

    def draw(self, canvas):
        self.objects.draw(canvas)
        # p.draw.rect(canvas.surface, (0, 0, 0), p.Rect((500, 500), (100, 100)))
