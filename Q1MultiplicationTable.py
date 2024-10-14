import time as t

print ("To see the multiplication table of a number from 1 to 10 times:")
input = float(input("Input the number here: "))

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    print (f"{input} x {num} is",num * input)
    t.sleep(0.5)