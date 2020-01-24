'''
Created on 23/01/2020
@author: Marvin Senjaliya
'''
'''
problem statement:
Write a Python programming to create a pie chart of the popularity of programming Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''
from matplotlib import pyplot as plt
languages=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.pie(popularity,labels=languages)
plt.show()
