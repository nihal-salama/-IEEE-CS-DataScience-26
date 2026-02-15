len = int(input())
score = map(int, input().split())
score = list(score)
score.sort()
score.reverse()

for i in range(len):
    if score[i] < score[0]:
        print(score[i])
        break