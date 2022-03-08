from Component import Component


class PlayerInput(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def update(self, delta_time):
        if self.controller.get_action_down("UP"):
            print("Jump")
