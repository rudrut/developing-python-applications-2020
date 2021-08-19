# Necessary imports
import random
import math
#-------------------------------------------------------------

# Task 1

#sum = 0.0
#values = []
#for i in range(30):
#    values.append(random.randint(0, 100))
#    sum += values[i]
#
#print("The list of values: " + str(values))
#average = sum / 30
#print("The sum: " + str(sum))
#print("The average: " + str(round(average, 2)))

#-------------------------------------------------------------

# Task 2

#values = []
#for i in range(30):
#    values.append(random.randint(0, 100))
#
#print("The list of values: " + str(values))
#
#max = values[0]
#for i in range(1, 30):
#    if values[i] > max:
#        max = values[i]
#print("Largest value is: " + str(max))

#-------------------------------------------------------------

# Task 3

#values = []
#for i in range(30):
#    values.append(random.randint(0, 100))
#
#print("The list of values: " + str(values))
#
#wantedNumber = 50
#result = "Wanted number not found."
#for i in range(1, 30):
#    if values[i] == wantedNumber:
#        result = "Found in index " + str(i)
#        break
#print(result)

#-------------------------------------------------------------

# Task 4

#firstValues = []
#secondValues = []
#
#for i in range(10):
#    firstValues.append(random.randint(0, 10))
#for j in range(10):
#    secondValues.append(random.randint(0, 10))
#print("The first array: " + str(firstValues))
#print("The second array: " + str(secondValues))
#
#sumValues = []
#for k in range(10):
#    sumValues.append(firstValues[k] + secondValues[k])
#print("The summed values of two arrays: " + str(sumValues))

#-------------------------------------------------------------

# Task 5

#lottoRow = []
#for i in range(7):
#    lottoRow.append(random.randint(1, 40))
#
#for j in range(len(lottoRow)):
#    for k in range(j + 1, len(lottoRow)):
#        if (lottoRow[j] > lottoRow[k]):
#            temp = lottoRow[j]
#            lottoRow[j] = lottoRow[k]
#            lottoRow[k] = temp
#print("Your lottorow is: " + str(lottoRow))

#-------------------------------------------------------------

# Task 6

#testList = [1, 2, 3, 4, 5]
#print(testList)
## Here I will append the list and add a number to the end of the list:
#testList.append(10)
#print(testList)
#
## list.extend can apparently be used with strings, tuples and lists for example. As in with object that can be iterated upon.
#anotherList = ["Matti", "Juha", "Helmi", "Aatu"]
#anotherList.extend(anotherList)
#print(anotherList)
#
## Here I will insert an item to a specified position as in, in front of a specified index.
#someList = [1,2,3,4,5,6,7,8,9]
#someList.insert(5, 5000)
#print(someList)
#
## How about removing an item?
#yetAnotherList = [1,2,3,4,5,6,7,8,9,0]
#yetAnotherList.remove(1)
#print(yetAnotherList)
#
## Or how about removing a specific value from a list? If not specified, the lst item will be removed.
#stopList = [1,2,3,4,5,6,7,8,9,0]
#print(stopList.pop())
#
## I could just wipe the entire list!
#oneMoreList = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
#print(oneMoreList)
#oneMoreList.clear()
#print(oneMoreList)
#
## Corresponding index when seeking a value from a list? We can limit the search.
#moreTestLists = [1,2,3,4,5,6,7,8,9,0]
#print(str(moreTestLists.index(2)))
#
## What if we want to know how many times an item can be found in a list?
#listCounter = [1,1,1,1,1,1,1,1,1,0]
#print(listCounter.count(0))
#
## list.sort() sorts the list automatically. Apparently it's possible to customize the sorting rules.
#FinalList = [345345634,345345634,5345634543,532432,41234,2543,645,67457,54856,8]
#FinalLista.sort()
#print(FinalLista)
#
##list.reverse() just puts the values in reverse order
#upsideDownList = [1,2,3,4,5,6,7,8,9]
#upsideDownList.reverse()
#print(upsideDownList)
#
##list.copy() makes a shallow copy of a list
#
#firstList = [1,2,3,4,5]
#secondList = firstList.copy()
#print(secondList)

#-------------------------------------------------------------

# Task 7

#englishToSwedish = [["to graduate","utexamineras"], ["also","även"], ["in cooperation","i samarbete"], ["to develop","utveckla"], ["a data system","ett datasystem"], ["to make better","förbättra"],
#                    ["a client company","ett kundföretag"], ["operational requirements","verksamhetsförutsättningar"], ["possibilities","möjligheter"], ["business","affärsverksamhet"], ["education",#"utbildning"], ["in tasks","i uppgifter"], ["in the industry","i branschen"], ["programming","programmering"], ["data administration","dataförvaltning"], ["services","tjänster"]]
#
#for i in range(len(englishToSwedish)):
#    print("English --> Swedish: " + str(englishToSwedish[i]))

#-------------------------------------------------------------

#Task 8

#myArray = []
#sum = 0
#
#for i in range(20):
#    myArray.append(random.randint(1, 9))
#    sum += myArray[i]
#average = sum / len(myArray)
#print(myArray)
#
#print()
#
#print("The sum of the values in the array is: " + str(sum))
#print("The average of the values in the array is: " + str(round(average, 2)))
#
#print()
#
#sumOfSquaredValues = 0
#
#for j in range(len(myArray)):
#    sumOfSquaredValues += math.pow(myArray[j] - average, 2)
#
#standardDeviation = math.sqrt(sumOfSquaredValues / len(myArray))
#print("Standard deviation is: " + str(standardDeviation))

#-------------------------------------------------------------

#Task 9

#mathGrades = []
#englishGrades = []
#
#mathSum = 0
#englishSum = 0
#
#varianceSumMath = 0
#varianceSumEnglish = 0
#
#for i in range(10):
#    mathGrades.append(random.randint(0, 5))
#    mathSum += mathGrades[i]
#    varianceSumMath += math.pow(mathGrades[i], 2)
#mathAverage = mathSum / len(mathGrades)
#
#print("Here are the Math grades: " + str(mathGrades))
#
#for j in range(10):
#    englishGrades.append(random.randint(0, 5))
#    englishSum += englishGrades[j]
#    varianceSumEnglish += math.pow(englishGrades[j], 2)
#englishAverage = englishSum / len(englishGrades)
#
#print("Here are the English grades: " + str(englishGrades))
#
#print("Sum of Math grades is: " + str(mathSum))
#print("Sum of English grades is: " + str(englishSum))
#
#print()
#
#print("Sum of SQUARED Math grades is: " + str(varianceSumMath))
#print("Sum of SQUARED English grades is: " + str(varianceSumEnglish))
#
#print()
#
#print("Mean(or average) of Math grades is: " + str(round(mathAverage, 2)))
#print("Mean(or average) of English grades is: " + str(round(englishAverage, 2)))
#
#print()
#
#varianceMath = (varianceSumMath / len(mathGrades)) - math.pow(mathAverage, 2)
#varianceEnglish = (varianceSumEnglish / len(englishGrades)) - math.pow(englishAverage, 2)
#
#print("Variance of Math is: " + str(varianceMath))
#print("Variance of English is: " + str(varianceEnglish))
#
#print()
#
#MathAndEnglishGradesMultiplied = []
#covarSum = 0
#
#for k in range(10):
#    MathAndEnglishGradesMultiplied.append(mathGrades[k] * englishGrades[k])
#    covarSum += MathAndEnglishGradesMultiplied[k]
#
#print("Here is the array with Math and English grades multiplied: " + str(MathAndEnglishGradesMultiplied))
#print("And here is the sum of said array values: " + str(covarSum))
#
#print()
#
#covariance = (covarSum / 10) - (mathAverage * englishAverage)
#print("Covariance between the two arrays is: " + str(covariance))
#
#correlation = covariance / (math.sqrt(varianceMath) * math.sqrt(varianceEnglish))
#print("Correlation between the two arrays is: " + str(correlation))
#-------------------------------------------------------------