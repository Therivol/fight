

class Component:
    def __init__(self, owner):
        self.owner = owner

    def awake(self):
        pass

    def start(self):
        pass

    def early_update(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    def late_update(self, delta_time):
        pass

    def draw(self, canvas):
        pass
    