def solution(n):
    answer = 0
    # for number in range(n+1):
    #     if number % 2 == 0:
    #         answer += number

    # n이 11같은 홀수라면?
    # 2 4 6 8 10 (11)
    # 10//2 = 5
    # 11//2 = 5
    
    # n = 40,000,000
    for number in range(0, n+1, 2):
        answer+=number
    # 시간복잡도 : O(N)
    
    # 1 ~ 100 -> n * (n+1) / 2
    # 2 ~ 200 (짝수만) -> 
    # 2, 4, 6, 8, 10 ... 200
    # 1, 2, 3, 4, 5, ... 100 * 2
    # n = 100
    # (n * (n+1) / 2) * 2
    # real_n = 200
    # (real_n/2 * (real_n/2+1) / 2) * 2
    
    # 1 ~ 100 (/2) * 2
    # n/2 * (n/2+1) / 2 * 2
    # n/2 * (n/2+1)
    # 시간복잡도 : O(1)
    
    return n//2*(n//2+1)