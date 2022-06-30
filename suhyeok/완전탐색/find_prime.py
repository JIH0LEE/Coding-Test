# %%
from itertools import permutations
import math

# %%


def is_Prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

# %%


def solution(numbers):
    num = list(numbers)
    answer_list = []
    temp = []

    for i in range(1, len(numbers)+1):
        # p순열(permutation)으로 모든 가능한 조합 찾기
        temp = temp + list(permutations(numbers, i))

    for j in range(1, len(temp+1)):
        num[j] = int(''.join(j))

    for k in num:
        if is_Prime(k) == True:
            answer_list.append(k)

    answer = len(answer_list)

    return answer

# %%
