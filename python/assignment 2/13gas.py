meter_reading_prev = float(input("Enter the gas meter reading for the previous month: "))
meter_reading_curr = float(input("Enter the gas meter reading for the current month: "))

gas_consumed_cubic_feet = meter_reading_curr - meter_reading_prev

gas_consumed_therms = gas_consumed_cubic_feet * 1.475

rate_125_or_less = 7.75
rate_126_to_250 = 9.75
surcharge_126_to_250 = 1.25 / 100  
rate_above_250 = 13.00
surcharge_above_250 = 2.5 / 100  
meter_rent = 25

if gas_consumed_therms <= 125:
    gas_bill = gas_consumed_therms * rate_125_or_less
elif gas_consumed_therms <= 250:
    gas_bill = gas_consumed_therms * rate_126_to_250
    gas_bill += gas_bill * surcharge_126_to_250
else:
    gas_bill = gas_consumed_therms * rate_above_250
    gas_bill += gas_bill * surcharge_above_250

total_bill = gas_bill + meter_rent

print(f"The monthly gas bill is Rs. {total_bill:.2f}")
