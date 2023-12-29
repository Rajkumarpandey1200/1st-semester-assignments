p=int(input("Enter 1st number :"))
q=int(input("Enter 2nd number :"))

S_Range=int(input("Enter starting range :"))
E_Range =int(input("Enter Ending range :"))
result_nums=[]

for num in range(S_Range,E_Range + 1):
    if num % p== 0 and num % q != 0: 
       result_nums.append(num)
print(f"The numbers divisible by {p} but not divisible by {q} in the range {S_Range} to{E_Range}  are: {result_nums}")
        
        