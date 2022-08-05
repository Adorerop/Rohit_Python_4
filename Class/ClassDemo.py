class Student:

    def getdata(self,fname,lname):
        self.f=fname
        self.l=lname

    def putdata(self):
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1=Student()
s2=Student()

s1.getdata("Jigar","Thakkar")
s1.putdata()

s2.getdata("Ajay","Patel")
s2.putdata()
