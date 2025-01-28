
class Cars:
    def __init__(self,m,b):
        self.model=m
        self.brand=b

    def displayData(self):
        print(f"The car data is {self.model},{self.brand}")

Car1=Cars("Swift","Maruti")
Car2=Cars("Innova;","Toyota")
Car1.displayData()
Car2.displayData()

class cars:
    def  __init__(self,m,b):
        self.model=m
        self.brand=b

    def displayData(self):
        print(f"This car data is {self.model},{self.brand}")

Car2=cars("Fourtuner","Toyota")
Car2.displayData()


