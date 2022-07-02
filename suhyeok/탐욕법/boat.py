def solution(people, limit):
    answer = 0

    left = 0
    right = len(people)-1

    people.sort()

    while left < right:
        if people[left]+people[right] <= limit:
            answer += 1
            left += 1
            right -= 1

        if people[left]+people[right] > limit:
            answer += 1
            right -= 1

        if left == right:
            answer += 1
            break

        return answer
