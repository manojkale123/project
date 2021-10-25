class A:

    def __init__(self):
        print("We are in A class")

    def feature1(self):
        print("Hello world")

    def feature2(self):
        print("Hows going")


class B:
    
    def __init__(self):
        #super().__init__()
        print("We are in class B")

    def feature1(self):
        print("Feature1 : working")

    def feature2(self):
        print("feature2 :working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("We are in class C")

    #To call super class methods
    def feat(self):
        super().feature2()

#whenever we have multiple classes it will call 
#left to right means it called first Class A init method

Obj1=C()
Obj1.feat()



