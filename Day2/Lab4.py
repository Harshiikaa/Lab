#N students take K apples and distribute them along each other evenly. 
# The remaining (the indivisible) part remains in the basket.
#  How many apples will each single student get? 
# How many apples will remain in the basket?
#  The program reads the number N and K.
# It should print the two answers for the given questions above
# N is the N number of students
# K is the K number of apples
# K//N gives the number of apples got by each student  


N= int(input("Enter the number of students"))
K= int(input("Enter the number of apples"))
eachStudentGets= K//N
inBasket= K%N
print(f"each student got {eachStudentGets}")
print(f"the remaining apples in the basket are {inBasket}")