

class ObjectCollection:
    def __init__(self):
        self.objects = []
        self.new_objects = []

    def add(self, *args):
        for new_object in args:
            self.new_objects.append(new_object)

    def early_update(self, delta_time):
        for obj in self.objects:
            obj.early_update(delta_time)

    def update(self, delta_time):
        for obj in self.objects:
            obj.update(delta_time)

    def late_update(self, delta_time):
        for obj in self.objects:
            obj.late_update(delta_time)

    def draw(self, canvas):
        for obj in self.objects:
            obj.draw(canvas)

    def process_new_objects(self):
        if len(self.new_objects) > 0:
            for obj in self.new_objects:
                obj.awake()

            for obj in self.new_objects:
                obj.start()

            self.objects += self.new_objects
            self.new_objects.clear()

    def process_removals(self):
        for obj_iterator, obj in enumerate(self.objects):
            if obj.is_queued_for_removal:
                self.objects.pop(obj_iterator)
