def solution(n, lost, reserve):    
    answer = 0

    reserve_uniq = set(reserve) - set(lost)
    lost_uniq = set(lost) - set(reserve)
    
    for i in reserve_uniq :
        if i-1 in lost_uniq :
            lost_uniq.remove(i-1)
            
        elif i+1 in lost_uniq :
            lost_uniq.remove(i+1)
    
    answer = n - len(lost_uniq)
    return answer