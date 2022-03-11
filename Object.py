from C_Transform import Transform
from C_InstanceID import InstanceID
from Debug import Debug


class Object:
    def __init__(self, name):
        self.name = name

        self.components = {}
        self.is_queued_for_removal = False

        self.transform = Transform(self)

        self.instance_ID = InstanceID(self)

        print(self.instance_ID.id)

        self.add_component(self.transform, self.instance_ID)

    def awake(self):
        for component in self.components.values():
            component.awake()

    def start(self):
        for component in self.components.values():
            component.start()

    def early_update(self, delta_time):
        for component in self.components.values():
            component.early_update(delta_time)

    def update(self, delta_time):
        for component in self.components.values():
            component.update(delta_time)

    def late_update(self, delta_time):
        for component in self.components.values():
            component.late_update(delta_time)

    def draw(self, canvas):
        for component in self.components.values():
            component.draw(canvas)

    def add_component(self, *args):
        for component in args:
            self.components[type(component)] = component

    def remove_component(self, comp_type):
        if self.get_component(comp_type) is not None:
            self.components.pop(comp_type)

    def get_component(self, comp_type):
        if comp_type in self.components:
            return self.components[comp_type]
        else:
            Debug.log_error(f"Component{comp_type} not found in {self.name}")
            return None

    def queue_for_removal(self):
        self.is_queued_for_removal = True
