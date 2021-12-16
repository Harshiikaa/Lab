# write a python program to sum three given integers.
# However, if two or more values are equal sum will be zero

First= int(input("Enter the first integer:"))
Second= int(input("Enter the second integer:"))
Third= int(input("Enter the third integer:"))
Total= First+Second+Third
sum= 0
if First==Second or Second==Third or First==Third:
    print(f"The sum will be {sum}")
else:
    print(f"The sum will be {Total}")
