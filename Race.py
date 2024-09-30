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

