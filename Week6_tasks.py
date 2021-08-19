import math
#----------------------------------------------------------------

# Task 1
def averageOfTwoInts(a, b):
    average = (a + b) / 2
    return round(average, 2)
#----------------------------------------------------------------

# Task 2
def averageOfFourFloats(a,b,c,d):
    average = (a+b+c+d) / 4
    return round(average, 2)
#----------------------------------------------------------------

# Task 3
def sumOfArray(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
#----------------------------------------------------------------

# Task 4
def factorialOf(n):
    factorial = 1
    if (n >= 1):
        for i in range(1, n + 1):
            factorial *= i
    return factorial
#----------------------------------------------------------------

# Task 5
def biggestOfThreeInts(a,b,c):
    values = [a,b,c]
    return max(values)
#----------------------------------------------------------------

# Task 6
def bodyMassIndex(weightInKilograms, heightInCentimeters):
    bodyMassIndex = weightInKilograms / heightInCentimeters**2
    bodyMassIndex *= 10000
    return bodyMassIndex
#----------------------------------------------------------------

# Task 7
def biggestOfFiveInts(a,b,c,d,e):
    values = [a,b,c,d,e]
    return max(values)
#----------------------------------------------------------------

# Task 8
def amountOfCombinations(n, k):
    comboAmount = 0
    comboAmount = factorialOf(n) / (factorialOf(k) * (factorialOf(n - k)))
    return comboAmount
#----------------------------------------------------------------

# Task 9
def standardDeviation(array):
    sum = sumOfArray(array)
    average = sum / len(array)

    sumOfSquaredValues = 0

    for i in range(len(array)):
        sumOfSquaredValues += math.pow(array[i] - average, 2)

    standardDeviation = math.sqrt(sumOfSquaredValues / len(array))

    return standardDeviation
#----------------------------------------------------------------

# Task 10
def searchFromArray(value, array):

    for i in range(len(array)):
        if array[i] == value:
            return True
    return False
#----------------------------------------------------------------

# Task 11
def squareRootOfTwo():
    x = 2
    y = 1
    e = 0.0000000000001
    n = x

    while(x - y > e): 
        x = (x + y)/2
        y = n / x 
      
    return x
#----------------------------------------------------------------

# Task 12
def eOfNeper():
    n = 1
    e = 1
    while n < 20:
        e += 1 / factorialOf(n)
        n += 1
    return round(e, 7)
#----------------------------------------------------------------

# Task 13
def cosInRadians(x):

    temp = 1
    temp2 = 0
    for i in range(2, 40, 4):
        temp -= x**i / factorialOf(i)

    for j in range(4, 44, 4):
        temp2 += x**j / factorialOf(j)

    cos = temp + temp2

    return cos

def sinInRadians(x):

    temp = x
    temp2 = 0
    for i in range(3, 90, 4):
        temp -= x**i / factorialOf(i)

    for j in range(5, 94, 4):
        temp2 += x**j / factorialOf(j)

    sin = temp + temp2

    return sin
#----------------------------------------------------------------

# Bonus Task 1
def arraySorter(array):
    n = len(array)
    arr = array

    for i in range(n):
        min = i
        for j in range(i+1, n):
            if (arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr
#----------------------------------------------------------------

# Bonus Task 2
def arrayMultiplier(array1,array2):
    arr1 = len(array1)
    arr2 = len(array2)

    if arr1 > arr2:
        while arr2 < arr1:
            array2.append(0)
            arr2 += 1

    if arr1 < arr2:
        while arr1 < arr2:
            array1.append(0)
            arr1 += 1

    x = 0
    y = 0

    resultArray = []

    for i in range(arr1):
        x = array1[i]
        y = array2[i]
        resultArray.append(x * y)
    return resultArray
#----------------------------------------------------------------