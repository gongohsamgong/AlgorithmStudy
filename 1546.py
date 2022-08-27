n = int(input())
arr = list(map(int, input().split()))

tot = 0

for i in range(n):
    tot += arr[i]
    avg = tot / n

new = avg / max(arr) * 100
print(new)