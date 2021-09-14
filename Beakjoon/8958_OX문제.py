t = int(input())

for i in range(t):
    case = input()
    score = 0;
    sum_score = 0

    for j in case:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)