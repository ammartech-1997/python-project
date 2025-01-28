class person:
    def __init__(self,name,age,city,mobile):
        self.name=name
        self.age=age
        self.city=city
        self.mobile=mobile

class student(person):
    def __init__(self,name,age,city,marks,subject,roll,division,school,grade,mobile):
        super().__init__(name,age,city,mobile)
        self.roll=roll
        self.age=age
        self.name=name
        self.city=city
        self.subject=subject
        self.division=division
        self.school=school
        self.marks=marks
        self.grade=grade
        self.mobile=mobile

    def display(self):
        print("Person Details:")
        print("name:",self.name)
        print("age:",self.age)
        print("city:",self.city)
        print("marks:",self.marks)
        print("subject:",self.subject)
        print("roll:",self.roll)
        print("division:",self.division)
        print("school:",self.school)
        print("grade:",self.grade)
        print("mobile:",self.mobile)

student1=student("Ammar","27","Malegaon","95","Python","01","A1","ATT High School","A++","9403803683")
student1.display()