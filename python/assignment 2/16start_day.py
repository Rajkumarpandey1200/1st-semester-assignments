import calendar

year = int(input("Enter the year: "))

start_day = calendar.weekday(year, 1, 1)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start_day_name = days_of_week[start_day]


print(f"The starting day of the year {year} is {start_day_name}.")
