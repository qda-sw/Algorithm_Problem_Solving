# sol 03. 
# 5자리만 기억하면서 곱하기
# 단, 곱해서 10이 될 수 있는 2, 5가 포함되어있다면, 제거하고 곱하기.

from collections import defaultdict

# return (no. of two) - (no. of five)
compressed_map = dict()
def compress_two_and_five(n, compressed):
    if n in compressed_map:
        return compressed_map[n]
    if n%2 != 0 and n%5 != 0:
        compressed_map[n] = n, 0
        return compressed_map[n]
    if n%2 == 0: 
        compressed_map[n] = compress_two_and_five(n//2, compressed+1)
        return compressed_map[n]
    else:
        compressed_map[n] = compress_two_and_five(n//5, compressed-1)
        return compressed_map[n]

n = int(input())
product = 1
compressed_total = 0
for i in range(1, n+1):
    result = compress_two_and_five(i, 0)
    product = (product * result[0])%10**5
    compressed_total += result[1]

factor = 2 if compressed_total > 0 else 5
for _ in range(abs(compressed_total)):
    product = (product * factor)%10**5
print(f"{product:05}")