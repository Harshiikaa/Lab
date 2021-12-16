# write a program to print absolute value of a number 
# entered by user. E.g:-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

num= int(input("enter a number:"))
if num<0:
    print(num*-1) # * will chnage the negation into positive
else:
    print(num)
