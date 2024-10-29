''' A spam comment is defined as a text containing following keyWords:
"Make a lot of money ", "buy now ", "Subscribe this ", "click this", .
 Write a program to detect these spams . '''

# spam filters 

p1 = "Make a lot of maney"
p2 = "buy now"
p3 = "subscribe this "
p4 ="click this"

message = input("Enter your comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
     print("this commant is spam ")

else:
     print("this commant is not spam")

