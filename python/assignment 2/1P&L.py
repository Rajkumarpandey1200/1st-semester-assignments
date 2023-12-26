

cost_price=float(input("Enter cost price :"))
selling_price=float(input("Enter selling price :"))

profit= selling_price - cost_price
loss= cost_price - selling_price
 
if profit > 0:
 print("profit :",profit)
elif loss >0:
 print("loss :",loss)
else:
 print("no profit no loss")