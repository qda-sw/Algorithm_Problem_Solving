# sol 00. naive approach

from math import factorial
N = int(input())
result= factorial(N)
while result%10 == 0:
    result //= 10
print(f"{result%10**5:05}")