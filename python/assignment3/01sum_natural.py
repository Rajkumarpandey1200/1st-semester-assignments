n = int(input("Enter a positive number :"))
sum_res = 0
for i in range(1,n+1):
    sum_res += i
print(f"The sum of the first {n} natural numbers is: {sum_res}")