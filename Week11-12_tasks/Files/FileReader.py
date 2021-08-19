# Files
strippedLines = []

with open("countries.txt") as file_object:
    for line in file_object:
        line = line.strip()
        strippedLines.append(line)

def addCountryAndPopulation(listToAppend, countryAndPopulation):
    countryAndPopulation.strip()
    listToAppend.append(countryAndPopulation)
    
addCountryAndPopulation(strippedLines, "Netherlands-17,138,553")
addCountryAndPopulation(strippedLines, "Vatican City-00,000,797")

splitList = []

for line in strippedLines:
    line = line.split('-')
    splitList.append(line)

countriesAndPopulations = {}

for i in range(len(splitList)):
    countriesAndPopulations[splitList[i][0]] = splitList[i][1]

def joinIntsInDict(dict):

    for x in dict:
        dict[x] = dict[x].replace(',','')

joinIntsInDict(countriesAndPopulations)

def convertValuesToIntegersInDict(dict):
    for x in dict:
        dict[x] = int(dict[x])

convertValuesToIntegersInDict(countriesAndPopulations)

def largestCountryAndPopulation(dict):
    largest = 0
    country = ""

    for key, value in dict.items():
        if value > largest:
            country = key
            largest = value

    return country, largest

print("The largest country by population is " + largestCountryAndPopulation(countriesAndPopulations)[0] + " and it's estimated population is: " + str(largestCountryAndPopulation(countriesAndPopulations)[1]) + '.')