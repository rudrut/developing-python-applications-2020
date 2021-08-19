#import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from collections import Counter

plt.style.use("fivethirtyeight")

data = pd.read_csv("arabica_data_cleaned.csv")
print("Amount of rows and columns: " + str(data.shape))

print(data.describe())

duplicate_rows = data.duplicated(subset=["Country.of.Origin", "Harvest.Year", "Expiration"])
print(data[duplicate_rows])

country_list = list(data["Country.of.Origin"].unique())
print(len(country_list))

point_grp = data.groupby(["Total.Cup.Points"], sort = False).mean().reset_index()
print(point_grp[["altitude_high_meters", "Total.Cup.Points"]])

df = pd.DataFrame(data=data, columns=['Total.Cup.Points','altitude_high_meters'])

df.plot.scatter(x='Total.Cup.Points', y='altitude_high_meters', title= "Correlation between altitude and points")
plt.xlabel("Total Cup Points")
plt.ylabel("Altitude in meters")

plt.tight_layout()
plt.show(block=True)

#uncomment csv at the top if you wish to read file with csv module

#countryData = data["Country.of.Origin"].apply(str)
#
#countryCounter = Counter()
#
#for country in countryData:
#    countryCounter.update(country.split(","))
#
#amount = []
#countries = []
#for item in countryCounter.most_common(10):
#    countries.append(item[0])
#    amount.append(item[1])
#
#print(countries)
#print(amount)
#countries.reverse()
#amount.reverse()
#plt.barh(countries, amount)
#plt.title("Top 10 origins of coffee")
#plt.xlabel("Different coffee varieties")
#plt.tight_layout()
#plt.show()