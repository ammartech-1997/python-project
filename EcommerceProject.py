class Ecommerce:
    def  __init__(self,type_of_ecomm):
      self.type_of_ecomm = type_of_ecomm

class Platform (Ecommerce):
    def  __init__(self,type_of_ecomm,name,portal,users):
        super().__init__(type_of_ecomm)
        self.name = name
        self.portal = portal
        self.users = users

    def display(self):
        print(f"Type of E-commerce: {self.type_of_ecomm}")
        print(f"Platform Name: {self.name}")
        print(f"Porta Name:{self.portal}")
        print(f"Number of Users: {self.users}")

platform = Platform("B2C","Amazon","www.amazon.com","100000")
platform.display()

class Ecommerce:
    def  __init__(self,type_of_ecomm):
        self.type_of_ecomm = type_of_ecomm

class Platform (Ecommerce):
    def  __init__(self,type_of_ecomm, name, portal, users):
        super().__init__(type_of_ecomm)
        self.name = name
        self.portal = portal
        self.users = users

    def display(self):
        print(f"Type of E-commerce: {self.type_of_ecomm}")
        print(f"Platform Name: {self.name}")
        print(f"Porta Name:{self.portal}")
        print(f"Number of Users: {self.users}")

platform = Platform("B2B","Flipkart","www.flipkart.com","10000")
platform.display()