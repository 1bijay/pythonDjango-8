# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 06:38:27 2022

@author: bijay
"""
#task2
#create an array to store 4 obtain of students 
#marks of student   (67,43,23,56)
from array import array
marks = array('i',[67,43,23,56])
print(marks)

#calculate the total obtained mark
sum = marks[0]+marks[1]+marks[2]+marks[3]
avg = sum/4
print(sum)
print(avg)
#after update
marks[2]=44
sum = marks[0]+marks[1]+marks[2]+marks[3]
print(sum)
avg = sum/4
print(avg)

# find largest obtain mark
print(max(marks))
print(min(marks))
#print(sum(marks))
print(len(marks)) #number of elements

# calculate result of student (pm=40)?


