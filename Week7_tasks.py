#----------------------------------------------------------------

#Task 1
#class Complex:
#    def __init__(self, real = 0, imaginary = 0):
#        self.real = real
#        self.imaginary = imaginary
#
#    def getReal(self):
#        return self.real
#    
#    def getImaginary(self):
#        return self.imaginary
#
#    def setReal(self, a):
#        self.real = a
#    
#    def setImaginary(self, b):
#        self.imaginary = b
#
#    def __str__(self):
#        return "{} {} {}i".format(self.real, '+' if self.imaginary >= 0 else '-', abs(self.imaginary))
#
#    def __add__(self, other):
#        return Complex(self.real + other.real, self.imaginary + other.imaginary)
#    
#    def __sub__(self, other):
#        return (self.real - other.real, self.imaginary - other.imaginary)
#
#    def conjugate(self):
#        return Complex(self.real, -self.imaginary)
#
#    def __neg__(self):
#        return Complex(-self.real, -self.imaginary)
#
#    def __mul__(self, other):
#        real = self.real * other.real - self.imaginary * other.imaginary
#        imaginary = self.imaginary * other.real + self.real * other.imaginary
#        return Complex(real, imaginary)
#
#    def __truediv__(self, other):
#        conjugate = other.conjugate()
#
#        den = other * conjugate
#        den = den.real
#
#        number = self / conjugate
#        return Complex(number.real/den, number.imaginary/den)
#----------------------------------------------------------------

#Task 2
#class Clock:
#    def __init__(self, hours, minutes, seconds):
#        self.hours = hours
#        self.minutes = minutes
#        self.seconds = seconds
#
#    def __str__(self):
#        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours, self.minutes, self.seconds)
#
#    def tick(self):
#        self.seconds += 1
#        if self.seconds == 60:
#            self.seconds = 0
#            self.minutes += 1
#        
#        if self.minutes == 60:
#            self.minutes = 0
#            self.hours += 1
#        
#        if self.hours == 24:
#            self.hours = 0

#class AlarmClock(Clock):

#    def __init__(self, hours, minutes, seconds):
#        super().__init__(hours, minutes, seconds)
#
#    def soundAlarm(self, alarmHour, alarmMinute):
#        if self.hours == alarmHour and self.minutes == alarmMinute and self.seconds == 0:
#            print("AAAAALLLLLEEEEERRRRRRTTTTTT")

#----------------------------------------------------------------

#Task 3
#class Bird:
#    def __init__(self, name, amountOfEggs = 1):
#        self.name = name
#        if amountOfEggs < 1:
#            self.amountOfEggs = 1
#        elif amountOfEggs > 10:
#            self.amountOfEggs = 10
#        else:
#            self.amountOfEggs = amountOfEggs
#            
#    def getName(self):
#        return self.name
#
#    def setName(self, desiredName):
#        self.name = desiredName
#
#    def getAmountOfEggs(self):
#        return self.amountOfEggs
#
#    def setAmountOfEggs(self, desiredAmount):
#        if desiredAmount >= 1 and desiredAmount <= 10:
#            self.amountOfEggs = desiredAmount
#    
#    def __str__(self):
#        return "Bird's name is: " + str(self.name) + ", and it has " + str(self.amountOfEggs) + " egg(s)."
#
#class Migratory(Bird):
#    def __init__(self, name, amountOfEggs, country, month):
#        super().__init__(name, amountOfEggs)
#
#        if len(country) < 5 and len(country) > 20:
#            print("Please specify country with capital first letter and with 5 to 20 characters!")
#        
#        elif country[0].isupper() == False:
#            self.country = country.capitalize()
#        else:
#            self.country = country
#
#        if month < 1:
#            self.month = 1
#        elif month > 12:
#            self.month = 12
#        else:
#            self.month = month
#
#    def getCountry(self):
#        return self.country
#    
#    def getMonth(self):
#        return self.month
#
#    def setCountry(self, desiredCountry):
#        if (len(desiredCountry) >= 5 and len(desiredCountry) <= 20 and desiredCountry[0].isupper()):
#            self.country = desiredCountry
#    
#    def setMonth(self, desiredMonth):
#        if (desiredMonth >= 1 and desiredMonth <= 12):
#            self.month = desiredMonth
#    
#    def __str__(self):
#        return "Migratory is called " + str(self.name) + ", and it has " + str(self.amountOfEggs) + " egg(s). It's destination is " + str(self.country) + " and it migrates there in month " + str(self.month) + '.'
#----------------------------------------------------------------

#Bonus Task 1

#----------------------------------------------------------------

#Bonus Task 2

#----------------------------------------------------------------