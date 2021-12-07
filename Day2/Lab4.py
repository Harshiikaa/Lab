#N students take K apples and distribute them along each other evenly. 
# The remaining (the indivisible) part remains in the basket.
#  How many apples will each single student get? 
# How many apples will remain in the basket?
#  The program reads the number N and K.
# It should print the two answers for the given questions above
# N is the N number of students
# K is the K number of apples
# K//N gives the number of apples got by each student  


# N= input("Enter the number of students")
# K= input("Enter the number of apples")
# eachStudentGets= K//N
# inBasket= K%N
# print(f"each student got {eachStudentGets}")
# print(f"the remaining apples in the basket are {inBasket}")

number_of_students = int(input("Enter Number of Students : "))
number_of_apples = int(input("Enter Number of Apples : "))
each_student_gets = number_of_apples // number_of_students


baskets = number_of_apples - (each_student_gets*number_of_students)
if number_of_apples < number_of_students:
    print("Sablai Pugne Gari Ta lyauna parchha ni ")
else:
    print(f"Each Students Gets {each_student_gets} Apples and {baskets} Remains in Basket ")