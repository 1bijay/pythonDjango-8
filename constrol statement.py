# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 06:42:06 2022

@author: bijay
"""

#constrol statement
#if statement
#select case statement

#if statement
#Data types
#bool,float,integer,str,complex,list,tuple,set,dict,array,class

#operator
#Assigment(=,==,+=)
#arithmetic(+,-,*,**,/,//,%,power,sqrt)
#relational(==,!=,>=,<=,<)
#logical(and,or,not)
#others(.,{},(),[])


#condition
#(value1 relationaloperator value2)-> true/false
#print(10>3)
"""
if (condition) :
   statement(s)#declre,input,process,output
"""
#debugging

#num1 = 30
#num2 = 7
#if (num1>num2): #stop point
   # print("hello")
    #print("hi")
    #print("how are you")
#print("welcome to broadway")
"""
#example-2
num1 =input("enter any number :")
num1 = int(num1)# sr
if (num1==0):
    print("zero")
if(num1!=0):
    print("non-zero")
    #example-3
    #write a prigram which print the number value
    #(i.e. 1->one)
num2 =input("entaer any number (0-9):")
num2 =int(num2)
if num2== 0:
   print("zero")
if num2== 1:
    print("one")
    #.....
if num2== 2:
    print("two") 
if num2 == 3:
    print("three")
if num2 == 4:
    print("four")
if num2 == 5:
    print("five")
if num2== 6:
    print("six")
if num2== 7:
    print("seven")
if num2 == 8:
    print("eight")
if num2== 9:
    print("nine")    
if num2>9:   
    print("other")
if num2<0:
    print("other")
    """
     
#if else  statement

    # if condition1:
  #      statement(s)
  #  elif cindition2:
  #      statement(s)
 # ........
  #  elif cinditionN:
  #      statement(s)
   # else:
   #     statement(s)
""" 
"""
   #write a program which accept number (day value)
   #print weekday
   #decalare
num1= None
result = None
   #input
num1 = input ("enter amy number (1-7): ")
   #process
num1 = int(num1)
if num1 ==1:
    result="sun"
elif num1 ==2:
    result="mon"
elif num1==3:
    result="tuesday"
else:
    result="others"
   #output
print("Result : ", result)
   
# nested if statement
#if condition1:
#    if condition2:
#    statement(s)

"""
"""
#find largest number among 3 numbers
#Declare
num1 = None
num2 = None
num3 = None 
num4 = None 

#input
num1 = input("enter any number :")
num2 = input("enter any number :")
num3 = input("enter any number :")
#process
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if (num1>=num2):
    if (num1>=num3):
        num4 = num1

if (num2>=num1):
    if (num2>=num3):
        num4= num2

if (num3>=num1):
    if (num3>=num2):
       num4= num3
           
           
#output
print ("largest number :", num4)
        
""" 
# write a program which print largest number
# among three numbers 
# syntax

#if condition1 and /or condition2 and/or condition3
#    statement(s)
#example 
#declare
num1 = None 
num2 = None 
num3 = None 
num4 = None 

 #input 

num1 = input("enter first no : ") 
num2 = input("enter second no : ")
num3 = input("enter third no : ") 
   
#process
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
 
if num1>=num2 and num1>=num3:
    num4=num1
elif num2>=num1 and num2>=num3:
    num4=num2 
elif num3>=num1 and num3>=num2:
    num4=num2        
#output
print("result : ",num4)   
"""