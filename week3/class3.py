class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def getLength(self):
        self.length = float(input())

    def area(self):
        return self.length**2
        
class rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
shape = Shape()
print(shape.area())

shape2 = rectangle(5,2)
print(shape2.area())



