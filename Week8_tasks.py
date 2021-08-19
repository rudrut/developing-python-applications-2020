#----------------------------------------------------------------

#Task 1
class Author:

    def __init__(self, firstName, lastName, biography):
        self.firstName = firstName
        self.lastName = lastName
        self.biography = biography
        self.listOfBooks = []

    @property
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
    
    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName
    
    @property
    def biography(self):
        return self._biography
    
    @biography.setter
    def biography(self, newBio):
        self._biography = newBio

    def writeBook(self, book):
        self.listOfBooks.append(book)
    
    def getBooks(self):
        if self.listOfBooks == []:
            return "No books written yet."
        else:
            return "Books written: " + str(self.listOfBooks)
        
    def getFullInfo(self):
        if self.listOfBooks == []:
            return "Author: " + self.fullName + '\n' + "Biography: " + self.biography + '\n' + "They haven't finished a book yet."
        else:
            return "Author: " + self.fullName + '\n' + "Biography: " + self.biography + '\n' + "Here is a collection of their work:" + '\n' + str(self.listOfBooks)

class Book:

    def __init__(self, name, author, releaseYear, genre, language, pageCount):
        self.name = name
        self.author = author
        self.releaseYear = releaseYear
        self.genre = genre
        self.language = language
        self.pageCount = pageCount
    
    def getFullInfo(self):
        return "Name: " + self.name + '\n' + "Author: " + self.author + '\n' + "Release year: " + str(self.releaseYear) + '\n' + "Genre: " + self.genre + '\n' + "Language: " + self.language + '\n' + "Page count: " + str(self.pageCount)
#----------------------------------------------------------------

#Task 2

class Apartment:
    
    def __init__(self, address, size, condition, yearOfConstruction):
        self.address = address
        self.size = size
        self.condition = condition
        self.roomAmount = 3
        self.yearOfConstruction = yearOfConstruction
        self.obj_kitchen = Kitchen()
        self.obj_bedroom = Bedroom()
        self.obj_bathroom = Bathroom()

    def kitchenInfo(self):
        return self.obj_kitchen.getAllInfo()
    
    def bedroomInfo(self):
        return self.obj_bedroom.getAllInfo()

    def bathroomInfo(self):
        return self.obj_bathroom.getAllInfo()
    
    def getAllInfo(self):
        return "Address: " + self.address + '\n' + "Size: " + str(self.size) + ' m2\n' + "Condition: " + self.condition + '\n' + "Amount of rooms: " + str(self.roomAmount) + '\n' + "Year of construction: " + str(self.yearOfConstruction)

class Kitchen:
    
    def __init__(self):
        self.freezerIncluded = True
        self.fridgeIncluded = True
        self.stoveIncluded = True
        self.containsWindow = True

    def getAllInfo(self):
        return "Freezer: " + str(self.freezerIncluded) + '\n' + "Fridge: " + str(self.fridgeIncluded) + '\n' + "Stove: " + str(self.stoveIncluded) + '\n' + "Windows: " + str(self.containsWindow)

class Bedroom:

    def __init__(self):
        self.bedIncluded = True
        self.containsWindow = True

    def getAllInfo(self):
        return "Bed: " + str(self.bedIncluded) + '\n' + "Windows: " + str(self.containsWindow)

class Bathroom:
    
    def __init__(self):
        self.containsToilet = True
        self.containsShower = True
        self.containsWasher = True

    def getAllInfo(self):
        return "Toilet: " + str(self.containsToilet) + '\n' + "Shower: " + str(self.containsShower) + '\n' + "Washing Machine: " + str(self.containsWasher)

