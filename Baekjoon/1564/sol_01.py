# sol 01. -> fail
# 5자리만 기억하면서 계산함
# 
def mul_scalar(vec, scalar):
    for i in range(len(vec)):
        vec[i] *= scalar
    return vec
def shift_left(vec):
    for i in range(0, len(vec)-1):
        vec[i] = vec[i+1]
    return vec


vec = [1, 0, 0, 0, 0, 0] # [LSD, ..., MSD, carry for MSD]
N = int(input())
for i in range(1, N+1):
    mul_scalar(vec, i)
    for j in range(len(vec)):
        if vec[j] > 9:
            if j+1 < len(vec):
                vec[j+1] += vec[j] // 10
            vec[j] %= 10
    while vec[0] == 0:
        shift_left(vec)
print(*reversed(vec[0:5]), sep='')