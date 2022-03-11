import pygame as p


class FrameCounter:
    def __init__(self):
        self.fps_update = 0
        self.fps_count = 0
        self.fps_text = p.Surface((0, 0))
        p.font.init()
        self.font = p.font.Font("assets/font/CONSOLA.TTF", 36)

    def update(self, dt):
        self.fps_update += dt
        if self.fps_update > 0.5:
            self.fps_count = str(int(1 / dt))
            self.fps_text = self.font.render(self.fps_count, True, (0, 0, 0))
            self.fps_update = 0

    def draw(self, canvas):
        canvas.render(self.fps_text, (10, 10), "UI")

