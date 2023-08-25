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
