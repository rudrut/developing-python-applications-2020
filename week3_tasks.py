# Task 1
#userValue = int(input("Give value: "))
#if userValue > 100:
#    print("Value is over 100!")
#else:
#    print("Value is not over 100!")

#------------------------------------------

# Task 2
#userWeekDayNumber = int(input("Give a weekday number: "))
#if userWeekDayNumber == 1:
#    print("Monday")
#elif userWeekDayNumber == 2:
#    print("Tuesday")
#elif userWeekDayNumber == 3:
#    print("Wednesday")
#elif userWeekDayNumber == 4:
#    print("Thursday")
#elif userWeekDayNumber == 5:
#    print("Friday")
#elif userWeekDayNumber == 6:
#    print("Saturday")
#elif userWeekDayNumber == 7:
#    print("Sunday")
#else:
#    print("Weekday not found!")

#------------------------------------------

# Task 3
#weightInKilograms = int(input("Give weight in kilograms: "))
#height = float(input("Give height in meters and centimeters, separated by a dot: "))
#bodyMassIndex = weightInKilograms / height**2
#print("Your BMI is: " + str(round(bodyMassIndex, 2)))
#if bodyMassIndex > 0 and bodyMassIndex < 16:
#    print("Severe thinness!")
#elif bodyMassIndex >= 16 and bodyMassIndex < 17:
#    print("Moderate thinness!")
#elif bodyMassIndex >= 17 and bodyMassIndex < 18.5:
#    print("Mild thinness!")
#elif bodyMassIndex >= 18.5 and bodyMassIndex < 25:
#    print("Normal range!")
#elif bodyMassIndex >= 25 and bodyMassIndex < 30:
#    print("Pre-obese!")
#elif bodyMassIndex >= 30 and bodyMassIndex < 35:
#    print("Obese class I")
#elif bodyMassIndex >= 35 and bodyMassIndex < 40:
#    print("Obese class II")
#elif bodyMassIndex >= 40:
#    print("Obese class III")
#else:
#    print("Invalid value!")

#------------------------------------------

# Task 4
#userMonthNumber = int(input("Give a month number: "))
#if userMonthNumber == 1:
#    print("January, Days in a month: " + str(31))
#elif userMonthNumber == 2:
#    print("February, Days in a month: " + str(28) + " (and 29 in leap years.)")
#elif userMonthNumber == 3:
#    print("March, Days in a month: " + str(31))
#elif userMonthNumber == 4:
#    print("April, Days in a month: " + str(30))
#elif userMonthNumber == 5:
#    print("May, Days in a month: " + str(31))
#elif userMonthNumber == 6:
#    print("June, Days in a month: " + str(30))
#elif userMonthNumber == 7:
#    print("July, Days in a month: " + str(31))
#elif userMonthNumber == 8:
#    print("August, Days in a month: " + str(31))
#elif userMonthNumber == 9:
#    print("September, Days in a month: " + str(30))
#elif userMonthNumber == 10:
#    print("October, Days in a month: " + str(31))
#elif userMonthNumber == 11:
#    print("November, Days in a month: " + str(30))
#elif userMonthNumber == 12:
#    print("December,Days in a month: " + str(31))
#else:
#    print("Invalid value!")

#------------------------------------------

# Task 5
#a = float(input("Give the length of triangle's first side: "))
#b = float(input("Give the length of triangle's second side: "))
#c = float(input("Give the length of triangle's third side: "))
#
#if a == b == c:
#    print("Triangle is equilateral!")
#elif a == b or b == c or c == a:
#    print("Triangle is isosceles!")
#else:
#    print("Triangle is scalene!")
#
#if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or #c**2 + a**2 == b**2:
#    print("Triangle is right angled!")
#else:
#    print("Triangle is oblique!")

#------------------------------------------

#Task 6
#a = 2
#b = 1
#c = 2

# Solution 1
#if a > b and a > c:
#    print("a is biggest")
#
#if b > a and b > c:
#    print("b is biggest")
#
#if c > b and c > a:
#    print("c is biggest")
#
#if a == b == c:
#    print("All values are the same.")
#
#if b > c and b == a:
#    print("a and b are the biggest values")
#
#if c > a and c == b:
#    print("b and c are the biggest values")
#
#if c > b and c == a:
#    print("a and c are the biggest values")

# Solution 2, and keyword heavily used
#if a == b and a == c:
#    print("All values are the same.")
#elif b > c and b == a:
#    print("a and b are the biggest values")
#elif c > a and c == b:
#    print("b and c are the biggest values")
#elif c > b and c == a:
#    print("a and c are the biggest values")
#elif a > b and a > c:
#    print("a is biggest")
#elif b > a and b > c:
#    print("b is biggest")
#elif c > b and c > a:
#    print("c is biggest")
#else:
#    print("Something else!")

#Solution 3, lots of nesting if-statements
#if a == b == c:
#    print("All values are the same.")
#elif a > b:
#    if a == c:
#        print("a and c are the biggest")
#    elif a < c:
#        print("c is the biggest")
#    else:
#        print("a is the biggest")
#elif a > c:
#    if a == b:
#        print("a and b are the biggest")
#    elif a < b:
#        print("b is the biggest")
#    else:
#        print("a is biggest")
#elif b > a:
#    if b == c:
#        print("b and c are the biggest")
#    elif b < c:
#        print("c is biggest")
#    else:
#        print("b is biggest")
#else:
#    print("Something else!")