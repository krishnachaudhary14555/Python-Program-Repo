item = input("Enter item Name : ")

org_price = float(input("Enter Original Price : "))
discount = float(input("Discount Percentage : "))

dis_amount = org_price * discount/100

final_price = org_price - dis_amount

print("Final price of ",item ," = ", final_price)
