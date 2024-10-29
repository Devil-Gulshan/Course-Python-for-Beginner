# write a program to find out whether a student has passed or failed if it requires  a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

c = int(input("Enter the marks c lang....:"))
python = int(input("Enter the marks python ...:"))
java = int(input("Enter the marks java ...:"))

# check for total percentage

# total_percentage =(100* (c + python + java))/300
total_percentage = (c + python + java)/3

if(total_percentage >= 40 and c>=33 and python>=33 and java>=33):
    print("You are pass:..")

else:
    print("You are fail, try again next year :..")

print("your percentage is ..", total_percentage)

