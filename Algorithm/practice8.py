# 양꼬치
def solution(n, k):
    answer = 0
    # 양꼬치 10인분을 먹으면, 음료수 하나 서비스
    # 10 * 12000 + 3 * 2000 - 1 * 2000
    answer = n * 12000 + k * 2000 - n//10 * 2000
    return answer