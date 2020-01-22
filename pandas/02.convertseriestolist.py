"""
Create on :1/21/2020
@author:Marvin Senjaliya
"""

"""
problem statement:
2. Write a Python program to convert a Panda module Series to Python list and it's type. 
"""

import pandas as pd
a1=[1,2,3,4,5]
s1=pd.Series(a1)
l1=list(s1)
print(l1)
