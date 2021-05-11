"""
Create a class Circle():
- parameters for the constructor: radius and center
- methods : area, perimeter
Then create an other class Cylinder() derivated from Circle
- the constructor contains the height parameter
- method : volume
Finally overwrite the cylinder class with Cone
"""


class Circle(object):
    """Class of circle objects, parameters at init: radius, center
    methods: area, perimeter, volume of the sphere, check if a point is in the circle"""

    type = "circle"
    PI = 3.14159

    def __init__(self, radius=2, center=(0, 0)):
        """Initializes parameter of a circle - center is a tuple (x, y)"""
        self.radius = radius
        self.circle_center = center
        self.circle_area = self.calculate_area()
        self.circle_perimeter = self.calculate_perimeter()

    def calculate_area(self):
        """Computes the area of the circle"""
        return Circle.PI * self.radius**2

    def calculate_perimeter(self):
        """Computes the perimeter of the circle"""
        return Circle.PI * 2 * self.radius

    def all_info(self):
        """Returns a string with all infos"""
        return f"Area: {self.circle_area:.2f} cm² | Perimeter: {self.circle_perimeter:.2f} cm"


class Cylinder(Circle):
    """Class of cylinder objects derived from Circle, parameter at init: height
    method: volume of the cylinder"""

    def __init__(self, radius, center, height=2):
        """Initializes the parameter of a cylinder: its height"""
        Circle.__init__(self, radius, center)
        self.height = height
        self.volume = self.calculate_volume()
        self.area = self.calculate_area()

    def calculate_volume(self):
        """Computes the volume of the cylinder"""
        return self.circle_area * self.height

    def calculate_area(self):
        """Computes the area of the cylinder"""
        return self.circle_perimeter * self.height + 2 * self.circle_area

    def all_info(self):
        """Returns a string with all infos"""
        return f"Area: {self.area:.2f} cm² | Cylinder Volume {self.volume:.2f} cm3"


class Cone(Cylinder):
    """Class of Cone objects derived from overwritten Circle, parameter at init: height
    method: volume of the cone"""

    def __init__(self, radius, center, height=3):
        """Initializes the parameter of a cone: its height"""

    def calculate_cylinder_volume(self):
        """Computes the volume of the cylinder"""
        return self.circle_area * self.height


def main():
    circle = Circle(10, (1, 1))
    print(circle.all_info())
    cylinder = Cylinder(3, (1, 1), 4)
    print(cylinder.all_info())


if __name__ == "__main__":
    main()
