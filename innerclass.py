class college:

    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.Lappy=self.laptop() #creating object of the inner class

    def show(self):
        print("Name is :",self.name)
        print("My id is :",self.id)
        self.Lappy.show()

    #inner class
    class laptop:

        def __init__(self):
            self.name='Lenovo'
            self.cpu='i3'
            

        def show(self):
            print(self.name)


    

c1=college("sammy",12)
c1.show()

# we can create the object using the outer class for inner class.
# Lappy=college.laptop()
# Lappy.show()