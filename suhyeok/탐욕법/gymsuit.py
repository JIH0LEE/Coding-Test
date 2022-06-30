# 아이디어

# 우선 lost배열과 reserve 배열에 중복되는 값이 있는지 체크
# 체크 후 lost 배열과 reserve 배열에서 중복되는 값 제거

# lost배열과 reserve 배열을 인덱스 값을 돌면서 lost 배열 index 값보다 하나 크거나 작은거가 있는지 reserve 배열에서 확인
# 있으면 count를 증가시켜주고 없으면 넘어가기
# 근데 이렇게 하면 for문을 너무 많이 돌아야할듯

# 1.여벌 체육복이 있는 학생은 무조건 내 앞 번호 학생에게 빌려준다
# 2.앞 번호 학생이 체육복이 있으면 뒷 번호 학생에게 빌려준다.
# 3.뒷 번호 학생도 체육복이 있으면 아무것도 안해도 된다.

def solution(n, lost, reserve):
    answer = 0

    # set을 해주는 이유: 제한사항에서 도난된 체육복과 여벌의 체육복은 중복이 없다고 하였기 때문
    # 잃어버렸지만 여벌 체육복을 가지고 있는 애들
    lost_but_reserve = set(lost) & set(reserve)

    # 잃어버린 애들
    lost_students = set(lost) - lost_but_reserve

    # 여벌만 있는 애들
    reserve_students = set(reserve) - lost_but_reserve
    answer = n - len(lost_students)

    print(lost_but_reserve)
    print("lost 배열", lost_students)
    print("reserve 배열", reserve_students)
    print(answer)

    # i가 lost의 0번째 index부터 len(lost)-1까지 돌면서
    for i in lost_students:
        print("현재 i값", i)
        # 만약 reserve 배열에 i-1이 있다면 reserve에서 해당 값을 빼주고
        # 체육복을 빌려주었으므로 answer증가
        if i-1 in reserve_students:
            print("제거될 reserve 배열의 인덱스와 값", i-1, reserve_students)
            reserve_students.remove(i-1)
            answer += 1

        # 작은 애들 중에 없다면 큰 애들 보기
        # 만약 reserve 배열에 i+1이 있으면 reserve에서 해당 값 빼주고
        # 체육복 빌려주었으므로 answer 증가
        elif i+1 in reserve_students:
            print("제거된 reserve 배열의 인덱스와 값", i+1, reserve_students)
            reserve_students.remove(i+1)
            answer += 1

        print("reserve배열", reserve_students)
    return answer
