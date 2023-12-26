n=(int(input("Enter a number :")))
sqr=n**2
som=0
temp=sqr
while temp>0:
    rem=temp%10
    som=som+rem
    temp=int(temp / 10)
if n==som:
        print("numb is a neon number")
else:
        print("isn't a neon number")
        
    