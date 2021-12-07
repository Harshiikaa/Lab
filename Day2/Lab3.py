# given the integer N- the numbers of minutes that is passed since midnight
#Hours and mintues are displayed on the 24th digital clock
# N= minutes passed
N= int(input("Enter the minutes passed since midnight"))
hour= int(N//60)
minutes= int(N%60)
print(f"{N} minutes passed since midnight is:{hour}:{minutes}")