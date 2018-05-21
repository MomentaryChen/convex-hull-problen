# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:30:16 2018

@author: Momentary
"""

import random as ra
import numpy as np
np.random.seed(19990801)
x = []
y = []
n=ra.randint(0,100)   #點的數量
for i in range(n):
    y.append(ra.randint(0,1000))
    x.append(ra.randint(0,1000))

print(n)

import matplotlib.pyplot as plt
fig =plt.figure()
ax = fig.add_subplot(111)
'''
#ax.plot(x, y, color='lightblue', linewidth=3)
ax.scatter(x,y,color='darkgreen',marker='^')
#plt.savefig(.//Desktop//Sort.png')
plt.show()
'''
middle = int((max(x)+min(x))/2)
print(middle)

m_x=[middle,middle]

m_y=[0,1000]
ax.plot(m_x,m_y, color='lightblue', linewidth=3)
ax.scatter(x,y,color='darkgreen',marker='^')
plt.show()

x_left=[]
x_right=[]
y_left=[]
y_right=[]
for i in range(len(x)):                            #分成左邊和右邊的頂點
   if(x[i]>middle):
       x_right.append(x[i])
       y_right.append(y[i])
   else:
       x_left.append(x[i])
       y_left.append(y[i])
print(x_right)

def findCenter(arr):                             #找出中心點finction
    total=0
    for i in arr:
        total+=i
    return int(total/len(arr))

center_x =[findCenter(x_right),findCenter(x_left)]          #找出中心點放入
center_y = [findCenter(y_right),findCenter(y_left)]
             
ax.plot(m_x,m_y, color='lightblue', linewidth=3)
ax.scatter(x,y,color='darkgreen',marker='^')
ax.scatter(center_x,center_y,color='darkgreen',marker='_')
plt.show()


    