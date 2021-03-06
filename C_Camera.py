import math

from Component import Component
from C_Transform import Transform


class Camera(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.canvas = None

    def late_update(self, delta_time):
        if self.canvas is not None:
            target_pos = self.owner.get_component(Transform).get_position_xy()
            self.canvas.set_scroll((-math.floor(target_pos[0]), -math.floor(target_pos[1])))

    def set_canvas(self, canvas):
        self.canvas = canvas
