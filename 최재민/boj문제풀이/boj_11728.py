a, b = map(int, input().split())

one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = one + two

print(*sorted(three))
