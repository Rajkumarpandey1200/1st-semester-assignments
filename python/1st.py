a,e = input("Enter age of retairment & life expectancy seperated by space").split()
age = int(a);
e = eval(e)
p,r = input("enter the amount of annuity followed by rate of inflamation seperated by space").split()
p= int (p)
r = float (r)/100
n = e- age;
pv= p*(1-(1+r)**(-n))/r;
print("amt is",pv)
