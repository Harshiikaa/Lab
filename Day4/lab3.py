# Ask user to enter age, gender(M or F) and then 
# using following rules print their service.
# if employee is female, 
# then she will work only in urban areas
# if employee is a male and is in between 20 to 40
# then he may work in anywhere
# if employ is male and age is in between 40 to 60 then
# he will work in Urban areas only>
# And any other input of age should print "ERROR"

Gender= input("Enter your Gender")
Age= int(input("Enter your age:"))
if Gender=="F":
    print("She will work only in Urban areas")
elif Gender=="M" and (Age<20 and Age>=40):
    print("He may work in anywhere")
elif Gender=="M" and (Age<40 and Age>=60):
    print("He will work in Urban areas only")
else:
    print("ERROR")