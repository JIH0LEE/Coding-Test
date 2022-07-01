#프로그래머스
#탐욕법
#큰수만들기

def solution(number, k):
    numbers=list(number)
    stack=[numbers[0]]
    for elem in numbers[1:]:
        while stack:
            if elem>stack[-1] and k>0:
                stack.pop()
                k-=1
            else:
                break
        stack.append(elem)
    for _ in range(k):
        stack.pop()
    answer="".join(stack)
    return answer