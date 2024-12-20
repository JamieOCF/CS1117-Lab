# a
air_temp = float(input("What is the current air temperature, in celsius? "))
wind_kph = float(input("What is the current wind speed, in kph? "))

WCI = 13.12 + (0.6215*air_temp) - (11.37*(wind_kph**0.16)) + (0.3965*air_temp*(wind_kph**0.16))
print (f"The wind chill index is: {round(WCI,0)}")


# b
def calcWindChillIndex (Air_Temp_C, Wind_Speed_KPH):
    WCI = 13.12 + (0.6215*Air_Temp_C) - (11.37*(Wind_Speed_KPH**0.16)) + (0.3965*Air_Temp_C*(Wind_Speed_KPH**0.16))
    return WCI

Air_Temp_C = float(input("What is the current air temperature, in celsius? "))
Wind_KPH = float(input("What is the current wind speed, in kph? "))

WCI = calcWindChillIndex (Air_Temp_C, Wind_KPH)
print ("The wind chill index is: %0d" %(WCI))


# c
def calcWindChillIndex (Air_Temp, Wind_Speed):
    WCI = 13.12 + (0.6215*Air_Temp) - (11.37*(Wind_Speed**0.16)) + (0.3965*Air_Temp*(Wind_Speed**0.16))
    print ("The wind chill index is: %0d" %(WCI))

Air_Temp_C = float(input("What is the current air temperature, in celsius? "))
Wind_KPH = float(input("What is the current wind speed, in kph? "))

calcWindChillIndex (Air_Temp_C, Wind_KPH)


# d
from wci_index import calcWindChillIndex

Air_Temp_C = float(input("What is the current air temperature, in celsius? "))
Wind_KPH = float(input("What is the current wind speed, in kph? "))

calcWindChillIndex (Air_Temp_C, Wind_KPH)
