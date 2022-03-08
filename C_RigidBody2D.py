from pygame.math import Vector2
from Component import Component
from Physics import Physics


class Force:
    def __init__(self, initial_force, resistance):
        self.vector = initial_force
        self.resistance = 1 - resistance
        self.is_queued_for_removal = False

    def queue_for_removal(self):
        self.is_queued_for_removal = True

    def update(self, delta_time):
        self.vector -= self.resistance * delta_time
        if self.vector < 0.001:
            self.queue_for_removal()


class RigidBody2D(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.forces = []
        self.velocity = Vector2()
        self.gravity = False
        self.gravity_const = 9.8

    def set_velocity(self, vel):
        self.velocity.update(vel)

    def set_gravity(self, gravity):
        self.gravity = gravity

    def add_force(self, vector, resistance):
        self.forces.append(Force(vector, resistance))

    def move_towards(self, pos):
        pass

    def update(self, delta_time):
        for force in self.forces:
            self.velocity += force.vector
            force.update(delta_time)
            if force.is_queued_for_removal:
                self.forces.remove(force)
        # stuff
        self.owner.transform.add_position_pos(self.velocity)
