max_score_gap = 0
result=[[-1]]
def is_smaller(comp,target):
    for i in range(10,-1,-1):
        if target[i]>comp[i]:
            return True
        elif target[i]<comp[i]:
            return False
    return False
def get_score_gap(apeach,ryan):
    result = 0
    for score in range(10,-1,-1):
        i = 10 - score
        if apeach[i]>ryan[i]:
            result = result-score
        if apeach[i]<ryan[i]:
            result = result+score
    return result


def brute_force(apeach,ryan,score,n):
    global max_score_gap

    if score == -1:
        score_gap = get_score_gap(apeach,ryan)
        if max_score_gap<score_gap:    
            max_score_gap = score_gap 
            result.pop()
            result.append(ryan[:])
            
        elif max_score_gap == score_gap and score_gap>0:
            if is_smaller(result[-1],ryan):
                result.pop()
                result.append(ryan[:])


            
        return
    else:
        i = 10 - score
        remain = n - sum(ryan)
        if remain >apeach[i]:
            
            if i == 10:
                ryan.append(remain)
            else:
                ryan.append(apeach[i]+1)
            brute_force(apeach,ryan,score-1,n)
            ryan.pop()
            
            if i==10:
                ryan.append(remain)
            else:
                ryan.append(0)
            brute_force(apeach,ryan,score-1,n)
            ryan.pop()
        else:
            if i == 10:
                ryan.append(remain)
            else:
                ryan.append(0)
            brute_force(apeach,ryan,score-1,n)
            ryan.pop()
            

def solution(n, info):
    answer=[-1]   
    brute_force(info,[],10,n)
    answer=result[-1]
    return answer
