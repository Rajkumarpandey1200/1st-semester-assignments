n = int(input("enter a number which factorial you want :"))

if n<0:
    print("value error number should be greater than 0")
else:
    fact_res= 1
    for i in range (1,n+1):
        fact_res *= i
    print(f"factorial value of {n} is {fact_res}")