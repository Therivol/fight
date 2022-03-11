from C_Collider import Collider
from C_Collider import Manifold
from C_Collider import CollisionLayer
import pygame as p
from pygame.math import Vector2
from C_Transform import Transform
from Debug import Debug


class BoxCollider(Collider):
    def __init__(self, owner):
        super().__init__(owner)

        self.rect = p.Rect((0, 0), (0, 0))
        self.offset = Vector2()

    def intersects(self, other):
        m = Manifold()
        m.colliding = False

        if type(other) == BoxCollider:
            rect_1 = self.get_rect()
            rect_2 = other.get_rect()

            if rect_1.colliderect(rect_2):
                m.colliding = True
                m.other = other

            return m
        else:
            Debug.log_error(f"{other} not of type BoxCollider")

    def resolve_overlap(self, manifold):
        transform = self.owner.get_component(Transform)
        if transform.is_static:
            return

        rect_1 = self.get_rect()
        rect_2 = manifold.other

        resolve = 0
        x_diff = (rect_1.left + (rect_1.width * 0.5)) - (rect_2.left + (rect_2.width * 0.5))
        y_diff = (rect_1.top + (rect_1.height * 0.5)) - (rect_2.top + (rect_2.height * 0.5))

        if abs(x_diff) > abs(y_diff):
            if x_diff > 0:
                resolve = (rect_2.left + rect_2.width) - rect_1.left
            else:
                resolve = -((rect_1.left + rect_1.width) - rect_2.left)

            transform.add_position_pos(resolve, 0)

        else:
            if y_diff > 0:
                resolve = (rect_2.top + rect_2.height) - rect_1.top
            else:
                resolve = -((rect_1.top + rect_1.height) - rect_2.top)

            transform.add_position_pos(0, resolve)

    def set_rect(self, rect):
        self.rect = rect
        self.set_position()

    def get_rect(self):
        self.set_position()
        return self.rect

    def set_position(self):
        pos = self.owner.get_component(Transform).get_position_xy()
        self.rect.center = pos

    def update(self, delta_time):
        self.set_position()
