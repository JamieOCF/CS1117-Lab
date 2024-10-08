num = int(input("Give a whole number between 1 and 4, inclusive: "))

def seasons():
    if num > 4 or num < 1:
        print ("Invalid number!")
    elif num == 1:
        print ("You chose Winter!")
    elif num == 2:
        print ("You chose Spring!")
    elif num == 3:
        print ("You chose Summer!")
    elif num == 4:
        print ("You chose Autumn!")

seasons()