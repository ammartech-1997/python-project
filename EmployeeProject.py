
class Employee:
    def __init__(self):
        print("This is employee constructor")

    def display(self):
        print("This is display method")

class Manager(Employee):
    Employee
    print("This is Manager construtor")

M1=Manager()
M1.display()

class Manager:
    def  __init__(self):
        print("This is Manager constuctor")

    def display(self):
            print("This is display Method")

class HR:
    Manager
    print("THis is HR constructor")
M1=Manager()
M1.display()