# 9. Fibonacci Series
n = int(input("Enter N: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
