def calculate_commission(sales, region):
    if region == 'A':
        if sales < 10000:
            return 0
        elif sales < 16000:
            return 6.5 * sales / 100
        else:
            return 8.5 * sales / 100 + 1500
    elif region == 'B':
        if sales < 15000:
            return 6.5 * sales / 100
        elif sales < 25000:
            return 8.5 * sales / 100 + 1500
        else:
            return 0
    else:
        return "Invalid region."

sales_amount = float(input("Enter the sales amount: "))
sales_region = input("Enter the sales region (A or B): ").upper()

commission = calculate_commission(sales_amount, sales_region)

if type(commission) == float:
    print(f"The commission is Rs. {commission:.2f}")
else:
    print(commission)
