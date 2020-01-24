
'''
Created on 23/01/2020
@author:Marvin Senjaliya
'''
'''
problem statement:
Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29)

'''
from matplotlib import pyplot as plt

men=[22,30,35,35,26]
women=[25,32,30,35,29]

plt.xlabel("Programming Languages",color='maroon')
plt.ylabel("Popularity",color='maroon')

plt.bar(languages,popularity)
plt.subplots_adjust(bottom=0.3)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',color='blue')
plt.grid(which='minor',linestyle=":",color='black')
plt.title("Popularity of programming languages", color='black')
plt.show()
