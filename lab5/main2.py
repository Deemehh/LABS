class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


def input_radius(erm):
    while True:
        try:
            radius = float(input(erm))
            if radius > 0: 
                return radius
            else:
                print("радиус должен быть положительным числом.")
        except ValueError:
            print("введите число.")


initial_radius = input_radius("Введите начальный радиус круга: ")
circle = Circle(initial_radius)

print("Текущий радиус круга:", circle.get_radius())

new_radius = input_radius("Введите новый радиус круга: ")
circle.set_radius(new_radius)

print("Новый радиус круга:", circle.get_radius())
