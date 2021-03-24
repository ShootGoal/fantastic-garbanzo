import math
N, X = map(int, input().split())
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N
j = 0
M_i = []

for i in range(N):
    a[i], b[i], c[i], d[i] = map(int, input().split())

while j <= N-1:
    if X >= a[j]:
        D = math.floor((X-a[j]) / c[j]) + 1
        M = D * d[j] + b[j]
        M_i.append(M)
    else:
        M = b[j]
        M_i.append(M)
    j += 1
M_i.sort()
print(int(M_i[0]), int(M_i[-1]))