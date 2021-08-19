import matplotlib.pyplot as plt
import numpy as np

#   stu_y = np.array([0, 30,33,30,16])
#   
#   stu_x = np.array(["Start", "Autumn 2018", "Spring 2019", "Autumn 2019", "Spring 2020"])
#   
#   plt.plot(stu_x, stu_y, marker = 'o')
#   
#   plt.xlabel("Semester", fontweight = "bold")
#   plt.ylabel("Amount of credits", fontweight = "bold")
#   
#   plt.show()

#gra_x = np.array([0,1,2,3,4,5])
#
#x_indexes = np.arange(len(gra_x))
#width = 0.25
#
#gra_y = np.array([0, 1, 2, 2, 8, 9])
#
#plt.bar(x_indexes, gra_y, width=width)
#
#plt.xlabel("Amount of grades", fontweight = "bold")
#plt.ylabel("Grades (0 to 5)", fontweight = "bold")
#
#plt.show()

#   slices = [21.9, 18.1, 17.9, 11.4, 10.9, 8.7, 4.3, 3.4, 1.8, 1.6]
#   labels = ["SDP", "PS", "KOK", "KESK", "VIHR", "VAS", "RKP", "KD", "LIIK", "muut"]
#   explode = [0.1,0,0,0,0,0,0,0,0,0]
#   colors = ["red", "cyan", "blue", "darkgreen", "lightgreen", "darkred", "yellow", "purple", "violet", "grey"]
#   
#   plt.pie(slices, labels = labels, explode = explode, shadow = True, wedgeprops={'edgecolor': 'black'}, colors=colors)
#   
#   plt.show()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clockedStudyHours = [5,8,7,2,4]

clockedPlayHours = [4,1,2,8,4]

labels = ["Days", "Working Hours", "Play Time"]

plt.stackplot(days, clockedStudyHours, clockedPlayHours, labels=labels)
plt.legend(loc = "upper left")
plt.show()