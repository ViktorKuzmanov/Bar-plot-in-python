import matplotlib.pyplot as plt
from collections import OrderedDict
from operator import itemgetter
import csv
from operator import attrgetter

class Subject:

     def __init__(self, name,timeInvsted,ifPassed):
          self.name = name;
          self.timeInvested = timeInvsted;
          self.ifPassed = ifPassed;

# Specify the path of your file
path = "data.csv"
googleStockData = open(path, newline='')

reader = csv.reader(googleStockData)
header = next(reader) # read the firs line
data = [row for row in reader] # add rows as arrays in array data

subjects = []

for line in data:
     name = line[0]
     timeInvested = line[1]
     ifPassed = line[2]
     subjects.append(Subject(name, timeInvested, ifPassed))

timeInvested = []
names = []
ifPassed = []

#Sorting my subject in ascending order before I add them to plot
subjects = sorted(subjects, key=lambda x: float(x.timeInvested), reverse=False)

for subject in subjects:
     timeInvested.append(float(subject.timeInvested))
     names.append(subject.name)
     ifPassed.append(int(subject.ifPassed))

barPlot = plt.bar(names, timeInvested)

#Add color to bars based if I have passed or failed
for i in range(len(ifPassed)):
     if(ifPassed[i] == 1):
          barPlot[i].set_color("g")
     if (ifPassed[i] == 0):
          barPlot[i].set_color("r")

plt.show()


