import sys
import math

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

T = int(sys.stdin.readline())

for i in range(T):
    z = int(sys.stdin.readline())
    while True:
        if is_prime(z):
            print(z)
            break
        else:
            z += 1