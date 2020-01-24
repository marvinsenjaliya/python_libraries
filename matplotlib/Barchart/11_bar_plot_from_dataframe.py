
'''
Created on 23/01/2020
@author : Marvin Senjaliya
'''
'''
problem statement:
Write a Python program to create bar plot from a DataFrame. 
Sample Data Frame:
a b c d e 
2 4,8,5,7,6
4 2,3,4,2,6
6 4,7,4,7,8
8 2,6,4,8,6
10 2,4,3,3,2

'''
from matplotlib import pyplot as plt
import numpy as np

men=[22,30,35,35,26]
women=[25,32,30,35,29]
group=np.arange(len(men))

fig, axis =plt.subplots()


plt.xlabel("Scores",color='maroon')
plt.ylabel("Groups",color='maroon')

plt.bar(group,men,0.35,alpha=0.8, color='black',label='Men')
plt.bar(group+0.35,women,0.35,alpha=0.8, color='gray',label='Women')
plt.xticks(group+0.35,('G1','G2','G3','G4','G5'))

plt.title("Scores of men and women", color='red')
plt.show()

