def solution(budgets, M):
    mx = max(budgets)
    mn = 0
    answer = 0
    while mx >= mn:
        mid = (mx+mn) // 2
        result = 0
        for i in budgets:
            if i < mid:
                result += i
            else:
                result += mid
        if result <= M:
            mn = mid+1
            answer = mid
        else:
            mx = mid-1
    return answer


print(solution([120, 110, 140, 150], 485))
