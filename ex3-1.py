# N = int(input())
# num = 0
#
# while N >= 10:
#     if N >= 500:
#         a = N // 500
#         N -= a * 500
#     elif N >= 100:
#         b = N // 100
#         N -= b * 100
#     elif N >= 50:
#         c = N // 50
#         N -= c * 50
#     elif N >= 10:
#         d = N // 10
#         N -= d * 10
#
# print(a+b+c+d)

N = int(input())
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N // coin
    N %= coin

print(count)