import time
n, k = map(int, input().split())
cnt = 0

start_time = time.time()

while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

end_time = time.time()
print(cnt, end_time - start_time)