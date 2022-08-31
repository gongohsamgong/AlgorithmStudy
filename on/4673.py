lst = [0] * 10001

def d(n):
    if n in [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]:
        n += 1
        lst[n] = 1
    else:
        new = n % 1000 + n % 100 + n % 10
        lst[n] = 0
        d(new)

for i in range(10001):
    if lst[i] == 1:
        print(i)

