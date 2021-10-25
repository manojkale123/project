class Demo1:

    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
        

    def config(self):
        print("CMD Processor",self.ram,self.cpu)

obj1=Demo1(5,"i3")
obj1.config()