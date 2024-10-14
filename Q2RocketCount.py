import time as t

counter = int(input("Enter an integer: "))

def blastOff():
    if counter < 2 or counter > 20:
        print ("Between 2 and 20 please :)")
    else:
        for x in range(counter,1,-1):
            print (f"There is {x} seconds to lift-off!")
            t.sleep(1)
        print ("There is 1 second to lift-off!")
        t.sleep(1)
        print ("We have blast-off!")

blastOff()


