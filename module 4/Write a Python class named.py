class Ractangle:

    def size(self,lenth,width):
        self.l=lenth
        self.w=width
    def area(self):
        area=self.l*self.w
        print(area)
a=Ractangle()
a.size(10,20)
a.area()