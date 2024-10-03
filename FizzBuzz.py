number = int(input("Please inter a positive integer: "))

if (number%(3*5)) == 0:
    print ("FizzBuzz")
elif (number%3) == 0:
    print ("Fizz")
elif (number%5) == 0:
    print ("Buzz")
else:
    print (number)