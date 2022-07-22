from math import pi


class Circle:
    def size(self,radius):
        self.r=radius
    def area(self):
        area=pi*self.r**2
        print(area)
    def  perimeter(self):
        peri=2*pi*self.r
        print(peri)
c=Circle()
c.size(7)
c.area()
c.perimeter()
