n = int(input())

num = list(map(int, input().split()))


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cnt = 0

for i in num:
    if is_prime(i):
        cnt += 1

print(cnt)
