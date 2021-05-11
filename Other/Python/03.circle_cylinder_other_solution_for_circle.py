"""
Create a class Circle():
- parameters for the constructor: radius and center
- methods : area, perimeter
Then creata an other class Cylinder() derivated from Circle
- the constructor contains the height parameter
- method : volume
cyl = Cylindre(5, 7)
print(cyl.surface()) 78.54
print(cyl.volume()) 549.78
"""


class Circle(object):
    """Defines a Circle, parameters at init: radius, center
    methods: area, perimeter, volume of the sphere, check if a point is in the circle"""

    type = "circle"
    PI = 3.14159

    def __init__(self, radius=2, center=(0, 0)):
        """Initializes parameter of a circle - center is a tuple (x, y)"""
        self.radius = radius
        self.center = center
        self.area = self.perimeter = self.volume = 0

    def calculate_area(self):
        """Computes the area of the circle"""
        self.area = Circle.PI * self.radius**2

    def calculate_perimeter(self):
        """Computes the perimeter of the circle"""
        self.perimeter = Circle.PI * 2 * self.radius

    def calculate_sphere_volume(self):
        """Computes the volume of the sphère"""
        self.volume = 4 / 3 * Circle.PI * self.radius ** 3

    def all_info(self):
        return f"The circle's properties are:\n-area: {self.area:.2f} cm²\n-perimeter: {self.perimeter:.2f}\n-sphere volume {self.volume:.2f}"


def main():
    c1 = Circle(10, (1, 1))
    c1.calculate_perimeter()
    c1.calculate_area()
    c1.calculate_sphere_volume()
    print(c1.all_info())


if __name__ == '__main__':
    main()
