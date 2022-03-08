import sys
import pygame as p
from Window import Window
from FrameCounter import FrameCounter
from Controller import Controller

from SceneStateMachine import SceneStateMachine
from SceneGame import SceneGame


class Game:
    def __init__(self):
        p.init()

        self.controller = Controller()

        self.window = Window((800, 450), "Fight", self.controller)

        self.scene_manager = SceneStateMachine(SceneGame(self.window, self.controller))

        self.fps = FrameCounter()

        self.is_running = True

        self.delta_time = 0
        self.last_frame_time = 0

    def capture_input(self):
        for ev in p.event.get():
            if ev.type == p.QUIT:
                self.is_running = False
                p.quit()
                sys.exit()

            if ev.type == p.VIDEORESIZE:
                self.window.resize((ev.w, ev.h))

            if ev.type == p.KEYDOWN:
                self.controller.set_key(ev.key)

            if ev.type == p.KEYUP:
                self.controller.reset_key(ev.key)

            if ev.type == p.MOUSEBUTTONDOWN or p.MOUSEBUTTONUP:
                self.controller.set_buttons()

    def early_update(self):
        self.scene_manager.early_update(self.delta_time)

    def update(self):
        self.window.update(self.delta_time)
        self.scene_manager.update(self.delta_time)
        self.fps.update(self.delta_time)

    def late_update(self):
        self.scene_manager.late_update(self.delta_time)

    def draw(self):
        self.window.begin_draw()
        self.scene_manager.draw(self.window.canvas)
        self.fps.draw(self.window.canvas)
        self.window.end_draw()

    def calculate_delta_time(self):
        self.delta_time = (p.time.get_ticks() - self.last_frame_time) / 1000
        self.last_frame_time = p.time.get_ticks()
