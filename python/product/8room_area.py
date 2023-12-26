# To determine the area of the walls of a rectangular room and hence
# the cost of its painting on the basis of charge per square unit
#area of a rectungalur room =2*height(length+width)

height= float(input("enter height of the room :"))
length= float(input("enter length of the  room :"))
width= float(input("enter width of the room :"))
cost= float(input("enter cost for per square unit :"))

area =2*height*(length+width);
paint_cost= area*cost;
print("Area of a rectangular room is :",area,"sq ft")
print("the cost of its painting on the basis of charge per square unit is:",round(paint_cost,2),u'\u20b9',"sq ft")

