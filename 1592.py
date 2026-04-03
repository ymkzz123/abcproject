import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
lst = [0]*N
cnt = i = 0
while lst[i] < M-1:
    lst[i] += 1
    cnt += 1
    i = (i+L)%N if lst[i]%2 == 1 else (i-L)%N
print(cnt)