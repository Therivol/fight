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

        self.test_surface = p.Surface((100, 100))
        self.test_surface.fill((0, 0, 0))

    def on_destroy(self):
        pass

    def on_activate(self):
        pass

    def early_update(self, delta_time):
        self.objects.early_update(delta_time)

    def update(self, delta_time):
        self.objects.process_removals()
        self.objects.process_new_objects()
        self.objects.update(delta_time)

    def late_update(self, delta_time):
        self.objects.late_update(delta_time)

    def draw(self, canvas):
        self.objects.draw(canvas)
        self.window.canvas.render(self.test_surface, (0, 0), "Terrain")
