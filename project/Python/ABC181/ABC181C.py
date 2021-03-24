N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
j = 0
k = 0
m = 0
Y = "No"
A = "a"
while j <= N-1:
    k = 0
    while k <= N-1:
        m = 0
        if j == k:
            A = "a"
        elif j == m:
            A = "a"
        else:
            JK = abs(x[j]-x[k]) ** 2 + abs(y[j]-y[k]) ** 2
            while m <= N-1:
                if m == j:
                    A = "a"
                elif m == k:
                    A = "a"
                else:
                    MK = abs(x[m] - x[k]) ** 2 + abs(y[m] - y[k]) ** 2
                    JM = abs(x[m] - x[j]) ** 2 + abs(y[m] - y[j]) ** 2
                    if JK == MK + JM:
                        Y = "Yes"
                    elif MK == JM + JK:
                        Y = "Yes"
                    elif JM == JK + MK:
                        Y = "Yes"
                m += 1
        k += 1
    j += 1

print(Y)

