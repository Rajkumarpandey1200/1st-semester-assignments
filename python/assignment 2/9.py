def categorize_triangle(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 != 180 or any(angle <= 0 for angle in (angle1, angle2, angle3)):
        return "Invalid triangle."

    if angle1 == angle2 == angle3:
        return "Equiangular triangle."

    if any(angle == 90 for angle in (angle1, angle2, angle3)):
        return "Right-angled triangle."

    if all(angle < 90 for angle in (angle1, angle2, angle3)):
        return "Acute-angled triangle."

    if any(angle > 90 for angle in (angle1, angle2, angle3)):
        return "Obtuse-angled triangle."

angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))

triangle_category = categorize_triangle(angle1, angle2, angle3)
print(f"The triangle is {triangle_category}")
