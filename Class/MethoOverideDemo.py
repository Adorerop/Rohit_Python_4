class A:

    def show(self):
        super().show()
        print("Show From A")

class B:

    def show(self):
        print("Show From B")

class C(A,B):

    def show(self):
        super().show()
        print("Show From C")

    def test(self):
        print("test with no argument")

    def test(self,a):
        print("test with 1 argument")

    def test(self,a,b):
        print("test with 2 argument")

c1=C()
c1.show()
c1.test(1,2)
