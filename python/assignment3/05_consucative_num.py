result =[]

for i in range(0, 1000-1):
    a=i-2
    b=i-1
    c=i
    d=i+1
    e=i+2
    if a**2 + b**2 + c**2 == d**2 + e**2:
        result.append((a,b,c,d,e))

    

for j in result:
    print(j)
    