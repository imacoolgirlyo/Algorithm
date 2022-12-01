def solution(genres, plays):
    answer = []
    result = []
    genre = {}
    idx = 0
    for i in range(len(genres)):
        if genres[i] not in genre:  # 장르 idx 추가
            genre[genres[i]] = idx
            idx += 1
            answer.append([genres[i], 0, []])
        genre_idx = genre[genres[i]]
        answer[genre_idx][1] += plays[i]
        answer[genre_idx][2].append([i, plays[i]])

    answer.sort(key=lambda x: -x[1])
    for num in range(idx):
        answer[num][2].sort(key=lambda y: [-y[1], y[0]])
        if len(answer[num][2]) >= 2:
            result.append(answer[num][2][0][0])
            result.append(answer[num][2][1][0])
        else:
            result.append(answer[num][2][0][0])

    return result


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]))
