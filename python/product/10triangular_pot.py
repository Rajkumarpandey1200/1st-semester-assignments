# To determine the perimeter of a triangular plot
#p=a+b+c
def triangular_plot(sideA,sideB,sideC):
    perimeter=sideA+sideB+sideC

    return perimeter
sideA = float(input("Enter side A : "))
sideB = float(input("Enter side B : "))
sideC = float(input("Enter side C : "))
perimeter=triangular_plot(sideA,sideB,sideC)
print ("Area of a perimeter is: units",perimeter)
