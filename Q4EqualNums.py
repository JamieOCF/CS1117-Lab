import math

num1 = float(input("Input any number: "))
num2 = float(input("Input another number, it may be the same or different to the first: "))

def num_equality(one, two):
    if one == two:
        answer = math.sqrt(two)
        return answer
    else:
        answer = round(one**2,0)
        return answer
    
answer = num_equality(num1,num2)
print (f"The result is {answer}")