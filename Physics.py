

class Physics:
    gravity_acceleration = 9.8

    @classmethod
    def apply_gravity(cls, vector):
        vector.y += cls.gravity_acceleration


