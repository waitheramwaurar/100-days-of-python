#This is a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0

for height in student_heights:
  total_height += height
students_no = 0
for height in student_heights:
  students_no += 1
average_height = round(total_height/students_no)
print(average_height)
  
  