#완전탐색 - 카펫

def solution(brown, yellow):
    
    s = brown + yellow
    
    for i in range(s,2,-1): #가로(i)
        if s % i == 0: # 세로(a)
            a = s//i
            if yellow == (i-2)*(a-2):
                return [i, a]