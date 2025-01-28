class Students:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        self.total=sum(self.marks)
        self.percent=round(self.total/len(self.marks),2)
        if   self.percent>=75:
             self.grade="A"
        elif self.percent>=60:
             self.grade="B"
        elif self.percent>=50:
             self.grade="C"
        else:
             self.grade="D"

    def displayResult(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)
        print("Total:",self.total)
        print("Percent:",self.percent)
        print("Grade:",self.grade)
S1=Students("Saif",11,[76,85,78,77,90])
S1.displayResult()
