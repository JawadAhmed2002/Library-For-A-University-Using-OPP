#A teacher issues three tests to a class of 5 students. The grades on these tests are integers in the
#range 0 to 100. Develop a system which should contain following functions to help teacher in finding

#Here i make a class name grade and student
class Student:
    def __init__(self,name,RollNo):
        self.name=name
        self.RollNo=RollNo
    def getname(self):
        print("The name of student is:",self.name)
    def getRollno(self):
        print("The Roll no of Student is:",self.RollNo)
class Grade:
    def __init__(self,test1,test2,test3):
        self.test1=test1
        self.test2=test2
        self.test3=test3

    def setTest_1_Marks(self,test1):
        self.test1=test1
    def setTest_2_Marks(self,test2):
        self.test2=test2
    def setTest_3_Marks(self,test3):
        self.test3=test3
    def getTest1(self):
        return self.test1
    def getTest2(self):
        return self.test2
    def getTest3(self):
        return self.test3
    def get_average(self):
        return (self.test1+self.test2+self.test3)/3

Stu1=Student("Jawad",59)
Stu1.getname()
Stu1=Grade(90,80,76)

print("The average of all the tests is:",Stu1.get_average())