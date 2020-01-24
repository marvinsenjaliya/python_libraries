"""
Created on:1/23/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
 Write a Python programming to display a bar chart of the popularity of programming Languages. Specify the position of each bar plot. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
"""

from matplotlib import pyplot as plt
programming_languages=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.bar(languages,popularity,data=[1,2,3,4,5,6])
plt.xlabel("Programming Languages",color='maroon')
plt.ylabel("Popularity",color='maroon')

x_pos=[index for index, value in enumerate(languages)]
plt.xticks(x_pos,languages)
y_pos=[0,1,2,3,4,5]
plt.bar(y_pos,popularity)

plt.minorticks_on()
plt.grid(which='major',linestyle='-',color='blue')
plt.grid(which='minor',linestyle=":",color='black')
plt.title("Popularity of programming languages", color='black')
plt.show()
