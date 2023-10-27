import sys

read = sys.stdin.readline
N, M = map(int, read().split())
arr = [0]
arr.extend(list(map(int, read().split())))

sum_arr = [0] * (N+1)
for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]

for _ in range(M):
    i, j = map(int, read().split())
    print(sum_arr[j] - sum_arr[i-1])
