#Import math library for some tasks:
import math

#Task 1
#oneFromMillion = 999999
#fivePointFive = 5.55555555555
#letter = 'x'
#city = "Kokkola"
#overTwo = 2.33
#ten = 10
#threeHundred = 300
#nineBillions = 9000000000
#threeBillions = 3000000000
#print(type(oneFromMillion))
#print(type(fivePointFive))
#print(type(letter))
#print(type(city))
#print(type(overTwo))
#print(type(ten))
#print(type(threeHundred))
#print(type(nineBillions))
#print(type(threeBillions))

#--------------------------------------

# Task 2
#v = float(input("Give voltage: "))
#i = float(input("Give current: "))
#r = v / i
#print("Resistance is: " + str(r))

#--------------------------------------

# Task 3
#speed = int(input("Give speed in km/h: "))
#distance = float(input("Give distance in kilometers: "))
#timeInHours = distance / speed
#hoursAndMinutes = math.modf(timeInHours)
#if (timeInHours % 1) == 0:
#    print("Amount of time in hours is: " + str(round(timeInHours)))
#else:
#    print("Amount of time in hours and minutes is: " + str(math.floor(timeInHours)) + " hours, " + str(round(hoursAndMinutes[0] * 60)) + " minutes.")

#--------------------------------------

# Task 4
#weightInKilograms = int(input("Give weight in kilograms: "))
#height = float(input("Give height in meters and centimeters, separated by a dot: "))
#bodyMassIndex = weightInKilograms / height**2
#print("Your BMI is: " + str(round(bodyMassIndex, 2)))

#--------------------------------------

#Task 5
#I use XE Currency Converter, which can be found at xe.com

#dollars = float(input("Give dollars. If it's not a whole number, use a dot for separating dollars and cents: "))
#euros = round(0.915356 * dollars, 2)
#print("Dollars to euros: " + str(euros))

#--------------------------------------

#Task 6
#seconds = int(input("Give seconds: "))
#minutes = seconds / 60
#hours = minutes / 60
#print(str(math.floor(hours)) + " hours, " + str(round(minutes - (math.floor(hours) * 60))) + " minutes, " + str(seconds - (math.floor(minutes) * 60)) + " seconds")

#--------------------------------------

#Task 7
#euros = float(input("Give euros. Must be a positive number: "))
#
#fiveEuroNote = euros / 5
#tenEuroNote = euros / 10
#twentyEuroNote = euros / 20
#fiftyEuroNote = euros / 50
#hundredEuroNote = euros / 100
#twoHundredEuroNote = euros / 200
#fiveHundredEuroNote = euros / 500

#print("Amount of euros: " + str(math.floor(euros)) + ".")
#print("Five euro notes: " + str(math.floor(fiveEuroNote)))
#print("Ten euro notes: " + str(math.floor(tenEuroNote)))
#print("Twenty euro notes: " + str(math.floor(twentyEuroNote)))
#print("Fifty euro notes: " + str(math.floor(fiftyEuroNote)))
#print("Hundred euro notes: " + str(math.floor(hundredEuroNote)))
#print("Two hundred euro notes: " + str(math.floor(twoHundredEuroNote)))
#print("Five hundred euro notes: " + str(math.floor(fiveHundredEuroNote)))