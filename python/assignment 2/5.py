def classify_quadrilateral(side_lengths, internal_angle):
    # Check if the given side lengths can form a quadrilateral
    if len(side_lengths) != 4 or any(side <= 0 for side in side_lengths):
        return "Invalid input. Please provide valid side lengths for a quadrilateral."

    # Check if the given internal angle is valid
    if internal_angle < 0 or internal_angle >= 180:
        return "Invalid input. Please provide a valid internal angle (0 <= angle < 180)."

    if all(side == side_lengths[0] for side in side_lengths) and internal_angle == 90:
        return "It's a square."

    if all(side == side_lengths[0] for side in side_lengths):
        return "It's a rhombus."

    if side_lengths[0] == side_lengths[2] and side_lengths[1] == side_lengths[3]:
        return "It's a parallelogram."

    return "It's an irregular quadrilateral."

side_lengths = [4, 4, 4, 4]  
internal_angle = 90 

result = classify_quadrilateral(side_lengths, internal_angle)
print(result)
