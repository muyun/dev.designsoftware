# 
# python's object system is dict that contain references to peroperities, functions, and oter dict
# 
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side 

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2



def test():
    examples = [Circle("ci", 2), Square("sq", 3)]
    
    for thing in examples:
        n = thing.name
        p = thing.perimeter()
        a = thing.area()
        print(f"{n} has perimeter {p:.2f} and area {a:.2f}")
    
    #return

# 
def shapes_dict():
    return

def main():
    test

if __name__ == "__main__":
    test()