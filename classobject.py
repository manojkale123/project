class Demo:
    def disp(self):
        """
        This function display the name of the person
        """
        print("The User Name")

Names=['Maddy','Manoj','Sam']

#Crearing object of the class
com=Demo()

#calling to the method of the class
Demo.disp(com) # This is the first way to calling method.
com.disp() # This is second way to calling object.
a=2
a.bit_length()