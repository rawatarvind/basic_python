#!/bin/bash

id=101
name="arvind"
age=28

print(id,name,age,sep=",")

row1=[102,"amit",34,"Delhi"]

for x in row1:
     print(x,end=" ")

x=int(input("Enter a number : "))

y=int(input("Enter a number : "))
z=x*y
print(z)


import os 

#data=os.popen("df -h").readlines)

# if else:

age=int(input("Enter the age : "))

if age>18:
  print("valid")
else:
  print("not valid")


# Netsted if else

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

if a!=b:
  if a>b:
    print("a is greater")
  else:
    print("y is greater")
else:
  print("both are equal")


##############

day=input("Enter day : ")
amount=int(input("Enter amount : "))

if day.lower()=="sunday" and amount>=5000:
  discount=(amount*10)/100
  Total=amount-discount
  print("After 10% discount price will be :",Total)
elif day.lower()=="sunday" and amount >=4000:
  discount=(amount*5)/100
  amount=amount-discount
  print("After 5% discount amount will be : ",amount)
else:
  print("Without discount price will be :",amount)

