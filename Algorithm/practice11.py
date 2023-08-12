def solution(n):
    answer = 0
    # O(n^2)
    # O(n)
    for num1 in range(1, n+1):
        if n % num1 != 0:
            continue
        
        num2 = n//num1
        (num1, num2)
        answer += 1
        
        # for num2 in range(n//num1, 0, -1):
        #     if num1 * num2 == n:
        #         answer += 1
        #         break

    return answer