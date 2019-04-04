n= int(input())
numbers = []
for _ in range(n):
    numbers.append(input())

print(*sorted(numbers, key=int), sep='\n')