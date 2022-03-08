

class Scene:
    def __init__(self, name, window):
        self.name = name
        self.window = window

    def on_destroy(self):
        pass

    def on_activate(self):
        pass

    def early_update(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    def late_update(self, delta_time):
        pass

    def draw(self, canvas):
        pass
