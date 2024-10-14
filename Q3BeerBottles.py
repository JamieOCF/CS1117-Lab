import time as t

numberOfBottles = int(input("How many bottles of beer do you have? "))

def bottlesOfBeer():
    for x in range(numberOfBottles,0,-1):
        if x == 1:
            print (f"{x} bottle of beer on the wall, {x} bottle of beer. Take it down, pass it around, {x-1} bottles of beer on the wall!")
        elif x != 1:
            print (f"{x} bottles of beer on the wall, {x} bottles of beer. Take one down, pass it around, {x-1} bottles of beer on the wall.")
            t.sleep(0.25)

bottlesOfBeer()
