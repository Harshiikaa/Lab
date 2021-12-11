# A school decided to replace the desks in three classrooms. 
# Each desk sits two students.
# Given the number of  students in each class, 
# print the smallest possible number of desks that can be purchased.
# The program should read three integers: 
# the number of students in each of the three classes, a,b and c respectively.



A= int(input("Enter Number of Students in First Class : "))
B= int(input("Enter Number of Students in Second Class : "))
C= int(input("Enter Number of Students in Third Class : "))
if A%2==0:
    noOfDesksIn1stClass= A//2
else:
    noOfDesksIn1stClass=(A//2)+1
if B%2==0:
    noOfDesksIn2ndClass= B//2
else:
    noOfDesksIn2ndClass=(B//2)+1
if C%2==0:
    noOfDesksIn3rdClass=C//2
else:
    no_Of_Desks_In_3rd_Class=(C//2)+1
print(f"first class needs {noOfDesksIn1stClass} desks\n second class needs {noOfDesksIn2ndClass} desks\n 3rd class needs {noOfDesksIn3rdClass}")
print(f"So {noOfDesksIn1stClass+noOfDesksIn2ndClass+noOfDesksIn3rdClass} desks are needed in total ")

    




# if first_class % 2 == 0:
#     first_class_chairs =  first_class/2
# else:
#     first_class_chairs =  (first_class//2 )+ 1
# if second_class % 2 == 0 :
#     second_class_chairs = second_class/2
# else:
#     second_class_chairs = (second_class//2)+1
# if third_class %2 == 0:
#     third_class_chairs = third_class/2
# else:
#     third_class_chairs = (third_class//2)+1


# print(f"First Class Needs {first_class_chairs} Chairs\nSecond Class Needs {second_class_chairs} Chairs\nThird Class Needs {third_class_chairs} Chairs\nIn Total We Need {first_class_chairs+second_class_chairs+third_class_chairs} Additional Chairs ")
