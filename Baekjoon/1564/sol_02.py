# sol 02. -> pass
# 후행하는 0을 제거하면서 
N = int(input())
result = 1
while N > 0:
    result *= N
    while result%10 == 0:
        result //= 10
    result %= 10**12
    N -= 1
print(f"{result%10**5:05}")