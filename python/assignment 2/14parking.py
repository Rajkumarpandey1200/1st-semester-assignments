parking_duration = float(input("Enter the parking duration in hours: "))

initial_rate = 55
additional_rate_per_2_hours = 13.75
beyond_23_hours_rate_per_minute = 5.50 / 60  

if parking_duration <= 8.5:
    parking_charge = initial_rate
elif parking_duration <= 23:
    additional_hours = parking_duration - 8.5
    additional_charge = (additional_hours // 2) * additional_rate_per_2_hours
    parking_charge = initial_rate + additional_charge
else:
    beyond_23_hours_duration = parking_duration - 23
    parking_charge = initial_rate + (14 * additional_rate_per_2_hours) + (beyond_23_hours_duration * beyond_23_hours_rate_per_minute)

print(f"The parking charge is Rs. {parking_charge:.2f}")
