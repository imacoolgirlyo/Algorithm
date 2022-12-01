N, r, c = map(int, input().split())

#list(map(int, input().split(" ")))
result = 0


def solve(w, x, y):
    global result
    # print(result)
    if w == 2:
        if x == r and y == c:
            return result  # 이렇게 하면 함수가 result를 반환하면서 끝나지만 바로 출력하지는 않는다.
        # 그 동안 다른 호출 된 함수들이 result 를 1씩 증가시킬거고 결국 마지막에는 모든 값이 다 더해진
        # result가 출력해서 오답이 되게 됨.
        result += 1
        if x == r and y+1 == c:
            return result
        result += 1
        if x+1 == r and y == c:
            return result
        result += 1
        if x+1 == r and y+1 == c:
            print(result)  # r,c에 맞는 x,y를 찾았을 때 바로 값을 출력해야함
            return
        result += 1
        return
    solve(w/2, x, y)
    solve(w/2, x, y+w/2)
    solve(w/2, x+w/2, y)
    solve(w/2, x+w/2, y+w/2)


solve(2**N, 0, 0)
print(result)
