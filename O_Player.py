import pygame as p
from Object import Object
from C_Sprite import Sprite
from C_Camera import Camera
from C_PlayerInput import PlayerInput


class Player(Object):
    def __init__(self, window, controller):
        super().__init__("player")

        self.window = window

        self.controller = controller

        self.sprite = Sprite(self)
        self.sprite.set_surface(p.transform.scale(p.image.load("assets/player/player_front1.png"), (64, 64)))

        self.camera = Camera(self)
        self.camera.set_canvas(window.canvas)

        self.input = PlayerInput(self)
        self.input.set_controller(controller)

        self.add_component(self.sprite, self.camera, self.input)
