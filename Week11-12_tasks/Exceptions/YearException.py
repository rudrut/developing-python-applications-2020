year1 = 0000
year2 = 0000

yearSum = 0

def sumOfYears(x, y):
    return x + y
    
while yearSum == 0:
    try:
        print("Enter year:")
        year1 = int(input())
        print("Enter another year:")
        year2 = input()
        yearSum = sumOfYears(year1, year2)
        print(yearSum)
    except ValueError as e: # Will be raised if the user presses Enter immediately.
        print("No integer from user. Please enter whole numbers.", e)
    except TypeError as f: # Will be raised because int and str can't be summed.
        print("Both numbers must be integers!", f)