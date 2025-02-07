import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, ch_x, ch_y):
        self.x = ch_x
        self.y = ch_y

    def dist(self, second_point):
        return math.sqrt((self.x - second_point.x)**2 + (self.y - second_point.y)**2)

p1 = Point(2,8)
p2 = Point(4, 2)

p1.show()
p2.show()

p1.move(10, 25)

p1.show()
p2.show()

print(p1.dist(p2))