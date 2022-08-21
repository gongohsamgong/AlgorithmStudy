lst = [0] * 10001

for i in range(10000):
    if i in [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]:
        lst[i] = 0
    else:
        lst[i] = 1
        nxt = i + i // 1000 + i // 100 + i // 10 + i % 10
        if nxt <= 10000:
            lst[nxt] = 1

for i in range(10000):
    if lst[i] == 0:
        print(i)