
# Qno2:Write python code to develop the classes shown in the following UML diagrams.



# HERE I MADE A CLASS NAME ACCOUNT HAVING TWO PRIVATE ATTRIBUTES
class Account:
    def __init__(self,accountNumber,balance=0):
        self.__accountNumber=accountNumber
        self.__balance=balance
        if not isinstance(balance, int):
            raise TypeError("Balance must be set to an integer")
        if not isinstance(accountNumber, int):
            raise TypeError("Account Number must be set to an integer")
    def getAccountNumber(self):
        return self.__accountNumber
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance=balance
        if not isinstance(balance, int):
            raise TypeError("Balance must be set to an integer")
    def credit(self,amount):
        self.__balance=amount
        if not isinstance(amount, int):
            raise TypeError("Balance must be set to an integer")
    def debit(self,amount):
        self.__balance=amount
        if not isinstance(amount, int):
            raise TypeError("Balance must be set to an integer")


# HERE I MAKE A CLASS NAME POINT WHICH HAVE TWO ATTRIBUTES
class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        self.__x=x
    def setY(self,y):
        self.__y=y
    def setXY(self,x,y):
        self.__x=x
        self.__y=y
    def getMagnitude(self):
        return (self.__x * self.__y)


# HERE I MAKE CLASS OF TIME WHICH HAVE THREE PARAMETER MIN,SEC,HOUR
class Time:
    def __init__(self,h,m,s):
        self.__hours=h
        self.__minutes=m
        self.__seconds=s
    def getHour(self):
        return self.__hours
    def getMinutes(self):
        return self.__minutes
    def getSeconds(self):
        return self.__seconds
    def setHour(self,h):
        self.__hours=h
    def setMinutes(self,m):
        self.__minutes=m
    def setSeconds(self,s):
        self.__seconds=s
    def setTime(self,h,m,s):
        self.__hours=h
        self.__minutes=m
        self.__seconds=s
    def getTime(self):
        print("The time given by the user is:",self.__hours,":",self.__minutes,":",self.__seconds)

A=Account(59,5000)
print("The balance in the account of user is :",A.getBalance())

P=Point(5,8)
print("The magnitude of two number is:",P.getMagnitude())
t=Time(3,40,50)
t.getTime()
