from pygame.math import Vector2
from Component import Component
from Physics import Physics


class Force:
    def __init__(self, resistance, velocity, remove):
        self.remove = remove
        self.velocity = velocity
        self.acceleration = Vector2()
        self.resistance = -abs(resistance)
        self.is_queued_for_removal = False

    def set_velocity(self, vel):
        self.velocity.update(vel)

    def set_acceleration(self, acc):
        self.acceleration.update(acc)

    def update(self, delta_time):
        self.acceleration += self.velocity * self.resistance
        self.velocity += self.acceleration

        if self.remove:
            if self.velocity.x <= 0:
                self.is_queued_for_removal = True


class RigidBody2D(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.forces = []
        self.velocity = Vector2()
        self.gravity = False
        self.gravity_const = 9.8

    def set_velocity(self, vel):
        self.velocity.update(vel)

    def add_velocity(self, vel):
        self.velocity += vel

    def set_gravity(self, gravity):
        self.gravity = gravity

    def add_force(self, resistance, velocity=Vector2(), remove=True):
        force = Force(resistance, velocity, remove)
        self.forces.append(force)

        return force

    def update(self, delta_time):
        # self.velocity.update((0, 0))

        new_forces = []
        for force in self.forces:
            self.velocity += force.velocity + 0.5 * force.acceleration
            force.update(delta_time)
            if not force.is_queued_for_removal:
                new_forces.append(force)
        self.forces = new_forces

        self.owner.transform.add_position_pos(self.velocity)
