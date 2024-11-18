import random
from math import factorial
def sol_truth_00(n):
    result= factorial(n)
    while result%10 == 0:
        result //= 10
    return result%10**5

def sol_truth_01(n):
    result = 1
    while n > 0:
        result *= n
        while result%10 == 0:
            result //= 10
        result %= 10**12
        n -= 1
    return result%10**5


def sol_02(n):
    result = 1
    while n > 0:
        result *= n
        while result%10 == 0:
            result //= 10
        result %= 10**8
        n -= 1
    return result%10**5

MAX = 1000000
for n in reversed(range(MAX+1)):
    print(n)
    #n = random.randint(0, MAX)
    truth = sol_truth_01(n)
    test = sol_02(n)
    if truth != test: raise Exception(n, truth, test)
print("passed")