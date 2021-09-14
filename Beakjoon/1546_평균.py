n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

result = []
for score in scores:
    result.append(score / max_score * 100)

result_avg = sum(result) / n
print(result_avg)