# given the integer N- the numbers of minutes that is passed since midnight
# Hours and mintues are displayed on the 24th digital clock
# The program should print two numbers: 
# the number of hours(Between 0 to 23)
# For example, if N= 150, 
# then 150 minutes have passed since midnight
# -i.e. now is 2:30 am so, the program should print 2 30
# N= minutes passed
# 
N= int(input("Enter the minutes passed since midnight"))
hour= int(N//60)
minutes= int(N%60)
print(f"{N} minutes passed since midnight is:{hour}:{minutes}")