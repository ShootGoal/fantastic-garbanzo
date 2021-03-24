N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
j = 0
Sn = 0
Sa = 0
while j <= N - 1:
    Sa = (y[j]-x[j]+1) * (x[j]+y[j]) * 0.5
    Sn += Sa
    j += 1

print(int(Sn))