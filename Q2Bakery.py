#a and b
def scone_price (scones,fresh,old):
    fresh_price = 1.49
    discount = ((fresh_price/10)*6)
    discount_price = fresh_price - discount
    print ("The full price is €",(fresh_price*scones), sep="")
    print ("Discount per old scone = €%0.2f" %(discount))
    
    old_total = round(old * discount_price,2)
    fresh_total = round(fresh * fresh_price)
    total_price = old_total + fresh_total
    print (f"The total price after discounts is €{total_price}")



scones = int(input("How many scones did you buy? "))
old_scones = int(input("Of those, how many were made over 2 days ago? "))
fresh_scones = scones - old_scones
scone_price (scones, fresh_scones, old_scones)


def scone_price (scones,fresh,old):
    fresh_price = 1.49
    discount = ((fresh_price/10)*6)
    discount_price = fresh_price - discount
    old_total = round(old * discount_price,2)
    fresh_total = round(fresh * fresh_price)
    total_price = old_total + fresh_total
    print ("The full price is €",(fresh_price*scones), sep="",end="\t"),
    print ("Discount per old scone = €%0.2f" %(discount), end="\t")
    print (f"The total price after discounts is €{total_price}")



scones = int(input("How many scones did you buy? "))
old_scones = int(input("Of those, how many were made over 2 days ago? "))
fresh_scones = scones - old_scones
scone_price (scones, fresh_scones, old_scones)
