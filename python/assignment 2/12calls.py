# For the first 75 calls, the charge is fixed and it is equal to Rs. 75;
# for the next 75 calls, the charge is calculated @Rs 0.75 per call; for
# the next 90 calls, the charge is Rs.0.65 per call and for the rest,
# if any, the rate is Rs.0.55 per call. It is required to determine the
# monthly bill of a subscriber.

calling=eval(input("Enter numbers of calls per month :"))

fix_rate_75_calls=75
next_76_to_150=0.75
next_151_to_240=.65
rate_per_call_above_240= 0.55
 
if calling <= 75:
      monthly_bill=fix_rate_75_calls
elif calling<=150:
     additional_76_to_150=calling-75
     monthly_bill=fix_rate_75_calls+(additional_76_to_150*next_76_to_150)

elif calling <= 240:
     additional_151_to_240=calling-75
     monthly_bill = fix_rate_75_calls + (75 * next_76_to_150) + (additional_151_to_240 * next_151_to_240)
else:
    additional_calls_above_240 = calling - 240
    monthly_bill = fix_rate_75_calls + (75 * next_76_to_150) + (90 * next_151_to_240) + (additional_calls_above_240 * rate_per_call_above_240)

    print(f"The monthly bill is Rs. {monthly_bill:.2f}")
    