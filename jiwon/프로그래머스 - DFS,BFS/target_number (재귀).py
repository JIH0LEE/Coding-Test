answer = 0
def DFS(L, sum, numbers, target):
    global answer
    N = len(numbers)
    if L == N:
        if target == sum:
            answer += 1
            return
    else:
        DFS(L+1, sum+numbers[L], numbers, target) # 1,0+4,[4121],4 / 4,sum+1,[4121],4
        DFS(L+1, sum-numbers[L], numbers, target)
        

def solution(numbers, target):
    global answer
    DFS(0,0, numbers, target)
    return answer