class Parent(object):
    def __init__(self, value=1):
        self.value = value

    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        return self.value + 1


p = Parent()
print(p.get_value())

c = Child()
print(c.get_value())