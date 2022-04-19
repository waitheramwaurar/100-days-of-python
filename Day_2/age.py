age = input("What is your current age?")
remaining_yrs = 90 - int(age)

months = remaining_yrs * 12
weeks = remaining_yrs * 52
days = remaining_yrs * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")