import sys
N = int(sys.stdin.readline())
stairs = list()
for i in range(N):
    stairs.append(int(sys.stdin.readline()))

score = list()
score.append(stairs[0])
score.append(stairs[1]+stairs[0])
score.append(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))

for i in range(3, N):
    score.append(max(stairs[i]+score[i-2], stairs[i]+stairs[i-1]+score[i-3]))

print('arr', stairs)
print('dp', score)
