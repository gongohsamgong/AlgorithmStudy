import sys

input_data = sys.stdin.readline()
row = int(input_data[1])
column = ord(input_data[0])
num = 0

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

for step in steps:
  if ((row + step[1]) >= 1 and (row + step[1] <= 8)) and ((column + step[0]) >= ord('a') and (column + step[0] <= ord('h'))):
    num += 1

print(num)
