# For average purposes
Student = input("Student's Full Name:")
ID_Number = eval(input("ID Number:"))
Course = input("Course:")
Section = input("Section:")
print()
print("4th Quarter Grades")
Number1 = eval(input("Enter Programming 1 Grade:"))
Number2 = eval(input("Enter Introduction to Computing Grade:"))
Number3 = eval(input("Enter CS Math Grade:"))

# compute grade
average = (Number1 + Number2 + Number3) / 3

# Print result
print("Here is the average of your grade!" + str(average))
print()
a = 74
b = average
if b > a:
  print("Congratulations!")
if b <= a:
  print("Better luck next time!")
