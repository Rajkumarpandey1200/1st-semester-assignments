result =[]

for i in range (1,100):
    # print(i)
    a=i+1
    b=i+2
    c=i
    if c**2 == a**2+b**2:
        result.append((a,b,c))
        print(result)