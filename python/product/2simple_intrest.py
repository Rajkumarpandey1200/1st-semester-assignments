# To determine the simple interest on a given amount of money at a
# given rate of interest for a given period of time/
# i=prt/100



p=eval(input("enter the principal amount :"))
r=eval(input("enter the rate of interest:"))
t=eval(input("enter time period:"))
si=p*r*t/100;
tot_amt=si+p;
print ("Total amount is :",tot_amt)
print("simple interest is :",si)
