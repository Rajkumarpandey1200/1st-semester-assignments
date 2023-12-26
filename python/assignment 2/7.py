import calendar

def print_days_in_each_month(year):
    for month in range(1, 13):
        days_in_month = calendar.monthrange(year, month)[1]
        print(f"Number of days in {calendar.month_name[month]} {year}: {days_in_month}")


user_year = int(input("Enter the year: "))
print_days_in_each_month(user_year)
