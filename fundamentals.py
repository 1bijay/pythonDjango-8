# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 06:09:12 2022

@author: bijay
"""
#j.array
from array import array #step1
#declarative an array
weights= array('i',[60,55,75,48,67])
#                 0,1,2,3,4
#print(help(array))
print(weights) #all element

weights[0] =62 #update
print(weights)
print(weights[3])


#user defined types i.e. class

class student:
    pass
#use
s1 = student()
s2 = student()
print(type(s1))
print(type(s2))
