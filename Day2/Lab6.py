# You live 4 miles from university.
# The bus drives at 25mph but
# spends 2 min at each of the 10 stops on the Way
# How long will the bus journey take?
# Alternatively, you could run to the university.
# you jog the first mile at 7mph;
# then run the next two at 15mph;
# before jogging the last at 7mph again.
# Will this be slower or quicker than the bus?


#In bus
distance= 4 # miles
velocity= 25 #mph
time1= (distance/velocity)*60 #we changed seconds into minutes by dividing it with 60
time2= 20 #minutes # 2* 10 cuz 2 min per stops
totalTimeTakenByBus= time1+time2
print(f"Total time taken by the bus is: {totalTimeTakenByBus}")

#By jogging
distance1= 1 #miles
velocity1= 7 #mph
distance2= 2 #miles
velocity2= 15 #mph
distance3= 1 #miles
velocity3= 7 #mph
totalTime1= (distance1/velocity1)*60
totalTime2= (distance2/velocity2)*60
totalTime3= (distance3/velocity3)*60
totalTimeTakenByJogging= totalTime1+totalTime2+totalTime3
print(f"total time taken by jogging is: {totalTimeTakenByJogging}")
if totalTimeTakenByBus<totalTimeTakenByJogging:
    print("this will be quicker than the bus")
else:
    print("this will be slower than the bus")


