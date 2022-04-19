#The program below calculates if a specific is a leap year
#A year is considered a leap year if the year is divisible by 4 except if the year is divisible by 100 unless the year is also divisible by 400

year = int(input("Which year do you want to check? "))

if (year % 4 == 0):
  if (year % 100 != 0):
    print("Leap year.")
  else:  
    if (year % 400 == 0):
      print("Leap year.")
    else:
      print("Not leap year.")
else:
  print("Not leap year.")  