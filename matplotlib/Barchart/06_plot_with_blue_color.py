'''
Created on 23/01/2020
@author:Marvin Senjaliya
'''
'''
problem statement:
6. Write a Python programming to display a bar chart of the popularity of programming Languages. Make blue border to each bar.  
Sample data: 
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 

'''
from matplotlib import pyplot as plt

languages=['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(languages,popularity,color='skyblue', edgecolor='blue')
plt.xlabel("Programming Languages",color='maroon')
plt.ylabel("Popularity",color='maroon')
plt.title("Popularity of programming languages", color='black')
plt.show()
