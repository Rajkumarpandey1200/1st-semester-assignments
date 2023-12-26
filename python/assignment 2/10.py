def categorize_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        if side1 == side2 == side3:
            return "Equilateral triangle."

        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles triangle."

        else:
            return "Scalene triangle."

    else:
        return "Invalid triangle."

side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))

triangle_category = categorize_triangle(side1, side2, side3)
print(f"The triangle is {triangle_category}")
