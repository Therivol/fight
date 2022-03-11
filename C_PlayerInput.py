from pygame.math import Vector2
from Component import Component
from C_RigidBody2D import RigidBody2D


class PlayerInput(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.controller = None
        self.rigid_body = None
        self.vector = Vector2()

    def awake(self):
        self.rigid_body = self.owner.get_component(RigidBody2D)

    def set_controller(self, controller):
        self.controller = controller

    def update(self, delta_time):
        self.vector.x = self.controller.get_action("RIGHT") - self.controller.get_action("LEFT")

        self.owner.get_component(RigidBody2D).set_velocity(self.vector * delta_time * 500)