def solution(n, lost, reserve):
    # 1. Set을 만든다
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    reserve_only.sort();
    
    # 2. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)

    #3. 최대한 나눠준 뒤에 lost에 남아있는 학생들은 체육복이 없는 학생들이다.
    return n - len(lost_only)

# 예시 출력
print(solution(5,[2, 4],[3]))
