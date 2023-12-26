import math

a = float (input("length of 1st side"))
b = float (input("length of 2nd side"))
c = float (input("length of 3rd side "))

s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))

print("area for the triangle will be :",area)