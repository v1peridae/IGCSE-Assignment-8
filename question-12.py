item_number = 0
total_cost = 0
item_price = 0
item_price_list = []

while item_price != "CHECKOUT":
    item_price = input("Enter the price of an item or 'CHECKOUT' to end >>> ")
    if item_price == "CHECKOUT" or item_price == "checkout":
        break
    else:
        item_price = float(item_price)
        total_cost += item_price
        item_number += 1
        item_price_list.append(item_price)
        print("Your total number of items are", item_number)
        print("Your total cost is", total_cost , " Kenyan Shillings.")

saved = total_cost * 2/10
print ("You have saved" , saved , "Kenyan Shillings.")
new_total = total_cost - saved
print ("Your new and final total is" , new_total , "Kenyan Shillings.")
print ("The price of each item bought is ", item_price_list, " (In Kenyan Shillings).")
