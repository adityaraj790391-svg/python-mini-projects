## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Persons living in room/flat

## Output
# Total amount you've to pay is

rent = int(input("Enter the total rent: "))
food = int(input("Enter the total food ordered: "))
electricity = int(input("Enter the electricity units spent: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the number of persons living: "))

total_electricity_charge = electricity * charge_per_unit
total_amount = rent + food + total_electricity_charge
amount_per_person = total_amount / persons
