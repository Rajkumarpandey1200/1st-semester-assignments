def calculate_bonus(basic_pay, designation):
    if designation == 'Manager':
        if basic_pay < 40000:
            bonus_percentage = 12
            bonus_min = 2500
            bonus_max = None
        else:
            bonus_percentage = 16
            bonus_min = None
            bonus_max = 7500
    elif designation == 'Officer':
        bonus_percentage = 14
        bonus_min = 2500
        bonus_max = 5000
    else:
        bonus_percentage = 8.9
        bonus_min = bonus_max = None

    bonus = basic_pay * (bonus_percentage / 100)

    if bonus_min is not None and bonus < bonus_min:
        bonus = bonus_min
    elif bonus_max is not None and bonus > bonus_max:
        bonus = bonus_max

    return bonus


basic_pay = float(input("Enter the basic pay: "))
designation = input("Enter the designation (Manager/Officer/Other): ").capitalize()

festival_bonus = calculate_bonus(basic_pay, designation)
print(f"The festival bonus for the employee is Rs. {festival_bonus:.2f}")
