import pygame as p
from Object import Object
from C_Image import Image
from C_Camera import Camera
from C_PlayerInput import PlayerInput
from C_RigidBody2D import RigidBody2D
from C_BoxCollider import BoxCollider


class Player(Object):
    def __init__(self, window, controller):
        super().__init__("player")

        self.window = window

        self.controller = controller

        self.sprite = Image(self)
        self.sprite.set_surface(p.transform.scale(p.image.load("assets/player/player_front1.png"), (64, 64)))
        self.sprite.set_draw_layer("Entities")

        self.camera = Camera(self)
        self.camera.set_canvas(window.canvas)

        self.input = PlayerInput(self)
        self.input.set_controller(controller)

        self.rigid_body = RigidBody2D(self)
        self.rigid_body.set_gravity(True)

        self.collider = BoxCollider(self)
        self.collider.set_rect(p.Rect((0, 0), (64, 64)))

        self.add_component(self.rigid_body, self.input, self.sprite, self.camera, self.collider)
