'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin. 
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 

'''
from matplotlib import pyplot as plt

languages=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.xlabel("Programming Languages",color='maroon')
plt.ylabel("Popularity",color='maroon')

x_pos=[index for index, value in enumerate(languages)]
plt.xticks(x_pos,languages)
y_pos=[0,1,2,3,4,5]
width=[0.5,0.8,0.6,0.7,0.4,0.25]
plt.bar(y_pos,popularity,width=width)
plt.xticks(y_pos,languages)
plt.minorticks_on()

plt.grid(which='major',linestyle='-',color='blue')
plt.grid(which='minor',linestyle=":",color='black')
plt.title("Popularity of programming languages", color='black')
plt.show()
