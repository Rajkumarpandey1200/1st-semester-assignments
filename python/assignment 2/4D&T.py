from datetime import datetime
date = input("Enter a date (DD-MM-YYYY): ")

try:
    
    datetime.strptime(date,'%d-%m-%Y')
    print(f"{date} is a valid date.")
except ValueError:
   
    print(f"{date} is not a valid date.")
