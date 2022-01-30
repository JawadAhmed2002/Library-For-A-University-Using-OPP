
#A teacher issues three tests to a class of 5 students. The grades on these tests are integers in the
#range 0 to 100. Develop a system which should contain following functions to help teacher in finding

import numpy as np
class Student:
    def __init__(self,name,RollNo):
        self.name=name
        self.RollNo=RollNo
    def getname(self):
        print("The name of student is:",self.name)
    def getRollno(self):
        print("The Roll no of Student is:",self.RollNo)
    def info(self):
        return self.name,self.RollNo
class Grade:
    def __init__(self):
        self.grade=np.zeros((5,3),"int64")
    def display_grade(self):
        return self.grade
    def take_input(self,teacher):
        r= int(input("Enter Row To Select Student:"))
        c= int(input("Enter Col To Select Test:"))
        isLegal = self.isLegalMove(r, c)

        if (isLegal == range(1)):
            self.grade[r, c] = teacher

    def isLegalMove(self,r,c):
        if(r>=0 and r<=3 and c>=0 and c<=3):
            if (self.grade[r,c]==0):
                return range(1)
            else:
                return 0
        else:
            return 0
    # HERE I DEFINE TO TAKE AVERAGE OF INDIVIDUAL TEST
    def takeAvg(self):
        takeavg=(self.grade[0,0]+self.grade[0,1]+self.grade[0,2])/3 or \
                (self.grade[1,0]+self.grade[1,1]+self.grade[1,2])/3 \
            or (self.grade[2,0]+self.grade[2,1]+self.grade[2,2])/3 \
            or (self.grade[3, 0] + self.grade[3, 1] + self.grade[3, 2]) / 3 \
            or (self.grade[4, 0] + self.grade[4, 1] + self.grade[4, 2]) / 3

        return takeavg
    def take_avg_wholeclass(self):
            wholeclassavg=(self.grade[0,0]+self.grade[0,1]+self.grade[0,2] + \
                self.grade[1,0]+self.grade[1,1]+self.grade[1,2] + \
                self.grade[2,0]+self.grade[2,1]+self.grade[2,2] + \
                self.grade[3, 0] + self.grade[3, 1] + self.grade[3, 2] + \
                self.grade[4, 0] + self.grade[4, 1] + self.grade[4, 2]) / 5
            return wholeclassavg

    def highestAvg(self):
        greateravg=(self.grade[0,0]+self.grade[0,1]+self.grade[0,2])/3 > \
                (self.grade[1,0]+self.grade[1,1]+self.grade[1,2])/3 \
             >(self.grade[2,0]+self.grade[2,1]+self.grade[2,2])/3 \
            > (self.grade[3, 0] + self.grade[3, 1] + self.grade[3, 2]) / 3 \
            > (self.grade[4, 0] + self.grade[4, 1] + self.grade[4, 2]) / 3

        return "The given student has greater average:",greateravg


Stu0=Student("Jawad",59)
Stu1=Student("Danish",50)
Stu2=Student("Sharjeel",60)
Stu3=Student("Zubair",40)
Stu4=Student("Anas",52)
for i in range(5):
    print(Stu0.info(),Stu1.info(),Stu2.info(),Stu3.info(),Stu4.info())
    INP=int(input("Enter Roll no to approach student tests:"))
    if INP==Stu0.RollNo:
        s0 = Grade()
        print("The Row showed the three Tests and the Coloumn Showed the 5 students:\n", s0.display_grade())
        for i in range(3):
            teacher = int(input("Enter Marks in specific test of Student1:"))
            s0.take_input(teacher)
            print(s0.display_grade())
        print("The average of three tests is:",s0.takeAvg())


    if INP==Stu1.RollNo:

        s0 = Grade()
        print("The Row showed the three Tests and the Coloumn Showed the 5 students:\n", s0.display_grade())
        for i in range(3):
            teacher = int(input("Enter Marks in specific test of Student2:"))
            s0.take_input(teacher)
            print(s0.display_grade())
        print("The average of tests is:",s0.takeAvg())



    if INP==Stu2.RollNo:
        s0 = Grade()
        print("The Row showed the three Tests and the Coloumn Showed the 5 students:\n", s0.display_grade())
        for i in range(3):
            teacher = int(input("Enter Marks of Student3:"))
            s0.take_input(teacher)
            print(s0.display_grade())
        print("The average of tests is:", s0.takeAvg())
    if INP==Stu3.RollNo:
        s0 = Grade()
        print("The Row showed the three Tests and the Coloumn Showed the 5 students:\n", s0.display_grade())
        for i in range(3):
            teacher = int(input("Enter Marks of Student4:"))
            s0.take_input(teacher)
            print(s0.display_grade())
        print("The average of tests is:",s0.takeAvg())
    if INP==Stu4.RollNo:
        s0 = Grade()
        print("The Row showed the three Tests and the Coloumn Showed the 5 students:\n", s0.display_grade())
        for i in range(3):
            teacher = int(input("Enter Marks of Student5:"))
            s0.take_input(teacher)
            print(s0.display_grade())
        print("The average of tests is:", s0.takeAvg())

classavg=input("Write whole_class_avg to take whole class average:")
if classavg=="whole_class_avg":
    wholeclassaverage=Grade()
    print(wholeclassaverage.take_avg_wholeclass())
highestavg=input("Write highest_avg to take whole class average:")
if highestavg=="whole_class_avg":
    highestavg=Grade()
    print(highestavg.highestAvg())