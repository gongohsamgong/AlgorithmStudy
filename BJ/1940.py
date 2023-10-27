import sys

read = sys.stdin.readline
N = int(read())
M = int(read())
ingredients = sorted(list(map(int, read().split())))

i, j = 0, N-1
cnt = 0

while i < j:
    if ingredients[i] + ingredients[j] < M:
        i += 1
    elif ingredients[i] + ingredients[j] > M:
        j -= 1
    else:
        i += 1
        j -= 1
        cnt += 1

print(cnt)
