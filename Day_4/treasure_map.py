#This is a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number.
#First your program must take the user input and convert it to a usable format.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

row = int(position[1])-1
column = int(position[0])-1

map[row][column] = "X"

print(f"{row1}\n{row2}\n{row3}")