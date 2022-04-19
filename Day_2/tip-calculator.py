#Calculates the total bill with the tip percentage chosen
print("Welcome to the tip calculator!!")

bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (bill/people) * (1 + tip_percent/100)
print(f"Each person should pay: ${bill_with_tip:.2f}")