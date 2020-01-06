N, K = map(int, input().split())
sche = list(map(int, input().split()))
plug = [0]*N
res = 0

for i in range(K):
    isPluggedIn = False
    for j in range(N):
        if sche[i] == plug[j]:
            isPluggedIn = True
            break
    if isPluggedIn:
        continue

    #print('동일 기기 플로그에 있을 때', plug)
    for j in range(N):
        if plug[j] == 0:
            plug[j] = sche[i]
            isPluggedIn = True
            break
    if isPluggedIn:
        continue
    #print('동일 기기 플로그에 없고 빈 자리 O 꽂았을 때 ', plug)

    nextsche = -1
    devicePos = 0
    for j in range(N):
        isScheduled = False
        for k in range(i+1, K):
            if plug[j] == sche[k]:
                isScheduled = True
                if nextsche < k:
                    nextsche = k
                    devicePos = j
                break
        if isScheduled == False:
            devicePos = j
            nextsche = 100

    plug[devicePos] = sche[i]
    res += 1
    #print('동일 기기 플로그에 없고 빈자리 없어서 꽂 ', plug)

print(res)
