''' Write a program to calculate the grade of a student from his marks from the following scheme:
90 -100 => ex
80-90=> A
70-80 => B
60-70 => C
50-60 => D
<50 => F'''

marks = int(input("Enter the marks in student :.."))

if(marks<=100 and marks >=90):
    # print(" Excelent Grade")
    grade = "Excelent"

elif(marks<90 and marks >=80):
    # print(" A Grade")
    grade = "A"

elif(marks<80 and marks >=70):
    # print(" B Grade")
    grade = "B"

elif(marks<70 and marks >=60):
    # print(" C Grade")
    grade = "C"

elif(marks<60 and marks >=50):
    # print(" D Grade")
    grade = "D"

elif(marks<50 ):
    # print(" F Grade")
    grade = "F"

print("your marks is :..",marks)
print("your grade is ", grade)