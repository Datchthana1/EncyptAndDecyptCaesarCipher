class Name:
    def __init__(self,Firstname,Lastname,SID):
        self.FirstName = Firstname
        self.LastName = Lastname
        self.SID = SID
    def GetFnandLn(self):
        return self.FirstName + " " + self.LastName + " " + self.SID
    def Input():
        Fname = str(input("โปรดใส่ชื่อของคุณ : "))
        Lname = str(input("โปรดใส่นามสกุลของคุณ : "))
        StudentID = str(input("โปรดใส่รหัสประจำตัว : "))
        P1 = Name(Fname,Lname,StudentID)
        print(P1.GetFnandLn())