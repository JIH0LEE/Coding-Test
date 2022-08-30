import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_dict = {}

for num in N_list:
    if num in N_dict.keys():
        N_dict[num] += 1
    else:
        N_dict[num] = 1

for key in M_list:
    if key in N_dict.keys():
        print(N_dict[key], end=' ')
    else:
        print(0, end=' ')
