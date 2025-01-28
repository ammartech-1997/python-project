class PersonalInfo:
    def __init__(self,name,age,gender,city,blood):
        self.name=name
        self.age=age
        self.gender=gender
        self.city=city
        self.blood=blood

class AcademicInfo:
    def  __init__(self,degree,grade,university):
        self.degree=degree
        self.grade=grade
        self.university=university

class Certification:
    def  __init__(self,certname,level,year):
        self.certname=certname
        self.level=level
        self.year=year

class WorkExperience:
    def  __init__(self,company,profile,years):
        self.company=company
        self.profile=profile
        self.years=years

class  Resume(PersonalInfo,AcademicInfo,Certification,WorkExperience):
    def  __init__(self,name,age,gender,city,blood,degree,grade,university,certname,level,year,company,profile,years):
        PersonalInfo.__init__(self,name,age,gender,city,blood)
        AcademicInfo.__init__(self,degree,grade,university)
        Certification.__init__(self,certname,level,year)
        WorkExperience.__init__(self,company,profile,years)

    def CreateResume(self):
        print("The Personal Information")
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)
        print("blood:",self.blood)
        print("city:",self.city)

        print("Academics")
        print("Highest Qualification:",self.degree)
        print("Grade:",self.grade)
        print("University:",self.university)

        print("Certification")
        print("Certification Title:",self.certname)
        print("level:",self.level)
        print("Year:",self.year)

        print("WorkExperience")
        print("Company:",self.company)
        print("Profile:",self.profile)
        print("Years:",self.years)

Object = Resume("Ammar","27","Male","Malegaon","O+","BCA","A++","Mani-pal University","Python","100%","2024","TCS","Python-Developer","2025")
Object.CreateResume()



