a = int(input("Enter your age:"))

if(a>=18):
    print("you are above the age of voting  ")
    print("Valid persion for you in voting :... ")
elif(a<0):
    print("You are entering an invalid age : ..")
elif(a==0):
    print ( " you are entering 0 which is not a valid age ")
else:
    print("You are below the age of not voting : ")

print("End of the program: ..")
