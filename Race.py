distance_km = 10
time_min = 42 + (42/60)


#a
time_sec = (42*60)+42
print ("Seconds Run:",time_sec)

#b
distance_mi = 10/161*100
print ("Miles:",distance_mi)

#c
print ("Average time per mile was: %im and %is" %(time_sec//60,time_sec%60))

#d
avr_speed_mph = distance_mi / (time_sec/60/60)
print ("Speed(mph):",round(avr_speed_mph,2))





#Input is mins, secs and kms
#Output is to be pace(Mins and secs) and speed per mile

def RaceAnalysis (time_s,distance_km):
    minutes = time_s//60
    seconds = time_s%60
    miles = distance_km/161*100
    pimas = f"{minutes//miles}m {round(minutes%miles + seconds,2)}s"
    spm = f"{round(miles/(time_s/60/60),2)}mph"
    return pimas, spm 

time_min = float(input("How many minutes did you run for, in decimal form? "))
time_s = time_min*60
distance_km = float(input("How many kilometers did you run? "))

pace_in_min_and_sec, speed_per_mile = RaceAnalysis (time_s, distance_km)

print(f"Your pace was: {pace_in_min_and_sec} per mile")
print(f"Your speed per mile was: {speed_per_mile}")

