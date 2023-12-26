pound=float(input("Enter amount in pounds :"))
Dollar=float(input("Enter amount in Dollar :"))
Euro=float(input("Enter amount in Euro:"))

pound_to_inr=100
Dollar_to_inr=75
euro_to_inr=80

inr_from_pound=pound*pound_to_inr
inr_from_Dollar=Dollar*Dollar_to_inr
inr_from_Euro=Euro*euro_to_inr

print("Currency Conversion Table:")
print(f"{pound} Pounds = {inr_from_pound} Indian Rupees")
print(f"{Dollar} Dollars = {inr_from_Dollar} Indian Rupees")
print(f"{Euro} Euros = {inr_from_Euro} Indian Rupees")