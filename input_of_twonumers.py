# program to calculate input of 2 numbers and give result 
# the numbers are predeteermined
a=3
b=5
c=a+b
print("this is your result "+str(int(c)))
# the next program take input from the user and print the result instead of pre-determined answer
d=input("Please input the first number ")
e=input("Please input the second number ")
f=int(str(d))+int(str(e))
print("this is your result "+str(int(f)))
# important thing to know that python is case sensitive language
# meaning if I write A it'll not overwrite a
A="Snippets"
B="useful"
print(str(A)+" are quite "+str(B))
# re-explaining of the code through variable print demonstration
print(f"Variables are {A} and {B}")
if type(A)==str:
    print("the type of data is string type")
else:
    print("the type of data is integer ")
if type(B)==str:
    print("the Variable is a type of string data ")
else:
    print("the type of data is integer ")
print("the type of data is "+str(type (B)))
#unpacking a list using variables
friuts=["apple","cherry","bannana"]
x,y,z=friuts
print(x)
print(y)
print(z)

