c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    count = 0

    for j in scores[1:]:
        if j > avg:
            count += 1

    print('%0.3f%%' % ((count / scores[0]) * 100))