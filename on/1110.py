N = int(input())

i = 0
new = 100
a = N
while new != N:
    f = a // 10
    s = a % 10
    tot = f + s
    new = s * 10 + tot % 10
    a = new
    i += 1
print(i)