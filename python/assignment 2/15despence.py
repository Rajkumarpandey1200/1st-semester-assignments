amount_to_dispense = int(input("Enter the amount to be dispensed: "))

denomination_2000 = 2000
denomination_500 = 500
denomination_200 = 200
denomination_100 = 100

num_notes_2000 = 0
num_notes_500 = 0
num_notes_200 = 0
num_notes_100 = 0

while amount_to_dispense > 0:
    if amount_to_dispense >= denomination_2000:
        num_notes_2000 += 1
        amount_to_dispense -= denomination_2000
    elif amount_to_dispense >= denomination_500:
        num_notes_500 += 1
        amount_to_dispense -= denomination_500
    elif amount_to_dispense >= denomination_200:
        num_notes_200 += 1
        amount_to_dispense -= denomination_200
    elif amount_to_dispense >= denomination_100:
        num_notes_100 += 1
        amount_to_dispense -= denomination_100
    else:
        break

print("Minimum number of notes:")
print(f"2000 rupee notes: {num_notes_2000}")
print(f"500 rupee notes: {num_notes_500}")
print(f"200 rupee notes: {num_notes_200}")
print(f"100 rupee notes: {num_notes_100}")
