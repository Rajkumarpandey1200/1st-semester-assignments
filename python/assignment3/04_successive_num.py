result = []

for i in range(1, 1000 - 1):
    a, b, c = i,i + 1,i + 2
    if b**2 == a * c + 1:
        result.append((a, b, c))

for group in result:
    print(group)
