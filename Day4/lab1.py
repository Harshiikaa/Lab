# Check whether the given year is leap year or not.
# If year is leap print "LEAP YEAR" else print "COMMON YEAR"

Year= int(input("Enter a year:"))
if Year%4==0 and Year%100!=0:
    print("The year is a leap year")
elif Year%400==0:
    print("The year is leap year")
else:
    print("The year is a common year")