import sys

t = int(sys.stdin.readline()) # sys.stdin.readline(): 시간이 오래 걸리는 input() 대신 사용

for i in range(t):
    # sys.stdin.readline().split(): 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
    a, b = map(int, sys.stdin.readline().split())

    print(a + b)