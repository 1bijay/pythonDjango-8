# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 07:01:49 2022

@author: bijay
"""
#enter start number : 1
#enter stop number  : 10
#print 1,2,3,...10
#sum : 55
#average : 5.5 
#max : 10
#min : 10
#declare
start = None
stop = None

#input

start = 1
stop = 10
while(start<=stop):
    print(start, end=" ")
    start+=1
 
for i in range(1,11):
  print(i, end=' ')
 
print([i for i in range (1,11)])
print(max(i)) 

sum = 0
for i in range(1,11):
  sum +=i
  print(sum)  
  
average = sum/10
print("The average is : ",average)

a =int(input("Enter the first: "))
b =int(input("enter the second: "))
c = a+b
print("Sum : ",c)
d= a-b
print("difference : ", d)
e = a*b
print("product : ", e)
f = a/b
print("division : ", f)
