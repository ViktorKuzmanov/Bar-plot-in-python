from numpy import *
import pandas as pd
from scipy.interpolate import *
from matplotlib.pyplot import *

df = pd.read_csv('data.csv')
#gradesAndHours = df[['timeInvested', 'Grades']].copy()
timeDf = df[['timeInvested']].copy()
gradesDf = df[['Grades']].copy()


timeArray = timeDf.to_numpy()
gradesArray = gradesDf.to_numpy()

yData = timeArray.astype(int64)
xData = gradesArray.astype(int64).tolist()

#Convert numpy array to list

xArray = [0] * 10
yArray = [0] * 10
count = 0
for a in xData:
    xArray[count] = a[0]
    count += 1
count = 0
for v in yData:
    yArray[count] = v[0]
    count += 1


pl = polyfit(xArray, yArray, 1)
plot(xArray, yArray, 'o')
plot(xArray,polyval(pl,xArray), 'r-')
show()

