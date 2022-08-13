arr = []
for i in range (10):
    n = int(input())
    remainder = n % 42
    if remainder not in arr:
        arr.append(remainder)

ans = len(arr)
print(ans)