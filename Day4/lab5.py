# A student will not be allowed to sit in exam if his/her
# attendance is less than 75%.
# take the following input from user
# number of classes held
# Number of classes attended
# and print
# percentage of class attended
# is Student is allowed to sit in exam or not.

A= int(input("Enter the number of classes held:"))
B= int(input("Enter the number of classes attended:"))
percentage= (B/A)*100
if percentage<75:
    print("The student is not allowed to sit in his/her exam ")
else:
    print("Student is allowed to sit in exam")