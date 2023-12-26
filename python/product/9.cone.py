# To determine the area of a cone


import math

r=float(input("Enter radious of the cone :"))
h=float(input("Enter Height of the cone :"))
slant_height=math.sqrt(r**2+h**2)
area= math.pi*r*slant_height+math.pi*r**2

print("The area of a cone is :",round(area,2))