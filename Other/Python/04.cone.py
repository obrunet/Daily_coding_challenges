class Circle(object):
    type = "Circle"
    PI = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()
        self.volume = self.get_volume()

    def get_perimeter(self):
        return self.PI * self.radius * 2

    def get_area(self):
        return self.PI * self.radius ** 2

    def get_volume(self):
        return 4 / 3 * self.PI * self.radius ** 3

    def properties(self):
        return f'Perimeter: {self.perimeter:.2f} | Area: {self.area:.2f} | Volume: {self.volume:.2f}'


class Cylinder(Circle):
    type = "Cylinder"

    def __init__(self, radius, height):
        Circle.__init__(self, radius)
        self.height = height
#        self.volume = self.get_volume()
        self.area = self.get_area()

    def get_area(self):
        return self.height

#    def get_volume(self):
#        return self.area * self.height

#    def properties(self):
#        return f'Area: {self.area:.2f} | Volume: {self.volume:.2f}'


circle = Circle(2)
print(circle.properties())

cylinder = Cylinder(2, 2)
print(cylinder.properties())
