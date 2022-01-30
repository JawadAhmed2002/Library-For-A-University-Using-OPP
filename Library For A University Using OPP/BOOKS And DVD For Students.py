# Define classes Book, Author and DVD.

class Books:
    TotalNoOfBooks=0
    def __init__(self,author,BookNumber,Title):
        self.author=author
        self.BookNumber=BookNumber
        self.Title=Title

        Books.TotalNoOfBooks+=1

    def getAuthor(self):
        return self.author
    def getBookNumber(self):
        return self.BookNumber
    def getTitle(self):
        return self.Title
    def getCountBooks(self):
        return self.CountBooks

    def setAuthor(self,author):
        self.author=author
    def setBookNumber(self,BookNumber):
        self.BookNumber=BookNumber
    def setTitle(self,Title):
        self.Title=Title
    def setCountBooks(self,CountBooks):
        self.CountBooks=CountBooks
    def DisplayAllInfo(self):
        print("Book Title is:",self.Title,"Book Author is:",self.author,"Book Reg Number is:",self.BookNumber)


class DVD:
    TotalNoDvD=0
    def __init__(self,Author,RegionCode,Subject):
        self.RegionCode=RegionCode
        self.Author=Author
        self.Subject=Subject

        DVD.TotalNoDvD+=1
    def getRegionCode(self):
        return self.RegionCode
    def getAuthor(self):
        return self.Author
    def getSubject(self):
        return self.Subject
    def getCountDvD(self):
        return self.CountDvD

    def setRegionCode(self,RegionCode):
        self.RegionCode=RegionCode
    def setAuthor(self,Author):
        self.Author=Author
    def setSubject(self,Subject):
        self.Subject=Subject
    def setCountDvD(self,CountDvD):
        self.CountDvD=CountDvD
    def DisplayAllInfo(self):
        print("DVD Title is:",self.Subject,"DVD Author is:",self.Author,"DVD Reg Number is:",self.RegionCode)



class Author:
    def __init__(self,Name,ContactInfo):
        self.Name=Name
        self.ContactInfo=ContactInfo
    def getName(self):
        return self.Name
    def getContactInfo(self):
        return self.ContactInfo

    def setName(self,Name):
        self.Name=Name
    def setContactInfo(self,ContactInfo):
        self.ContactInfo=ContactInfo


ListOfBooks=[]
ListOfDvD=[]

ListOfBooks.append( Books("paul coelho",1,"Alchemist") )
ListOfBooks.append( Books("Plato",2,"Gorgias") )
ListOfBooks.append( Books("Saint Augustain",3,"Confession") )
ListOfBooks.append( Books("Imam Ghazali",4,"Sharghasht-e-Ghazali") )
ListOfBooks.append( Books("Elif Shafak",5,"Forty Rules Of Love") )
for obj in ListOfBooks:
    obj.DisplayAllInfo()
print("Total Number Of Books Stored Are:",Books.TotalNoOfBooks,'\n')


ListOfDvD.append( DVD("paul coelho",1,"Alchemist") )
ListOfDvD.append( DVD("Plato",2,"Gorgias") )
ListOfDvD.append( DVD("Saint Augustain",3,"Confession") )
ListOfDvD.append( DVD("Imam Ghazali",4,"Sharghasht-e-Ghazali") )
ListOfDvD.append( DVD("Elif Shafak",5,"Forty Rules Of Love") )

for obj in ListOfDvD:
    obj.DisplayAllInfo()
print("Total Number Of Books Stored Are:",DVD.TotalNoDvD)
