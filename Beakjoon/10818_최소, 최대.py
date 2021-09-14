n = int(input())
a = list(map(int, input().split()))
min_num = a[0]; max_num = a[0]

for i in range(1, n):
    if a[i] < min_num:
        min_num = a[i]
    elif a[i] > max_num:
        max_num = a[i]

print(min_num, max_num)