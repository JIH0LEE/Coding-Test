import sys

input = sys.stdin.readline

N = int(input())
Str = input()
n_str = list(map(int, Str.strip()))
sum = 0

for num in n_str:
    sum += num

print(sum)
