import sys

read = sys.stdin.readline
N = int(read())
total = 1
start_index = 1
end_index = 1
cnt = 1

while end_index != N:
    if total == N:
        cnt += 1
        end_index += 1
        total += end_index
    elif total > N:
        total -= start_index
        start_index += 1
    elif total < N:
        end_index += 1
        total += end_index

print(cnt)
