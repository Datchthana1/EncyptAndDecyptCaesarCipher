class Name:
    def __init__(self,Firstname,Lastname,SID):
        self.FirstName = Firstname
        self.LastName = Lastname
        self.SID = SID
    def GetFnandLn(self):
        return self.FirstName + " " + self.LastName + " " + self.SID
    def Input():
        Fname = str(input("Please Type your First Name : "))
        Lname = str(input("Please Type your Last name  : "))
        StudentID = str(input("Please Type Your Student ID : "))
        P1 = Name(Fname,Lname,StudentID)
        print(P1.GetFnandLn())
class University:
    def __str__(self,UniversityName,Department):
        self.UniversityName = UniversityName
        self.Department = Department
    def Output(self):
        return self.UniversityName + "and in Department : " + self.Department
    def Input():
        UniversityName = str(input("What is your University Name? : "))
        Department = str(input("What is your department? : "))
        U1 = University(UniversityName,Department)
        print(U1)