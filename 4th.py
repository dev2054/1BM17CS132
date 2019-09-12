class Myuniversity:


    def __init__(self):
        self.marks=-1
        self.age=0
        stud_id=""

    def validate_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True

        else:
            return False

    def validate_age(self):
        if(self.age>=20):
            return True
        else:
            return False

    def check_qual(self):
        if(self.validate_marks() is True and self.validate_age() is True):
            if(self.marks>=65):
                return True
            else:
                return False
        else:
            return False

    def setter(self,marks,age,stud_id):
        self.marks=marks
        self.age=age
        self.stud_id=stud_id

    def getter(self):
        print("Student ID: ", self.stud_id)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

stud1=Myuniversity()
stud1.setter(80,25,"mote")
stud1.getter()
print(stud1.check_qual())
