# Necessary imports
import random
import math
#-------------------------------------------------------------
# I've used sum and index variables in the first 3 tasks.

sum = 0
index = 0

# Task 1

#for x in range(6):
#    sum += x
#    print(sum)

#while(index < 5):
#    index += 1
#    sum += index
#    print(sum)

#-------------------------------------------------------------

# Task 2
#
#for x in range(2, 41, 2):
#    sum += x
#    print(sum)
#
#while (index < 41):
#    if (index % 2 == 0):
#        sum += index
#        print(sum)
#    index += 1
#
#-------------------------------------------------------------

# Task 3

#for x in range(5, 101, 5):
#    sum += x
#    print(sum)

#while (index < 101):
#    if (index % 5 == 0):
#        sum += index
#        print(sum)
#    index += 1
#
#-------------------------------------------------------------

# Task 4

#for x in range(101):
#    y = random.randint(1, 6)
#    print(str(x) + " throw: " + str(y))
#
#-------------------------------------------------------------

# Task 5

#start = "Welcome to Account Manager!"
#choice1 = "Type 'end' to stop using Account Manager."
#choice2 = "Type 'check' to view your account balance."
#choice3 = "Type 'withdraw' to subtract money from your account."
#choice4 = "Type 'deposit' to make a deposit and add money to your account"
#ending = "Thank you for using Account Manager! Have a nice day!"
#
#accountBalance = 0.00
#
#userInput = ""
#print(start)
#while (userInput != "end"):
#    print(choice1)
#    print(choice2)
#    print(choice3)
#    print(choice4)
#    userInput = input("")
#    if (userInput == "end"):
#        print(ending)
#        break
#    elif (userInput == "check"):
#        print("Your account balance is: " + str(round(accountBalance, 2)))
#    elif (userInput == "withdraw"):
#        withdrawAmount = float(input("How much are you willing to withdraw?: "))
#        if (accountBalance - withdrawAmount >= 0):
#            accountBalance -= round(withdrawAmount, 2)
#            print("Your account balance is: " + str(round(accountBalance, 2)))
#        else:
#            print("Transaction denied! Not enough money in account or command not understood!")
#    elif (userInput == "deposit"):
#        depositAmount = float(input("How much would you like to deposit?: "))
#        accountBalance += round(depositAmount, 2)
#        print("Your account balance is: " + str(round(accountBalance, 2)))
#    else:
#        print("Please type one of the choices or end session!")
#    
#-------------------------------------------------------------

# Task 6
#
#a = 3
#b = 4
#c = 9
#d = 5
#y = 0.0
#x = -5.0
#
#while True:
#    y = a * math.pow(x, 3) - b * math.pow(x, 2) + c * x + d
#    if y > -0.001 and y < 0.001:
#        break
#    x += 0.0001
#
#print("One of the roots is: " + str(x))
#-------------------------------------------------------------

# Task 7

#rows = int(input("Give amount of rows: "))
#start = 0
#for x in range(start, rows):
#    start += 1
#    for x in range(0, start):
#        print("m", end="")
#    print()
#
#-------------------------------------------------------------

# Task 8

#n = int(input("Give a value for n: "))
#factorial = 1
#if (n >= 1):
#    for i in range(1, n + 1):
#        factorial *= i
#print("Factorial of " + str(n) + " is: " + str(factorial))
#
#-------------------------------------------------------------

# Task 9

#base = float(input("For base number, give either a real or whole number: "))
#exp = int(input("Give a whole number for exponent: "))
#product = base * base
#print("When base is " + str(base) + "...")
#for x in range(1, exp):
#    print(product)
#    product *= base

#-------------------------------------------------------------