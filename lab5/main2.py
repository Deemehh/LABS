class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(24)

print("Текущий радиус круга:", circle.get_radius())

circle.set_radius(53)

print("Новый радиус круга:", circle.get_radius())
