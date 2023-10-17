item1_price = float(input("Enter the 1st item price in Kenyan Shillings >>> "))
item2_price = float(input("Enter the 2nd item price in Kenyan Shillings >>> "))
item3_price = float(input("Enter the 3rd item price in Kenyan Shillings >>> "))
total_cost = item1_price + item2_price + item3_price
print ("The cost of all yout items is " , total_cost , " Kenyan Shillings.")

saved = total_cost * 2/10
print ("You have recieved a 20% discount, saving" , saved , "Kenyan Shillings.")

new_total = total_cost - saved
print ("Your total is" , new_total , "Kenyan Shillings")
if new_total >= 50:
    print ("You have recieved a 25% discount off your next purchase!")
elif new_total >=20 and new_total <=50 :
    print ("You have recieved a 10% discount off your next purchase!")
else:
    print ("Thanks for shopping with us!")
