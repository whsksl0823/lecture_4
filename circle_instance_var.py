import math

class Circle:
    def __init__(self, name, radius, PI):
        self.name = name
        self.radius = radius
        self.PI = PI
        
    def area(self):
        return self.PI * self.radius ** 2

    def __del_(self):
        pass

c1 = Circle('C1', 10, math.pi)
print('{}의 면적은 {}'.format(c1.name, c1.area()))

c2 = Circle('C2', 20, math.pi)
print('{}의 면적은 {}'.format(c2.name, c2.area()))

print(c1.__dict__)