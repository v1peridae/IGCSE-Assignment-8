item1_price = float(input("Enter the 1st item price in Kenyan Shillings >>> "))
item2_price = float(input("Enter the 2nd item price in Kenyan Shillings >>> "))
item3_price = float(input("Enter the 3rd item price in Kenyan Shillings >>> "))

total_cost = item1_price + item2_price + item3_price
print ("The total cost of all yout items is " , total_cost , " Kenyan Shillings.")
saved = total_cost * 2/10
print ("You have saved" , saved , "Kenyan Shillings.")
new_total = total_cost - saved
print ("Your new and final total is" , new_total , "Kenyan Shillings.")
