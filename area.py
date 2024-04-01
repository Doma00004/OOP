import math
class Shape:
    def area(self):
        raise NotImplementedError('Subclasses must implement this method')
    
class Rectangle(Shape):
    # def __init__(self, l, w):
    #     self.l=l
    #     self.w=w
    def area(self,l,w):
        return l*w
    
class Circle(Shape):
    def area(self,r):
        return math.pi*r**2
    
class Triangle(Shape):
    def area(self,b,h):
        return 1/2*b*h

rect=Rectangle()
print("Area of rectangle:",rect.area(2,8))

cir=Circle()
print("Area of Circle:",cir.area(5))

tri=Triangle()
print("Area of triangle",tri.area(4,2))
