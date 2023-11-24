class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = "black"

    def set_color(self, color):
        self.current_color = color

    def add_shape(self, shape):
        self.canvas.append(shape)

    def draw_all_shapes(self):
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.clear_canvas()

    def clear_canvas(self):
        self.canvas = []


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, color):
        print(f"Drawing Circle: {self.center} with radius {self.radius} in {color} color")


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

    def draw(self, color):
        print(f"Drawing Triangle: {self.vertex1}, {self.vertex2}, {self.vertex3} in {color} color")


class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def draw(self, color):
        print(f"Drawing Rectangle: {self.top_left} with width {self.width} and height {self.height} in {color} color")


# Пример использования:

def test_engine_2d():
    engine = Engine2D()

    circle = Circle((0, 0), 5)
    triangle = Triangle((1, 1), (2, 2), (3, 3))
    rectangle = Rectangle((0, 0), 4, 3)

    # Добавление фигур на холст
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)

    # Установка цвета и отрисовка всех фигур
    engine.set_color("red")
    engine.draw_all_shapes()

    # Очистка холста и добавление новых фигур
    engine.clear_canvas()
    engine.set_color("blue")

    new_circle = Circle((2, 2), 3)
    new_triangle = Triangle((3, 3), (4, 4), (5, 5))

    engine.add_shape(new_circle)
    engine.add_shape(new_triangle)

    # Отрисовка новых фигур
    engine.draw_all_shapes()


# Вызов тестов
test_engine_2d()
