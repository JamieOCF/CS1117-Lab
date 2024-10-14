#a
# number = int(input("Enter an integer from 1 to 10: "))
# numerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X']

# for x in range(len(numerals)):
#     if number == x:
#         print (f"The Roman Numeral of {number} is {numerals[x-1]}")




#b
number = int(input("Enter an integer from 1 to 10: "))
numbers = [1,2,3,4,5,6,7,8,9,10]
numerals = ['I','II','III','IV','V','VI','VII','VIII','IX','X']

if number in numbers:
    for x in range(len(numerals)):
        if number == x:
            print (f"The Roman Numeral of {number} is {numerals[x-1]}")



