n, m = map(int, input().split())
temp = 0

for i in range(n):
    data = list(map(int, input().split()))
    if min(data) > temp:
        temp = min(data)

print(temp)