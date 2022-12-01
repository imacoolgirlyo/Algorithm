
def solution(n):
    total = 2**n
    answer = [-1]*(total - 1)
    init_idx = (total - 2) // 2

    def check(s, n):
        check_value = int(n/2)

        answer[s-check_value] = 0
        answer[s+check_value] = 1
        if check_value == 1:
            return
        check(s-check_value, check_value)
        check(s+check_value, check_value)

    answer[init_idx] = 0
    check(init_idx, total/2)
    return answer


print(solution(5))
