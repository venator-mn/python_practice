
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_bill = float(bill)
tip_amount = int(tip) 
person_count = int(people)

tip_calc = tip_amount / 100
total_tip = (total_bill * tip_calc)
total_inc_tip = (total_bill + total_tip)

final_total = round(total_inc_tip / person_count, 2)
result = f"Each person should pay {final_total}"

print(result)

