n = 2
p = int(input("Enter a prime number: "))  # Ensure the input is converted to an integer
perfect_num = (n**(p - 1)) * (n**p - 1)
print(perfect_num)
