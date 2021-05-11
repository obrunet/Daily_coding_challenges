"""
Create a class Circle():
- parameters for the constructor: radius and center
- methods : area, perimeter
Then create an other class Cylinder() derivated from Circle
- the constructor contains the height parameter
- method : volume
"""


class Circle(object):
    """Class of circle objects, parameters at init: radius, center
    methods: area, perimeter, volume of the sphere, check if a point is in the circle"""

    type = "circle"
    PI = 3.14159

    def __init__(self, radius=2):
        """Initializes the parameter of a circle"""
        self.radius = radius
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

    def __init__(self, radius=3, height=2):
        """Initializes the parameter of a cylinder: its height"""
        Circle.__init__(self, radius)
        self.height = height
        self.cylinder_volume = self.calculate_cylinder_volume()

    def calculate_cylinder_volume(self):
        """Computes the volume of the cylinder"""
        return self.circle_area * self.height

    def all_info(self):
        """Returns a string with all infos"""
        return f"Cylinder Volume {self.cylinder_volume:.2f} cm3"


def main():
    circle = Circle(10)
    print(circle.all_info())
    cylinder = Cylinder(3   , 4)
    print(cylinder.all_info())


if __name__ == "__main__":
    main()
