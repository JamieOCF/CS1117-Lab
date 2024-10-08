def calcWindChillIndex (Air_Temp, Wind_Speed):
    WCI = 13.12 + (0.6215*Air_Temp) - (11.37*(Wind_Speed**0.16)) + (0.3965*Air_Temp*(Wind_Speed**0.16))
    print ("The wind chill index is: %0d" %(WCI))