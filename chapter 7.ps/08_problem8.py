# write a program to print the following star patten:
'''
For n =3
*
***
***** 
 '''

n = int(input("Enter the number :.."))
for i in range (1 , n+1):
    print("*"* (2*i-1), end="")
    print("")